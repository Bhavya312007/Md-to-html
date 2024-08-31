import re

def markdown_to_html(markdown_text):
    # Convert headers
    html = re.sub(r'###### (.*)', r'<h6>\1</h6>', markdown_text)
    html = re.sub(r'##### (.*)', r'<h5>\1</h5>', html)
    html = re.sub(r'#### (.*)', r'<h4>\1</h4>', html)
    html = re.sub(r'### (.*)', r'<h3>\1</h3>', html)
    html = re.sub(r'## (.*)', r'<h2>\1</h2>', html)
    html = re.sub(r'# (.*)', r'<h1>\1</h1>', html)

    # Convert blockquotes
    html = re.sub(r'^> (.*)', r'<blockquote>\1</blockquote>', html, flags=re.MULTILINE)

    # Convert code blocks (```)
    html = re.sub(r'```\n([\s\S]*?)\n```', r'<pre><code>\1</code></pre>', html)

    # Convert inline code (`code`)
    html = re.sub(r'`(.*?)`', r'<code>\1</code>', html)

    # Convert bold text
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)

    # Convert italic text
    html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)

    # Convert links
    html = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', html)

    # Convert images
    html = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1">', html)

    # Convert unordered lists
    html = re.sub(r'\n\* (.*?)', r'<ul>\n<li>\1</li>\n</ul>', html)

    # Convert ordered lists
    html = re.sub(r'\n[0-9]+\. (.*?)', r'<ol>\n<li>\1</li>\n</ol>', html)

    # Convert line breaks
    html = re.sub(r'\n', r'<br>\n', html)

    return html

def convert_file(markdown_file, html_file):
    with open(markdown_file, 'r') as md_file:
        markdown_text = md_file.read()

    html_content = markdown_to_html(markdown_text)

    with open(html_file, 'w') as html_file:
        html_file.write(html_content)

    print(f"Converted {markdown_file} to {html_file.name}")

# Example usage
convert_file('README.md', 'output2.html')
