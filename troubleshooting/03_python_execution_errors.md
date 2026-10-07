# 03. Python 코드 실행 문제 해결

## 1. 파일을 찾을 수 없음

오류 예:
```text
python: can't open file 'hello.py': [Errno 2] No such file or directory
```

현재 작업 위치와 파일 목록을 확인합니다.

```bash
pwd
ls
```

Windows CMD에서는 `cd`, `dir`을 사용할 수 있습니다. 파일이 있는 폴더로 이동한 뒤 실행합니다.

```bash
cd 폴더이름
python hello.py
```

## 2. 실행했는데 아무것도 출력되지 않음

`.py` 파일에서는 계산 결과가 자동 출력되지 않습니다.

```python
a = 10
b = 20
c = a + b
print(c)
```

## 3. 잘못된 파일을 실행함

`test.py`, `test1.py`, `test_final.py`처럼 비슷한 이름이 있다면 실행 명령의 파일명을 확인합니다.

## 4. 실행이 끝나지 않음

무한 반복일 수 있습니다. Terminal에서 보통 `Ctrl + C`로 중단합니다.

## 5. 상대경로 문제

현재 작업 폴더를 확인합니다.

```python
import os
print(os.getcwd())
```

파일 경로가 현재 작업 폴더 기준으로 올바른지 확인합니다.

[← Troubleshooting 목차](./README.md)