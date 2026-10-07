# 04. pip 및 패키지 설치 문제 해결

## 1. `pip` 명령을 찾을 수 없음

먼저 현재 Python에 연결된 pip를 확인합니다.

```bash
python -m pip --version
```

패키지 설치도 가능하면 다음 형태를 사용합니다.

```bash
python -m pip install pandas
```

## 2. `ModuleNotFoundError`

오류 예:
```text
ModuleNotFoundError: No module named 'pandas'
```

가능한 원인:
- 패키지가 설치되지 않음
- 다른 Python 환경에 설치함
- VS Code Interpreter와 Terminal 환경이 다름
- Jupyter Kernel이 다른 환경을 사용함

현재 Python에 직접 설치합니다.

```bash
python -m pip install pandas
python -c "import pandas; print(pandas.__version__)"
```

## 3. 설치했는데 import가 안 됨

```bash
python -c "import sys; print(sys.executable)"
python -m pip --version
```

두 명령이 같은 Python 환경을 가리키는지 확인합니다.

## 4. `Requirement already satisfied`

오류가 아니라 해당 패키지가 이미 설치되어 있다는 뜻입니다. 다만 설치 위치가 현재 실행 환경과 같은지 확인합니다.

## 5. 패키지 버전 충돌

```bash
python -m pip list
python -m pip check
```

교육 과정에서는 가능하면 동일한 `requirements.txt`를 사용합니다.

```bash
python -m pip install -r requirements.txt
```

[← Troubleshooting 목차](./README.md)