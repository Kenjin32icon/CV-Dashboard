‎import streamlit as st
‎import pandas as pd
‎import plotly.express as px
‎from PIL import Image
‎
‎# --- PAGE CONFIGURATION ---
‎st.set_page_config(page_title="Lewis Kariuki | Data Portfolio", page_icon="📊", layout="wide")
‎
‎# --- CUSTOM CSS FOR FLOATING BUTTON & STYLING ---
‎st.markdown("""
‎    <style>
‎    .float-btn {
‎        position: fixed;
‎        bottom: 20px;
‎        right: 20px;
‎        background-color: #25d366;
‎        color: white;
‎        border-radius: 50px;
‎        text-align: center;
‎        box-shadow: 2px 2px 3px #999;
‎        z-index: 100;
‎        width: 60px;
‎        height: 60px;
‎        display: flex;
‎        align-items: center;
‎        justify-content: center;
‎        text-decoration: none;
‎    }
‎    [data-testid="stSidebar"] img {
‎        border-radius: 50%;
‎    }
‎    </style>
‎    """, unsafe_allow_html=True)
‎
‎# --- SIDEBAR NAVIGATION ---
‎with st.sidebar:
‎    # Profile Picture Placeholder (Ensure 'profile.jpg' is in your folder)
‎    try:
‎        st.image("profile.jpg", width=150)
‎    except:
‎        st.info("Upload 'profile.jpg' to show photo")
‎    
‎    st.title("Lewis Kariuki")
‎    st.subheader("Navigation")
‎    selection = st.radio("Go to:", ["Dashboard Home", "Professional Experience", "Key Projects", "Education & Certs"])
‎    
‎    st.divider()
‎    st.header("🛠️ Core Competencies")
‎    skills_data = pd.DataFrame({
‎        'Skill': ['Data Entry', 'Analysis', 'Visualization', 'Research', 'Digital Media'],
‎        'Proficiency': [95, 90, 85, 85, 75]
‎    })
‎    fig_skills = px.line_polar(skills_data, r='Proficiency', theta='Skill', line_close=True, template="plotly_dark")
‎    fig_skills.update_traces(fill='toself')
‎    st.plotly_chart(fig_skills, use_container_width=True)
‎
‎# --- MAIN SECTIONS ---
‎
‎if selection == "Dashboard Home":
‎    st.title("📊 Lewis Kariuki")
‎    st.subheader("Data Research & Analysis Service Provider")
‎    st.markdown("**📍 Nairobi, Kenya | 📞 +254746668098 | 🔗 [LinkedIn](https://www.linkedin.com/in/lewis-kariuki-7aa753236/) | 🔗 [Github](https://github.com/kenjin32icon)**")
‎    st.write("""
‎    Detail-oriented Data Analyst and Researcher with a strong background in Information Science. 
‎    [span_1](start_span)Expert in transforming raw datasets into actionable insights through rigorous cleaning, analysis, and visualization[span_1](end_span).
‎    """)
‎    st.divider()
‎    
‎    # Quick highlights
‎    col_a, col_b = st.columns(2)
‎    with col_a:
‎        st.info("🚀 **Currently focused on:** Advanced Data Analysis & Machine Learning")
‎    with col_b:
‎        [span_2](start_span)st.success("🏆 **Latest Achievement:** Mapping project presented at Kenyan National Museum[span_2](end_span).")
‎
‎elif selection == "Professional Experience":
‎    st.header("💼 Professional Experience")
‎
‎    # --- COSEKE SECTION ---
‎    with st.expander("Data Entry Clerk | COSEKE KENYA LIMITED", expanded=True):
‎        st.markdown("### **COSEKE KENYA LIMITED**")
‎        st.caption("📅 May 2023 - Feb 2026 (2 yrs 10 mos) | Full-time | On-site (Nairobi County, Kenya)")
‎        st.write("""
‎        COSEKE enabled me to update my knowledge in document digitization procedures, data cleaning, and indexing. 
‎        I participated in digitizing records for various organizations around Nairobi CBD, including:
‎        - **Kenya Police Office** (Sky Park Westlands)
‎        - **Stima Sacco Plaza**
‎        - **Trade Development Bank Tower** (TDB Tower Lenana Road)
‎        """)
‎        
‎        st.write("**Key Contributions:**")
‎        [span_3](start_span)[span_4](start_span)st.write("- **Data Optimization:** Revamped entry procedures to increase accuracy and significantly reduce reporting turnaround time[span_3](end_span)[span_4](end_span).")
‎        [span_5](start_span)[span_6](start_span)st.write("- **Dataset Validation:** Extracted and validated large-scale datasets to ensure high-fidelity information for stakeholders[span_5](end_span)[span_6](end_span).")
‎        [span_7](start_span)[span_8](start_span)st.write("- **Efficiency Automation:** Automated routine data tasks, resulting in measurable improvements in daily operational workflows[span_7](end_span)[span_8](end_span).")
‎        
‎        st.markdown("**Skills:** `Data Entry`, `Data Cleaning`, `Digitization`")
‎
‎    # --- CHURCH SECTION ---
‎    with st.expander("Media Team Member | ACK St. Peters Kahawa Sukari Church", expanded=True):
‎        st.markdown("### **Media Team Apprenticeship**")
‎        st.caption("📅 Mar 2025 - Present (1 yr) | Nairobi County, Kenya")
‎        st.write("I participate in the church Media Team, which has evolved the following skills:")
‎        
‎        [span_9](start_span)[span_10](start_span)st.write("- **Live Production:** Managing live social media broadcasts for Sunday youth services[span_9](end_span)[span_10](end_span).")
‎        [span_11](start_span)[span_12](start_span)st.write("- **Visual Presentation:** Designing and executing presentation slides to enhance delivery and engagement[span_11](end_span)[span_12](end_span).")
‎        [span_13](start_span)[span_14](start_span)st.write("- **Technical Operation:** Serving as a camera operator for high-quality visual capture of events[span_13](end_span)[span_14](end_span).")
‎        
‎        st.markdown("**Skills:** `Live Video Streaming`, `Video Camera Operation`, `Sound Board Operation`")
‎
‎elif selection == "Key Projects":
‎    st.header("🚀 Key Projects & Research")
‎    with st.container(border=True):
‎        st.subheader("🗺️ Digitization of Historical Maps")
‎        st.caption("TU-K & FH Potsdam University | Presented Nov 2025")
‎        st.info("🏛️ Presented at the Kenyan National Museum")
‎        st.write("""
‎        - **[span_15](start_span)Process Design:** Implemented a cost-effective digitization procedure using QGIS and Hugin Panorama[span_15](end_span).
‎        - **[span_16](start_span)Standard Compliance:** Adhered to the Open Archival Information System (OAIS) framework[span_16](end_span).
‎        """)
‎
‎elif selection == "Education & Certs":
‎    st.header("🎓 Education & Certifications")
‎    col1, col2 = st.columns(2)
‎    with col1:
‎        st.subheader("Education")
‎        st.write("**Bachelor of Library & Information Science (Informatics)**")
‎        [span_17](start_span)st.caption("Technical University of Kenya | Current Year 4 Student[span_17](end_span).")
‎    with col2:
‎        st.subheader("Top Certifications")
‎        [span_18](start_span)st.write("🥇 IBM Business Intelligence Analyst[span_18](end_span).")
‎        [span_19](start_span)st.write("🥈 IBM Data Science Practitioner[span_19](end_span).")
‎
‎# --- FLOATING WHATSAPP BUTTON ---
‎whatsapp_url = "https://wa.me/254746668098?text=Hello%20Lewis,%20I%20viewed%20your%20dashboard%20and..."
‎st.markdown(f"""
‎    <a href="{whatsapp_url}" class="float-btn" target="_blank">
‎        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="35px">
‎    </a>
‎    """, unsafe_allow_html=True)
‎
