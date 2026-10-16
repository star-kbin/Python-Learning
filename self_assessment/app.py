import json
import random
from pathlib import Path

import streamlit as st

st.set_page_config(page_title="Python & Data 자가진단", page_icon="🐍", layout="centered")
BASE = Path(__file__).parent
QUESTIONS = json.loads((BASE / "questions.json").read_text(encoding="utf-8"))
AREAS = {
    "syntax": ("Python 문법·자료구조", 25, "https://github.com/star-kbin/Python_Basic"),
    "debug": ("코드 해석·디버깅", 20, "https://github.com/star-kbin/Python_Basic"),
    "data": ("데이터 처리·전처리", 25, "https://pandas.pydata.org/docs/getting_started/index.html"),
    "stats": ("통계·시각화", 15, "https://matplotlib.org/stable/tutorials/index.html"),
    "solve": ("분석 문제 해결", 15, "https://scikit-learn.org/stable/user_guide.html"),
}

def level(score):
    if score < 40: return "Level 1 · 입문"
    if score < 60: return "Level 2 · 기초"
    if score < 75: return "Level 3 · 실무 기초"
    if score < 90: return "Level 4 · 실무 활용"
    return "Level 5 · 심화"

def begin():
    st.session_state.order = random.sample(range(len(QUESTIONS)), len(QUESTIONS))
    st.session_state.answers = {}
    st.session_state.position = 0
    st.session_state.finished = False
    st.session_state.started = True

st.title("🐍 Python & Data Skills Assessment")
st.caption("파이썬·데이터 분석 역량 자가진단 | 30문항 · 약 20~30분")
st.warning("**독립 응시 원칙:** AI Agent(ChatGPT, Copilot, Claude 등), 인터넷 검색, 다른 사람의 도움, IDE 자동완성 및 외부 코드 실행 없이 스스로 풀어주세요. 이 방식은 자기진단의 신뢰도를 높이기 위한 안내이며 실제 도움 사용 여부를 기술적으로 감지하거나 차단하지는 않습니다.")
st.info("현재는 비공인 **자가진단**입니다. 객관식·코드 해석 능력을 측정하며, 실제 코딩·데이터 프로젝트 수행능력까지 검증하지는 않습니다. 문제·정답은 공개 저장소에서 확인할 수 있어 시험·채용 선발용으로는 적합하지 않습니다.")

if "started" not in st.session_state:
    st.session_state.started = False
if not st.session_state.started:
    st.markdown("**응시 전 체크**\n\n- AI·검색·타인 도움 없이 응시합니다.\n- 정답을 모르면 추측하여 답할 수 있습니다.\n- 결과는 본인 학습 계획 수립에 활용합니다.")
    agree = st.checkbox("독립 응시 원칙과 자가진단의 한계를 확인했습니다.")
    st.button("테스트 시작", disabled=not agree, on_click=begin, type="primary")
elif not st.session_state.finished:
    pos = st.session_state.position
    q = QUESTIONS[st.session_state.order[pos]]
    st.progress((pos + 1) / len(QUESTIONS))
    st.write(f"**{pos+1} / {len(QUESTIONS)}** · {AREAS[q['area']][0]}")
    st.subheader(q["question"])
    value = st.session_state.answers.get(q["id"])
    selection = st.radio("정답 선택", range(4), format_func=lambda n: q["options"][n],
                         index=value, key=f"q_{q['id']}")
    st.session_state.answers[q["id"]] = selection
    left, right = st.columns(2)
    with left:
        if st.button("이전 문제", disabled=pos == 0):
            st.session_state.position -= 1
            st.rerun()
    with right:
        if pos + 1 == len(QUESTIONS):
            if st.button("제출 및 결과 확인", type="primary"):
                st.session_state.finished = True
                st.rerun()
        elif st.button("다음 문제", type="primary"):
            st.session_state.position += 1
            st.rerun()
else:
    scores = {}
    for key, (label, weight, url) in AREAS.items():
        items = [q for q in QUESTIONS if q["area"] == key]
        correct = sum(st.session_state.answers.get(q["id"]) == q["answer"] for q in items)
        scores[key] = (correct, len(items), weight * correct / len(items))
    score = round(sum(v[2] for v in scores.values()), 1)
    st.success("평가를 완료했습니다.")
    st.metric("종합 점수 (100점 만점)", f"{score:.1f}")
    st.subheader(level(score))
    st.caption("초기 제안 등급 기준이며 표준화된 검증 점수가 아닙니다.")
    st.markdown("### 영역별 성취도")
    for key, (correct, count, weighted) in scores.items():
        label, weight, url = AREAS[key]
        st.write(f"**{label}** · 정답 {correct}/{count} · 가중점수 {weighted:.1f}/{weight}")
        st.progress(correct/count)
    st.markdown("### 다음 학습 추천")
    weak = sorted(scores, key=lambda k: scores[k][0] / scores[k][1])
    for key in weak[:3]:
        label, _, url = AREAS[key]
        st.markdown(f"- **{label}**: [추천 학습자료]({url}) → 개념 복습 후 유사 문제를 직접 작성하고 실행해 보세요.")
    if score < 40:
        st.write("**우선순위:** Python 환경·변수·자료형·조건문·반복문 기초부터 학습하세요.")
    elif score < 60:
        st.write("**우선순위:** 함수·자료구조·오류 분석을 반복하고 소규모 CSV 실습에 도전하세요.")
    elif score < 75:
        st.write("**우선순위:** Pandas 전처리·집계·시각화 과제를 완성하세요.")
    elif score < 90:
        st.write("**우선순위:** 시계열 검증, 데이터 누수 방지, 지표 선택 등 실무 분석을 연습하세요.")
    else:
        st.write("**우선순위:** 재현 가능한 프로젝트, 테스트 코드, 분석 보고서 작성으로 검증하세요.")
    st.markdown("### 오답 복습")
    for q in QUESTIONS:
        if st.session_state.answers.get(q["id"]) != q["answer"]:
            with st.expander(f"문항 {q['id']}: {q['question']}"):
                st.write(f"정답: **{q['options'][q['answer']]}**")
                st.write(q["explanation"])
    st.caption("응시 결과는 이 브라우저 세션에서만 사용하며 별도 서버 DB에 저장하지 않습니다.")
    st.download_button("결과 JSON 내려받기", json.dumps({
        "score":score,"level":level(score),
        "area_correct":{AREAS[k][0]:{"correct":v[0],"total":v[1]} for k,v in scores.items()}
    },ensure_ascii=False,indent=2),file_name="python_skill_result.json",mime="application/json")
    if st.button("새 테스트 시작"):
        begin()
        st.rerun()
