# 01. Python 설치 문제 해결

## 1. `python` 명령을 찾을 수 없음

### 증상
```bash
python --version
```

Windows에서 명령을 찾을 수 없다는 메시지가 표시됩니다.

### 가능한 원인
- Python이 설치되지 않음
- 설치 시 `Add python.exe to PATH`를 체크하지 않음
- 설치 후 Terminal을 다시 열지 않음
- PATH 등록이 잘못됨

### 확인
```bat
where python
```

Python 설치 폴더 예:
```text
C:\Users\사용자이름\AppData\Local\Programs\Python\
```

### 해결
Python 설치 프로그램을 다시 실행하고 `Add python.exe to PATH`를 체크합니다. 설치 후 VS Code와 Terminal을 다시 시작합니다.

```bash
python --version
```

정상 결과 예: `Python 3.x.x`

## 2. `python` 입력 시 Microsoft Store가 열림

Windows의 **앱 실행 별칭(App execution aliases)**이 Python 명령을 가로채는 경우가 있습니다. 설치한 Python을 사용하도록 Python 관련 별칭을 확인한 뒤 Terminal을 다시 실행합니다.

## 3. 설치한 버전과 실행 버전이 다름

여러 Python 버전이 설치되어 있을 수 있습니다.

```bat
where python
```

Windows Python Launcher가 있다면 다음도 확인합니다.

```bash
py -0p
```

VS Code에서는 `Python: Select Interpreter`에서 수업에 사용할 Python을 선택합니다.

[← Troubleshooting 목차](./README.md)