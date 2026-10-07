# 02. Windows에 Python 설치하기

## 🎯 학습 목표

- Python 설치 파일을 다운로드한다.
- Windows에 Python을 설치한다.
- PATH 설정의 필요성을 이해한다.
- Python이 정상적으로 설치되었는지 확인한다.

---

# 1. Python 설치 파일 다운로드

Python 공식 홈페이지에 접속합니다.

https://www.python.org/

상단 메뉴의 `Downloads`에서 Windows용 Python 설치 파일을 다운로드합니다.

> 수업에서는 강사가 지정한 Python 버전을 사용하는 것을 권장합니다.

---

# 2. Python 설치 프로그램 실행

다운로드한 설치 프로그램을 실행합니다.

예:

```text
python-3.xx.x-amd64.exe
```

설치 화면에서 다음 항목을 반드시 확인합니다.

```text
☑ Add python.exe to PATH
```

이후 `Install Now`를 선택하고 설치를 완료합니다.

---

# 3. PATH란?

PATH는 운영체제가 프로그램의 위치를 찾기 위해 사용하는 경로 정보입니다.

Python이 PATH에 등록되어 있으면 터미널에서 아래 명령만으로 Python을 실행할 수 있습니다.

```bash
python
```

---

# 4. Python 설치 확인

Windows Terminal 또는 명령 프롬프트에서 다음 명령을 실행합니다.

```bash
python --version
```

정상적인 경우:

```text
Python 3.xx.x
```

---

# 5. pip 확인

```bash
pip --version
```

버전 정보가 출력되면 정상적으로 사용할 수 있습니다.

---

# 🧪 실습

```bash
python --version
pip --version
```

두 명령 모두 버전이 표시되는지 확인합니다.

---

# ✅ 설치 체크리스트

- [ ] Python 설치 파일 다운로드
- [ ] Add python.exe to PATH 선택
- [ ] Python 설치 완료
- [ ] `python --version` 확인
- [ ] `pip --version` 확인

---

[← Python 이해](./01_python_intro.md)  
[다음 → VS Code 설치](./03_vscode_setup.md)
