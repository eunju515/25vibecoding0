import streamlit as st

mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

mbti_meme = {
    "ISTJ": "🧐 [ISTJ] \"내가 짠 시간표, 한 칸도 어길 수 없다!\" (수첩에 할 일 빼곡)",
    "ISFJ": "🧸 [ISFJ] \"친구 도시락 뚜껑도 챙겨주는 진정한 반의 엄마/아빠\"",
    "INFJ": "🔮 [INFJ] \"친구 고민 상담하다가 인생 명언 제조 중...\"",
    "INTJ": "🧠 [INTJ] \"시험 출제 경향 분석해서 예상문제 뽑는 중\"",
    "ISTP": "🛠️ [ISTP] \"교실 의자 삐걱이면 바로 고쳐주는 의자 수리공\"",
    "ISFP": "🎨 [ISFP] \"수업 시간에 필기하다가 노트 구석에 그림 한가득\"",
    "INFP": "🌱 [INFP] \"교실 창밖 보며 ‘내 미래는...’ 상상하는 몽상가\"",
    "INTP": "💡 [INTP] \"수업 듣다가 갑자기 ‘왜?’가 백 번 떠오름\"",
    "ESTP": "🏄‍♂️ [ESTP] \"체육대회 때 응원단장 맡아서 반 분위기 UP!\"",
    "ESFP": "🎉 [ESFP] \"급식 메뉴 좋으면 점심시간에 댄스파티 각!\"",
    "ENFP": "🚀 [ENFP] \"동아리, 학생회, 봉사활동 다 하고도 에너지 넘침\"",
    "ENTP": "🦜 [ENTP] \"수업 중 선생님께 질문 폭격, 토론은 내 무대!\"",
    "ESTJ": "📋 [ESTJ] \"조별과제 팀장 맡아서 역할 분배 완벽하게!\"",
    "ESFJ": "🤗 [ESFJ] \"시험 끝나면 친구들 모아 다 같이 떡볶이 먹으러!\"",
    "ENFJ": "🦸 [ENFJ] \"반 분위기 안 좋으면 먼저 나서서 분위기 메이커!\"",
    "ENTJ": "👑 [ENTJ] \"학생회장 지원, 목표는 전교 1등!\"",
}

st.title("🎯 오늘의 MBTI 밈")
st.write("당신의 MBTI 유형을 선택하면, 오늘의 고등학생 밈을 알려드려요!")

selected_mbti = st.selectbox("MBTI 유형을 골라주세요 👇", mbti_types, index=0)

if selected_mbti:
    st.markdown("---")
    st.markdown(f"## {selected_mbti}의 오늘의 밈")
    st.info(mbti_meme.get(selected_mbti, "오늘도 나만의 길을 가는 중!"))
