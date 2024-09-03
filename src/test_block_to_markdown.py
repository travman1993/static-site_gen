import unittest
from block_to_markdown import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):

    def test_heading(self):
        markdown = "# This is a heading\n\nThis is a paragraph."
        expected = ["# This is a heading", "This is a paragraph."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_paragraph_with_formatting(self):
        markdown = "This is a paragraph of text. It has some **bold** and *italic* words inside of it."
        expected = ["This is a paragraph of text. It has some **bold** and *italic* words inside of it."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_list_items(self):
        markdown = "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        expected = ["* This is the first list item in a list block", "* This is a list item", "* This is another list item"]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_multiple_blocks(self):
        markdown = "# Heading\n\nThis is a paragraph.\n\n* List item 1\n* List item 2"
        expected = ["# Heading", "This is a paragraph.", "* List item 1", "* List item 2"]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_empty_blocks(self):
        markdown = "\n\n# Heading\n\n\nThis is a paragraph.\n\n\n* List item 1\n* List item 2\n\n\n"
        expected = ["# Heading", "This is a paragraph.", "* List item 1", "* List item 2"]
        self.assertEqual(markdown_to_blocks(markdown), expected)

if __name__ == "__main__":
    unittest.main()