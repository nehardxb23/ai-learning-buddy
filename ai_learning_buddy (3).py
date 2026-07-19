import streamlit as st
from google import genai

# ===========================
# Configure Gemini
# ===========================

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

# ===========================
# Page Configuration
# ===========================

st.set_page_config(
    page_title="AI Learning Buddy",
    page_icon="🎓",
    layout="centered"
)

# ===========================
# Custom CSS
# ===========================

st.markdown("""
<style>

.main{
    background-color:#f5f7fb;
}

.block-container{
    padding-top:2rem;
}

h1{
    text-align:center;
}

.stButton>button{
    width:100%;
    background:#4F46E5;
    color:white;
    border-radius:12px;
    height:50px;
    font-size:18px;
    font-weight:bold;
    border:none;
}

.stButton>button:hover{
    background:#3730a3;
}

.response-box{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 2px 10px rgba(0,0,0,0.15);
}

.footer{
    text-align:center;
    color:gray;
    font-size:14px;
}

</style>
""", unsafe_allow_html=True)

# ===========================
# Sidebar
# ===========================

st.sidebar.title("🎓 AI Learning Buddy")

st.sidebar.markdown("""
## Features

📘 Explain Concepts

🌍 Real-Life Examples

📝 Generate Quiz

🤖 Ask Anything

---

Powered by **Google Gemini**

Made using **Streamlit**
""")

# ===========================
# Header
# ===========================

st.markdown("""
<h1 style="color:#4F46E5;">
🎓 AI Learning Buddy
</h1>

<h4 style="text-align:center;color:gray;">
Your Personal AI Tutor powered by Gemini
</h4>
""", unsafe_allow_html=True)

st.write("")

# ===========================
# Input
# ===========================

topic = st.text_input(
    "📚 Enter a Topic",
    placeholder="Example: Cricket, AI, Python, Photosynthesis..."
)

option = st.selectbox(
    "🎯 Choose Learning Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    ]
)

# ===========================
# Generate Button
# ===========================

if st.button("🚀 Generate Answer"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")

    else:

        if option == "Explain Concept":
            prompt = f"Explain {topic} in simple language for a beginner using headings and bullet points."

        elif option == "Real-Life Example":
            prompt = f"Give one easy real-life example of {topic}. Explain it simply."

        elif option == "Generate Quiz":
            prompt = f"Create 5 multiple-choice questions about {topic} with 4 options and the correct answer."

        else:
            prompt = topic

        with st.spinner("🤖 Gemini is thinking..."):

            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=prompt
            )

        st.success("✅ Response Generated Successfully!")

        st.markdown("## 📖 AI Response")

        st.markdown(
            f"""
<div class="response-box">
{response.text}
</div>
""",
            unsafe_allow_html=True
        )

# ===========================
# Footer
# ===========================

st.markdown("---")

st.markdown(
"""
<div class="footer">
Developed by <b>Neha</b><br>
Powered by <b>Google Gemini 3.5 Flash</b> & Streamlit
</div>
""",
unsafe_allow_html=True)
