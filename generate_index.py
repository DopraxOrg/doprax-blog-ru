import os

BLOG_DIR = "blog"

posts = sorted(os.listdir(BLOG_DIR), reverse=True)

lines = []

for post in posts:
    if post.endswith(".md"):
        name = post.replace(".md","")
        parts = name.split("-")

        date = "-".join(parts[:3])
        title = " ".join(parts[3:]).replace("-", " ").title()

        lines.append(f"- **{date}** — [{title}](blog/{post})")

blog_index = "\n".join(lines)


def update_file(filename):
    with open(filename) as f:
        content = f.read()

    start = "<!-- BLOG START -->"
    end = "<!-- BLOG END -->"

    before = content.split(start)[0]
    after = content.split(end)[1]

    new_content = before + start + "\n" + blog_index + "\n" + end + after

    with open(filename, "w") as f:
        f.write(new_content)


update_file("README.md")
update_file("index.md")