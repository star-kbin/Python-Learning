# 07. Python에서 자주 발생하는 오류

## 1. SyntaxError

문법이 잘못된 경우 발생합니다.

```python
print("Hello"
```

수정:
```python
print("Hello")
```

괄호, 따옴표, 콜론(`:`), 오타를 확인합니다.

## 2. NameError

정의하지 않은 변수나 함수를 사용했을 때 발생합니다.

```python
score = 90
print(score)
```

## 3. IndentationError

들여쓰기가 잘못된 경우 발생합니다.

```python
if score >= 60:
    print("Pass")
```

## 4. TypeError

서로 맞지 않는 자료형으로 연산할 때 발생합니다.

```python
age = 20
print("나이:", age)
```

## 5. ValueError

자료형 변환은 가능하지만 값이 적절하지 않을 때 발생합니다.

```python
age = int("hello")
```

## 6. ModuleNotFoundError

```text
ModuleNotFoundError: No module named 'pandas'
```

```bash
python -m pip install pandas
```

## 7. FileNotFoundError

파일명, 확장자, 현재 작업 폴더, 상대경로를 확인합니다.

```python
import os
print(os.getcwd())
```

## 8. IndexError

리스트 범위를 벗어난 인덱스를 사용했는지 확인합니다.

## 9. KeyError

Dictionary에 존재하지 않는 Key를 사용했는지 확인합니다.

## 오류 메시지 읽는 방법

```text
Traceback ...
  File "test.py", line 5
    print(score)
NameError: name 'score' is not defined
```

핵심은 **파일명 → 줄 번호 → 오류 종류 → 상세 메시지**입니다. 오류 메시지의 마지막 줄부터 읽으면 원인을 빠르게 찾기 쉽습니다.

[← Troubleshooting 목차](./README.md)