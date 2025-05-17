import streamlit as st
import random

# 질문 리스트 (각 질문마다 이모지 포함)
questions = [
    ("🤝 주변 사람들과 함께 있을 때 더 에너지가 솟나요?", "E"),
    ("🏡 혼자만의 시간이 더 편안하게 느껴지나요?", "I"),
    ("💬 문제를 겪을 때 다른 사람과 이야기하며 해결하나요?", "E"),
    ("🧘 생각을 말하기 전에 머릿속으로 먼저 정리하나요?", "I"),
    ("🎉 파티에서 새로운 사람과 대화하는 걸 좋아하나요?", "E"),
    ("📚 주말엔 외출보다 집에서 조용히 보내는 걸 선호하나요?", "I"),
    ("🔍 주변의 세부사항과 사실에 더 집중하나요?", "S"),
    ("🌌 추상적 이론이나 미래 가능성에 더 관심이 많나요?", "N"),
    ("🛠️ 새로운 걸 배울 때 직접 해보는 걸 선호하나요?", "S"),
    ("🤔 오늘의 행동이 미래에 미칠 영향에 대해 자주 생각하나요?", "N"),
    ("🗺️ 여행 계획 시 상세한 일정표를 만드는 걸 좋아하나요?", "S"),
    ("📖 이야기에서 상징이나 은유 해석을 즐기나요?", "N"),
    ("🧠 결정할 때 논리와 사실을 우선시하나요?", "T"),
    ("💓 결정이 타인에게 미칠 감정적 영향을 더 신경 쓰나요?", "F"),
    ("⚖️ 논쟁 시 감정보다 논리로 설득하려 하나요?", "T"),
    ("🤝 집단에서 조화 유지를 위해 양보하는 편인가요?", "F"),
    ("📊 객관적 기준으로 상황을 판단하나요?", "T"),
    ("🤗 친구가 속상할 때 위로부터 먼저 건네나요?", "F"),
    ("📅 명확한 계획을 세우고 갑작스러운 변화를 싫어하나요?", "J"),
    ("🌊 상황에 맞게 유연하게 대처하는 걸 좋아하나요?", "P"),
    ("⏰ 마감 기한을 잘 지키는 편인가요?", "J"),
    ("🎲 즉흥적으로 다양한 선택지를 열어두는 걸 즐기나요?", "P"),
    ("✅ 일을 끝내고 결정을 내릴 때 만족감을 느끼나요?", "J"),
    ("🌀 결정을 내리기 전 다양한 가능성을 탐색하나요?", "P"),
]

# 질문 순서 섞기 (앱 실행마다 고정, 세션 상태가 없으므로)
random.seed(42)
questions = random.sample(questions, len(questions))

st.title("🎲 MBTI 랜덤 퀴즈")
st.write("아래 질문에 답하고, 당신의 MBTI 유형을 재미있게 알아보세요! 😆")

# 진행 상태를 숨겨진 폼으로 관리
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
            f"'{q.replace('🤝','사교성 폭발!').replace('🏡','집콕 마스터!').replace('🎉','파티의 주인공!').replace('📚','조용한 시간 애호가!').replace('🔍','관찰력 최고!').replace('🌌','상상력 풍부!').replace('🛠️','실전파!').replace('🤔','깊은 사색가!').replace('🗺️','계획형 여행자!').replace('📖','문학적 감성!').replace('🧠','이성적인 두뇌!').replace('💓','따뜻한 마음!').replace('⚖️','논리왕!').replace('🤝','협동의 달인!').replace('📊','객관적 평가자!').replace('🤗','공감능력자!').replace('📅','계획의 신!').replace('🌊','유연한 사고!').replace('⏰','시간 엄수!').replace('🎲','즉흥적 모험가!').replace('✅','완벽주의자!').replace('🌀','다양성 탐험가!')}'"
            for q in picked
        ])
        st.markdown(f"**당신의 성격 한 줄 평:**<br> {comment}", unsafe_allow_html=True)
    else:
        st.write("아직 당신의 성격을 파악할 단서가 부족해요! 😅")

    if st.button("🔄 다시하기"):
        st.session_state.quiz_index = 0
        st.session_state.answers = []
        st.experimental_rerun() if hasattr(st, "experimental_rerun") else None  # 구버전 호환
