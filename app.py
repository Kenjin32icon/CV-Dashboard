import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Lewis Kariuki | AI & Data Portfolio", page_icon="📊", layout="wide")

# --- CUSTOM CSS FOR FLOATING BUTTON & STYLING ---
st.markdown("""
    <style>
    .float-btn {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background-color: #25d366;
        color: white;
        border-radius: 50px;
        text-align: center;
        box-shadow: 2px 2px 3px #999;
        z-index: 100;
        width: 60px;
        height: 60px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-decoration: none;
    }
    [data-testid="stSidebar"] img {
        border-radius: 50%;
    }
    .metric-card {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }
    .project-header {
        font-size: 1.3em;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .tech-stack {
        background-color: #f0f7ff;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #0066cc;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    # Profile Picture Placeholder (Ensure 'profile.jpg' is in your folder)
    try:
        st.image("Profile pic.jpeg", width=150)
    except:
        st.info("Upload 'profile.jpg' to show photo")
    
    st.title("Lewis Kariuki")
    st.caption("Full-Stack AI Developer & Data Analyst")
    
    st.subheader("Navigation")
    selection = st.radio("Go to:", ["Dashboard Home", "Projects & Experience", "Education & Certs"])

# --- PAGE LOGIC ---
if selection == "Dashboard Home":
    st.header("👋 Welcome to My Interactive Portfolio")
    st.write("""
    I am an Information Scientist bridging the gap between **Data Analysis** and **Intelligent Web Systems**. 
    From orchestrating large-scale data digitization to architecting full-stack AI career mapping platforms, I build solutions that transform raw data into actionable insights.
    """)
    
    st.divider()
    
    # Quick Metrics
    st.subheader("Career Highlights At a Glance")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="metric-card"><h2>1+</h2><p>Enterprise AI Systems Built</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><h2>1.8</h2><p>Years Digitization Exp.</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><h2>3+</h2><p>IBM / Industry Certs</p></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="metric-card"><h2>10k+</h2><p>Records Digitized & Cleaned</p></div>', unsafe_allow_html=True)

    st.divider()

    # Core Competencies 
    st.subheader("🛠️ Core Technical Stack")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="tech-stack"><b>Full-Stack AI:</b><br>React.js • Node.js • Express<br>MongoDB Atlas • Firebase (RBAC)<br>Groq AI SDK (Llama 3)</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="tech-stack"><b>Data Science:</b><br>Python (Pandas, Numpy, Streamlit)<br>IBM Cognos Analytics<br>SQL • Data Visualization</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="tech-stack"><b>Cloud & DevOps:</b><br>Vercel • Render<br>Google Sheets API<br>Data Pipelines</div>', unsafe_allow_html=True)

elif selection == "Projects & Experience":
    st.header("💼 Professional Experience & Systems Built")
    
    # NEW FLAGSHIP PROJECT - Using st.expander (corrected from st.subheader)
    with st.expander("🚀 TUK-Map AI: Intelligent Graduate to Job Mapping System", expanded=True):
        st.markdown("**Technical University of Kenya**")
        st.caption("Lead Architect & Developer")
        st.write("""
**Overview:** Designed and engineered an enterprise-grade Software as a Service (SaaS) platform to solve graduate unemployment by translating university coursework into marketable tech services.
        """)
        st.markdown('<div class="tech-stack"><b>🤖 AI Integration:</b> Implemented Groq SDK (Llama-3.3-70b) to parse student CVs (PDF/DOCX) and automatically synthesize a "Single Source of Truth" master profile.</div>', unsafe_allow_html=True)
        st.markdown('<div class="tech-stack"><b>🏗️ System Architecture:</b> Built a decoupled stack using React (Frontend), Node.js/Express (Backend), and MongoDB Atlas (Materialized State Storage).</div>', unsafe_allow_html=True)
        st.markdown('<div class="tech-stack"><b>🔐 Security:</b> Engineered strict Role-Based Access Control (RBAC) via Firebase, featuring a Developer Super-Panel for live privilege mutation and system auditing.</div>', unsafe_allow_html=True)
        st.markdown('<div class="tech-stack"><b>📊 Data Pipeline:</b> Developed an event-driven background worker that pushes AI-generated student readiness KPIs directly to live Google Sheets using the Google Cloud API.</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("**Skills:** Python, React, Node.js, MongoDB, Firebase, Google Cloud API, Groq AI")
        with col2:
            st.link_button("🔗 Visit Live System", "https://tuk-mapping-system-frontend.vercel.app", use_container_width=True)
    
    st.divider()

    # --- COSEKE SECTION ---
    with st.expander("💻 Data Entry Clerk | COSEKE KENYA LIMITED", expanded=True):
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("**COSEKE KENYA LIMITED**")
            st.caption("📅 May 2023 - Feb 2025 (1 yrs 10 mos) | Full-time | Nairobi County, Kenya")
        with col2:
            st.metric("Projects", "5+")
        
        st.write("**Organizations Served:**")
        st.write("🏢 Kenya Police Office (Sky Park Westlands) • Stima Sacco Plaza (Ngara) • Trade Development Bank Tower (TDB Tower)")
        st.write("🏢 ICT Authority (GPO TelPosta Towers) • KPLC (Stima Plaza, Nairobi CBD)")
        
        st.markdown("---")
        st.write("**Key Contributions:**")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("✅ **Data Optimization**<br>Revamped entry procedures for higher accuracy & faster turnaround", unsafe_allow_html=True)
        with col2:
            st.markdown("✅ **Dataset Validation**<br>Extracted & validated large-scale datasets for stakeholders", unsafe_allow_html=True)
        with col3:
            st.markdown("✅ **Efficiency Automation**<br>Automated routine tasks for operational improvements", unsafe_allow_html=True)
        
        st.markdown("**Skills:** `Data Entry` • `Data Cleaning` • `Digitization` • `Data Validation`")

    st.divider()

    # --- CHURCH SECTION ---
    with st.expander("🎬 Media Team Member | ACK St. Peters Kahawa Sukari Church", expanded=True):
        st.markdown("**ACK St. Peters Kahawa Sukari Church - Media Team**")
        st.caption("📅 Mar 2025 - Present | Nairobi County, Kenya")
        st.write("Participating in evolving media production capabilities for the church's digital presence and service delivery.")
        
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("📹 **Live Production**<br>Managing live social media broadcasts for Sunday youth services", unsafe_allow_html=True)
        with col2:
            st.markdown("🎨 **Visual Design**<br>Designing and executing presentation slides for enhanced delivery", unsafe_allow_html=True)
        with col3:
            st.markdown("📷 **Camera Operation**<br>Capturing high-quality visual content for events", unsafe_allow_html=True)
        
        st.markdown("**Skills:** `Live Streaming` • `Video Production` • `Sound Engineering` • `Visual Design`")

elif selection == "Key Projects":
    st.header("🚀 Key Projects & Research")
    with st.container(border=True):
        st.subheader("🗺️ Digitization of Historical Maps")
        st.caption("TU-K & FH Potsdam University | Presented Nov 2025")
        st.info("🏛️ Presented at the Kenyan National Museum")
        st.write("""
        - **Process Design:** Implemented a cost-effective digitization procedure using QGIS and Hugin Panorama.
        - **Standard Compliance:** Adhered to the Open Archival Information System (OAIS) framework.
        """)

elif selection == "Education & Certs":
    st.header("🎓 Education & Certifications")
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.subheader("🏫 University Education")
        st.markdown("""
        **Bachelor of Science in Information Science (Informatics)**
        
        📍 *Technical University of Kenya*  
        📊 *Year 4 Student - Graduating 2026*
        
        **Key Coursework:**
        - Database Design & SQL
        - Programming (Java, Python, JavaScript)
        - Enterprise Systems
        - Information Security & Audit
        - Web Development
        """)
    
    with col2:
        st.subheader("🏆 Professional Certifications")
        st.info("🥇 **IBM Business Intelligence Analyst** (Mastery)", icon="✅")
        st.caption("[View Credential](https://www.credly.com/badges/a49e015a-a78d-4b5f-96d8-b629798a627f/print)")
        
        st.info("🥈 **IBM Data Science Practitioner** (Professional)", icon="✅")
        st.caption("[View Credential](https://www.credly.com/badges/97142d0d-2d08-48fd-8e09-7b35723d97cf/print)")
        
        st.info("🥉 **Responsive Web Design** (FreeCodeCamp)", icon="✅")
        st.caption("[View Credential](https://www.freecodecamp.org/certification/Sage32icon/responsive-web-design)")

# --- FLOATING WHATSAPP BUTTON ---
whatsapp_url = "https://wa.me/254746668098?text=Hello%20Lewis,%20I%20viewed%20your%20portfolio%20and%20would%20like%20to%20connect."
st.markdown(f"""
    <a href="{whatsapp_url}" target="_blank" class="float-btn">
        <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-whatsapp" viewBox="0 0 16 16">
          <path d="M13.601 2.326A7.85 7.85 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c0 1.399.366 2.76 1.057 3.965L0 16l4.204-1.102a7.9 7.9 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.9 7.9 0 0 0 13.6 2.326zM7.994 14.521a6.6 6.6 0 0 1-3.356-.92l-.24-.144-2.494.654.666-2.433-.156-.251a6.56 6.56 0 0 1-1.007-3.505c0-3.626 2.957-6.584 6.591-6.584a6.56 6.56 0 0 1 4.66 1.931 6.56 6.56 0 0 1 1.928 4.66c-.004 3.639-2.961 6.592-6.592 6.592m3.615-4.934c-.197-.099-1.17-.578-1.353-.646-.182-.065-.315-.099-.445.099-.133.197-.513.646-.627.775-.114.133-.232.148-.43.05-.197-.1-.836-.308-1.592-.985-.59-.525-.985-1.175-1.103-1.372-.114-.198-.011-.304.088-.403.087-.088.197-.232.296-.346.1-.114.133-.198.198-.33.065-.134.034-.248-.015-.347-.05-.099-.445-1.076-.612-1.47-.16-.389-.323-.335-.445-.34-.114-.007-.247-.007-.38-.007a.73.73 0 0 0-.529.247c-.182.198-.691.677-.691 1.654s.71 1.916.81 2.049c.098.133 1.394 2.132 3.383 2.992.47.205.84.326 1.129.418.475.152.904.129 1.246.08.38-.058 1.171-.48 1.338-.943.164-.464.164-.86.114-.943-.049-.084-.182-.133-.38-.232z"/>
        </svg>
    </a>
    """, unsafe_allow_html=True)