import re

def extract_markdown_images(text):
    pattern = r'!\[(.*?)\]\((.*?)\)'
    return re.findall(pattern, text)

def extract_markdown_links(text):
    pattern = r'\[(.*?)\]\((.*?)\)'
    return re.findall(pattern, text)

text_images = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
text_links = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"

print(extract_markdown_images(text_images))
print(extract_markdown_links(text_links))