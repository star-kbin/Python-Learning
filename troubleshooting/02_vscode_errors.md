# 02. VS Code 문제 해결

## 1. Python Interpreter가 보이지 않음

`Ctrl + Shift + X` → `Python` 검색 → Microsoft의 Python Extension을 설치합니다.

그 다음:
```text
Ctrl + Shift + P
→ Python: Select Interpreter
```
설치한 Python 환경을 선택합니다.

## 2. 실행 버튼이 보이지 않음

- 파일 확장자가 `.py`인지 확인
- Python Extension 설치 여부 확인
- VS Code 오른쪽 아래 Language Mode가 `Python`인지 확인

## 3. Terminal과 VS Code 실행 결과가 다름

현재 Interpreter와 Terminal의 Python이 다를 수 있습니다.

```bash
python --version
python -c "import sys; print(sys.executable)"
```

## 4. 수정한 코드가 반영되지 않음

`Ctrl + S`로 저장한 뒤 다시 실행합니다.

## 5. Terminal이 보이지 않음

`Terminal → New Terminal` 또는 `Ctrl + \``를 사용합니다.

## 빠른 체크
- [ ] `.py` 파일인가?
- [ ] Python Extension이 설치되어 있는가?
- [ ] 올바른 Interpreter인가?
- [ ] 파일을 저장했는가?
- [ ] Terminal에서 Python 버전을 확인했는가?

[← Troubleshooting 목차](./README.md)