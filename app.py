"""
Blythswood AI - Grant Writing System
By Philip Ross
"""

import streamlit as st
import os
from dotenv import load_dotenv
from generator import generate_complete_application
from document_formatter import create_word_document, create_pdf_document, create_text_file
from config import *
from blythswood_data import get_master_doc, get_past_grants, get_organization_name
from url_fetcher import fetch_from_url, validate_url
import time

load_dotenv()  # For local development
# Load API key from environment or Streamlit secrets
try:
    API_KEY = st.secrets["ANTHROPIC_API_KEY"]  # Streamlit Cloud
except:
    API_KEY = os.getenv('ANTHROPIC_API_KEY')  # Local .env file

st.set_page_config(
    page_title=f"{APP_NAME}",
    page_icon="🎯",
    layout="centered"
)

with open('styles_blythswood.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'welcome'
if 'grant_requirements' not in st.session_state:
    st.session_state.grant_requirements = ""
if 'generated_application' not in st.session_state:
    st.session_state.generated_application = ""
if 'metadata' not in st.session_state:
    st.session_state.metadata = {}

def go_to_page(page_name):
    st.session_state.page = page_name
    st.rerun()

# ===== WELCOME PAGE =====
def welcome_page():
    st.markdown(f"""
    <div class='hero-section'>
        <h1 class='hero-title'>{APP_NAME}</h1>
        <p class='hero-subtitle'>{APP_TAGLINE}</p>
        <p class='creator-credit'>{CREATOR}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='info-card'>
        <h3>🎯 How This Works</h3>
        <p>This system is <strong>pre-loaded with Blythswood Care's information</strong> - your programs, impact stories, financials, and past successful grant applications.</p>
        <p><strong>All you need to do:</strong> Provide the grant requirements you're applying for (paste a URL, upload a PDF, or paste the text). The system will automatically generate a professional application in Blythswood's voice.</p>
        <p><strong>Time:</strong> 3-5 minutes vs. 8 hours manual writing</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='info-card accent-card'>
        <h3>💡 What Makes This Special</h3>
        <ul class='benefit-list'>
            <li><strong>No setup required:</strong> Blythswood's data is already loaded</li>
            <li><strong>Learns your voice:</strong> Analyzes past winning applications</li>
            <li><strong>Quality assured:</strong> Auto-scores and refines weak sections</li>
            <li><strong>Ready to submit:</strong> Download as Word, PDF, or text</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Start Application", use_container_width=True, type="primary"):
            go_to_page('input')

# ===== INPUT PAGE =====
def input_page():
    st.markdown(f"""
    <div class='page-header'>
        <h1>Grant Requirements</h1>
        <p>Provide the grant you're applying for</p>
    </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["📎 Paste URL", "📤 Upload File", "✏️ Paste Text"])
    
    with tab1:
        st.markdown("""
        <div class='info-box'>
            🔗 Paste the URL of the grant application page or PDF
        </div>
        """, unsafe_allow_html=True)
        
        url_input = st.text_input(
            "Grant URL",
            placeholder="https://example.com/grant-application.pdf",
            label_visibility="collapsed"
        )
        
        if url_input:
            is_valid, result = validate_url(url_input)
            if is_valid:
                with st.spinner("📡 Fetching grant requirements..."):
                    success, content = fetch_from_url(result)
                    if success:
                        st.session_state.grant_requirements = content
                        st.success(f"✅ Loaded {len(content.split())} words")
                        with st.expander("Preview"):
                            st.text_area("", content[:1000] + "...", height=200, disabled=True)
                    else:
                        st.error(f"❌ {content}")
            else:
                st.warning(f"⚠️ {result}")
    
    with tab2:
        st.markdown("""
        <div class='info-box'>
            📄 Upload grant requirements (PDF, Word, or text)
        </div>
        """, unsafe_allow_html=True)
        
        uploaded_file = st.file_uploader(
            "Upload",
            type=ALLOWED_FILE_TYPES,
            label_visibility="collapsed"
        )
        
        if uploaded_file:
            try:
                ext = uploaded_file.name.split('.')[-1].lower()
                
                if ext == 'txt':
                    content = uploaded_file.read().decode('utf-8', errors='ignore')
                elif ext == 'pdf':
                    from url_fetcher import extract_pdf_text
                    success, content = extract_pdf_text(uploaded_file.read())
                    if not success:
                        st.error(f"❌ {content}")
                        content = ""
                elif ext in ['doc', 'docx']:
                    from url_fetcher import extract_word_text
                    success, content = extract_word_text(uploaded_file.read())
                    if not success:
                        st.error(f"❌ {content}")
                        content = ""
                else:
                    st.error("❌ Unsupported file type")
                    content = ""
                
                if content:
                    st.session_state.grant_requirements = content
                    st.success(f"✅ Loaded {len(content.split())} words")
                    with st.expander("Preview"):
                        st.text_area("", content[:1000] + "...", height=200, disabled=True)
                        
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    
    with tab3:
        st.markdown("""
        <div class='info-box'>
            📝 Paste the grant requirements directly
        </div>
        """, unsafe_allow_html=True)
        
        text_input = st.text_area(
            "Requirements",
            value=st.session_state.grant_requirements,
            height=400,
            placeholder="Paste grant requirements here...",
            label_visibility="collapsed"
        )
        
        if text_input:
            st.session_state.grant_requirements = text_input
            st.caption(f"📊 {len(text_input.split())} words")
    
    if st.session_state.grant_requirements:
        st.markdown(f"""
        <div class='success-box'>
            ✅ Grant requirements loaded ({len(st.session_state.grant_requirements.split())} words)
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<div style='margin-top: 2rem;'>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("← Back", use_container_width=True):
            go_to_page('welcome')
    
    with col2:
        if st.session_state.grant_requirements:
            if st.button("Generate Application →", use_container_width=True, type="primary"):
                go_to_page('loading')
        else:
            st.button("Generate Application →", use_container_width=True, disabled=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# ===== LOADING PAGE =====
def loading_page():
    st.markdown("""
    <div class='loading-container'>
        <div class='loading-spinner'></div>
        <h2 class='loading-title'>Generating Your Application...</h2>
        <p class='loading-subtitle'>Using Blythswood's pre-loaded data and past grants</p>
        <div class='loading-steps'>
            <div class='loading-step'>🎨 Analyzing Blythswood's writing style</div>
            <div class='loading-step'>📝 Generating sections</div>
            <div class='loading-step'>✨ Quality checking</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    status_container = st.empty()
    
    def update_status(message):
        status_container.markdown(f"<div class='status-message'>{message}</div>", unsafe_allow_html=True)
    
try:
        # Debug logging
        st.write("DEBUG: API Key exists:", API_KEY is not None and len(API_KEY) > 0)
        st.write("DEBUG: Master doc size:", len(get_master_doc()) if get_master_doc() else 0)
        st.write("DEBUG: Past grants size:", len(get_past_grants()) if get_past_grants() else 0)
        
        success, result, metadata = generate_complete_application(
            grant_requirements=st.session_state.grant_requirements,
            master_doc=get_master_doc(),
            past_grants=get_past_grants(),
            api_key=API_KEY,
            progress_callback=update_status
        )
        
        st.write("DEBUG: Success:", success)
        st.write("DEBUG: Result length:", len(result) if result else 0)
        st.write("DEBUG: Metadata:", metadata)
        
        if success:
            st.session_state.generated_application = result
            st.session_state.metadata = metadata
            time.sleep(1)
            go_to_page('results')
        else:
            st.error(f"❌ Generation failed: {result}")
            st.write("Full error:", result)
            if st.button("Try Again"):
                go_to_page('input')
    
    except Exception as e:
        import traceback
        st.error(f"❌ Exception: {str(e)}")
        st.code(traceback.format_exc())
        if st.button("Try Again"):
            go_to_page('input')
        
        if success:
            st.session_state.generated_application = result
            st.session_state.metadata = metadata
            time.sleep(1)
            go_to_page('results')
        else:
            st.error(f"❌ {result}")
            if st.button("Try Again"):
                go_to_page('input')
    
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
        if st.button("Try Again"):
            go_to_page('input')

# ===== RESULTS PAGE =====
def results_page():
    st.markdown(f"""
    <div class='page-header'>
        <h1>✅ Application Generated</h1>
        <p>Review and download</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class='metrics-row'>
        <div class='metric-card'>
            <div class='metric-value'>{st.session_state.metadata.get('sections_generated', 0)}/{st.session_state.metadata.get('sections_total', 0)}</div>
            <div class='metric-label'>Sections</div>
        </div>
        <div class='metric-card'>
            <div class='metric-value'>{st.session_state.metadata.get('average_quality', 0):.0f}/100</div>
            <div class='metric-label'>Quality</div>
        </div>
        <div class='metric-card'>
            <div class='metric-value'>{len(st.session_state.generated_application.split())}</div>
            <div class='metric-label'>Words</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📥 Download")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        docx_bytes = create_word_document(st.session_state.generated_application, ORGANIZATION)
        st.download_button(
            "📄 Word",
            docx_bytes,
            f"{ORGANIZATION.replace(' ', '_')}_grant.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            use_container_width=True,
            type="primary"
        )
    
    with col2:
        pdf_bytes = create_pdf_document(st.session_state.generated_application, ORGANIZATION)
        st.download_button(
            "📕 PDF",
            pdf_bytes,
            f"{ORGANIZATION.replace(' ', '_')}_grant.pdf",
            mime="application/pdf",
            use_container_width=True,
            type="primary"
        )
    
    with col3:
        txt_content = create_text_file(st.session_state.generated_application)
        st.download_button(
            "📝 Text",
            txt_content,
            f"{ORGANIZATION.replace(' ', '_')}_grant.txt",
            mime="text/plain",
            use_container_width=True,
            type="primary"
        )
    
    st.markdown("---")
    st.markdown("### ✏️ Review and Edit")
    
    edited_text = st.text_area(
        "",
        st.session_state.generated_application,
        height=500,
        label_visibility="collapsed"
    )
    
    if edited_text != st.session_state.generated_application:
        st.session_state.generated_application = edited_text
        st.info("💾 Updated. Re-download to get edited version.")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Generate Another", use_container_width=True):
            st.session_state.grant_requirements = ""
            st.session_state.generated_application = ""
            st.session_state.metadata = {}
            go_to_page('welcome')
    
    with col2:
        if st.button("← Back to Input", use_container_width=True):
            go_to_page('input')

# ===== ROUTER =====
def main():
    if not API_KEY:
        st.error("⚠️ No API key in .env")
        st.stop()
    
    page = st.session_state.page
    
    if page == 'welcome':
        welcome_page()
    elif page == 'input':
        input_page()
    elif page == 'loading':
        loading_page()
    elif page == 'results':
        results_page()

if __name__ == "__main__":
    main()
