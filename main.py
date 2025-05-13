import streamlit as st

# Set the page title and icon
st.set_page_config(page_title="MBTI 직업 추천 💼", page_icon="🎯")

# Header
st.title("✨ MBTI 유형별 직업 추천 💡")
st.write("당신의 MBTI 유형을 선택하고, 어울리는 직업을 찾아보세요! 🌱")

# MBTI Career Recommendations in Korean
mbti_careers_kr = {
    "INTJ": "🧠 데이터 과학자, 📊 금융 분석가, 💻 소프트웨어 엔지니어",
    "INTP": "🔬 연구 과학자, 💡 발명가, 👨‍💻 시스템 아키텍트",
    "ENTJ": "📈 경영 컨설턴트, 🗣️ 기업 임원, 🌐 비즈니스 전략가",
    "ENTP": "💡 기업가, 🎯 마케팅 전략가, 🎥 창의적 감독",
    "INFJ": "📝 작가, 🧘‍♂️ 심리 상담사, 🌱 사회복지사",
    "INFP": "🎨 그래픽 디자이너, 🎥 영화 제작자, 📝 소설가",
    "ENFJ": "👩‍🏫 교사, 🗣️ 홍보 전문가, 🤝 인적 자원 관리자",
    "ENFP": "🎤 동기부여 연설가, 🎨 창작 감독, 📚 라이프 코치",
    "ISTJ": "📊 회계사, 👮 경찰, 📐 건축가",
    "ISFJ": "🧑‍⚕️ 간호사, 👩‍🍳 요리사, 👨‍🏫 초등학교 교사",
    "ESTJ": "🗃️ 프로젝트 매니저, 👩‍⚖️ 변호사, 🏛️ 공무원",
    "ESFJ": "💼 인사 관리자, 🏥 의료 관리자, 👩‍💻 고객 서비스 전문가",
    "ISTP": "🛠️ 기계 기술자, 🚀 파일럿, 👨‍🔧 엔지니어",
    "ISFP": "🖌️ 아티스트, 🎸 음악가, 🧵 패션 디자이너",
    "ESTP": "💥 영업 관리자, 🏋️‍♂️ 피트니스 트레이너, 🚀 모험 가이드",
    "ESFP": "🎤 배우, 🎶 음악 퍼포머, 🥂 이벤트 플래너",
}

# User input for MBTI type
mbti_type = st.selectbox("당신의 MBTI 유형을 선택하세요:", list(mbti_careers_kr.keys()))

# Display the recommended careers
if mbti_type:
    st.subheader(f"💫 {mbti_type}에게 어울리는 직업 추천:")
    st.success(mbti_careers_kr[mbti_type])

# Footer
st.write("📝 당신의 잠재력을 발견하고, 꿈을 향해 도전하세요! ✨")
