from extraction_markdown import extract_markdown_images, extract_markdown_links

def test_extract_markdown_images():
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
    assert extract_markdown_images(text) == expected

def test_extract_markdown_links():
    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
    assert extract_markdown_links(text) == expected

# Run the tests
test_extract_markdown_images()
test_extract_markdown_links()

print("All tests passed!")