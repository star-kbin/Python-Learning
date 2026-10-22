# 📱 Python 역량진단 모바일 웹앱

기존 [30문항 평가](../self_assessment/TEST.md)와 동일한 문항·정답·배점(100점)을 사용합니다.

## 기능
- 모바일과 PC 지원, 문항별 답 선택 및 이전/다음 이동
- 30문항 자동 채점, Level 1~5 분류
- 영역별 점수·정답률 및 오답 해설, 학습 링크
- 로그인 및 별도 Python 설치 없이 사용 가능 (배포 후)
- 서버·DB에 개인 응시 기록 저장하지 않음. 현재 접속 세션 내에서만 답변을 유지합니다.

## 로컬 실행

```bash
python -m pip install -r streamlit_quiz/requirements.txt
python -m streamlit run streamlit_quiz/app.py
```

## Streamlit Community Cloud 배포
1. [share.streamlit.io](https://share.streamlit.io/) 접속 및 GitHub 로그인
2. **Create app → Deploy a public app from GitHub** 선택
3. Repository: `star-kbin/Python-Learning`
4. Branch: `main`
5. Main file path: `streamlit_quiz/app.py`
6. 앱 URL 지정 후 **Deploy** 클릭
7. 배포 완료된 실제 URL을 [루트 README](../README.md)에 연결

Community Cloud의 배포 승인은 저장소 소유자의 GitHub/Streamlit 계정에서 진행해야 합니다. 기존 평가 문항 원본은 변경하지 않았습니다.

## 문제 관리
문제를 고칠 때 `self_assessment/TEST.md`와 `streamlit_quiz/questions.json`을 함께 갱신하고, 정답·배점 총합(100점)을 검증하세요.
