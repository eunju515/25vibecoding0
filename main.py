import streamlit as st

# Set the page title and icon
st.set_page_config(page_title="MBTI Career Recommender 💼", page_icon="🎯")

# Header
st.title("✨ MBTI Career Recommender 💡")
st.write("Choose your MBTI personality type to discover careers that match your strengths. 🌱")

# MBTI Career Recommendations
mbti_careers = {
    "INTJ": "🧠 Data Scientist, 📊 Financial Analyst, 💻 Software Engineer",
    "INTP": "🔬 Research Scientist, 💡 Inventor, 👨‍💻 Systems Architect",
    "ENTJ": "📈 Management Consultant, 🗣️ Corporate Executive, 🌐 Business Strategist",
    "ENTP": "💡 Entrepreneur, 🗣️ Marketing Strategist, 🎥 Creative Director",
    "INFJ": "📝 Writer, 🧘‍♂️ Psychologist, 🌱 Social Worker",
    "INFP": "🎨 Graphic Designer, 🎥 Filmmaker, 📝 Author",
    "ENFJ": "👩‍🏫 Teacher, 🗣️ Public Relations Specialist, 🤝 Human Resources Manager",
    "ENFP": "🎤 Motivational Speaker, 🎨 Creative Director, 📚 Life Coach",
    "ISTJ": "📊 Accountant, 👮 Police Officer, 📐 Architect",
    "ISFJ": "🧑‍⚕️ Nurse, 👩‍🍳 Chef, 👨‍🏫 Elementary School Teacher",
    "ESTJ": "🗃️ Project Manager, 👩‍⚖️ Lawyer, 🏛️ Government Official",
    "ESFJ": "💼 HR Manager, 🏥 Healthcare Administrator, 👩‍💻 Customer Service Representative",
    "ISTP": "🛠️ Mechanic, 🚀 Pilot, 👨‍🔧 Engineer",
    "ISFP": "🖌️ Artist, 🎸 Musician, 🧵 Fashion Designer",
    "ESTP": "💥 Sales Manager, 🏋️‍♂️ Fitness Trainer, 🚀 Adventure Tour Guide",
    "ESFP": "🎤 Actor, 🎶 Music Performer, 🥂 Event Planner",
}

# User input for MBTI type
mbti_type = st.selectbox("Select your MBTI type:", list(mbti_careers.keys()))

# Display the recommended careers
if mbti_type:
    st.subheader(f"💫 Recommended Careers for {mbti_type}:")
    st.success(mbti_careers[mbti_type])

# Footer
st.write("📝 Discover your potential and shine in your ideal career path! ✨")
