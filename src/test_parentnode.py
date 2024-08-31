import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        node = ParentNode(
            tag="div",
            children=[
                LeafNode("p", "First paragraph"),
                ParentNode(
                    tag="section",
                    children=[
                        LeafNode("h1", "Header"),
                        ParentNode(
                            tag="ul",
                            children=[
                                LeafNode("li", "Item 1"),
                                LeafNode("li", "Item 2"),
                            ]
                        ),
                    ]
                ),
            ]
        )
        expected_html = (
            "<div>"
            "<p>First paragraph</p>"
            "<section>"
            "<h1>Header</h1>"
            "<ul>"
            "<li>Item 1</li>"
            "<li>Item 2</li>"
            "</ul>"
            "</section>"
            "</div>"
        )
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_no_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(tag=None, children=[LeafNode("b", "Text")])

    def test_to_html_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode(tag="p", children=[])

if __name__ == "__main__":
    unittest.main()