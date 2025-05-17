import streamlit as st

mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# MBTI 친구궁합 유형/설명 예시
friendship_types = {
    "소울메이트": "함께 있으면 마음이 편안~ 서로 의지되는 찐친 조합!",
    "덕질메이트": "관심사 똑같아서 덕질할 때 환상의 짝꿍! 서로 터치 안 해서 더 편함.",
    "환상의 짝꿍": "이야기가 끊이지 않는 케미! 같이 있으면 시간 순삭!",
    "거울관계": "비슷한 듯 다른, 서로의 부족함을 채워주는 신기한 조합.",
    "사교성 만렙": "처음 봐도 금방 친해지는 인싸력 폭발 콤비!",
    "쌍둥이": "성향, 문제점까지 닮아서 서로를 잘 이해하지만 가끔 같이 헤매기도...",
    "신비주의": "서로 너무 달라서 신비롭게 느껴지는 관계! 서로에게 새로운 자극이 됨.",
    "파국주의": "만나면 입을 못 다무는 환장의 콤비... 하지만 추억은 많음!",
}

# 궁합 매트릭스 예시 (실제 궁합표를 참고해 조합을 더 추가해도 됩니다)
mbti_friendship = {
    ("ENFP", "INTJ"): ("소울메이트", "ENFP의 열정과 INTJ의 전략이 만나면, 현실과 꿈을 넘나드는 찐친 케미!"),
    ("ENFP", "INFJ"): ("소울메이트", "말 안 해도 통하는 텔레파시 조합! 고민 상담, 인생 토크는 이 둘이 최고!"),
    ("ISTJ", "ENFP"): ("거울관계", "ENFP의 자유로움과 ISTJ의 꼼꼼함이 만나면 서로를 배우는 신기한 조합!"),
    ("ISFJ", "ESFP"): ("덕질메이트", "조용한 ISFJ와 밝은 ESFP, 덕질할 땐 둘이 최고!"),
    ("ENTP", "INFJ"): ("환상의 짝꿍", "토론광 ENTP와 깊은 INFJ, 대화가 끝나지 않는 환상의 케미!"),
    ("ISTP", "ESTP"): ("사교성 만렙", "둘 다 즉흥적! 같이 있으면 어디든 모험 떠나는 콤비!"),
    ("INFP", "ENFP"): ("쌍둥이", "둘 다 감성파! 서로를 완벽히 이해하지만 같이 몽상하다 시간 순삭 주의!"),
    ("INTP", "ENTP"): ("덕질메이트", "궁금한 게 많은 두 사람, 덕질 얘기 시작하면 밤샘 각!"),
    ("ESFJ", "ISFP"): ("환상의 짝꿍", "상냥한 ESFJ와 감성 ISFP, 서로 챙겨주며 힐링하는 조합!"),
    ("ENTJ", "ENFP"): ("거울관계", "리더십 강한 ENTJ와 자유로운 ENFP, 서로에게 자극이 되는 콤비!"),
    ("ISTJ", "ISTJ"): ("쌍둥이", "계획표, 규칙, 성실함까지 다 닮아 서로를 너무 잘 이해함!"),
    ("ENFP", "ENFP"): ("파국주의", "에너지 폭발! 만나면 텐션이 하늘을 뚫음. 선생님이 제일 두려워하는 조합!"),
    # ... 더 많은 조합을 추가해도 좋아요!
}

def get_friendship_result(mbti1, mbti2):
    # 같은 MBTI끼리면 쌍둥이, ENFP끼리는 파국주의
    if mbti1 == mbti2:
        if mbti1 == "ENFP":
            return ("파국주의", "에너지 폭발! 만나면 텐션이 하늘을 뚫음. 선생님이 제일 두려워하는 조합!")
        else:
            return ("쌍둥이", f"성향, 문제점까지 닮아서 서로를 너무 잘 이해하는 {mbti1} 쌍둥이 케미!")
    # 조합이 있으면 해당 결과, 없으면 랜덤/기본값
    result = mbti_friendship.get((mbti1, mbti2)) or mbti_friendship.get((mbti2, mbti1))
    if result:
        return result
    else:
        # 랜덤하게 궁합 유형을 부여
        import random
        key = random.choice(list(friendship_types.keys()))
        return (key, friendship_types[key])

st.title("💌 MBTI 친구궁합 테스트")
st.write("두 명의 MBTI를 선택하면, 오늘의 친구궁합과 케미를 알려드려요!")

col1, col2 = st.columns(2)
with col1:
    mbti1 = st.selectbox("나의 MBTI", mbti_types, index=0)
with col2:
    mbti2 = st.selectbox("친구의 MBTI", mbti_types, index=1)

if mbti1 and mbti2:
    st.markdown("---")
    궁합유형, 설명 = get_friendship_result(mbti1, mbti2)
    st.markdown(f"## 👫 오늘의 친구궁합: **{궁합유형}**")
    st.success(설명)
    st.caption(f"({mbti1} & {mbti2} 조합)")

    st.markdown("### 궁합 유형별 해설")
    for k, v in friendship_types.items():
        st.markdown(f"- **{k}** : {v}")
