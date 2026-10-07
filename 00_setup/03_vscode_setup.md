# 03. VS Code 설치 및 Python 개발환경 설정

## 🎯 학습 목표

- Python과 VS Code의 차이를 이해한다.
- VS Code를 설치한다.
- Python Extension을 설치한다.
- 첫 번째 Python 파일을 생성한다.
- Python 코드를 실행한다.

---

# 1. Python과 VS Code의 관계

```text
Python = 자동차 엔진
VS Code = 자동차 운전석
```

Python은 프로그램을 실행하는 언어와 실행 환경이고, VS Code는 Python 코드를 편리하게 작성하고 관리하는 코드 편집기입니다.

```text
VS Code
   ↓
Python 코드 작성
   ↓
Python Interpreter
   ↓
코드 실행
   ↓
결과 출력
```

---

# 2. VS Code 설치

VS Code 공식 홈페이지에서 Windows용 설치 파일을 다운로드하여 설치합니다.

https://code.visualstudio.com/

---

# 3. VS Code 주요 영역

```text
Explorer   → 파일과 폴더 확인
Editor     → 코드 작성
Extensions → 확장 프로그램 설치
Terminal   → 명령어 입력 및 프로그램 실행
```

---

# 4. Python Extension 설치

Extensions를 선택합니다.

단축키:

```text
Ctrl + Shift + X
```

검색창에 `Python`을 입력하고 Microsoft에서 제공하는 Python Extension을 설치합니다.

---

# 5. 첫 Python 파일 만들기

```text
hello.py
```

다음 코드를 작성합니다.

```python
print("Hello, Python!")
```

---

# 6. Python 실행

VS Code 오른쪽 위의 실행 버튼을 사용하거나 터미널에서 실행합니다.

```bash
python hello.py
```

결과:

```text
Hello, Python!
```

---

# 🧪 실습 1 : 기본 출력

```python
print("Python Programming")
print("Hello, Python!")
print("My First Python Program")
```

# 🧪 실습 2 : 간단한 계산

```python
print(10 + 20)
print(100 - 30)
print(5 * 4)
```

# 🧪 실습 3 : 변수 사용

```python
name = "Python"
year = 1991

print("Language:", name)
print("Year:", year)
```

---

# ✅ 확인 체크리스트

- [ ] VS Code 설치
- [ ] Python Extension 설치
- [ ] `.py` 파일 생성
- [ ] Python 코드 작성
- [ ] Python 코드 실행
- [ ] Terminal에서 결과 확인

---

[← Python 설치](./02_python_install.md)  
[다음 → Jupyter Notebook](./04_jupyter_setup.md)
