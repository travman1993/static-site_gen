import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_to_html_no_tag(self):
        node = LeafNode(value="Just Plain Text")
        self.assertEqual(node.to_html(), "Just Plain Text")
    
    def test_to_html_with_tag(self):
        node = LeafNode(tag="a", value="Click Here", props={"href": "https://www.example.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.example.com">Click Here</a>')

    def test_value_required(self):
        with self.assertRaises(ValueError):
            LeafNode(tag="p")

if __name__ == "__main__":
    unittest.main()