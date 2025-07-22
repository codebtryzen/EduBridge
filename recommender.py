import streamlit as st

# --------------- Custom CSS for Gemini Theme ---------------
def inject_gemini_style():
    st.markdown("""
        <style>
            html, body, [class*="css"]  {
                background: linear-gradient(to right, #0f172a, #1e293b);
                color: #f8fafc;
                font-family: 'Segoe UI', sans-serif;
            }
            .stSelectbox > div, .stTextInput > div, .stButton > button {
                background-color: #1e293b !important;
                color: #f8fafc !important;
                border-radius: 10px;
                border: 1px solid #334155 !important;
            }
            .stButton > button:hover {
                background-color: #10b981 !important;
                color: white !important;
            }
            .recommend-box {
                background-color: #1e293b;
                padding: 20px;
                border-radius: 15px;
                border: 1px solid #334155;
                box-shadow: 0px 4px 12px rgba(16, 185, 129, 0.3);
            }
            .career-title {
                color: #10b981;
                font-size: 24px;
                font-weight: bold;
            }
        </style>
    """, unsafe_allow_html=True)

# --------------- Career Path UI and Logic ---------------
def show_recommendations():
    inject_gemini_style()
    st.markdown("<h1 style='text-align:center;'>🚀 Career Path Recommendations</h1>", unsafe_allow_html=True)

    degree = st.selectbox(
        "Select your field of study:",
        [
            "",
            "BCA",
            "B.Sc. Computer Science",
            "B.Sc. Biology",
            "BA English",
            "B.Com",
            "BBA",
            "Diploma in Art & Design",
            "B.Ed (Education)",
            "B.Sc. Mathematics",
            "B.Tech",
            "BA Psychology",
            "B.Sc. Agriculture",
            "Other"
        ]
    )

    degree_to_fields = {
        "BCA": ["Software Development", "Data Science", "Cybersecurity", "IT Support"],
        "B.Sc. Computer Science": ["Software Development", "AI & ML", "Data Analytics", "Cloud Computing"],
        "B.Sc. Biology": ["Biotech", "Research", "Pharma Sales", "Environmental Science"],
        "BA English": ["Content Writing", "Teaching", "Media & Journalism", "Publishing"],
        "B.Com": ["Accounting", "Banking", "Finance Analysis", "Taxation"],
        "BBA": ["Management", "Marketing", "HR", "Business Analysis"],
        "Diploma in Art & Design": ["Graphic Design", "Animation", "UX/UI Design", "Illustration"],
        "B.Ed (Education)": ["School Teacher", "Curriculum Developer", "Online Tutor", "Educational Consultant"],
        "B.Sc. Mathematics": ["Data Science", "Quantitative Analyst", "Actuarial Science", "Academia"],
        "B.Tech": ["Engineering", "Product Management", "Software Dev", "IoT & Robotics"],
        "BA Psychology": ["Clinical Psychologist", "HR", "Counseling", "Research"],
        "B.Sc. Agriculture": ["Agronomist", "Soil Scientist", "Agri-Tech", "Farming Consultancy"]
    }

    field_to_roles = {
        "software": {
            "roles": ["Software Developer", "Web Developer", "Mobile App Developer"],
            "roadmap": "1. Learn Programming (Python/Java)\n2. Build Projects\n3. Learn Git & GitHub\n4. Explore Frameworks (React, Django)\n5. Contribute to Open Source & Intern"
        },
        "data": {
            "roles": ["Data Analyst", "Data Scientist", "BI Analyst"],
            "roadmap": "1. Master Python & Pandas\n2. Learn SQL\n3. Perform EDA\n4. Study ML Algorithms\n5. Build Dashboards with Power BI/Tableau"
        },
        "cyber": {
            "roles": ["Cybersecurity Analyst", "Pen Tester", "Security Consultant"],
            "roadmap": "1. Learn Networking Basics\n2. Understand OS & Linux\n3. Explore Ethical Hacking\n4. Get CEH Certification\n5. Practice on TryHackMe"
        },
        "ai": {
            "roles": ["AI Engineer", "ML Engineer", "AI Researcher"],
            "roadmap": "1. Learn Python & Numpy\n2. Study ML with scikit-learn\n3. Dive into Deep Learning\n4. Work on NLP projects\n5. Use TensorFlow/PyTorch"
        },
        "research": {
            "roles": ["Research Scientist", "Lab Technician", "Clinical Research Associate"],
            "roadmap": "1. Pursue MSc\n2. Learn Research Methodologies\n3. Gain Lab Experience\n4. Publish Research\n5. Join Research Institutes"
        },
        "teaching": {
            "roles": ["School Teacher", "Online Tutor", "Lecturer"],
            "roadmap": "1. Complete B.Ed\n2. Prepare TET/NET Exams\n3. Join Schools or EdTech\n4. Create Online Courses\n5. Build Education Portfolio"
        },
        "design": {
            "roles": ["Graphic Designer", "Animator", "Creative Director"],
            "roadmap": "1. Master Tools (Photoshop/Figma)\n2. Create Portfolio\n3. Learn Animation Basics\n4. Freelance or Intern\n5. Stay Updated with Trends"
        },
        "marketing": {
            "roles": ["Digital Marketer", "SEO Specialist", "Brand Manager"],
            "roadmap": "1. Learn Digital Channels\n2. SEO & Google Ads\n3. Practice on Real Campaigns\n4. Certify via Google/Facebook\n5. Analyze Metrics"
        },
        "finance": {
            "roles": ["Financial Analyst", "Investment Banker", "Tax Consultant"],
            "roadmap": "1. Master Excel & Accounting\n2. Study Financial Markets\n3. Learn Valuation\n4. Pursue CFA/CA\n5. Apply to Banks/Firms"
        },
        "management": {
            "roles": ["Business Analyst", "Project Manager", "Ops Manager"],
            "roadmap": "1. Study MBA Concepts\n2. Learn Excel & PPT\n3. Understand Agile/Scrum\n4. Use Project Tools (JIRA)\n5. Gain Internship"
        },
        "psychology": {
            "roles": ["Counselor", "Clinical Psychologist", "Organizational Psychologist"],
            "roadmap": "1. Pursue MA in Psychology\n2. Do Internships\n3. Get Licensed (if required)\n4. Practice or Join Clinics\n5. Upskill with Specializations"
        },
        "agriculture": {
            "roles": ["Agri Officer", "Agronomist", "Agri-Tech Specialist"],
            "roadmap": "1. Study Modern Farming Techniques\n2. Learn GIS & Remote Sensing\n3. Work with Govt/Private Firms\n4. Get Agri Certifications\n5. Build Agri Startup"
        }
    }

    if degree and degree != "Other":
        fields = degree_to_fields.get(degree, [])
        st.markdown(f"<div class='recommend-box'><div class='career-title'>Based on <em>{degree}</em>, possible fields:</div><ul>{''.join([f'<li>{f}</li>' for f in fields])}</ul></div>", unsafe_allow_html=True)

        interest = st.text_input("Which of these fields or topics interests you most?")

        if st.button("🔍 Get Recommendations"):
            if not interest.strip():
                st.warning("Please enter an interest.")
                return

            found = False
            for keyword, data in field_to_roles.items():
                if keyword in interest.lower():
                    roles = data['roles']
                    roadmap = data['roadmap']
                    st.success(f"Recommended Career Roles for *{interest}*: {', '.join(roles)}")
                    st.markdown(f"### 🛣 Career Roadmap:\n{roadmap}")
                    found = True
                    break

            if not found:
                st.info("Couldn't find specific matches. Explore general paths like Civil Services, Entrepreneurship, or NGOs.")

    elif degree == "Other":
        st.info("Please enter your degree and interests in detail so we can help you better.")



# Call the function to run it
if __name__ == "__main__":
    show_recommendations()