# 04. Jupyter Notebook 환경 설정

## 🎯 학습 목표

- Jupyter Notebook의 개념을 이해한다.
- VS Code에 Jupyter Extension을 설치한다.
- `.ipynb` 파일을 생성한다.
- Python Kernel을 연결한다.
- Notebook Cell을 실행한다.

---

# 1. Jupyter Notebook이란?

Jupyter Notebook은 Python 코드와 설명, 실행 결과를 하나의 문서에서 함께 관리할 수 있는 환경입니다.

```text
Python 파일        : program.py
Jupyter Notebook : practice.ipynb
```

---

# 2. Python 파일과 Jupyter Notebook

| 구분 | Python 파일 | Jupyter Notebook |
|---|---|---|
| 확장자 | `.py` | `.ipynb` |
| 실행 | 파일 단위 | Cell 단위 |
| 설명 | 주석 중심 | Markdown 사용 가능 |
| 결과 | Terminal | Cell 아래 |
| 활용 | 프로그램 개발 | 학습, 분석, 실험 |

---

# 3. Jupyter Extension 설치

Extensions 메뉴에서 `Jupyter`를 검색하고 Microsoft의 Jupyter Extension을 설치합니다.

---

# 4. Jupyter Notebook 생성

새 파일을 생성하고 확장자를 `.ipynb`로 저장합니다.

예:

```text
practice.ipynb
```

또는 `Ctrl + Shift + P`를 눌러 Jupyter Notebook 생성을 선택합니다.

---

# 5. Python Kernel 연결

Notebook 오른쪽 위의 `Select Kernel`을 선택한 뒤 `Python Environments`에서 현재 설치된 Python 환경을 선택합니다.

---

# 6. 첫 Notebook 실행

```python
print("주피터 노트북 연동 성공!")
```

`Shift + Enter`로 실행합니다.

---

# 7. Code Cell과 Markdown Cell

Code Cell은 Python 코드를 실행하고, Markdown Cell은 설명을 작성할 때 사용합니다.

```python
a = 10
b = 20
print(a + b)
```

Notebook을 이용하면 다음과 같은 학습 흐름을 만들 수 있습니다.

```text
설명 → 코드 → 실행 결과 → 추가 설명
```

---

# 🧪 실습

`first_notebook.ipynb`를 만들고 다음 코드를 Cell별로 실행합니다.

```python
print("Hello, Jupyter!")
```

```python
a = 100
b = 200
print(a + b)
```

```python
name = "Python"
print("Programming Language:", name)
```

---

# ✅ 확인 체크리스트

- [ ] Jupyter Extension 설치
- [ ] `.ipynb` 파일 생성
- [ ] Python Kernel 선택
- [ ] Code Cell 생성
- [ ] Shift + Enter 실행
- [ ] 실행 결과 확인

---

[← VS Code 설정](./03_vscode_setup.md)  
[다음 → 기본 패키지 설치](./05_package_setup.md)
