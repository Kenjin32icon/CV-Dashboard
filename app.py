import streamlit as st
import sqlite3
import urllib.parse
from datetime import datetime

# --- DATABASE INITIALISATION (SQLite) ---
# Mirrors the Mfano Bora lightweight drop-in database architecture.
def init_db():
    conn = sqlite3.connect('portfolio_leads.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS project_leads
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  date TEXT, 
                  service_type TEXT, 
                  budget TEXT, 
                  timeline TEXT, 
                  analysis_result TEXT)''')
    conn.commit()
    conn.close()

def log_lead(service, budget, timeline, analysis):
    conn = sqlite3.connect('portfolio_leads.db')
    c = conn.cursor()
    c.execute("INSERT INTO project_leads (date, service_type, budget, timeline, analysis_result) VALUES (?, ?, ?, ?, ?)",
              (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), service, budget, timeline, analysis))
    conn.commit()
    conn.close()

init_db()

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Lewis Kariuki | AI & Data Systems Architect",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS: UK UX, FLOATING ANIMATED BUTTON & DARK MODE ---
st.markdown("""
    <style>
    /* Animated Floating WhatsApp/Chat Button */
    .float-whatsapp {
        position: fixed;
        bottom: 25px;
        right: 25px;
        background-color: #25d366;
        color: white !important;
        border-radius: 50px;
        text-align: center;
        box-shadow: 2px 4px 12px rgba(0,0,0,0.3);
        z-index: 9999;
        width: 65px;
        height: 65px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-decoration: none !important;
        transition: all 0.3s ease-in-out;
        animation: pulse-animation 2s infinite;
    }
    
    @keyframes pulse-animation {
        0% { box-shadow: 0 0 0 0 rgba(37, 211, 102, 0.7); }
        70% { box-shadow: 0 0 0 15px rgba(37, 211, 102, 0); }
        100% { box-shadow: 0 0 0 0 rgba(37, 211, 102, 0); }
    }

    .float-whatsapp:hover {
        transform: scale(1.12);
        background-color: #20ba5a;
        animation: none;
        box-shadow: 2px 6px 16px rgba(0,0,0,0.4);
    }
    
    /* Sidebar Image Radius */
    [data-testid="stSidebar"] img {
        border-radius: 50%;
        margin-bottom: 15px;
        border: 2px solid #0066cc;
    }
    
    /* Card Styles for Light/Dark Mode Compatibility */
    .feature-card {
        background-color: #f8fafc;
        padding: 18px;
        border-radius: 10px;
        border-left: 5px solid #0066cc;
        margin-bottom: 15px;
    }
    .highlight-card {
        background-color: #f0fdf4;
        padding: 14px;
        border-radius: 8px;
        border-left: 4px solid #16a34a;
        margin-bottom: 10px;
        color: #14532d;
    }
    .chat-module {
        background-color: #f1f5f9;
        padding: 20px;
        border-radius: 12px;
        border: 2px dashed #94a3b8;
    }

    /* Dark Mode Theme Tuning */
    @media (prefers-color-scheme: dark) {
        .feature-card { background-color: #0f172a; border-left: 5px solid #3b82f6; color: #f8fafc; }
        .highlight-card { background-color: #064e3b; border-left: 4px solid #34d399; color: #f0fdf4; }
        .chat-module { background-color: #1e293b; border: 2px dashed #475569; }
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION & PROFILE ---
with st.sidebar:
    try:
        st.image("Profile pic.jpeg", width=140)
    except Exception:
        st.info("💡 Add 'Profile pic.jpeg' to your application folder.")
    
    st.title("Lewis Kariuki")
    st.markdown("**Data Systems & AI Architect**")
    st.caption("📍 Nairobi, Kenya • C1 English Proficiency")
    
    st.divider()
    st.subheader("Navigation")
    navigation = st.radio(
        "Select Page:",
        ["Home & Capability Overview", "Flagship Systems & Projects", "Qualifications & Education", "AI Service Estimator & Contact"],
        label_visibility="collapsed"
    )

# --- PAGE LOGIC ---

# 1. HOME & OVERVIEW
if navigation == "Home & Capability Overview":
    st.title("⚡ Enterprise Data Portals & Intelligent AI Systems")
    st.subheader("Specialised in Retrieval-Augmented Generation (RAG) & Custom Web Databases")
    
    st.write("""
    I assist businesses and public sector organisations in turning unstructured records into secure, high-speed digital assets. 
    By bridging traditional **Data Digitisation** with **Generative AI Workflows**, I build software solutions that eliminate factual 
    hallucinations, streamline administrative workflows, and enable automated customer engagement.
    """)
    st.divider()
    
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric(label="Enterprise Records Digitised", value="10,000+", delta="Zero-loss indexing")
    with col2: st.metric(label="System Response Time", value="< 200ms", delta="Optimised PHP/PostgreSQL")
    with col3: st.metric(label="AI Hallucination Rate", value="0.0%", delta="Strict RAG Architecture")
    with col4: st.metric(label="Industry Certifications", value="3 Awards", delta="IBM & FreeCodeCamp")
    st.divider()

    st.subheader("🛠️ Technical Specialisations")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""<div class="feature-card"><h4>🤖 AI & RAG Architecture</h4><ul><li>Groq API (Llama-3.3-70b)</li><li>PostgreSQL (<code>pgvector</code>)</li><li>HuggingFace Transformers</li></ul></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class="feature-card"><h4>🌐 Custom Backend & Web</h4><ul><li>Vanilla PHP & PDO REST APIs</li><li>Node.js / Express Architecture</li><li>React.js & Tailwind CSS</li></ul></div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""<div class="feature-card"><h4>📊 Data Operations & Auditing</h4><ul><li>Large-Scale Digitisation</li><li>Dublin Core & OAIS Standards</li><li>Python (Pandas, NumPy) Analytics</li></ul></div>""", unsafe_allow_html=True)

# 2. FLAGSHIP SYSTEMS & PROJECTS
elif navigation == "Flagship Systems & Projects":
    st.title("💼 Case Studies & Live Technical Implementations")
    tab1, tab2, tab3, tab4 = st.tabs(["🤖 AI Chatbot", "📂 Resource Portal", "🎓 TU-K Mapping", "🏛️ Data Digitisation"])
    
    with tab1:
        st.subheader("Mfano Bora AI Chatbot System (Ongoing Development)")
        st.caption("Role: AI System Architect | Stack: Python, PostgreSQL (pgvector), Groq API")
        st.markdown('<div class="highlight-card"><b>📌 Vector Search Engine:</b> Automated Python pipelines extract, chunk, and embed web contents using HuggingFace Sentence Transformers into a PostgreSQL database.</div>', unsafe_allow_html=True)

    with tab2:
        st.subheader("Mfano Bora Resources Portal (Production)")
        st.caption("Role: Lead Backend Architect | Stack: PHP, PostgreSQL (GIN Indexing), Vanilla JS")
        st.markdown('<div class="highlight-card"><b>🔍 High-Speed Querying:</b> Designed PostgreSQL tables using Generalized Inverted Indexes (GIN) for instant full-text search.</div>', unsafe_allow_html=True)

    with tab3:
        st.subheader("TU-K Talent Pipeline & AI Career Mapping System")
        st.caption("Role: Lead Developer | Stack: Node.js, Express, MongoDB Atlas, Groq AI SDK")
        st.link_button("🌐 Launch TUK-Map Portal", "https://tuk-mapping-system-frontend.vercel.app")

    with tab4:
        st.subheader("Data Entry & Document Digitisation | COSEKE Kenya Ltd")
        st.write("Managed high-volume document extraction for Kenya Police HQ, KPLC, and ICT Authority.")

# 3. QUALIFICATIONS & EDUCATION
elif navigation == "Qualifications & Education":
    st.title("🎓 Education & Professional Accreditations")
    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.subheader("🏫 Academic Qualifications")
        st.write("**BSc Information Science (Informatics)** - Technical University of Kenya (2026)")
    with col2:
        st.subheader("📜 Industry Certifications")
        st.info("🥇 IBM Business Intelligence Analyst (Mastery Award)")
        st.info("🥈 IBM Data Science Practitioner")

# 4. AI SERVICE ESTIMATOR & CONTACT (The Scope Analysis Engine)
elif navigation == "AI Service Estimator & Contact":
    st.title("🤖 Free Project Scope & Cost Analysis")
    st.write("Let's calculate the feasibility, time, and budget for your data system. Answer 3 simple questions below.")
    
    st.markdown('<div class="chat-module">', unsafe_allow_html=True)
    
    # Scope Form
    with st.form("scope_engine_form"):
        service_type = st.selectbox("1. What type of system do you need developed?", 
            ["Custom Web Portal & Database (PHP/PostgreSQL)", 
             "Zero-Hallucination AI Chatbot (RAG/Groq)", 
             "Enterprise Data Digitisation & Structuring",
             "Other Custom Software"])
        
        budget = st.select_slider("2. What is your estimated project budget?", 
            options=["Under KES 50,000", "KES 50k - 150k", "KES 150k - 300k", "KES 300k+"])
        
        timeline = st.radio("3. What is your expected timeline?", 
            ["ASAP (Rush Build)", "Within 1 Month", "1 - 3 Months", "Flexible"])
        
        submitted = st.form_submit_button("🧠 Analyse My Project Scope")
        
    if submitted:
        st.success("Analysis Complete! Review your recommendations below:")
        
        # Scope Logic Engine
        analysis = ""
        if "Web Portal" in service_type:
            if budget == "Under KES 50,000":
                analysis = "Your budget is best suited for a lightweight template modification. A fully custom PostgreSQL portal with RBAC security typically requires a slightly higher tier. However, we can build a stripped-down MVP within your timeframe."
            else:
                analysis = f"Excellent. With a budget of {budget} over a '{timeline}' timeline, we can implement a highly secure, event-driven web portal with GIN indexing for high-speed document search."
        elif "AI Chatbot" in service_type:
            if budget in ["Under KES 50,000", "KES 50k - 150k"]:
                analysis = "For this tier, we can integrate a standard fallback-enabled chatbot. To achieve true Zero-Hallucination via pgvector and the Groq API (including data ingestion), we can structure a phased rollout starting with your core FAQs."
            else:
                analysis = "This is a perfect fit. We will design a custom Retrieval-Augmented Generation (RAG) pipeline that guarantees the AI answers *strictly* from your corporate documents."
        else:
            analysis = f"Based on your budget of {budget} and '{timeline}' timeline, I will draft a custom implementation plan focusing on data integrity and OAIS archival standards."
        
        st.info(f"**Architect's Note:** {analysis}")
        
        # Log to SQLite
        log_lead(service_type, budget, timeline, analysis)
        
        # Generate WhatsApp Redirect Link
        whatsapp_message = f"Hello Lewis, I completed the project estimator on your portfolio.\n\n*Service:* {service_type}\n*Budget:* {budget}\n*Timeline:* {timeline}\n\nI would like to book a service appointment to discuss this further."
        encoded_message = urllib.parse.quote(whatsapp_message)
        wa_link = f"https://wa.me/254746668098?text={encoded_message}"
        
        st.markdown("### 📅 Next Step: Book Your Appointment")
        st.write("Click below to send these exact details securely to my WhatsApp and finalize your consultation.")
        st.link_button("📱 Send Scope to Lewis via WhatsApp", wa_link, type="primary", use_container_width=True)
        
        # Fallback Protocol
        st.caption("⚠️ **Fallback Protocol:** If WhatsApp is unavailable or you prefer a voice call, please dial **+254 746 668 098** directly or send an email to kariukilewis04@gmail.com.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# --- FLOATING WHATSAPP ACTION BUTTON ---
# This button pulses to attract attention regardless of the page the user is on.
default_wa = "https://wa.me/254746668098?text=Hello%20Lewis,%20I%20am%20interested%20in%20your%20services.%20Can%20we%20chat?"
st.markdown(f"""
    <a href="{default_wa}" target="_blank" class="float-whatsapp" title="Chat on WhatsApp">
        <svg xmlns="http://www.w3.org/2000/svg" width="35" height="35" fill="currentColor" class="bi bi-whatsapp" viewBox="0 0 16 16">
          <path d="M13.601 2.326A7.85 7.85 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c0 1.399.366 2.76 1.057 3.965L0 16l4.204-1.102a7.9 7.9 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.9 7.9 0 0 0 13.6 2.326zM7.994 14.521a6.6 6.6 0 0 1-3.356-.92l-.24-.144-2.494.654.666-2.433-.156-.251a6.56 6.56 0 0 1-1.007-3.505c0-3.626 2.957-6.584 6.591-6.584a6.56 6.56 0 0 1 4.66 1.931 6.56 6.56 0 0 1 1.928 4.66c-.004 3.639-2.961 6.592-6.592 6.592m3.615-4.934c-.197-.099-1.17-.578-1.353-.646-.182-.065-.315-.099-.445.099-.133.197-.513.646-.627.775-.114.133-.232.148-.43.05-.197-.1-.836-.308-1.592-.985-.59-.525-.985-1.175-1.103-1.372-.114-.198-.011-.304.088-.403.087-.088.197-.232.296-.346.1-.114.133-.198.198-.33.065-.134.034-.248-.015-.347-.05-.099-.445-1.076-.612-1.47-.16-.389-.323-.335-.445-.34-.114-.007-.247-.007-.38-.007a.73.73 0 0 0-.529.247c-.182.198-.691.677-.691 1.654s.71 1.916.81 2.049c.098.133 1.394 2.132 3.383 2.992.47.205.84.326 1.129.418.475.152.904.129 1.246.08.38-.058 1.171-.48 1.338-.943.164-.464.164-.86.114-.943-.049-.084-.182-.133-.38-.232z"/>
        </svg>
    </a>
    """, unsafe_allow_html=True)