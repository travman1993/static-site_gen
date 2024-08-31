import unittest
from textnode import TextNode

class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node1, node2)

    def test_neq_text(self):
        node1 = TextNode("Text A", "bold")
        node2 = TextNode("Text B", "bold")
        self.assertNotEqual(node1, node2)

    def test_neq_text_type(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node1, node2)

    def test_neq_url(self):
        node1 = TextNode("This is a text node", "bold", "https://www.example.com")
        node2 = TextNode("This is a text node", "bold", "https://www.anotherexample.com")
        self.assertNotEqual(node1, node2)

    def test_default_url(self):
        node = TextNode("This is a text node", "bold")
        self.assertIsNone(node.url)

if __name__ == "__main__":
    unittest.main()
