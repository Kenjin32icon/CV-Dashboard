import streamlit as st
import pandas as pd

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Lewis Kariuki | AI & Data Portfolio", page_icon="📊", layout="wide")

# --- CUSTOM CSS FOR FLOATING BUTTON, STYLING & DARK MODE ---
st.markdown("""
    <style>
    /* Floating WhatsApp Button */
    .float-btn {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background-color: #25d366;
        color: white;
        border-radius: 50px;
        text-align: center;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.3);
        z-index: 100;
        width: 60px;
        height: 60px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-decoration: none;
        transition: transform 0.3s ease;
    }
    .float-btn:hover {
        transform: scale(1.1);
    }
    
    /* Sidebar Image Styling */
    [data-testid="stSidebar"] img {
        border-radius: 50%;
        margin-bottom: 20px;
    }
    
    /* DEFAULT LIGHT MODE: Tech Stack & Achievements */
    .tech-stack {
        background-color: #f0f7ff;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #0066cc;
        margin: 10px 0;
        height: 100%;
    }
    .achievement-highlight {
        background-color: #e6fced;
        padding: 10px;
        border-radius: 5px;
        border-left: 4px solid #198754;
        margin-bottom: 10px;
    }

    /* DARK MODE OVERRIDES */
    @media (prefers-color-scheme: dark) {
        .tech-stack {
            background-color: #0f172a; /* Deep dark blue */
            border-left: 4px solid #3b82f6; /* Brighter blue border for contrast */
            color: #f8fafc; /* Crisp white text */
        }
        .achievement-highlight {
            background-color: #064e3b; /* Deep dark green */
            border-left: 4px solid #34d399; /* Brighter green border for contrast */
            color: #f8fafc; /* Crisp white text */
        }
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    # Profile Picture Placeholder
    try:
        st.image("Profile pic.jpeg", width=150)
    except:
        st.info("Upload 'Profile pic.jpeg' to your directory to show your photo.")
    
    st.title("Lewis Kariuki")
    st.caption("Full-Stack AI Developer & Data Analyst")
    
    st.divider()
    st.subheader("Navigation")
    selection = st.radio("Go to:", ["Home & Overview", "Experience & Projects", "Education & Certifications"])

# --- PAGE LOGIC ---

# 1. HOME PAGE
if selection == "Home & Overview":
    st.header("👋 Welcome to My Interactive Portfolio")
    st.write("""
    I am an Information Scientist who bridges the gap between **Data Analysis** and **Intelligent Web Systems**. 
    From managing large-scale data digitisation projects for major enterprises to building automated AI platforms, 
    I create software solutions that transform complex data into clear, actionable business insights.
    """)
    
    st.divider()
    
    # Quick Metrics
    st.subheader("Career Highlights At a Glance")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="🏗️ Enterprise Systems Built", value="1+", delta="Launched this year")
    with col2:
        st.metric(label="⏱️ Years Data Experience", value="1.8", delta="Continuous growth")
    with col3:
        st.metric(label="📜 Professional Certs", value="3+", delta="IBM & FreeCodeCamp")
    with col4:
        st.metric(label="📊 Records Processed", value="10k+", delta="High accuracy rate")

    st.divider()

    # Core Competencies 
    st.subheader("🛠️ Core Technical Stack")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="tech-stack"><b>🌐 Full-Stack Development:</b><br>React.js • Node.js • Express<br>MongoDB Atlas • Firebase<br>Groq AI Integration</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="tech-stack"><b>📈 Data Science & Analytics:</b><br>Python (Pandas, Numpy)<br>IBM Cognos Analytics<br>SQL • QGIS</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="tech-stack"><b>☁️ Cloud & Architecture:</b><br>Vercel • Render<br>Google Cloud APIs<br>Automated Data Pipelines</div>', unsafe_allow_html=True)

# 2. EXPERIENCE & PROJECTS PAGE
elif selection == "Experience & Projects":
    st.header("💼 Professional Experience & Systems Built")
    st.write("Click through the tabs below to explore my recent roles and flagship technical projects.")
    
    # Using Tabs for better UX (prevents endless scrolling)
    tab1, tab2, tab3, tab4 = st.tabs(["🚀 TUK-Map AI Platform", "💻 COSEKE Kenya Ltd", "🗺️ Historical Mapping", "🎬 Digital Media Production"])
    
    with tab1:
        st.subheader("TUK-Map AI: Intelligent Graduate Job Mapping System")
        st.caption("Lead Architect & Developer | Technical University of Kenya")
        st.write("""
        **The Challenge:** Graduates often struggle to map their academic coursework to real-world job requirements.  
        **The Solution:** I designed and built an intelligent web platform that reads student CVs and automatically translates their university skills into marketable technology services.
        """)
        
        st.markdown('<div class="achievement-highlight"><b>🤖 AI Integration:</b> Programmed an AI tool (using Llama-3) to read complex documents and generate a clean, unified profile for each user.</div>', unsafe_allow_html=True)
        st.markdown('<div class="achievement-highlight"><b>🏗️ System Architecture:</b> Built a highly responsive web application using React and Node.js, ensuring reliable and secure data storage with MongoDB.</div>', unsafe_allow_html=True)
        st.markdown('<div class="achievement-highlight"><b>🔐 Security:</b> Engineered strict login controls, allowing administrators to safely manage user access and permissions on the fly.</div>', unsafe_allow_html=True)
        st.markdown('<div class="achievement-highlight"><b>📊 Data Automation:</b> Created background processes that instantly send real-time performance metrics straight to Google Sheets for easy viewing.</div>', unsafe_allow_html=True)
        
        st.link_button("🔗 Visit Live System", "https://tuk-mapping-system-frontend.vercel.app", use_container_width=False)

    with tab 2("💻 Data Entry Clerk | COSEKE KENYA LIMITED", expanded=True):
   # --- COSEKE SECTION ---

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
    with tab3:
        st.subheader("Digitisation of Historical Maps")
        st.caption("Research Project | Presented at the Kenyan National Museum (Nov 2025)")
        st.write("A comprehensive archival project focused on preserving historical geographical data using modern digital tools.")
        st.write("- **Cost-Effective Design:** Developed a highly efficient digitisation process using open-source mapping software (QGIS).")
        st.write("- **Archival Standards:** Ensured all historical data was catalogued perfectly according to strict international archiving standards (OAIS framework).")

    with tab4:
        st.subheader("Media Production Team Member")
        st.caption("Mar 2025 - Present | ACK St. Peters Kahawa Sukari Church")
        st.write("Managing technical audio/visual operations to enhance the church's digital presence and community outreach.")
        st.write("- Directed and managed live video broadcasts for weekly youth services.")
        st.write("- Operated professional camera equipment and soundboards to ensure high-quality live streaming.")

# 3. EDUCATION & CERTS PAGE
elif selection == "Education & Certifications":
    st.header("🎓 Education & Certifications")
    st.write("A foundation in Informatics backed by globally recognised industry credentials.")
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.subheader("🏫 University Education")
        st.markdown("""
        **Bachelor of Science in Information Science (Informatics)** *Technical University of Kenya* **Expected Graduation:** 2026
        
        **Relevant Coursework:**
        * Database Design & Management
        * Software Programming (Java, Python, JavaScript)
        * Enterprise IT Systems
        * Information Security & Auditing
        * Research Methodologies
        """)
    
    with col2:
        st.subheader("🏆 Professional Certifications")
        st.info("🥇 **IBM Business Intelligence Analyst** (Mastery)", icon="✅")
        st.caption("[View Credential](https://www.credly.com/badges/a49e015a-a78d-4b5f-96d8-b629798a627f/print)")
        
        st.info("🥈 **IBM Data Science Practitioner** (Professional)", icon="✅")
        st.caption("[View Credential](https://www.credly.com/badges/97142d0d-2d08-48fd-8e09-7b35723d97cf/print)")
        
        st.info("🥉 **Responsive Web Design** (FreeCodeCamp)", icon="✅")
        st.caption("[View Credential](https://www.freecodecamp.org/certification/Kenjin32icon/responsive-web-design)")

# --- FLOATING WHATSAPP BUTTON ---
whatsapp_url = "https://wa.me/254746668098?text=Hello%20Lewis,%20I%20viewed%20your%20portfolio%20and%20would%20like%20to%20connect."
st.markdown(f"""
    <a href="{whatsapp_url}" target="_blank" class="float-btn" title="Contact me on WhatsApp">
        <svg xmlns="http://www.w3.org/2000/svg" width="35" height="35" fill="currentColor" class="bi bi-whatsapp" viewBox="0 0 16 16">
          <path d="M13.601 2.326A7.85 7.85 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c0 1.399.366 2.76 1.057 3.965L0 16l4.204-1.102a7.9 7.9 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.9 7.9 0 0 0 13.6 2.326zM7.994 14.521a6.6 6.6 0 0 1-3.356-.92l-.24-.144-2.494.654.666-2.433-.156-.251a6.56 6.56 0 0 1-1.007-3.505c0-3.626 2.957-6.584 6.591-6.584a6.56 6.56 0 0 1 4.66 1.931 6.56 6.56 0 0 1 1.928 4.66c-.004 3.639-2.961 6.592-6.592 6.592m3.615-4.934c-.197-.099-1.17-.578-1.353-.646-.182-.065-.315-.099-.445.099-.133.197-.513.646-.627.775-.114.133-.232.148-.43.05-.197-.1-.836-.308-1.592-.985-.59-.525-.985-1.175-1.103-1.372-.114-.198-.011-.304.088-.403.087-.088.197-.232.296-.346.1-.114.133-.198.198-.33.065-.134.034-.248-.015-.347-.05-.099-.445-1.076-.612-1.47-.16-.389-.323-.335-.445-.34-.114-.007-.247-.007-.38-.007a.73.73 0 0 0-.529.247c-.182.198-.691.677-.691 1.654s.71 1.916.81 2.049c.098.133 1.394 2.132 3.383 2.992.47.205.84.326 1.129.418.475.152.904.129 1.246.08.38-.058 1.171-.48 1.338-.943.164-.464.164-.86.114-.943-.049-.084-.182-.133-.38-.232z"/>
        </svg>
    </a>
    """, unsafe_allow_html=True)