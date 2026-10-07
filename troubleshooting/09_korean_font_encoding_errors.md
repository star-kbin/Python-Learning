# 09. 한글 폰트 및 파일 인코딩 문제 해결

Python에서 한글을 사용할 때 자주 발생하는 문제는 크게 두 가지입니다.

1. **그래프에서 한글이 깨지는 문제** → 폰트(Font) 문제
2. **CSV/TXT 파일을 읽거나 저장할 때 한글이 깨지는 문제** → 인코딩(Encoding) 문제

둘은 원인이 다르므로 구분해서 해결해야 합니다.

---

# 1. 그래프에서 한글이 깨지는 경우

## 🔴 증상

Matplotlib 또는 Seaborn 그래프에서 제목, 축 이름, 범례의 한글이 다음과 같이 표시될 수 있습니다.

```text
□□□
???
```

또는 실행 중 다음과 비슷한 경고가 나타날 수 있습니다.

```text
UserWarning: Glyph ... missing from font(s)
```

## 🔍 원인

Matplotlib이 현재 사용 중인 기본 폰트에서 한글 글리프를 찾지 못해서 발생합니다.

즉, Python 문자열 자체가 잘못된 것이 아니라 **그래프에 사용하는 폰트가 한글을 지원하지 않는 것**이 원인입니다.

---

# 2. Windows에서 Matplotlib 한글 폰트 설정

Windows에서는 일반적으로 `Malgun Gothic`을 사용할 수 있습니다.

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.plot(x, y)
plt.title("월별 생산량")
plt.xlabel("월")
plt.ylabel("생산량")
plt.show()
```

### `axes.unicode_minus = False`를 사용하는 이유

한글 폰트를 설정한 뒤 그래프의 음수 기호가 깨지는 경우가 있습니다.

```python
plt.rcParams["axes.unicode_minus"] = False
```

를 추가하면 일반적인 마이너스 기호로 표시할 수 있습니다.

---

# 3. macOS에서 한글 폰트 설정

macOS에서는 다음과 같이 설정할 수 있습니다.

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "AppleGothic"
plt.rcParams["axes.unicode_minus"] = False
```

---

# 4. Linux / GitHub Codespaces에서 한글 폰트 설정

Linux 또는 GitHub Codespaces에는 한글 폰트가 기본 설치되어 있지 않을 수 있습니다.

먼저 현재 사용할 수 있는 폰트를 확인합니다.

```python
import matplotlib.font_manager as fm

fonts = sorted(set(font.name for font in fm.fontManager.ttflist))

for font in fonts:
    if "Noto" in font or "Nanum" in font:
        print(font)
```

예를 들어 `Noto Sans CJK KR` 또는 `NanumGothic`이 설치되어 있다면 다음과 같이 사용할 수 있습니다.

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Noto Sans CJK KR"
plt.rcParams["axes.unicode_minus"] = False
```

또는:

```python
plt.rcParams["font.family"] = "NanumGothic"
```

> Codespaces 환경에 해당 폰트가 없다면 폰트 패키지를 추가로 설치해야 할 수 있습니다. 환경마다 설치 가능한 폰트명이 다르므로 먼저 사용 가능한 폰트를 확인하는 것이 좋습니다.

---

# 5. 현재 Matplotlib 폰트 확인

현재 Matplotlib이 사용하는 기본 폰트를 확인할 수 있습니다.

```python
import matplotlib.pyplot as plt

print(plt.rcParams["font.family"])
```

시스템에 설치된 폰트 전체를 확인하려면:

```python
import matplotlib.font_manager as fm

for font in fm.fontManager.ttflist:
    print(font.name)
```

---

# 6. Seaborn에서 한글이 깨지는 경우

Seaborn은 내부적으로 Matplotlib을 사용하므로 Matplotlib 폰트 설정을 먼저 적용하면 됩니다.

```python
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

tips = [10, 20, 15, 30]

sns.lineplot(x=[1, 2, 3, 4], y=tips)
plt.title("한글 그래프 테스트")
plt.show()
```

---

# 7. 그래프를 파일로 저장했는데 한글이 깨지는 경우

화면에서는 정상인데 저장한 PNG/PDF에서 한글이 깨지는 경우에도 폰트 설정을 먼저 확인합니다.

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

plt.plot([1, 2, 3], [10, 20, 15])
plt.title("생산량 그래프")

plt.savefig("생산량_그래프.png", dpi=150, bbox_inches="tight")
plt.show()
```

그래프를 저장하기 전에 폰트 설정이 적용되어 있어야 합니다.

---

# 8. 한글 파일 읽기 문제는 폰트가 아니라 인코딩 문제

CSV, TXT 파일을 읽을 때 한글이 깨지는 문제는 대부분 **폰트 문제가 아니라 문자 인코딩 문제**입니다.

대표적인 인코딩:

| 인코딩 | 주로 사용되는 환경 |
|---|---|
| UTF-8 | Python, GitHub, 웹, Linux |
| UTF-8-SIG | Excel 호환이 필요한 UTF-8 CSV |
| CP949 | Windows 한글 환경 |
| EUC-KR | 오래된 한글 시스템 |

---

# 9. CSV 파일 읽기

## 기본 UTF-8

```python
import pandas as pd

df = pd.read_csv("data.csv", encoding="utf-8")
```

## Windows에서 만든 한글 CSV

다음과 같이 시도할 수 있습니다.

```python
df = pd.read_csv("data.csv", encoding="cp949")
```

또는:

```python
df = pd.read_csv("data.csv", encoding="euc-kr")
```

---

# 10. UnicodeDecodeError가 발생하는 경우

## 🔴 오류 예

```text
UnicodeDecodeError: 'utf-8' codec can't decode byte ...
```

## 🔍 원인

파일의 실제 인코딩과 Python에서 지정한 인코딩이 서로 다를 때 발생합니다.

예를 들어 CP949 파일을 UTF-8로 읽으면 오류가 발생할 수 있습니다.

## 🛠 해결

```python
import pandas as pd

df = pd.read_csv("data.csv", encoding="cp949")
```

UTF-8이 아니라고 무조건 CP949라고 단정하기보다는 파일이 생성된 환경을 먼저 확인합니다.

---

# 11. CSV 파일 저장 시 한글 깨짐 방지

Python에서 생성한 CSV를 Excel로 열었을 때 한글이 깨지는 경우가 있습니다.

이 경우 `utf-8-sig`를 사용하면 Windows Excel과의 호환성이 좋아집니다.

```python
df.to_csv(
    "result.csv",
    index=False,
    encoding="utf-8-sig"
)
```

교육용 프로젝트에서는 CSV 저장 시 다음 방식을 권장합니다.

```python
df.to_csv("result.csv", index=False, encoding="utf-8-sig")
```

---

# 12. TXT 파일 읽기

UTF-8 파일:

```python
with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()

print(text)
```

CP949 파일:

```python
with open("sample.txt", "r", encoding="cp949") as file:
    text = file.read()
```

---

# 13. TXT 파일 저장

가능하면 새 파일은 UTF-8로 저장하는 것을 권장합니다.

```python
text = "파이썬 한글 파일 저장 테스트"

with open("result.txt", "w", encoding="utf-8") as file:
    file.write(text)
```

---

# 14. 파일 이름 자체가 한글인 경우

Python 3와 최신 운영체제에서는 대부분 한글 파일명을 사용할 수 있습니다.

```python
import pandas as pd

df = pd.read_csv(
    "생산데이터.csv",
    encoding="utf-8"
)
```

다만 협업, 서버, Linux, Docker, Codespaces 등 다양한 환경을 고려하면 프로젝트 파일명은 영문과 숫자 중심으로 작성하는 것이 관리하기 편합니다.

예:

```text
production_data.csv
battery_result.csv
sensor_data.csv
```

데이터 내부의 컬럼명이나 값에는 한글을 사용해도 됩니다.

---

# 15. 권장 파일 저장 규칙

Python-Learning 과정에서는 가능하면 다음 기준을 권장합니다.

```text
Python 소스 코드      → UTF-8
Markdown 문서          → UTF-8
TXT 파일               → UTF-8
CSV 파일               → UTF-8 또는 UTF-8-SIG
Excel 호환 CSV         → UTF-8-SIG
기존 Windows 한글 CSV  → 필요 시 CP949
```

---

# 16. VS Code 파일 인코딩 확인

VS Code 오른쪽 아래 상태 표시줄에서 현재 파일의 인코딩을 확인할 수 있습니다.

보통:

```text
UTF-8
```

로 표시됩니다.

다른 인코딩의 파일을 열어야 한다면 상태 표시줄의 인코딩 표시를 클릭하여 다음 기능을 사용할 수 있습니다.

```text
Reopen with Encoding
Save with Encoding
```

가능하면 새로 작성하는 Python 코드와 Markdown 파일은 UTF-8로 통일합니다.

---

# 17. 빠른 문제 판단 방법

## 그래프의 한글만 깨진다

```text
→ Font 문제 가능성이 높음
→ Matplotlib font.family 확인
```

## CSV/TXT 내용을 읽을 때 한글이 깨진다

```text
→ Encoding 문제 가능성이 높음
→ utf-8 / cp949 / euc-kr 확인
```

## CSV를 Excel에서 열었을 때만 한글이 깨진다

```text
→ utf-8-sig로 저장
```

## Notebook에서는 되는데 다른 PC에서 그래프 한글이 깨진다

```text
→ 해당 PC에 같은 한글 폰트가 설치되어 있는지 확인
```

---

# ✅ 권장 기본 설정

Windows 환경에서 그래프를 그릴 때:

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False
```

CSV를 저장할 때:

```python
df.to_csv(
    "result.csv",
    index=False,
    encoding="utf-8-sig"
)
```

CSV를 읽을 때:

```python
import pandas as pd

df = pd.read_csv(
    "data.csv",
    encoding="utf-8"
)
```

UTF-8 오류가 발생하고 Windows에서 생성된 파일이라면:

```python
df = pd.read_csv(
    "data.csv",
    encoding="cp949"
)
```

---

# 핵심 정리

```text
그래프 한글 깨짐
→ 폰트(Font) 문제

파일 한글 깨짐
→ 인코딩(Encoding) 문제

Matplotlib
→ 한글 지원 폰트 지정

Python 파일/Markdown
→ UTF-8 권장

CSV + Excel
→ UTF-8-SIG 권장

기존 Windows CSV
→ 필요 시 CP949 확인
```

---

[← Troubleshooting 목차](./README.md)
