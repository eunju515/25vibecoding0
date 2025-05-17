import streamlit as st
import random

# --- MBTI Dichotomy Questions (24 questions, 6 per dichotomy) ---
questions = [
    # E/I
    ("🤝 주변 사람들과 함께 있을 때 더 에너지가 솟나요?", "E"),
    ("🏡 혼자만의 시간이 더 편안하게 느껴지나요?", "I"),
    ("💬 문제를 겪을 때 다른 사람과 이야기하며 해결하나요?", "E"),
    ("🧘 생각을 말하기 전에 머릿속으로 먼저 정리하나요?", "I"),
    ("🎉 파티에서 새로운 사람과 대화하는 걸 좋아하나요?", "E"),
    ("📚 주말엔 외출보다 집에서 조용히 보내는 걸 선호하나요?", "I"),
    # S/N
    ("🔍 주변의 세부사항과 사실에 더 집중하나요?", "S"),
    ("🌌 추상적 이론이나 미래 가능성에 더 관심이 많나요?", "N"),
    ("🛠️ 새로운 걸 배울 때 직접 해보는 걸 선호하나요?", "S"),
    ("🤔 오늘의 행동이 미래에 미칠 영향에 대해 자주 생각하나요?", "N"),
    ("🗺️ 여행 계획 시 상세한 일정표를 만드는 걸 좋아하나요?", "S"),
    ("📖 이야기에서 상징이나 은유 해석을 즐기나요?", "N"),
    # T/F
    ("🧠 결정할 때 논리와 사실을 우선시하나요?", "T"),
    ("💓 결정이 타인에게 미칠 감정적 영향을 더 신경 쓰나요?", "F"),
    ("⚖️ 논쟁 시 감정보다 논리로 설득하려 하나요?", "T"),
    ("🤝 집단에서 조화 유지를 위해 양보하는 편인가요?", "F"),
    ("📊 객관적 기준으로 상황을 판단하나요?", "T"),
    ("🤗 친구가 속상할 때 위로부터 먼저 건네나요?", "F"),
    # J/P
    ("📅 명확한 계획을 세우고 갑작스러운 변화를 싫어하나요?", "J"),
    ("🌊 상황에 맞게 유연하게 대처하는 걸 좋아하나요?", "P"),
    ("⏰ 마감 기한을 잘 지키는 편인가요?", "J"),
    ("🎲 즉흥적으로 다양한 선택지를 열어두는 걸 즐기나요?", "P"),
    ("✅ 일을 끝내고 결정을 내릴 때 만족감을 느끼나요?", "J"),
    ("🌀 결정을 내리기 전 다양한 가능성을 탐색하나요?", "P"),
]

# --- Shuffle questions for each session ---
if "quiz_questions" not in st.session_state:
    st.session_state.quiz_questions = random.sample(questions, len(questions))
    st.session_state.quiz_answers = [None] * len(questions)
    st.session_state.current_q = 0
    st.session_state.show_result = False

st.title("🎲 MBTI 랜덤 퀴즈")
st.write("아래 질문에 예/아니오로 답해보세요! 당신의 MBTI 유형을 재미있게 알아볼 수 있어요 😆")

# --- Quiz Progress ---
total_q = len(st.session_state.quiz_questions)
q_idx = st.session_state.current_q

if not st.session_state.show_result:
    q_text, q_trait = st.session_state.quiz_questions[q_idx]
    st.markdown(f"**{q_idx+1} / {total_q}**")
    st.markdown(f"### {q_text}")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("👍 예"):
            st.session_state.quiz_answers[q_idx] = "Yes"
            if q_idx < total_q - 1:
                st.session_state.current_q += 1
            else:
                st.session_state.show_result = True
            st.experimental_rerun()
    with col2:
        if st.button("👎 아니오"):
            st.session_state.quiz_answers[q_idx] = "No"
            if q_idx < total_q - 1:
                st.session_state.current_q += 1
            else:
                st.session_state.show_result = True
            st.experimental_rerun()
else:
    # --- MBTI 계산 ---
    trait_scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
    dichotomy_map = {
        "E/I": [1, 0, 1, 0, 1, 0],
        "S/N": [1, 0, 1, 0, 1, 0],
        "T/F": [1, 0, 1, 0, 1, 0],
        "J/P": [1, 0, 1, 0, 1, 0]
    }
    for i, (ans, (q, trait)) in enumerate(zip(st.session_state.quiz_answers, st.session_state.quiz_questions)):
        if i < 6:
            trait_pair = ("E", "I")
            trait_key = "E/I"
        elif i < 12:
            trait_pair = ("S", "N")
            trait_key = "S/N"
        elif i < 18:
            trait_pair = ("T", "F")
            trait_key = "T/F"
        else:
            trait_pair = ("J", "P")
            trait_key = "J/P"
        if ans == "Yes":
            trait_scores[trait_pair[0]] += dichotomy_map[trait_key][i % 6]
        else:
            trait_scores[trait_pair[1]] += dichotomy_map[trait_key][i % 6]

    mbti = ""
    mbti += "E" if trait_scores["E"] >= trait_scores["I"] else "I"
    mbti += "S" if trait_scores["S"] >= trait_scores["N"] else "N"
    mbti += "T" if trait_scores["T"] >= trait_scores["F"] else "F"
    mbti += "J" if trait_scores["J"] >= trait_scores["P"] else "P"

    st.markdown("---")
    st.header(f"🎉 당신의 MBTI 유형은: **{mbti}** 🎉")
    st.write("👇 다시 도전하거나 결과를 공유해보세요!")
    st.button("🔄 다시하기", on_click=lambda: st.session_state.clear())

    # (선택) 유형별 이모지, 설명 등 추가 가능

