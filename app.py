import streamlit as st
import sqlite3
import urllib.parse
from datetime import datetime
import os

# Try importing Groq client; handle gracefully if not installed
try:
    from groq import Groq
    GROQ_AVAILABLE = True
except ImportError:
    GROQ_AVAILABLE = False

# --- DATABASE INITIALISATION (SQLite Lead Logger) ---
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

# --- CUSTOM CSS: UK UX, FLOATING ANIMATED BUTTON & STYLING ---
st.markdown("""
    <style>
    /* Animated Floating WhatsApp Button */
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
    
    /* Card Styles */
    .feature-card {
        background-color: #f8fafc;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #0066cc;
        margin-bottom: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .highlight-card {
        background-color: #f0fdf4;
        padding: 16px;
        border-radius: 8px;
        border-left: 4px solid #16a34a;
        margin-bottom: 10px;
        color: #14532d;
    }
    .psych-banner {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
        padding: 30px;
        border-radius: 12px;
        color: white;
        margin-bottom: 25px;
    }

    /* Dark Mode Tuning */
    @media (prefers-color-scheme: dark) {
        .feature-card { background-color: #0f172a; border-left: 5px solid #3b82f6; color: #f8fafc; }
        .highlight-card { background-color: #064e3b; border-left: 4px solid #34d399; color: #f0fdf4; }
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION & PROFILE ---
with st.sidebar:
    try:
        st.image("Profile pic.jpeg", width=140)
    except Exception:
        st.info("💡 Add 'Profile pic.jpeg' to your folder.")
    
    st.title("Lewis Kariuki")
    st.markdown("**Data Systems & AI Architect**")
    st.caption("📍 Nairobi, Kenya • C1 English Proficiency")
    
    st.divider()
    st.subheader("Navigation")
    navigation = st.radio(
        "Select Page:",
        ["Home & Capability Overview", "AI Groq Assistant", "Flagship Systems & Projects", "Qualifications & Education", "Project Scope & Cost Analysis"],
        label_visibility="collapsed"
    )
    
    st.divider()
    st.markdown("💬 **Direct Contact:**")
    st.markdown("[📱 WhatsApp Chat](https://wa.me/254746668098?text=Hello%20Lewis,%20I%20am%20interested%20in%20your%20services.)")

# --- PAGE LOGIC ---

# 1. HOME & CAPABILITY OVERVIEW (Psychologically Optimised)
if navigation == "Home & Capability Overview":
    st.markdown("""
        <div class="psych-banner">
            <h1>Stop Losing Revenue to Slow Databases & Flawed AI.</h1>
            <p style="font-size: 1.1rem; margin-top: 10px;">
                Most business software is bloated, and most AI chatbots hallucinate wrong answers. 
                I bridge Information Science with high-performance engineering to build <b>secure PostgreSQL web portals</b> 
                and <b>Zero-Hallucination RAG AI systems</b> that protect your brand and automate customer conversion.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1], gap="large")
    with col1:
        st.subheader("👋 Who I Am & What I Solve")
        st.write("""
        I am **Lewis Kariuki**, a Full-Stack Data Analyst and Systems Architect. Having managed large-scale enterprise 
        digitisation projects for institutions like the **Kenya Police HQ, KPLC, and the ICT Authority**, I understand 
        that businesses do not just need "code"—they need reliable systems that eliminate administrative bottlenecks, secure sensitive records, 
        and deliver lightning-fast data retrieval.
        """)
        
        st.subheader("🛠️ Core Services Offered")
        st.markdown("""
        * **Custom Web Portals & Databases:** Lightweight, high-speed PHP/PostgreSQL applications featuring GIN indexing and Role-Based Access Control (RBAC).
        * **Zero-Hallucination AI Chatbots:** RAG architecture using Groq API (`llama-3.3-70b`) and `pgvector` to ensure customer queries are answered *strictly* from your corporate knowledge base.
        * **Enterprise Data Digitisation:** Archival structuring, cleaning, and metadata indexing following international Dublin Core and OAIS frameworks.
        """)
    
    with col2:
        st.info("💡 **Ready to scale your operations?**\n\nSkip the guesswork. Calculate your exact system timeline and budget instantly using my interactive cost engine.")
        if st.button("🚀 Calculate Project Scope & Cost", type="primary", use_container_width=True):
            st.switch_page = True # Note: Streamlit handles radio navigation via state or user click
            st.info("Please select 'Project Scope & Cost Analysis' from the sidebar navigation menu.")

    st.divider()
    
    # Quick Performance Metrics
    st.subheader("Proven Track Record At a Glance")
    m1, m2, m3, m4 = st.columns(4)
    with m1: st.metric(label="Records Digitised", value="10,000+", delta="Zero-loss indexing")
    with m2: st.metric(label="Query Speed", value="< 200ms", delta="Optimised PHP/PostgreSQL")
    with m3: st.metric(label="AI Hallucination Rate", value="0.0%", delta="Strict RAG Guardrails")
    with m4: st.metric(label="Global Certifications", value="3 Awards", delta="IBM & FreeCodeCamp")

# 2. AI GROQ ASSISTANT (Interactive Chat Module)
elif navigation == "AI Groq Assistant":
    st.title("🤖 Chat with Lewis's AI Assistant (Powered by Groq)")
    st.write("""
    This interactive module runs on the **Groq API (Llama-3.3-70b)**, simulating the exact Retrieval-Augmented Generation (RAG) 
    architecture Lewis builds for enterprise clients. Ask about his technical stack, past projects at COSEKE or Mfano Bora, 
    or how to commission a custom web system.
    """)
    
    # API Key Input
    groq_api_key = st.text_input("Enter your Groq API Key (or use default demo session if configured):", type="password")
    
    if not GROQ_AVAILABLE:
        st.error("The `groq` Python package is not installed. Run `pip install groq` in your terminal.")
    else:
        # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = [
                {"role": "assistant", "content": "Hello! I am Lewis Kariuki's AI assistant. Ask me anything about his data systems, PHP/PostgreSQL backend work, or AI RAG chatbot projects. How can I help you today?"}
            ]

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("Ask about Lewis's skills, pricing, or system architectures..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                if not groq_api_key:
                    response_text = "Please enter a valid Groq API key above to enable live inference, or reach out to Lewis directly via WhatsApp!"
                    st.markdown(response_text)
                else:
                    try:
                        client = Groq(api_key=groq_api_key)
                        system_prompt = """You are Lewis Kariuki's professional AI sales assistant and technical representative. 
                        Lewis is an Information Scientist, Full-Stack AI Developer, and Data Analyst based in Nairobi, Kenya, graduating in 2026 from the Technical University of Kenya. 
                        He specialises in:
                        1. Custom PHP & PostgreSQL web portals (with GIN full-text indexing).
                        2. Zero-hallucination RAG AI chat systems using Groq API (Llama-3.3-70b) and pgvector.
                        3. Enterprise document digitisation and metadata cataloguing (Dublin Core / OAIS standards).
                        Keep answers concise, professional, and always encourage the user to visit the 'Project Scope & Cost Analysis' page or click the WhatsApp button to book an appointment with Lewis."""
                        
                        messages = [{"role": "system", "content": system_prompt}] + [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
                        
                        chat_completion = client.chat.completions.create(
                            model="llama-3.3-70b-versatile",
                            messages=messages,
                            temperature=0.3,
                            max_completion_tokens=500
                        )
                        response_text = chat_completion.choices[0].message.content
                        st.markdown(response_text)
                    except Exception as e:
                        response_text = f"Error connecting to Groq API: {str(e)}"
                        st.error(response_text)
                
                st.session_state.messages.append({"role": "assistant", "content": response_text})

# 3. FLAGSHIP SYSTEMS & PROJECTS
elif navigation == "Flagship Systems & Projects":
    st.title("💼 Enterprise Systems & Case Studies")
    st.write("Explore production-grade architectures built for real-world enterprise operations.")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🤖 Mfano Bora AI Chatbot", "📂 Resources Portal", "🎓 TU-K Career Mapping", "🏛️ Enterprise Digitisation"])
    
    with tab1:
        st.subheader("Mfano Bora AI Chatbot System (Ongoing)")
        st.caption("Role: AI System Architect | Stack: Python, PostgreSQL (pgvector), Groq API (Llama-3.3-70b)")
        st.write("Engineered a Retrieval-Augmented Generation (RAG) pipeline to restrict the LLM to answering solely from a verified corporate knowledge base, eliminating hallucinations.")
        st.markdown('<div class="highlight-card"><b>📌 Vector Embedding Pipeline:</b> Python scripts clean, chunk, and embed scraped data using HuggingFace Sentence Transformers into PostgreSQL `pgvector`.</div>', unsafe_allow_html=True)

    with tab2:
        st.subheader("Mfano Bora Resources Portal (Production)")
        st.caption("Role: Lead Backend Architect | Stack: PHP, PostgreSQL (GIN Indexing), Vanilla JS")
        st.write("Refactored backend infrastructure into a lightweight, high-speed PHP and Vanilla JavaScript stack to securely manage organisational assets.")
        st.markdown('<div class="highlight-card"><b>🔍 High-Speed Indexing:</b> Designed normalized PostgreSQL tables featuring Generalized Inverted Indexes (GIN) for instant full-text searching.</div>', unsafe_allow_html=True)

    with tab3:
        st.subheader("TU-K Talent Pipeline & AI Career Mapping")
        st.caption("Role: Lead Developer | Stack: Node.js, Express, MongoDB Atlas, Groq AI SDK")
        st.write("Engineered a web application parsing student CVs to translate academic coursework into marketable tech industry offerings.")
        st.link_button("🌐 Launch Live System", "https://tuk-mapping-system-frontend.vercel.app")

    with tab4:
        st.subheader("Data Entry & Digitisation | COSEKE Kenya Ltd")
        st.caption("May 2023 – February 2025 | Nairobi, Kenya")
        st.write("Managed high-volume document extraction, cleaning, and indexing for enterprise clients including Kenya Police HQ, KPLC, and the ICT Authority.")

# 4. QUALIFICATIONS & EDUCATION
elif navigation == "Qualifications & Education":
    st.title("🎓 Education & Professional Accreditations")
    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.subheader("🏫 Academic Qualifications")
        st.markdown("""
        **Bachelor of Science in Information Science (Informatics)**  
        *Technical University of Kenya (Graduating 2026)*
        
        **Core Focus Areas:** Database Design & Management, Enterprise IT Systems, Software Programming (Python, JavaScript, PHP), Information Security & Auditing.
        """)
    with col2:
        st.subheader("📜 Industry Certifications")
        st.info("🥇 **IBM Business Intelligence Analyst** (Mastery Award)")
        st.caption("[Verify Credential](https://www.credly.com/badges/a49e015a-a78d-4b5f-96d8-b629798a627f/print)")
        
        st.info("🥈 **IBM Data Science Practitioner** (Professional Certificate)")
        st.caption("[Verify Credential](https://www.credly.com/badges/97142d0d-2d08-48fd-8e09-7b35723d97cf/print)")
        
        st.info("🥉 **Responsive Web Design** (freeCodeCamp)")
        st.caption("[Verify Credential](https://www.freecodecamp.org/certification/Kenjin32icon/responsive-web-design)")

# 5. PROJECT SCOPE & COST ANALYSIS
elif navigation == "Project Scope & Cost Analysis":
    st.title("🤖 Project Scope, Time & Cost Estimator")
    st.write("Configure your requirements below. Our analysis engine will evaluate your timeline, technical scope, and provide a direct booking link.")
    
    with st.form("scope_engine_form"):
        service_type = st.selectbox("1. Select Required Service:", [
            "Custom Web Portal & Database (PHP/PostgreSQL)", 
            "Zero-Hallucination AI Chatbot (RAG/Groq)", 
            "Enterprise Data Digitisation & Structuring",
            "Full-Stack Software Architecture Consultation"
        ])
        
        budget = st.select_slider("2. Estimated Project Budget:", options=[
            "Under KES 50,000", "KES 50k - 150k", "KES 150k - 300k", "KES 300k+"
        ])
        
        timeline = st.radio("3. Expected Timeline:", [
            "ASAP (Rush Implementation)", "Within 1 Month", "1 - 3 Months", "Flexible / Long-term"
        ])
        
        submitted = st.form_submit_button("🧠 Run Scope Analysis")
        
    if submitted:
        st.success("Analysis Complete! Review your custom recommendations below:")
        
        # Scope Analysis Logic
        analysis = f"For a '{service_type}' with a budget of '{budget}' over a '{timeline}' timeframe, our engineering team recommends structuring the project into phased milestones focusing on secure database indexing and zero-loss data validation."
        st.info(f"**Architect's Note:** {analysis}")
        
        # Log lead in SQLite
        log_lead(service_type, budget, timeline, analysis)
        
        # WhatsApp redirect payload
        whatsapp_msg = f"Hello Lewis, I ran the scope estimator on your portfolio.\n\n*Service:* {service_type}\n*Budget:* {budget}\n*Timeline:* {timeline}\n\nI would like to book a service appointment."
        encoded_msg = urllib.parse.quote(whatsapp_msg)
        wa_url = f"https://wa.me/254746668098?text={encoded_msg}"
        
        st.markdown("### 📅 Next Step: Book Your Consultation")
        st.link_button("📱 Send Scope to Lewis via WhatsApp", wa_url, type="primary", use_container_width=True)
        st.caption("⚠️ **Fallback Protocol:** If WhatsApp is unavailable, call **+254 746 668 098** or email **kariukilewis04@gmail.com**.")

# --- FLOATING WHATSAPP ACTION BUTTON ---
default_wa_url = "https://wa.me/254746668098?text=Hello%20Lewis,%20I%20visited%20your%20portfolio%20and%20would%20like%20to%20discuss%20a%20project."
st.markdown(f"""
    <a href="{default_wa_url}" target="_blank" class="float-whatsapp" title="Chat on WhatsApp">
        <svg xmlns="http://www.w3.org/2000/svg" width="35" height="35" fill="currentColor" class="bi bi-whatsapp" viewBox="0 0 16 16">
          <path d="M13.601 2.326A7.85 7.85 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c0 1.399.366 2.76 1.057 3.965L0 16l4.204-1.102a7.9 7.9 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.9 7.9 0 0 0 13.6 2.326zM7.994 14.521a6.6 6.6 0 0 1-3.356-.92l-.24-.144-2.494.654.666-2.433-.156-.251a6.56 6.56 0 0 1-1.007-3.505c0-3.626 2.957-6.584 6.591-6.584a6.56 6.56 0 0 1 4.66 1.931 6.56 6.56 0 0 1 1.928 4.66c-.004 3.639-2.961 6.592-6.592 6.592m3.615-4.934c-.197-.099-1.17-.578-1.353-.646-.182-.065-.315-.099-.445.099-.133.197-.513.646-.627.775-.114.133-.232.148-.43.05-.197-.1-.836-.308-1.592-.985-.59-.525-.985-1.175-1.103-1.372-.114-.198-.011-.304.088-.403.087-.088.197-.232.296-.346.1-.114.133-.198.198-.33.065-.134.034-.248-.015-.347-.05-.099-.445-1.076-.612-1.47-.16-.389-.323-.335-.445-.34-.114-.007-.247-.007-.38-.007a.73.73 0 0 0-.529.247c-.182.198-.691.677-.691 1.654s.71 1.916.81 2.049c.098.133 1.394 2.132 3.383 2.992.47.205.84.326 1.129.418.475.152.904.129 1.246.08.38-.058 1.171-.48 1.338-.943.164-.464.164-.86.114-.943-.049-.084-.182-.133-.38-.232z"/>
        </svg>
    </a>
    """, unsafe_allow_html=True)