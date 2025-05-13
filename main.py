import streamlit as st

# Set the page title and icon
st.set_page_config(page_title="MBTI 직업 및 학습 추천 💼📚", page_icon="🎯")

# Header
st.title("✨ MBTI 유형별 직업 및 학습 추천 💡")
st.write("당신의 MBTI 유형을 선택하고, 어울리는 직업과 효과적인 학습 방법을 찾아보세요! 🌱")

# MBTI Career and Learning Recommendations in Korean
mbti_data = {
    "INTJ": {
        "jobs": "🧠 데이터 과학자, 📊 금융 분석가, 💻 소프트웨어 엔지니어",
        "learning": "🔍 논리적 사고를 키우는 문제 해결형 학습, 📚 깊이 있는 이론 공부, 📊 복잡한 데이터 분석"
    },
    "INTP": {
        "jobs": "🔬 연구 과학자, 💡 발명가, 👨‍💻 시스템 아키텍트",
        "learning": "🧠 새로운 아이디어 탐구, 📚 복잡한 개념 이해, 🛠️ 실험과 테스트를 통한 실습"
    },
    "ENTJ": {
        "jobs": "📈 경영 컨설턴트, 🗣️ 기업 임원, 🌐 비즈니스 전략가",
        "learning": "📊 목표 설정과 전략적 계획, 🗣️ 리더십 훈련, 📈 사례 연구 및 실전 경험"
    },
    "ENTP": {
        "jobs": "💡 기업가, 🎯 마케팅 전략가, 🎥 창의적 감독",
        "learning": "💥 토론과 브레인스토밍, 💡 혁신적인 아이디어 생성, 📚 다양한 분야의 폭넓은 지식"
    },
    "INFJ": {
        "jobs": "📝 작가, 🧘‍♂️ 심리 상담사, 🌱 사회복지사",
        "learning": "📝 깊이 있는 글쓰기, 🌱 사람의 감정 이해, 💫 비전과 철학을 통한 통찰"
    },
    "INFP": {
        "jobs": "🎨 그래픽 디자이너, 🎥 영화 제작자, 📝 소설가",
        "learning": "🎨 감정 표현 중심의 창작, 💭 상상력과 영감을 자극하는 학습, 🌱 자율적인 학습 환경"
    },
    "ENFJ": {
        "jobs": "👩‍🏫 교사, 🗣️ 홍보 전문가, 🤝 인적 자원 관리자",
        "learning": "💬 그룹 토론과 협력 학습, 💡 인간관계와 소통 기술, 🌍 사회적 책임 의식 함양"
    },
    "ENFP": {
        "jobs": "🎤 동기부여 연설가, 🎨 창작 감독, 📚 라이프 코치",
        "learning": "✨ 창의적인 프로젝트, 🎤 자유로운 아이디어 표현, 🌱 의미 있는 경험에서 배우기"
    },
    "ISTJ": {
        "jobs": "📊 회계사, 👮 경찰, 📐 건축가",
        "learning": "📏 정확한 사실 학습, 📚 체계적인 지식 쌓기, 🗃️ 규칙과 구조에 충실한 학습"
    },
    "ISFJ": {
        "jobs": "🧑‍⚕️ 간호사, 👩‍🍳 요리사, 👨‍🏫 초등학교 교사",
        "learning": "📝 세부 사항에 주의하는 학습, 🌱 실용적인 지식 쌓기, ❤️ 타인에게 도움을 주는 실습"
    },
    "ESTJ": {
        "jobs": "🗃️ 프로젝트 매니저, 👩‍⚖️ 변호사, 🏛️ 공무원",
        "learning": "📊 계획적이고 목표 지향적인 학습, 💼 리더십 훈련, 🗂️ 구조적인 자료 정리"
    },
    "ESFJ": {
        "jobs": "💼 인사 관리자, 🏥 의료 관리자, 👩‍💻 고객 서비스 전문가",
        "learning": "💬 타인과의 상호작용을 통한 학습, 📚 체계적인 정보 수집, 🌱 사람을 돕는 실습"
    },
    "ISTP": {
        "jobs": "🛠️ 기계 기술자, 🚀 파일럿, 👨‍🔧 엔지니어",
        "learning": "🔧 실습을 통한 학습, 🛠️ 문제 해결 능력 개발, 📐 정확한 기술 이해"
    },
    "ISFP": {
        "jobs": "🖌️ 아티스트, 🎸 음악가, 🧵 패션 디자이너",
        "learning": "🎨 감각적인 표현 중심의 학습, 🎵 창의성을 자극하는 활동, 🌸 개인의 감정을 담은 작업"
    },
    "ESTP": {
        "jobs": "💥 영업 관리자, 🏋️‍♂️ 피트니스 트레이너, 🚀 모험 가이드",
        "learning": "⚡ 실전 경험 중심의 학습, 🥊 경쟁적 환경에서 배우기, 📈 즉각적인 피드백 수용"
    },
    "ESFP": {
        "jobs": "🎤 배우, 🎶 음악 퍼포머, 🥂 이벤트 플래너",
        "learning": "🎉 활동적이고 참여적인 학습, 🎤 현장에서 배우기, 🌟 실생활에서의 감정 표현"
    },
}

# User input for MBTI type
mbti_type = st.selectbox("당신의 MBTI 유형을 선택하세요:", list(mbti_data.keys()))

# Display the recommended careers and learning tips
if mbti_type:
    st.subheader(f"💫 {mbti_type}에게 어울리는 직업 추천:")
    st.success(mbti_data[mbti_type]["jobs"])
    st.subheader("📚 효과적인 학습 방법:")
    st.info(mbti_data[mbti_type]["learning"])

# Footer
st.write("📝 당신의 잠재력을 발견하고, 꿈을 향해 도전하세요! ✨")
