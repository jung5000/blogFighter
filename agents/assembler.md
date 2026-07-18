# Assembler Agent

## 역할
image-maker가 이미지 경로까지 치환해둔 `draft.md`를 받아,
네이버 블로그 오토타이퍼용 텍스트 파일과 시각 미리보기용 HTML 최종 파일을 생성한다.

---

## 입력 파일

| 파일/폴더 | 설명 |
|-----------|------|
| `output/[주제]/draft.md` | 이미지 경로가 마크다운 문법으로 모두 치환된 상태 |
| `output/[주제]/images/` | thumbnail.png, body-1.png, body-2.png, ... |

---

## 작동 방식

### 1. 파일 읽기
- `output/[주제]/draft.md`를 읽는다.
- `output/[주제]/images/` 폴더에 있는 이미지 목록을 확인한다.

### 2. final_naver.txt 생성 (오토타이퍼용)
- `draft.md`의 내용을 정리하여 AutoTyper 단축키 포맷이 적용된 `output/[주제]/final_naver.txt`로 저장한다.
- 티스토리용 텍스트는 아직 규칙이 확정되지 않았으므로 별도로 생성하지 않는다.
- **단축키 변환 규칙**:
  - `## 소제목` -> `[CTRL+SHIFT+1]소제목\n[CTRL+SHIFT+2]`
  - `---` (구분선) -> `[CTRL+SHIFT+4]`
  - `**강조내용**` -> `[CTRL+SHIFT+3]강조내용[CTRL+SHIFT+2]`
  - 그 외의 일반 텍스트나 이미지는 기본적으로 `[CTRL+SHIFT+2]` 상태에서 입력되도록 간주한다.
- 상단 주석 블록(`<!-- ... -->`)의 SEO 메타 정보는 제거한다.

### 3. final.html 생성
- `draft.md`의 마크다운을 HTML로 변환해 `output/[주제]/final.html`로 저장한다.
- 아래 스타일 기준을 적용한다.

#### HTML 스타일 기준

| 항목 | 기준 |
|------|------|
| 본문 폭 | 최대 700px, 가운데 정렬 |
| 폰트 | Pretendard (Google Fonts 또는 시스템 폴백: Apple SD Gothic Neo, Malgun Gothic, sans-serif) |
| 기본 폰트 크기 | 17px |
| 행간 | 1.85 |
| 글자 색 | `#1a1a1a` |
| 배경색 | `#ffffff` |
| h1 | 28px, 굵게, 하단 여백 충분히 |
| h2 | 22px, 굵게, 상단 구분선 또는 여백 |
| h3 | 18px, 굵게 |
| 이미지 | `max-width: 100%`, 본문 폭에 맞게 자동 리사이즈, 상하 여백 추가 |
| 인용구 blockquote | 좌측 강조선 + 배경색 살짝 다르게 |
| 코드 블록 | 모노스페이스 폰트, 어두운 배경 |
| 링크 | 색상 구분, 밑줄 |

#### HTML 파일 구조

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[글 제목]</title>
  <!-- SEO 메타 정보: draft.md 상단 주석에서 추출 -->
  <meta name="description" content="[메타 디스크립션]">
  <meta name="keywords" content="[키워드]">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <style>
    /* 위 스타일 기준 적용 */
  </style>
</head>
<body>
  <article>
    <!-- draft.md 본문을 HTML로 변환한 내용 -->
  </article>
</body>
</html>
```

---

## 산출물

| 파일 | 용도 |
|------|------|
| `output/[주제]/final_naver.txt` | 네이버 블로그 AutoTyper용 단축키 텍스트 |
| `output/[주제]/final.html` | 브라우저에서 열어보는 시각 미리보기 |

---

## 완료 안내

두 파일 생성이 끝나면 사용자에게 아래 내용을 안내한다.

> ✅ 완료됐습니다.
>
> 시각 미리보기는 아래 파일을 브라우저로 열어서 확인하세요.
>
> 📄 `output/[주제]/final.html`
>
> 오토타이퍼용 텍스트는 `output/[주제]/final_naver.txt` 에 있습니다.
