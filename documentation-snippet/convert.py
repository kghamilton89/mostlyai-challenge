import markdown

with open("documentation-snippet.md", "r", encoding="utf-8") as f:
    md_content = f.read()

html_content = markdown.markdown(md_content)

with open("documentation-snippet.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✅ HTML file saved: documentation-snippet.html")
