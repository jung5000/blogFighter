import os
import subprocess
import sys
import re

def install_pkg():
    try:
        import markdown
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "markdown"])

install_pkg()
import markdown

output_dir = "output/LED손거울"

def process_file(md_filename, out_html, out_md):
    md_path = os.path.join(output_dir, md_filename)
    if not os.path.exists(md_path):
        return
        
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    with open(os.path.join(output_dir, out_md), 'w', encoding='utf-8') as f:
        f.write(content)
        
    # Extract metadata
    title = ""
    description = ""
    keywords = ""
    
    title_match = re.search(r'<!--\s*title:\s*(.*?)\s*-->', content)
    if title_match: title = title_match.group(1)
    
    desc_match = re.search(r'<!--\s*description:\s*(.*?)\s*-->', content)
    if desc_match: description = desc_match.group(1)
    
    kw_match = re.search(r'<!--\s*keywords:\s*(.*?)\s*-->', content)
    if kw_match: keywords = kw_match.group(1)
    
    html_content = markdown.markdown(content)
    
    html_template = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="keywords" content="{keywords}">
  <style>
    body {{
      max-width: 700px;
      margin: 0 auto;
      font-family: 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;
      font-size: 17px;
      line-height: 1.85;
      color: #1a1a1a;
      background-color: #ffffff;
      padding: 20px;
    }}
    h1 {{ font-size: 28px; font-weight: bold; margin-bottom: 40px; }}
    h2 {{ font-size: 22px; font-weight: bold; margin-top: 40px; border-top: 1px solid #eee; padding-top: 20px; }}
    h3 {{ font-size: 18px; font-weight: bold; }}
    img {{ max-width: 100%; height: auto; margin: 20px 0; display: block; }}
    blockquote {{ border-left: 4px solid #4facfe; background-color: #f8f9fa; padding: 10px 20px; margin: 20px 0; }}
    code {{ font-family: monospace; background-color: #333; color: #fff; padding: 2px 5px; border-radius: 4px; }}
    a {{ color: #0066cc; text-decoration: underline; }}
  </style>
</head>
<body>
  <article>
    {html_content}
  </article>
</body>
</html>
"""
    with open(os.path.join(output_dir, out_html), 'w', encoding='utf-8') as f:
        f.write(html_template)

process_file("draft_naver.md", "final_naver.html", "final_naver.md")
process_file("draft_tistory.md", "final_tistory.html", "final_tistory.md")
print("Assembly complete.")
