# 🛠 Python Troubleshooting Guide

Python 학습 및 개발환경 구성 과정에서 자주 발생하는 문제와 해결 방법을 정리합니다.

오류가 발생하면 먼저 **오류 메시지를 그대로 확인**한 뒤 아래 항목에서 비슷한 문제를 찾아보세요.

## 🔍 문제 찾기

- [01. Python 설치 문제](./01_python_install_errors.md) — `python` 명령 인식, 설치, 버전 문제
- [02. VS Code 문제](./02_vscode_errors.md) — Interpreter, 실행 버튼, Terminal 문제
- [03. Python 코드 실행 문제](./03_python_execution_errors.md) — 파일 경로, 실행 위치, 출력 문제
- [04. pip / 패키지 문제](./04_pip_package_errors.md) — pip, ModuleNotFoundError, 패키지 충돌
- [05. Jupyter Notebook 문제](./05_jupyter_errors.md) — Kernel, ipykernel, Cell 실행 문제
- [06. PATH / Python 환경 문제](./06_path_environment_errors.md) — 여러 Python 버전, 환경 충돌
- [07. 자주 발생하는 Python 오류](./07_common_python_errors.md) — SyntaxError, NameError, TypeError 등
- [08. GitHub Codespaces 문제](./08_codespaces_errors.md) — Codespace, Git, 환경 문제

## 🚨 오류가 발생했을 때 기본 확인 순서

```text
1. 오류 메시지를 처음부터 끝까지 읽는다.
2. 오류가 발생한 파일과 줄 번호를 확인한다.
3. 현재 Python 버전과 실행 환경을 확인한다.
4. 파일 경로, 패키지, 변수명을 확인한다.
5. 한 번에 한 가지 원인만 수정한다.
6. 다시 실행하여 결과를 확인한다.
```

## 📝 오류 문의 시 기록할 정보

```text
운영체제:
Python 버전:
VS Code 또는 Codespaces 사용 여부:
실행한 파일:
실행 명령:
전체 오류 메시지:
이미 시도한 해결 방법:
```

## 🔄 업데이트 원칙

이 폴더는 실제 학습 중 발생하는 문제를 계속 추가하는 형태로 운영합니다.
새 문제는 **문제 증상 → 오류 메시지 → 가능한 원인 → 확인 방법 → 해결 방법 → 정상 동작 확인** 순서로 정리합니다.

[← Python-Learning 메인](../README.md)