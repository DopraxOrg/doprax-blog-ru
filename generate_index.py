import os
import re

BLOG_DIR = "blog"

def get_title(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    match = re.search(r'^title:\s*(.+)', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return os.path.basename(filepath).replace(".md","")  # fallback

posts = sorted(os.listdir(BLOG_DIR), reverse=True)

lines = []

for post in posts:
    if post.endswith(".md"):
        filepath = os.path.join(BLOG_DIR, post)
        title = get_title(filepath)
        date = post[:10]  # YYYY-MM-DD
        lines.append(f"- **{date}** — [{title}](blog/{post})")

blog_index = "\n".join(lines)

def update_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    start = "<!-- BLOG START -->"
    end = "<!-- BLOG END -->"
    before = content.split(start)[0]
    after = content.split(end)[1]
    new_content = before + start + "\n" + blog_index + "\n" + end + after
    with open(filename, "w", encoding="utf-8") as f:
        f.write(new_content)

update_file("README.md")
update_file("index.md")