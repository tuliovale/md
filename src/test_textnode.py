import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr_eq(self):
        node = TextNode("This is jarvis cloud", TextType.LINK, "https://cloud.tuliovale.com")
        self.assertEqual(node.__repr__(), "TextNode(This is jarvis cloud, TextType.LINK, https://cloud.tuliovale.com)")

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is jarvis cloud", TextType.LINK, "https://cloud.tuliovale.com")
        node2 = TextNode("This is jarvis cloud", TextType.LINK, "https://cloud.tuliovale.com")
        self.assertEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("This is jarvis cloud", TextType.LINK, "https://cloud.tuliovale.com")
        node2 = TextNode("This is jarvis cloud", TextType.LINK, "https://tuliovale.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()