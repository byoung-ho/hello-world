# Hello DevOps - GitHub Actions 실습

DevOps CI/CD 파이프라인을 3단계로 체험하는 실습 프로젝트입니다.

## 프로젝트 구조

```
hello-world/
├── .github/workflows/
│   ├── 01-hello.yml        # 1단계: CI 기본
│   ├── 02-lint-test.yml    # 2단계: 린트 + 테스트
│   └── 03-docker.yml       # 3단계: Docker 빌드
├── app/
│   └── main.py             # FastAPI 앱
├── tests/
│   └── test_main.py        # 테스트 코드
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 실습 전 준비

1. 이 저장소를 GitHub에 push 합니다
2. GitHub 웹에서 **Actions** 탭을 클릭합니다

---

## 1단계: CI 기본 - "push하면 자동으로 뭔가 돌아간다"

**워크플로우:** `01-hello.yml`

**체험 포인트:**
- 코드를 push하기만 하면 GitHub이 자동으로 스크립트를 실행한다
- Actions 탭에서 실행 결과를 확인한다 (초록 체크 = 성공, 빨간 X = 실패)

**실습:**
```bash
# 아무 파일이나 수정 후 push
git add .
git commit -m "1단계: CI 체험"
git push
```
→ Actions 탭에서 "Step 1 - Hello CI" 워크플로우 확인

---

## 2단계: CI 심화 - "코드 품질을 자동으로 검사한다"

**워크플로우:** `02-lint-test.yml`

**체험 포인트:**
- **린트(Ruff):** 코딩 스타일이 규칙에 맞는지 자동 검사
- **테스트(Pytest):** 함수가 올바르게 동작하는지 자동 확인
- 하나라도 실패하면 빨간불 → PR 머지 차단 가능

**실습 A - 성공 케이스:**
```bash
git push  # 현재 코드는 모든 검사 통과
```

**실습 B - 일부러 실패시키기:**
```python
# app/main.py 에서 add 함수를 고의로 망가뜨려 보세요
def add(a: int, b: int) -> int:
    return a - b  # 일부러 빼기로 변경!
```
```bash
git add .
git commit -m "2단계: 일부러 테스트 실패시키기"
git push
```
→ Actions 탭에서 테스트가 **실패(빨간 X)** 하는 것을 확인

---

## 3단계: CD 체험 - "Docker 이미지가 자동으로 빌드된다"

**워크플로우:** `03-docker.yml`

**체험 포인트:**
- 2단계(린트+테스트) 를 **통과해야만** Docker 빌드가 진행됨 (`needs` 키워드)
- 빌드된 이미지로 컨테이너를 띄우고 `/health` API를 호출해서 검증
- 실제 배포 파이프라인의 축소판

**실습:**
```bash
# 2단계에서 망가뜨린 코드를 원래대로 복구
def add(a: int, b: int) -> int:
    return a + b
```
```bash
git add .
git commit -m "3단계: 코드 복구 → Docker 빌드 체험"
git push
```
→ Actions 탭에서 린트+테스트 통과 후 Docker 빌드까지 성공하는 **전체 파이프라인** 확인

---

## DevOps 핵심 개념 정리

| 개념 | 설명 | 이 실습에서 |
|------|------|------------|
| **CI (지속적 통합)** | 코드 변경 시 자동으로 빌드/테스트 | 1~2단계 |
| **CD (지속적 배포)** | 검증 통과 후 자동 배포 | 3단계 |
| **파이프라인** | CI→CD로 이어지는 자동화 흐름 | 3단계의 `needs` |
| **실패 시 차단** | 품질 미달 코드가 배포되지 않게 방지 | 2단계 실패 실습 |
