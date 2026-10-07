# 08. GitHub Codespaces 문제 해결

## 1. Codespace가 시작되지 않음

GitHub 로그인 상태, Repository 접근 권한, 기존 Codespace 상태를 확인합니다. Repository의 **Code → Codespaces**에서 다시 시작하거나 새 Codespace를 생성합니다.

## 2. Python 명령이 동작하지 않음

```bash
python --version
python3 --version
which python
which python3
```

## 3. Jupyter Notebook이 열리지 않음

Python과 Jupyter Extension이 설치되어 있는지 확인하고 올바른 Kernel을 선택합니다.

## 4. pip로 설치했는데 Notebook에서 찾지 못함

Terminal:
```bash
python -c "import sys; print(sys.executable)"
```

Notebook:
```python
import sys
print(sys.executable)
```

경로가 같은지 확인합니다.

## 5. 수정한 파일이 GitHub에 보이지 않음

파일 저장과 GitHub 반영은 별개입니다.

```bash
git status
git add .
git commit -m "Update learning materials"
git push
```

## 6. `git push` 실패

```bash
git status
git branch
git remote -v
```

다른 곳에서 먼저 변경되었다면 최신 내용을 받아야 할 수 있습니다.

```bash
git pull
```

충돌이 발생하면 충돌 내용을 해결한 뒤 다시 Commit합니다.

## 7. 새 Codespace에서 패키지가 없음

필요한 패키지는 `requirements.txt`에 기록하고 다시 설치합니다.

```bash
python -m pip install -r requirements.txt
```

장기적으로 `.devcontainer/devcontainer.json`에 환경 구성을 정의하면 재현성을 높일 수 있습니다.

## 기본 점검 명령

```bash
python --version
python -m pip --version
git status
pwd
ls
```

[← Troubleshooting 목차](./README.md)