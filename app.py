import streamlit as st
import subprocess
from pathlib import Path

# Custom theme with gradient background and feature colors
def set_custom_theme():
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1E3A8A, #3B82F6);
    }
    .big-font {
        font-size: 50px !important;
        color: #FFFFFF;
        font-weight: bold;
    }
    .feature-text {
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .about-us {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 10px;
        margin-top: 30px;
    }
    .team-member {
        background-color: rgba(255, 255, 255, 0.05);
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 15px;
    }
    .team-member h3 {
        color: #FDE68A;
        margin-bottom: 5px;
    }
    .team-member p {
        color: #E0F2FE;
        font-size: 14px;
    }
    .stButton > button {
        width: 100%;
        border-radius: 20px;
        font-weight: bold;
        margin-top: 0.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Set page config
st.set_page_config(page_title="Sarvagyaata AI", page_icon="🛡️", layout="wide")

# Apply custom theme
set_custom_theme()

# Title
st.markdown('<p class="big-font">Welcome to Sarvagyaata AI</p>', unsafe_allow_html=True)

# Subheader
st.markdown('<h2 style="color: #E0F2FE;">Your All-in-One Intelligent Business Solution</h2>', unsafe_allow_html=True)

# Features with colors and corresponding script names and directories
features = [
    ("Personalized Content Chatbot", "#FDE68A", "Personalized  chatbot"),
    ("Chat with any PDF", "#A7F3D0", "chatwithpdf"),
    ("Personalized Computer Vision", "#BFDBFE", "Object_Detection"),
    ("Movie Recommendation System", "#FCA5A5", "movie_recommendation"),
    ("Business Analyst Dashboard", "#C7D2FE", "Bussiness Dashboard"),
    ("Casual Inference of Blockchain", "#FCD34D", "Casual_Inference"),
    ("Sentiment Analysis of Twitter", "#A5B4FC", "Twitter_Sentiment_Analysis"),
    ("Stock Price Predictive Analytics", "#6EE7B7", "Stock_Index_App"),
    ("CryptoCurrency Predictive Analytics", "#6EE7B7", "Crypto"),
    ("Company Chat Analyser", "#93C5FD", "whatsapp-chat-analysis"),
    ("AutoML for Auto EDA", "#FDBA74", "AutoML"),
    
]

# Function to run subprocess for selected feature
def run_subprocess(script_path):
    subprocess.Popen(["streamlit", "run", str(script_path)])

# Create three columns
col1, col2, col3 = st.columns(3)

# Distribute features across columns
for i, (feature, color, script_directory) in enumerate(features):
    with [col1, col2, col3][i % 3]:
        st.markdown(f'<p class="feature-text" style="color: {color};">{feature}</p>', unsafe_allow_html=True)
        
        # Custom button style
        button_style = f"""
        <style>
        div.stButton > button:first-child {{
            background-color: {color};
            color: #1E3A8A;
        }}
        div.stButton > button:hover {{
            background-color: {color};
            color: #1E3A8A;
            opacity: 0.8;
        }}
        </style>
        """
        st.markdown(button_style, unsafe_allow_html=True)
        
        # Button for each feature
        if st.button(f"Try Now", key=f"feature_{i}"):
            script_path = Path(script_directory) / "app.py"
            if script_path.exists():
                st.write(f"You clicked on {feature}! Loading {feature}...")
                run_subprocess(script_path)
            else:
                st.error(f"Script {script_path} not found!")

# About Us Section
st.markdown('<div class="about-us">', unsafe_allow_html=True)
st.markdown('<h2 style="color: #FDE68A;">About Us</h2>', unsafe_allow_html=True)
st.markdown('<p style="color: #E0F2FE;">We are a team of passionate third-year engineering students in Artificial Intelligence and Data Science (AIDS), dedicated to revolutionizing business intelligence through innovative solutions.</p>', unsafe_allow_html=True)

team_members = [
    {
        "name": "Harsh Chitaliya",
        "bio": "Harsh is a creative problem-solver with a keen interest in AI-driven chatbots and natural language processing. His innovative approach to personalized content delivery forms the backbone of our content chatbot feature."
    },
    {
        "name": "Gaurav Singh Khati",
        "bio": "Gaurav excels in computer vision and machine learning. His expertise in developing tailored CV models has been crucial in creating our personalized computer vision solutions for various industry applications."
    },
    {
        "name": "Satyavrat Tiwari",
        "bio": "Satyavrat is passionate about data analytics and predictive modeling. His work on real-time predictive analytics for stock prices and cryptocurrency has added significant value to our financial intelligence offerings."
    }
]

for member in team_members:
    st.markdown(f'''
    <div class="team-member">
        <h3>{member['name']}</h3>
        <p>{member['bio']}</p>
    </div>
    ''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown('<p style="color: #E0F2FE;">© 2024 Sarvagyaata AI. All rights reserved.</p>', unsafe_allow_html=True)
