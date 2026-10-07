# 06. Python 프로젝트 Workspace 구성

## 🎯 학습 목표

- Python 프로젝트 폴더 구조를 이해한다.
- 데이터와 코드를 구분하여 관리한다.
- Notebook과 Python 모듈을 구분한다.
- 프로젝트 결과물을 체계적으로 관리한다.

---

# 1. 왜 폴더 구조가 필요한가?

프로젝트가 커지면 Python 코드, 데이터, Notebook, 그래프, 모델, 앱 등 다양한 파일이 만들어집니다.

파일의 역할에 따라 폴더를 구분하면 프로젝트를 훨씬 쉽게 관리할 수 있습니다.

---

# 2. 기본 프로젝트 구조

```text
python_project/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
├── src/
├── models/
│
├── outputs/
│   ├── figures/
│   └── results/
│
├── app/
├── README.md
└── requirements.txt
```

---

# 3. 각 폴더의 역할

- `data/raw/` : 원본 데이터
- `data/processed/` : 전처리 데이터
- `notebooks/` : Jupyter Notebook
- `src/` : 재사용 가능한 Python 함수/모듈
- `models/` : 학습된 머신러닝·딥러닝 모델
- `outputs/figures/` : 그래프와 이미지
- `outputs/results/` : CSV 등 분석 결과
- `app/` : Streamlit 등 애플리케이션
- `README.md` : 프로젝트 설명
- `requirements.txt` : 필요한 Python 패키지 목록

---

# 4. Workspace 생성 실습

Codespace Terminal에서 다음 명령을 실행합니다.

```bash
mkdir -p python_project/data/raw
mkdir -p python_project/data/processed
mkdir -p python_project/notebooks
mkdir -p python_project/src
mkdir -p python_project/models
mkdir -p python_project/outputs/figures
mkdir -p python_project/outputs/results
mkdir -p python_project/app

touch python_project/README.md
touch python_project/requirements.txt
```

생성 결과는 다음 명령으로 확인할 수 있습니다.

```bash
find python_project
```

---

# 5. requirements.txt 예시

```text
numpy
pandas
matplotlib
seaborn
scikit-learn
jupyter
```

다음 명령으로 한 번에 설치할 수 있습니다.

```bash
pip install -r requirements.txt
```

---

# ✅ 확인 문제

1. `data/raw`에는 어떤 데이터를 저장하나요?
2. `data/processed`는 어떤 용도로 사용하나요?
3. `notebooks`와 `src`의 차이는 무엇인가요?
4. 학습한 AI 모델은 어느 폴더에 저장하나요?
5. `requirements.txt`는 왜 필요한가요?

---

[← 기본 패키지 설치](./05_package_setup.md)  
[처음으로 → 개발환경 구축 목차](./README.md)
