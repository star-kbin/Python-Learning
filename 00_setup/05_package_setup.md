# 05. Python 기본 패키지 설치

## 🎯 학습 목표

- Python 패키지의 개념을 이해한다.
- pip를 이용하여 패키지를 설치한다.
- 데이터 분석에 사용하는 기본 패키지를 알아본다.
- 설치된 패키지를 import하여 확인한다.

---

# 1. Python 패키지란?

Python은 외부 패키지를 추가하여 기능을 확장할 수 있습니다.

주요 패키지는 다음과 같습니다.

- NumPy : 수치 계산 및 다차원 배열
- Pandas : 표 형태 데이터 처리
- Matplotlib : 기본 데이터 시각화
- Seaborn : 통계 시각화
- Scikit-learn : 머신러닝

---

# 2. 패키지 설치

VS Code Terminal에서 다음 명령어를 실행합니다.

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

---

# 3. 설치 확인

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

print("모든 패키지가 에러 없이 정상적으로 로드되었습니다!")
```

---

# 4. 설치된 패키지 목록 확인

```bash
pip list
```

---

# 🧪 간단한 실습

NumPy:

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])
print(numbers)
```

Pandas:

```python
import pandas as pd

data = {
    "name": ["A", "B", "C"],
    "score": [80, 90, 85]
}

df = pd.DataFrame(data)
print(df)
```

---

# ✅ 확인 체크리스트

- [ ] pip 명령 실행 확인
- [ ] NumPy 설치
- [ ] Pandas 설치
- [ ] Matplotlib 설치
- [ ] Seaborn 설치
- [ ] Scikit-learn 설치
- [ ] import 테스트 완료

---

[← Jupyter 설정](./04_jupyter_setup.md)  
[다음 → Workspace 구성](./06_workspace.md)
