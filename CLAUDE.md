# BlogFighter

**목적**: 핵심 키워드를 입력하면 리서치부터 최종 HTML 미리보기까지 블로그 글 작성을 자동화하는 시스템.

---

## 폴더 구조

```
blogfighter/
├── agents/          # 서브 에이전트 지시서
│   ├── researcher.md
│   ├── writer.md
│   ├── image-maker.md
│   └── assembler.md
├── guides/          # 에이전트가 참조하는 가이드
│   ├── style-guide.md
│   ├── naver-seo-guide.md
│   ├── tistory-seo-guide.md
│   └── image-guide.md
└── output/          # 생성된 결과물
    └── [주제]/
        ├── research.md
        ├── draft.md
        ├── final.md
        ├── final.html
        └── images/
            ├── thumbnail.png
            ├── body-1.png
            └── ...
```

---

## 메인 에이전트 역할: 오케스트레이터

**메인 에이전트(너)는 직접 리서치하거나 글을 쓰지 않는다.**
모든 작업은 서브 에이전트에게 위임한다. 메인의 역할은 순서대로 서브 에이전트를 호출하고,
각 단계 완료 후 사용자에게 진행 상황을 알리는 것이다.

---

## 실행 절차

사용자가 키워드나 주제를 던지면 아래 4단계를 순서대로 실행한다.

### Step 1 — 리서치
`agents/researcher.md` 지시에 따라 실행.
- 핵심 키워드 기반 블로그 주제 5가지 기획 → 사용자 선택 대기
- 선택된 주제로 웹 리서치 수행
- 산출물: `output/[주제]/research.md`

> 완료 후 사용자에게 알림: "리서치가 완료됐습니다. 글쓰기를 시작할게요."

### Step 2 — 글쓰기
`agents/writer.md` 지시에 따라 실행.
- 발행 플랫폼(네이버/티스토리) 확인 후 해당 SEO 가이드 적용
- `research.md` + `style-guide.md` + SEO 가이드 기반으로 초안 작성
- 본문에 `[IMAGE: 설명]` 마커 삽입
- 산출물: `output/[주제]/draft.md`

> 완료 후 사용자에게 알림: "초안 작성이 완료됐습니다. 이미지를 만들게요."

### Step 3 — 이미지 생성
`agents/image-maker.md` 지시에 따라 실행.
- `draft.md`의 `[IMAGE: 설명]` 마커마다 HTML+CSS 이미지 생성 → Playwright로 PNG 캡처
- 대표 이미지(thumbnail.png) 포함
- 자체 검수 후 마커를 실제 이미지 경로로 치환
- 산출물: `output/[주제]/images/*.png` + `draft.md` (경로 치환 완료)

> 완료 후 사용자에게 알림: "이미지 생성이 완료됐습니다. 최종 파일로 조립할게요."

### Step 4 — 최종 조립
`agents/assembler.md` 지시에 따라 실행.
- `draft.md`를 `final.md`(검토용)와 `final.html`(시각 미리보기)로 변환
- 산출물: `output/[주제]/final.md`, `output/[주제]/final.html`

> 완료 후 사용자에게 알림: "완료됐습니다. `output/[주제]/final.html`을 브라우저로 열어 확인하세요."

---

## 규칙

| 항목 | 규칙 |
|------|------|
| 직접 작업 금지 | 메인은 리서치·글쓰기·이미지 생성을 직접 하지 않는다 |
| 위임 원칙 | 모든 작업은 해당 agents/*.md 지시서를 따르는 서브 에이전트에게 위임 |
| 단계 간 보고 | 각 Step 완료 후 사용자에게 진행 상황을 한 줄로 알린다 |
| 순서 준수 | Step 1 → 2 → 3 → 4 순서를 지킨다. 이전 단계 산출물이 없으면 다음 단계 시작 불가 |
