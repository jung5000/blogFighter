import os
import subprocess
import sys

def install_playwright():
    try:
        import playwright
    except ImportError:
        print("Installing playwright...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright"])
        subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])

install_playwright()

from playwright.sync_api import sync_playwright

output_dir = "output/LED손거울/images"
os.makedirs(output_dir, exist_ok=True)

html_template = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
body {{
    margin: 0; padding: 0; background: linear-gradient(135deg, #1a1a2e, #16213e);
    color: white; font-family: 'Malgun Gothic', sans-serif;
    display: flex; flex-direction: column; justify-content: center; align-items: center;
    text-align: center; height: {height}px; width: {width}px;
}}
.container {{
    width: 80%; padding: 40px; border: 2px solid rgba(255,255,255,0.1);
    border-radius: 20px; background: rgba(0,0,0,0.3);
}}
h1 {{ font-size: {h1_size}px; margin-bottom: 20px; color: #4facfe; }}
p {{ font-size: {p_size}px; color: #ccc; line-height: 1.5; }}
</style>
</head>
<body>
<div class="container">
    <h1>{title}</h1>
    <p>{desc}</p>
</div>
</body>
</html>
"""

images = [
    {"name": "thumbnail_naver.png", "title": "LED 손거울 3가지 필수 기준!", "desc": "실패 없는 메이크업 거울 고르기", "w":1080, "h":1080, "h1":80, "p":40},
    {"name": "thumbnail_tistory.png", "title": "LED 메이크업 거울 구매 가이드", "desc": "CRI, 디밍, 확대경 완벽 분석", "w":1080, "h":1080, "h1":80, "p":40},
    {"name": "화장대 위 밝게 켜진 세련된 LED 손거울 클로즈업 사진.png", "title": "조명 거울 필수 체크포인트", "desc": "화장대 위의 완벽한 조명 솔루션", "w":800, "h":600, "h1":50, "p":30},
    {"name": "CRI 지수에 따른 색상 왜곡 차이를 보여주는 비교 다이어그램.png", "title": "연색성(CRI) 비교표", "desc": "CRI 90 이상 vs 일반 조명", "w":800, "h":600, "h1":50, "p":30},
    {"name": "얼굴 정면을 고르게 비춰 그림자가 없는 화사한 인물 사진.png", "title": "그림자 방지 설계", "desc": "디밍 기능으로 맞춤형 밝기 조절", "w":800, "h":600, "h1":50, "p":30},
    {"name": "파우치 옆에 놓인 작고 깔끔한 C타입 충전식 휴대용 LED 거울.png", "title": "휴대성 & 충전방식", "desc": "파우치에 쏙 들어가는 C타입 충전형", "w":800, "h":600, "h1":50, "p":30},
    {"name": "따뜻한 자연광이 들어오는 창가에 놓인 화사한 탁상용 LED 거울.png", "title": "빛의 질 = 메이크업의 질", "desc": "자연광과 유사한 최적의 조명 환경", "w":800, "h":600, "h1":50, "p":30},
    {"name": "연색성(CRI) 수치가 높을수록 본연의 색을 잘 보여준다는 인포그래픽.png", "title": "STEP 1: CRI 지수 확인", "desc": "가장 먼저 확인해야 할 연색성(CRI)", "w":800, "h":600, "h1":50, "p":30},
    {"name": "조명 밝기가 여러 단계로 조절되는 스마트 터치식 LED 거울 작동 모습.png", "title": "STEP 2: 디밍(Dimming)", "desc": "시간과 장소에 구애받지 않는 밝기 조절", "w":800, "h":600, "h1":50, "p":30},
    {"name": "아이라인을 그리는 눈을 선명하게 비춰주는 확대경 거울 사용 컷.png", "title": "STEP 3: 확대 기능", "desc": "디테일을 완성하는 확대경 필수 체크", "w":800, "h":600, "h1":50, "p":30},
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    for img in images:
        html = html_template.format(width=img["w"], height=img["h"], h1_size=img["h1"], p_size=img["p"], title=img["title"], desc=img["desc"])
        page.set_viewport_size({"width": img["w"], "height": img["h"]})
        page.set_content(html)
        page.screenshot(path=os.path.join(output_dir, img["name"]))
    browser.close()

print("Images generated successfully.")
