import streamlit as st
import random

# 재미있는 질문 리스트
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

# MBTI 유형별 한줄평
mbti_comment = {
    "ISTJ": "🧐 원칙을 지키는 현실주의자! 체크리스트 없인 못 살아~",
    "ISFJ": "🧸 모두를 챙기는 다정한 집사! 숨은 배려왕!",
    "INFJ": "🔮 세상을 읽는 마음의 마법사! 조용한 혁명가!",
    "INTJ": "🧠 치밀한 전략 설계자! 계획 세우기의 달인!",
    "ISTP": "🛠️ 고장난 건 다 맡겨! 손재주 만렙 실전 해결사!",
    "ISFP": "🎨 감성 한 스푼, 자유 두 스푼! 예술혼이 불타는 낭만파!",
    "INFP": "🌱 몽상과 상상의 나라, 진정성 가득한 이상주의자!",
    "INTP": "💡 궁금한 건 못 참아! 논리와 아이디어의 끝판왕!",
    "ESTP": "🏄‍♂️ 오늘도 모험 출발! 즉흥과 에너지의 화신!",
    "ESFP": "🎉 파티엔 내가 빠질 수 없지! 분위기 띄우는 핵인싸!",
    "ENFP": "🚀 열정이 폭발한다! 아이디어 샘솟는 자유로운 영혼!",
    "ENTP": "🦜 토론은 나의 힘! 재치와 창의력의 대마왕!",
    "ESTJ": "📋 조직의 기둥! 믿고 맡기는 현실파 리더!",
    "ESFJ": "🤗 모두의 든든한 응원군! 친절함이 묻어나는 소셜왕!",
    "ENFJ": "🦸 세상을 바꾸는 따뜻한 리더! 정의감 뿜뿜!",
    "ENTJ": "👑 목표를 향해 직진! 카리스마 넘치는 추진력 갑!",
}


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
        st.session_state.answers.append((trait, answer))
        st.session_state.quiz_index += 1
        st.experimental_rerun() if hasattr(st, "experimental_rerun") else None
else:
    # MBTI 계산
    scores = {"E":0, "I":0, "S":0, "N":0, "T":0, "F":0, "J":0, "P":0}
    for trait, ans in st.session_state.answers:
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
    st.subheader(f"👉 {mbti_comment.get(mbti, '개성만점!')} 👈")

    if st.button("🔄 다시하기"):
        st.session_state.quiz_index = 0
        st.session_state.answers = []
        st.experimental_rerun() if hasattr(st, "experimental_rerun") else None
