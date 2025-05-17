import streamlit as st
import random

# 고등학생 공감 질문 리스트
fun_questions = [
    ("🏫 쉬는 시간마다 친구들이랑 수다 떠는 게 꿀잼이다?", "E"),
    ("🎧 혼자 이어폰 끼고 음악 듣는 시간이 제일 힐링이다?", "I"),
    ("📱 단톡방에서 이슈 생기면 바로 의견 남기는 편이다?", "E"),
    ("🤔 말하기 전에 머릿속으로 시뮬레이션 돌려본다?", "I"),
    ("🎤 반 친구들이랑 노래방 가면 마이크는 내 차지!", "E"),
    ("📚 주말엔 집에서 넷플릭스나 책 보며 시간 보내는 게 최고!", "I"),
    ("👀 시험 볼 때 문제 속 숨은 의도를 잘 캐치한다?", "S"),
    ("🌠 공부하다가 갑자기 인생이나 미래를 상상할 때가 많다?", "N"),
    ("🛠️ 이론보다 직접 해보는 게 더 잘 이해된다?", "S"),
    ("💭 오늘 한 행동이 나중에 어떤 영향을 줄지 자주 생각한다?", "N"),
    ("🗓️ 수행평가나 과제는 미리미리 계획 세워서 한다?", "S"),
    ("🎬 영화나 소설 볼 때 숨은 의미나 상징 찾는 게 재밌다?", "N"),
    ("🧑‍🔬 토론이나 발표에서 논리적으로 설득하는 게 자신 있다?", "T"),
    ("💌 친구가 힘들어하면 먼저 다가가서 얘기 들어준다?", "F"),
    ("⚖️ 친구랑 의견 다를 때 감정보다 논리로 설득한다?", "T"),
    ("🤝 분위기 흐릴까 봐 양보하는 편이다?", "F"),
    ("📊 내 선택의 기준은 객관적인 데이터나 사실이다?", "T"),
    ("🤗 친구 고민엔 공감부터 해주는 스타일이다?", "F"),
    ("📅 시험 공부나 과제, 계획표 짜는 게 습관이다?", "J"),
    ("🌊 계획 없이 그날그날 컨디션 따라 움직인다?", "P"),
    ("⏰ 마감 기한은 무조건 지키는 게 내 철칙!", "J"),
    ("🎲 즉흥적으로 친구들이랑 약속 잡는 게 재밌다?", "P"),
    ("✅ 해야 할 일 끝내고 나면 뿌듯함이 크다?", "J"),
    ("🌀 결정 내릴 때 여러 가능성 상상하고 고민이 길다?", "P"),
]

mbti_comment = {
    "ISTJ": "🧐 체크리스트 없인 못 사는 현실주의자! 계획대로 착착!",
    "ISFJ": "🧸 모두를 챙기는 다정한 집사! 숨은 배려왕!",
    "INFJ": "🔮 조용한 혁명가! 마음을 읽는 마법사!",
    "INTJ": "🧠 전략 세우기 달인! 미래를 설계하는 천재!",
    "ISTP": "🛠️ 손재주 만렙! 뭐든 직접 해봐야 직성이 풀림!",
    "ISFP": "🎨 감성 한 스푼, 자유 두 스푼! 예술혼 불타는 낭만파!",
    "INFP": "🌱 상상력 무한대! 진정성 가득한 이상주의자!",
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

st.title("🎲 고등학생 MBTI 랜덤 퀴즈")
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
    st.subheader(f"{mbti_comment.get(mbti, '개성만점!')}")

    if st.button("🔄 다시하기"):
        st.session_state.quiz_index = 0
        st.session_state.answers = []
        st.experimental_rerun() if hasattr(st, "experimental_rerun") else None
