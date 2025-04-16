import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode("a", "example", None, {"href": "https://www.google.com"})
        node2 = HTMLNode("a", "example", None, {"href": "https://www.google.com"})
        self.assertEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()