import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Lewis Kariuki | Data Portfolio", page_icon="📊", layout="wide")

# --- LOAD PROFILE PIC ---
# Use the file name you saved in your folder
profile_pic = "Profile pic.jpeg" 

# --- DISPLAY IN SIDEBAR ---
with st.sidebar:
    # This centers the image and gives it a nice width
    st.image(profile_pic, width=150)
    st.markdown(f"### { 'Lewis Kariuki' }") # Your name from CV [cite: 1]
    
# --- HEADER SECTION ---
st.title("📊 Lewis Kariuki")
st.subheader("Data Research & Analysis Service Provider")
st.markdown("**📍 Nairobi, Kenya | 📞 +254746668098 | 🔗 [LinkedIn](https://www.linkedin.com/in/lewis-kariuki-7aa753236/) | 🔗 [Github](https://github.com/kenjin32icon)**")
st.write("""
Detail-oriented Data Analyst and Researcher with a strong background in Information Science. 
Expert in transforming raw datasets into actionable insights through rigorous cleaning, analysis, and visualization.
""")
st.divider()

# --- SIDEBAR: SKILLS & TOOLS ---
st.sidebar.header("🛠️ Core Competencies")

# Radar chart for skills
skills_data = pd.DataFrame({
    'Skill': ['Data Entry & Mgmt', 'Cleaning & Analysis', 'Visualization', 'Research & Archival', 'Digital Media'],
    'Proficiency': [95, 90, 85, 85, 75]
})

fig_skills = px.line_polar(skills_data, r='Proficiency', theta='Skill', line_close=True,
                           title="Skill Matrix", template="plotly_dark")
fig_skills.update_traces(fill='toself', line_color='#4CAF50')
st.sidebar.plotly_chart(fig_skills, use_container_width=True)

st.sidebar.header("⚙️ Technical Stack")
st.sidebar.write("🟢 **Python & Libraries**")
st.sidebar.caption("Pandas, Numpy, Matplotlib, Seaborn, Streamlit")
st.sidebar.write("🟢 **Data & Analytics**")
st.sidebar.caption("IBM Cognos Analytics, Database Design & Management")
st.sidebar.write("🟢 **Mapping & Digitization**")
st.sidebar.caption("QGIS, Hugin Panorama")
st.sidebar.write("🟢 **Additional Programming**")
st.sidebar.caption("Java, Javascript")

# --- MAIN BODY: EXPERIENCE & PROJECTS ---
col1, col2 = st.columns(2)

with col1:
    st.header("💼 Professional Experience")
    
    with st.expander("Data Entry Clerk | COSEKE LIMITED", expanded=True):
        st.caption("May 2023 - September 2024")
        st.write("""
        - **Data Optimization:** Revamped entry procedures to increase accuracy and significantly reduce reporting turnaround time.
        - **Dataset Validation:** Extracted and validated large-scale datasets to ensure high-fidelity information.
        - **Efficiency Automation:** Automated routine data tasks, resulting in measurable improvements in daily operational workflows.
        """)
        
    with st.expander("Media Team Member | ACK St. Peters Kahawa Sukari Church"):
        st.caption("Ongoing")
        st.write("""
        - **Live Production:** Managed live social media broadcasts for Sunday youth services.
        - **Visual Presentation:** Designed and executed presentation slides.
        - **Technical Operation:** Served as a camera operator for high-quality visual capture.
        """)

with col2:
    st.header("🚀 Key Projects")
    
    with st.container(border=True):
        st.subheader("🗺️ Digitization of Historical Maps")
        st.markdown("*TU-K & FH Potsdam University*")
        # Highlighted the prestigious presentation location
        st.info("🏛️ **Presented at the Kenyan National Museum, November 2025**") 
        st.write("""
        - **Process Design:** Implemented a cost-effective digitization procedure using open-source tools (Hugin Panorama and QGIS).
        - **Metadata Architecture:** Collected multi-stage metadata using Dublin Core elements to create Submission Information Packages (SIP).
        - **Standard Compliance:** Ensured all project outputs adhered to the Open Archival Information System (OAIS) framework.
        """)

st.divider()

# --- EDUCATION & CERTIFICATIONS ---
col3, col4 = st.columns(2)

with col3:
    st.header("🎓 Education")
    st.write("**Bachelor of Information Science (Informatics)**")
    st.write("🏫 *Technical University of Kenya (Current Year 4 Student)*")
    st.write("**Relevant Coursework:**")
    st.caption("""
    Database Design, Development and Management, Programming (Java, Python, Javascript), 
    ICT Networking, Data Management, Research Methodologies, Information Security & Audit, 
    and Enterprise Systems.
    """)

with col4:
    st.header("🏆 Certifications")
    st.info("🥇 **IBM Business Intelligence Analyst** - [IBM Mastery Award](https://www.credly.com/badges/a49e015a-a78d-4b5f-96d8-b629798a627f/print)")
    st.info("🥈 **IBM Data Science Practitioner** - [IBM Practitioner Certificate](https://www.credly.com/badges/97142d0d-2d08-48fd-8e09-7b35723d97cf/print)")
    st.success("🥉 **Responsive Web Design** - [FreeCodeCamp Certificate](https://www.freecodecamp.org/certification/Sage32icon/responsive-web-design)")
    
    # Combined ongoing certifications
    st.warning("⏳ **Data Analysis with Python & Data Science** - freeCodeCamp (Ongoing)")
    
    # --- WHATSAPP FLOATING BUTTON ---
def add_whatsapp_button(phone_number, message="Hello Lewis! I'm interested in your services."):
    import urllib.parse
    encoded_message = urllib.parse.quote(message)
    whatsapp_url = f"https://wa.me/{phone_number}?text={encoded_message}"

    st.markdown(
        f"""
        <style>
        .float-btn {{
            position: fixed;
            bottom: 20px;
            right: 20px;
            background-color: #25d366;
            color: white;
            border-radius: 50px;
            text-align: center;
            font-size: 30px;
            box-shadow: 2px 2px 3px #999;
            z-index: 100;
            width: 60px;
            height: 60px;
            display: flex;
            align-items: center;
            justify-content: center;
            text-decoration: none;
        }}
        </style>
        <a href="{whatsapp_url}" class="float-btn" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="35px">
        </a>
        """,
        unsafe_allow_html=True
    )

# 2. CALL the function at the very bottom of your script with your real number
# Use quotes around the number so Python treats it as a string
add_whatsapp_button("254746668098")
