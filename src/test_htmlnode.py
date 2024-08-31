import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode(tag="a", props={"href": "https://www.example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), 'href="https://www.example.com" target="_blank"')

    def test_default_values(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})

    def test_repr(self):
        node = HTMLNode(tag="p", value="Hello, world!", props={"class": "intro"})
        expected_repr = ("HTMLNode(tag='p', value='Hello, world!', "
                         "children=[], props={'class': 'intro'})")
        self.assertEqual(repr(node), expected_repr)

if __name__ == "__main__":
    unittest.main()
