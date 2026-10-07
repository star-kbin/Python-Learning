# 05. Jupyter Notebook 문제 해결

## 1. Kernel을 선택할 수 없음

VS Code에 **Python**과 **Jupyter** Extension이 설치되어 있는지 확인합니다. Notebook 오른쪽 위에서 `Select Kernel`을 선택합니다.

## 2. ipykernel 오류

```bash
python -m pip install ipykernel
```

설치 후 Notebook을 다시 열고 Kernel을 선택합니다.

## 3. Terminal에서는 되는데 Notebook에서는 `ModuleNotFoundError`

Notebook Kernel과 패키지를 설치한 Python 환경이 다를 수 있습니다.

Notebook Cell:
```python
import sys
print(sys.executable)
```

Terminal:
```bash
python -c "import sys; print(sys.executable)"
```

두 경로를 비교합니다.

## 4. Cell이 계속 실행 중임

무한 반복이나 오래 걸리는 작업일 수 있습니다. **Interrupt Kernel**을 먼저 사용하고, 필요하면 **Restart Kernel**을 실행합니다.

## 5. 위 Cell을 실행하지 않아 `NameError` 발생

Notebook은 Cell 실행 순서의 영향을 받습니다. 문제가 의심되면 다음 순서로 다시 실행합니다.

```text
Restart Kernel
→ Run All
```

## 6. 이전 결과가 남아 있음

출력 결과를 지우고 Kernel을 재시작한 뒤 전체 실행합니다.

[← Troubleshooting 목차](./README.md)