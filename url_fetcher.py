"""
Blythswood AI - URL and PDF Fetcher
"""

import requests
import re
from typing import Tuple
import PyPDF2
import io
from docx import Document

def fetch_from_url(url: str) -> Tuple[bool, str]:
    try:
        url = url.strip()
        if not url.startswith('http'):
            url = 'https://' + url
        
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        content_type = response.headers.get('content-type', '').lower()
        
        if 'pdf' in content_type or url.lower().endswith('.pdf'):
            return extract_pdf_text(response.content)
        elif 'word' in content_type or url.lower().endswith(('.doc', '.docx')):
            return extract_word_text(response.content)
        else:
            return extract_webpage_text(response.text)
    
    except requests.Timeout:
        return False, "Request timed out."
    except requests.RequestException as e:
        return False, f"Could not fetch URL: {str(e)}"
    except Exception as e:
        return False, f"Error: {str(e)}"

def extract_pdf_text(pdf_bytes: bytes) -> Tuple[bool, str]:
    try:
        pdf_file = io.BytesIO(pdf_bytes)
        reader = PyPDF2.PdfReader(pdf_file)
        text_parts = []
        
        for page in reader.pages:
            try:
                text = page.extract_text()
                if text.strip():
                    text_parts.append(text)
            except:
                continue
        
        if not text_parts:
            return False, "PDF appears empty."
        
        return True, "\n\n".join(text_parts)
    except Exception as e:
        return False, f"PDF error: {str(e)}"

def extract_word_text(doc_bytes: bytes) -> Tuple[bool, str]:
    try:
        doc_file = io.BytesIO(doc_bytes)
        doc = Document(doc_file)
        text_parts = [para.text for para in doc.paragraphs if para.text.strip()]
        
        if not text_parts:
            return False, "Word document appears empty."
        
        return True, "\n\n".join(text_parts)
    except Exception as e:
        return False, f"Word error: {str(e)}"

def extract_webpage_text(html: str) -> Tuple[bool, str]:
    try:
        html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)
        html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r'<[^>]+>', ' ', html)
        text = re.sub(r'\s+', ' ', text).strip()
        
        if len(text) < 100:
            return False, "Could not extract meaningful text."
        
        return True, text
    except Exception as e:
        return False, f"Webpage error: {str(e)}"

def validate_url(url: str) -> Tuple[bool, str]:
    url = url.strip()
    if not url:
        return False, "URL is empty."
    
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    return True, url
