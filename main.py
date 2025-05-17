import streamlit as st

# 페이지 타이틀과 아이콘 설정
st.set_page_config(page_title="MBTI 재미있는 정보", page_icon="🧠")

# 메인 헤더
st.title("✨ MBTI로 알아보는 재미있는 정보 💡")
st.write("MBTI 유형별로 흥미로운 사실과 정보를 탐색해보세요! 🌟")

# 섹션 예시: MBTI 유형별 특징 소개
st.subheader("MBTI 유형별 특징")
st.write("각 MBTI 유형은 고유한 성격 특성과 행동 양식을 가지고 있습니다.")

# 사용자 상호작용: MBTI 유형 선택 안내
st.write("아래에서 당신의 MBTI 유형을 선택하고, 관련된 재미있는 정보를 확인해보세요.")

# (추후 구현) MBTI 유형 선택 박스 예시
# mbti_type = st.selectbox('당신의 MBTI 유형을 선택하세요', ['ISTJ', 'ISFJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP', 'INTP', 'ESTP', 'ESFP', 'ENFP', 'ENTP', 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ'])
# st.write(f"선택한 MBTI 유형: {mbti_type}")
