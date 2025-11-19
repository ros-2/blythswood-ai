"""
Ross AI Grant Writer - Generation Engine
Section-by-section generation with quality checks
"""

import anthropic
import os
import re
from typing import List, Dict, Tuple
from config import QUALITY_THRESHOLD, MAX_RETRY_ATTEMPTS

def extract_sections_from_requirements(grant_requirements: str) -> List[Dict]:
    """
    Extract individual sections/questions from grant requirements.
    Returns list of section definitions.
    """
    sections = []
    
    # Pattern 1: Numbered questions with word limits
    pattern1 = r'(\d+)\.\s+([A-Z][A-Z\s]+)\s*\((\d+)\s*words?\s*max'
    matches = re.finditer(pattern1, grant_requirements, re.IGNORECASE)
    
    for match in matches:
        sections.append({
            'number': match.group(1),
            'title': match.group(2).strip().title(),
            'word_limit': int(match.group(3)),
            'type': 'numbered'
        })
    
    # Pattern 2: Questions without numbers but with word limits
    if not sections:
        pattern2 = r'([A-Z][A-Za-z\s]+)\s*\((\d+)\s*words?\s*max'
        matches = re.finditer(pattern2, grant_requirements, re.IGNORECASE)
        
        for i, match in enumerate(matches):
            sections.append({
                'number': str(i+1),
                'title': match.group(1).strip(),
                'word_limit': int(match.group(2)),
                'type': 'inferred'
            })
    
    # Fallback: Create generic sections if none found
    if not sections:
        sections = [
            {'number': '1', 'title': 'Organization Background', 'word_limit': 300, 'type': 'default'},
            {'number': '2', 'title': 'Need Statement', 'word_limit': 400, 'type': 'default'},
            {'number': '3', 'title': 'Project Description', 'word_limit': 500, 'type': 'default'},
            {'number': '4', 'title': 'Impact and Evaluation', 'word_limit': 300, 'type': 'default'},
            {'number': '5', 'title': 'Budget', 'word_limit': 200, 'type': 'default'},
            {'number': '6', 'title': 'Sustainability', 'word_limit': 200, 'type': 'default'},
        ]
    
    return sections

def generate_single_section(
    section: Dict,
    grant_requirements: str,
    master_doc: str,
    past_grants: str,
    api_key: str,
    attempt: int = 1
) -> Tuple[bool, str, int]:
    """
    Generate a single section with quality check.
    Returns: (success, text, quality_score)
    """
    
    try:
        client = anthropic.Anthropic(api_key=api_key)
        
        # Analyze style from past grants
        style_prompt = f"""Based on these past successful grant applications, what is the writing style?

{past_grants[:1500]}

Describe in 2-3 sentences: tone (formal/passionate), structure (data-heavy/story-focused), sentence length, use of statistics vs narratives."""
        
        style_analysis = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=300,
            messages=[{"role": "user", "content": style_prompt}]
        )
        
        style_guide = style_analysis.content[0].text
        
        # Generate section
        section_prompt = f"""You are an expert grant writer. Write ONLY the "{section['title']}" section of this grant application.

STYLE TO MATCH:
{style_guide}

GRANT REQUIREMENTS:
{grant_requirements}

CHARITY INFORMATION:
{master_doc}

PAST SUCCESSFUL APPLICATIONS (for reference):
{past_grants[:2000]}

CRITICAL INSTRUCTIONS:
1. Write ONLY the {section['title']} section
2. Stay within {section['word_limit']} words (strict limit)
3. Match the tone and style of past successful applications
4. Use specific facts, data, and stories from the charity information
5. Address the exact question asked in the requirements
6. Be compelling and evidence-based
7. Format with a clear header: ## {section['title']}

Write this section now. Make it excellent."""

        section_response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1500,
            messages=[{"role": "user", "content": section_prompt}]
        )
        
        section_text = section_response.content[0].text
        
        # Quality check
        quality_score = assess_section_quality(
            section_text,
            section,
            master_doc,
            client
        )
        
        return True, section_text, quality_score
        
    except Exception as e:
        return False, f"Error: {str(e)}", 0

def assess_section_quality(section_text: str, section: Dict, master_doc: str, client) -> int:
    """
    Assess quality of generated section (0-100).
    """
    
    try:
        quality_prompt = f"""Rate this grant application section 0-100.

SECTION REQUIREMENTS:
- Title: {section['title']}
- Word limit: {section['word_limit']}
- Should be specific, evidence-based, compelling

GENERATED SECTION:
{section_text}

CHARITY INFORMATION (for checking specificity):
{master_doc[:1000]}

Score on:
- Completeness (addresses the question fully): 30 points
- Word count (within limit): 20 points  
- Specificity (uses concrete examples/data): 25 points
- Writing quality (clear, compelling): 25 points

Return ONLY a number 0-100, nothing else."""

        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=50,
            messages=[{"role": "user", "content": quality_prompt}]
        )
        
        score_text = response.content[0].text.strip()
        score = int(re.search(r'\d+', score_text).group())
        return min(max(score, 0), 100)
        
    except:
        # Fallback: basic scoring
        word_count = len(section_text.split())
        score = 50  # Base score
        
        # Word count check
        if word_count <= section['word_limit']:
            score += 20
        elif word_count <= section['word_limit'] * 1.1:
            score += 10
        
        # Has header check
        if section['title'].lower() in section_text.lower():
            score += 15
        
        # Has some substance
        if word_count > 100:
            score += 15
        
        return min(score, 100)

def generate_complete_application(
    grant_requirements: str,
    master_doc: str,
    past_grants: str,
    api_key: str,
    progress_callback=None
) -> Tuple[bool, str, Dict]:
    """
    Generate complete application section by section.
    Retry sections if quality is below threshold.
    """
    
    metadata = {
        'sections_generated': 0,
        'sections_total': 0,
        'retries_used': 0,
        'average_quality': 0,
        'failed_sections': []
    }
    
    try:
        # Extract sections from requirements
        sections = extract_sections_from_requirements(grant_requirements)
        metadata['sections_total'] = len(sections)
        
        if progress_callback:
            progress_callback(f"Found {len(sections)} sections to generate")
        
        complete_application = ""
        quality_scores = []
        
        # Generate each section
        for i, section in enumerate(sections):
            if progress_callback:
                progress_callback(f"Generating: {section['title']}")
            
            best_text = ""
            best_score = 0
            
            # Try up to MAX_RETRY_ATTEMPTS times
            for attempt in range(1, MAX_RETRY_ATTEMPTS + 1):
                success, text, score = generate_single_section(
                    section,
                    grant_requirements,
                    master_doc,
                    past_grants,
                    api_key,
                    attempt
                )
                
                if not success:
                    if progress_callback:
                        progress_callback(f"⚠ Error generating {section['title']}")
                    metadata['failed_sections'].append(section['title'])
                    break
                
                # Keep best attempt
                if score > best_score:
                    best_text = text
                    best_score = score
                
                # If good enough, stop trying
                if score >= QUALITY_THRESHOLD:
                    break
                
                # Otherwise, retry
                if attempt < MAX_RETRY_ATTEMPTS:
                    metadata['retries_used'] += 1
                    if progress_callback:
                        progress_callback(f"↻ Improving {section['title']} (attempt {attempt+1})")
            
            # Add best version to application
            if best_text:
                complete_application += best_text + "\n\n"
                quality_scores.append(best_score)
                metadata['sections_generated'] += 1
                
                if progress_callback:
                    progress_callback(f"✓ {section['title']} complete (quality: {best_score}/100)")
        
        # Calculate average quality
        if quality_scores:
            metadata['average_quality'] = sum(quality_scores) / len(quality_scores)
        
        if progress_callback:
            progress_callback("✓ Application complete!")
        
        return True, complete_application, metadata
        
    except Exception as e:
        return False, f"Generation failed: {str(e)}", metadata
