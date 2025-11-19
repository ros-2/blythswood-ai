import re
from typing import Dict, List, Tuple

def count_words(text: str) -> int:
    """Count words in text."""
    return len(text.split())

def extract_requirements(grant_text: str) -> List[Dict]:
    """
    Extract questions and word limits from grant requirements.
    Returns list of {question, word_limit, section_name}
    """
    requirements = []
    
    # Pattern to find sections with word limits
    pattern = r'(\d+)\.\s+([A-Z\s]+)\s*\((\d+)\s*words?\s*max\)'
    matches = re.finditer(pattern, grant_text, re.IGNORECASE)
    
    for match in matches:
        section_num = match.group(1)
        section_name = match.group(2).strip().title()
        word_limit = int(match.group(3))
        
        requirements.append({
            'section_num': section_num,
            'section_name': section_name,
            'word_limit': word_limit,
            'status': 'pending'
        })
    
    return requirements

def check_word_limit(text: str, limit: int, tolerance: int = 10) -> Tuple[bool, str]:
    """
    Check if text is within word limit.
    Returns (is_within_limit, status_message)
    """
    word_count = count_words(text)
    
    if word_count <= limit:
        return True, f"✓ {word_count}/{limit} words"
    elif word_count <= limit + tolerance:
        return True, f"⚠ {word_count}/{limit} words (slightly over)"
    else:
        return False, f"✗ {word_count}/{limit} words (too many)"

def extract_style_patterns(past_grants: str) -> Dict:
    """
    Analyze past successful grants to extract style patterns.
    Returns dict of style characteristics.
    """
    word_count = count_words(past_grants)
    
    # Simple analysis
    avg_sentence_length = len(past_grants.split('.')) / max(len(past_grants.split('\n\n')), 1)
    
    # Check for common patterns
    uses_statistics = bool(re.search(r'\d+%|\d+\s+(people|children|families)', past_grants))
    uses_stories = bool(re.search(r'(story|example|case|testimonial)', past_grants, re.IGNORECASE))
    uses_quotes = bool(re.search(r'[""].*?[""]', past_grants))
    
    tone = "professional"
    if re.search(r'(we believe|passionate|dedicated|committed)', past_grants, re.IGNORECASE):
        tone = "passionate and professional"
    
    return {
        'avg_sentence_length': avg_sentence_length,
        'uses_statistics': uses_statistics,
        'uses_stories': uses_stories,
        'uses_quotes': uses_quotes,
        'tone': tone,
        'total_words': word_count
    }

def calculate_quality_score(generated_text: str, requirements: List[Dict], master_doc: str) -> int:
    """
    Calculate quality score 0-100 based on various factors.
    """
    score = 0
    
    # Check if addresses requirements (40 points)
    sections_addressed = 0
    for req in requirements:
        if req['section_name'].lower() in generated_text.lower():
            sections_addressed += 1
    if requirements:
        score += int((sections_addressed / len(requirements)) * 40)
    
    # Check word count appropriateness (20 points)
    total_words = count_words(generated_text)
    if 1500 <= total_words <= 2500:
        score += 20
    elif 1000 <= total_words <= 3000:
        score += 10
    
    # Check for specific details from master doc (20 points)
    # Count how many unique facts from master doc appear
    master_sentences = master_doc.split('.')[:20]  # First 20 sentences
    references = 0
    for sentence in master_sentences:
        if len(sentence.strip()) > 20:  # Meaningful sentence
            # Check if key phrases appear
            words = sentence.split()
            if len(words) > 5:
                phrase = ' '.join(words[:5])
                if phrase.lower() in generated_text.lower():
                    references += 1
    
    if references > 5:
        score += 20
    elif references > 2:
        score += 10
    
    # Check for professional structure (20 points)
    has_headers = bool(re.search(r'#{1,3}\s+[A-Z]', generated_text))
    has_paragraphs = len(generated_text.split('\n\n')) > 5
    
    if has_headers and has_paragraphs:
        score += 20
    elif has_headers or has_paragraphs:
        score += 10
    
    return min(score, 100)  # Cap at 100

def format_cost(tokens: int) -> str:
    """Format API cost based on token usage."""
    # Approximate: Claude Sonnet 4 pricing
    cost = (tokens / 1000) * 0.003  # $3 per million tokens = $0.003 per 1k
    return f"£{cost:.3f}"
