import streamlit as st

# MBTI 학과 선택 및 학습 유형 정보
mbti_info = {
    "INTJ": {
        "title": "🧠 INTJ - 전략가형",
        "description": "논리적이고 분석적인 사고를 가진 전략가입니다. 목표 지향적이며 독립적으로 문제를 해결하는 것을 선호합니다.",
        "major_tips": [
            "📊 논리적 사고와 복잡한 문제 해결이 필요한 전공을 고려해보세요.",
            "🧩 장기적인 계획 수립과 분석이 중요한 분야에 강합니다.",
            "🖥️ 기술 발전과 데이터 연구에 관심이 많다면 IT, 공학, 경영도 좋은 선택입니다."
        ],
        "recommended_majors": [
            "💻 컴퓨터공학",
            "📊 데이터사이언스",
            "🏛️ 경영학",
            "⚙️ 기계공학"
        ],
        "learning_styles": [
            "📝 체계적인 자료 정리와 논리적 분석이 중요한 학습 스타일",
            "📚 깊이 있는 연구와 비판적 사고를 활용한 자기주도 학습",
            "🗂️ 복잡한 문제를 단계적으로 해결하는 접근법"
        ]
    },
    "ENFP": {
        "title": "🌈 ENFP - 활동가형",
        "description": "열정적이고 창의적이며 사람들과의 교류를 즐기는 성격입니다. 다양한 아이디어와 경험을 탐구하는 것을 좋아합니다.",
        "major_tips": [
            "🎨 창의적인 표현이 중요한 전공을 고려해보세요.",
            "🗣️ 사람들과 소통하고 다양한 시각을 받아들일 수 있는 분야가 어울립니다.",
            "📢 예술, 미디어, 심리학, 마케팅 등 자유로운 사고가 중요한 전공이 좋습니다."
        ],
        "recommended_majors": [
            "🎥 미디어 커뮤니케이션",
            "📚 문예창작",
            "🧠 심리학",
            "📢 광고홍보학"
        ],
        "learning_styles": [
            "💡 창의적이고 자유로운 아이디어를 중심으로 한 학습",
            "🗣️ 그룹 토론과 협력을 통한 활발한 학습",
            "🎨 시각적 자료와 스토리텔링을 통한 이해"
        ]
    },
    "ISFJ": {
        "title": "💖 ISFJ - 수호자형",
        "description": "배려심이 많고 책임감 있는 성격으로, 타인을 돕는 일에서 보람을 느낍니다. 세심하고 헌신적인 태도를 보입니다.",
        "major_tips": [
            "🛡️ 사람을 돕고 보살피는 전공을 고려해보세요.",
            "📘 안정적이고 체계적인 환경에서 잘 성장할 수 있는 학과가 좋습니다.",
            "🎗️ 실용적인 지식을 배우고 싶은 분야를 선택하세요."
        ],
        "recommended_majors": [
            "🧑‍⚕️ 간호학",
            "👨‍🏫 교육학",
            "📋 사회복지학",
            "🏥 보건행정학"
        ],
        "learning_styles": [
            "📑 꼼꼼하고 체계적인 학습 방식",
            "❤️ 사람을 돕는 실습과 사례 중심의 학습",
            "📝 반복적인 복습과 정확한 정보 정리에 강함"
        ]
    }
}

# 앱 설정
st.set_page_config(page_title="학생 MBTI 학과 선택 도우미 💬", layout="centered", page_icon="🎓")
st.title("💬 학생 MBTI 학과 선택 및 학습 유형 도우미")
st.markdown("학생의 MBTI를 선택하면, 해당 성격의 특징, 어울리는 대학 학과, 효과적인 학습 유형을 알려드릴게요! 😊")

# MBTI 선택
mbti = st.selectbox("🔍 학생의 MBTI를 선택해주세요:", list(mbti_info.keys()))

# 정보 표시
if mbti:
    st.markdown("---")
    st.subheader(mbti_info[mbti]["title"])
    st.markdown(f"**📌 성격 특징:**\n\n{mbti_info[mbti]['description']}")
    
    st.markdown("**🎯 추천 전공:**")
    for major in mbti_info[mbti]["recommended_majors"]:
        st.markdown(f"- {major}")
    
    st.markdown("**🛠️ 학과 선택 팁:**")
    for tip in mbti_info[mbti]["major_tips"]:
        st.markdown(f"- {tip}")
    
    st.markdown("**📚 학습 유형:**")
    for style in mbti_info[mbti]["learning_styles"]:
        st.markdown(f"- {style}")
    
    st.markdown("---")
    st.success("📚 학생의 잠재력을 발견하고 꿈을 향해 나아가는 것이 최고의 시작입니다! 🙌")

# 하단 문구
st.markdown("""
<div style='text-align: center; font-size: 16px; margin-top: 30px;'>
    🙌 학과 선택은 학생의 미래를 결정하는 중요한 과정입니다. <br>
    <b>진심 어린 관심</b>과 <b>MBTI 이해</b>로 더 깊은 상담을 시작해 보세요!
</div>
""", unsafe_allow_html=True)
