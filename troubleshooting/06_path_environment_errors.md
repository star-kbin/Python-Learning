# 06. PATH 및 Python 환경 문제 해결

Python 설치는 되어 있지만 버전, pip, VS Code, Jupyter가 서로 다른 환경을 사용하는 문제를 다룹니다.

## 1. 현재 실행 중인 Python 확인

```bash
python --version
python -c "import sys; print(sys.executable)"
```

## 2. Windows에서 Python 경로 확인

```bat
where python
where pip
```

여러 경로가 출력되면 Python이 여러 버전 설치되어 있을 수 있습니다.

## 3. pip 연결 환경 확인

```bash
python -m pip --version
```

단순 `pip`보다 `python -m pip`를 사용하면 현재 Python 환경을 명확히 지정할 수 있습니다.

## 4. VS Code Interpreter 확인

```text
Ctrl + Shift + P
→ Python: Select Interpreter
```

## 5. Jupyter Kernel 확인

```python
import sys
print(sys.executable)
```

Terminal 결과와 비교합니다.

## 6. 가상환경 사용 시

```bash
python -m venv .venv
```

Windows PowerShell:
```powershell
.\.venv\Scripts\Activate.ps1
```

활성화 후 `python --version`, `python -m pip --version`을 확인합니다.

## 환경 문제 점검 순서

```text
python --version
→ Python 실행 파일 경로
→ python -m pip --version
→ VS Code Interpreter
→ Jupyter Kernel
```

[← Troubleshooting 목차](./README.md)