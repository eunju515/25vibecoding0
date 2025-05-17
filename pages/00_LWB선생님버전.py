import streamlit as st
import random

# 더 재미있고 유쾌하게 바꾼 질문 리스트
fun_questions = [
    ("🤝 친구들과 있을 때 에너지가 펑펑 솟나요? 아니면 혼자 있을 때 충전되나요?", "E"),
    ("🏡 혼자만의 시간이 꿀맛처럼 달콤하게 느껴지나요?", "I"),
    ("💬 문제가 생기면 친구들과 수다 떨며 푸나요?", "E"),
    ("🧘 생각을 먼저 정리하고 말하는 편인가요?", "I"),
    ("🎉 파티에서 새로운 사람과 신나게 대화하는 걸 좋아하나요?", "E"),
    ("📚 주말엔 집콕하며 책 읽는 게 최고라고 생각하나요?", "I"),
    ("🔍 주변의 작은 디테일까지 놓치지 않는 꼼꼼함이 있나요?", "S"),
    ("🌌 미래에 대한 상상과 꿈꾸는 걸 즐기나요?", "N"),
    ("🛠️ 새로운 걸 배울 때 직접 해보는 게 더 재밌나요?", "S"),
    ("🤔 오늘 한 행동이 내일에 어떤 영향을 줄지 자주 생각하나요?", "N"),
    ("🗺️ 여행 계획을 꼼꼼하게 세우는 편인가요?", "S"),
    ("📖 이야기 속 숨은 의미를 찾아내는 걸 좋아하나요?", "N"),
    ("🧠 결정을 내릴 때 논리와 사실을 가장 중요하게 생각하나요?", "T"),
    ("💓 타인의 감정을 세심하게 살피는 편인가요?", "F"),
    ("⚖️ 논쟁할 때 감정보다 논리로 승부하나요?", "T"),
    ("🤝 집단에서 조화를 위해 양보하는 편인가요?", "F"),
    ("📊 객관적인 기준으로 상황을 판단하는 걸 좋아하나요?", "T"),
    ("🤗 친구가 속상할 때 먼저 다가가 위로하나요?", "F"),
    ("📅 계획을 세우고 그 계획대로 움직이는 걸 좋아하나요?", "J"),
    ("🌊 상황에 따라 유연하게 대처하는 걸 즐기나요?", "P"),
    ("⏰ 마감 기한을 꼭 지키는 편인가요?", "J"),
    ("🎲 즉흥적으로 다양한 선택지를 열어두는 걸 좋아하나요?", "P"),
    ("✅ 일을 끝까지 마무리하는 데서 큰 만족을 느끼나요?", "J"),
    ("🌀 결정을 내리기 전에 여러 가능성을 탐색하는 편인가요?", "P"),
]

# 질문 순서 섞기
random.seed(42)
questions = random.sample(fun_questions, len(fun_questions))

st.title("🎲 MBTI 랜덤 퀴즈")
st.write("아래 질문에 답하고, 당신의 MBTI 유형을 재미있게 알아보세요! 😆")

if 'quiz_index' not in st.session_state:
    st.session_state.quiz_index = 0
    st.session_state.answers = []

quiz_len = len(questions)
if st.session_state.quiz_index < quiz_len:
    q, trait = questions[st.session_state.quiz_index]
    st.markdown(f"**{st.session_state.quiz_index+1} / {quiz_len}**")
    st.markdown(f"### {q}")

    answer = st.radio("선택하세요:", ("예 👍", "아니오 👎"), key=f"q{st.session_state.quiz_index}")
    if st.button("다음 ▶️"):
        st.session_state.answers.append((trait, answer, q))
        st.session_state.quiz_index += 1
        st.experimental_rerun() if hasattr(st, "experimental_rerun") else None  # 구버전 호환
else:
    # 결과 계산
    scores = {"E":0, "I":0, "S":0, "N":0, "T":0, "F":0, "J":0, "P":0}
    for idx, (trait, ans, qtext) in enumerate(st.session_state.answers):
        if trait in scores:
            if ans.startswith("예"):
                scores[trait] += 1
            else:
                # 반대축 점수 올리기
                if trait == "E": scores["I"] += 1
                if trait == "I": scores["E"] += 1
                if trait == "S": scores["N"] += 1
                if trait == "N": scores["S"] += 1
                if trait == "T": scores["F"] += 1
                if trait == "F": scores["T"] += 1
                if trait == "J": scores["P"] += 1
                if trait == "P": scores["J"] += 1

    mbti = ""
    mbti += "E" if scores["E"] >= scores["I"] else "I"
    mbti += "S" if scores["S"] >= scores["N"] else "N"
    mbti += "T" if scores["T"] >= scores["F"] else "F"
    mbti += "J" if scores["J"] >= scores["P"] else "P"

    st.header(f"🎉 당신의 MBTI 유형은: **{mbti}** 🎉")

    # 사용자가 "예"라고 답한 질문 중 2~3개를 랜덤으로 선택해서 성격 문장 생성
    yes_questions = [qtext for trait, ans, qtext in st.session_state.answers if ans.startswith("예")]
    if yes_questions:
        picked = random.sample(yes_questions, min(3, len(yes_questions)))
        comment = " ".join([
            f"'{q.replace('🤝','사교력 만렙!').replace('🏡','집콕 마스터!').replace('🎉','파티의 주인공!').replace('📚','책벌레!').replace('🔍','디테일 장인!').replace('🌌','상상력 부자!').replace('🛠️','실전파!').replace('🤔','깊은 사색가!').replace('🗺️','여행계획러!').replace('📖','문학 감성러!').replace('🧠','이성파!').replace('💓','공감왕!').replace('⚖️','논리왕!').replace('📊','객관적 평가자!').replace('🤗','위로천사!').replace('📅','계획의 신!').replace('🌊','유연한 사고!').replace('⏰','시간 엄수!').replace('🎲','즉흥적 모험가!').replace('✅','완벽주의자!').replace('🌀','다방면 탐구자!')}'"
            for q in picked
        ])
        st.markdown(f"**당신의 성격 한 줄 평:**<br> {comment}", unsafe_allow_html=True)
    else:
        st.write("아직 당신의 성격을 파악할 단서가 부족해요! 😅")

    if st.button("🔄 다시하기"):
        st.session_state.quiz_index = 0
        st.session_state.answers = []
        st.experimental_rerun() if hasattr(st, "experimental_rerun") else None  # 구버전 호환
