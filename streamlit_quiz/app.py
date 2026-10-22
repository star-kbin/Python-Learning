"""Mobile-friendly 30-question Python & Data self-assessment."""
import json
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parent
QUESTIONS = json.loads((ROOT / "questions.json").read_text(encoding="utf-8"))
LEVELS = [
    (39, "Level 1 · 입문", "Python 개발환경과 변수·자료형부터 시작하세요.", "https://github.com/star-kbin/Python-Learning/tree/main/00_setup"),
    (59, "Level 2 · 기초", "조건문, 반복문, 함수와 자료구조를 복습하세요.", "https://github.com/star-kbin/Python_Basic"),
    (74, "Level 3 · 실무 기초", "Pandas CSV 처리, 필터링, 결측값 처리를 연습하세요.", "https://pandas.pydata.org/docs/getting_started/index.html"),
    (89, "Level 4 · 실무 활용", "통계·시각화와 데이터 누수 예방 프로젝트에 도전하세요.", "https://scikit-learn.org/stable/user_guide.html"),
    (100, "Level 5 · 심화", "재현 가능한 데이터 분석 프로젝트를 완성하세요.", "https://github.com/star-kbin/Python-Learning"),
]
STUDY = {
    "A": ("Python 문법·자료구조", "https://github.com/star-kbin/Python_Basic"),
    "B": ("코드 이해·오류", "https://github.com/star-kbin/Python_Basic"),
    "C": ("Pandas·데이터 처리", "https://pandas.pydata.org/docs/getting_started/index.html"),
    "D": ("통계·시각화", "https://matplotlib.org/stable/tutorials/index.html"),
    "E": ("데이터 분석 사고", "https://scikit-learn.org/stable/user_guide.html"),
}

st.set_page_config(page_title="Python 역량진단", page_icon="🐍", layout="centered", initial_sidebar_state="collapsed")
st.markdown("""
<style>
.block-container {max-width: 780px; padding-top: 1.2rem; padding-bottom: 4rem;}
div.stButton > button {min-height: 3rem;}
div[role="radiogroup"] label {padding: .45rem .2rem;}
@media(max-width: 640px) {
  .block-container {padding-left: 1rem; padding-right: 1rem;}
  h1 {font-size: 1.8rem !important;}
}
</style>
""", unsafe_allow_html=True)

if "answers" not in st.session_state:
    st.session_state.answers = {}
if "current" not in st.session_state:
    st.session_state.current = 0
if "submitted" not in st.session_state:
    st.session_state.submitted = False

def restart():
    for i in range(len(QUESTIONS)):
        st.session_state.pop(f"q_{i}", None)
    st.session_state.answers = {}
    st.session_state.current = 0
    st.session_state.submitted = False

def save_choice():
    i = st.session_state.current
    st.session_state.answers[i] = st.session_state.get(f"q_{i}")

def move(step):
    save_choice()
    st.session_state.current = max(0, min(len(QUESTIONS) - 1, st.session_state.current + step))

st.title("🐍 Python & Data 역량진단")
st.caption("30문항 · 100점 · 권장 25~35분 | 설치 없이 모바일에서 응시")
st.info("비공인 기초 지식 자가진단입니다. 실제 코딩 능력을 인증하지 않으며, 응답은 서버에 저장하지 않습니다.")

if not st.session_state.submitted:
    i = st.session_state.current
    q = QUESTIONS[i]
    count = sum(v is not None for v in st.session_state.answers.values())
    st.progress(count / len(QUESTIONS), text=f"답변 완료 {count} / {len(QUESTIONS)}")
    st.subheader(f"문제 {q['id']} / {len(QUESTIONS)}")
    st.caption(f"{q['category']}. {q['category_title']} · {q['points']}점")
    st.markdown(f"**{q['question']}**")
    previous = st.session_state.answers.get(i)
    key = f"q_{i}"
    if key not in st.session_state:
        st.session_state[key] = previous
    choice = st.radio(
        "정답 하나를 선택하세요",
        options=list(range(4)),
        format_func=lambda n: f"{n+1}. {q['options'][n]}",
        index=None,
        key=key,
    )
    st.session_state.answers[i] = choice
    left, right = st.columns(2)
    with left:
        if st.button("← 이전", disabled=i == 0, use_container_width=True):
            move(-1)
            st.rerun()
    with right:
        if i < len(QUESTIONS) - 1:
            if st.button("다음 →", use_container_width=True, type="primary"):
                move(1)
                st.rerun()
        else:
            if st.button("채점하기", use_container_width=True, type="primary"):
                save_choice()
                st.session_state.submitted = True
                st.rerun()
    with st.expander("응시 안내"):
        st.write("앞뒤 이동 가능 · 미응답은 0점 · 제출 후 정답과 해설 공개")
        if st.button("첫 문제로 이동"):
            save_choice()
            st.session_state.current = 0
            st.rerun()
else:
    answers = st.session_state.answers
    score = sum(q["points"] for i, q in enumerate(QUESTIONS) if answers.get(i) == q["answer"])
    correct = sum(answers.get(i) == q["answer"] for i, q in enumerate(QUESTIONS))
    level = next(row for row in LEVELS if score <= row[0])
    st.success("채점이 완료되었습니다.")
    st.metric("최종 점수", f"{score} / 100점")
    a, b = st.columns(2)
    a.metric("정답", f"{correct} / 30문항")
    b.metric("미응답", sum(answers.get(i) is None for i in range(len(QUESTIONS))))
    st.subheader(level[1])
    st.write(level[2])
    st.link_button("추천 학습 바로가기", level[3], use_container_width=True)
    st.markdown("### 영역별 분석")
    for category, (name, link) in STUDY.items():
        subset = [(i,q) for i,q in enumerate(QUESTIONS) if q["category"] == category]
        earned = sum(q["points"] for i,q in subset if answers.get(i) == q["answer"])
        total = sum(q["points"] for _,q in subset)
        ncorrect = sum(answers.get(i) == q["answer"] for i,q in subset)
        rate = ncorrect / len(subset)
        st.write(f"**{category}. {name}** — {earned}/{total}점 · 정답률 {rate:.0%}")
        st.progress(earned / total)
        if rate < 0.7:
            st.markdown(f"📚 [이 영역 보충 학습]({link})")
    st.markdown("### 문제별 정답 및 해설")
    for i, q in enumerate(QUESTIONS):
        chosen = answers.get(i)
        passed = chosen == q["answer"]
        label = "✅" if passed else "❌"
        with st.expander(f"{label} {q['id']}번 · {q['points'] if passed else 0}/{q['points']}점"):
            st.write(q["question"])
            st.write("내 답:", "미응답" if chosen is None else f"{chosen+1}. {q['options'][chosen]}")
            st.write("정답:", f"{q['answer']+1}. {q['options'][q['answer']]}")
            st.info(q["explanation"])
    st.caption("반복 응시는 문제 기억 효과가 있으므로, 점수 향상을 실제 실력 향상으로 단정하지 마세요.")
    if st.button("처음부터 다시 풀기", use_container_width=True):
        restart()
        st.rerun()
