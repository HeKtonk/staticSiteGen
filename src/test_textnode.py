import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_notEqText(self):
        node = TextNode("I'm a text node", TextType.LINK, "[link](https:boot.dev)")
        node2 = TextNode("I'm another one text node", TextType.IMAGE, "![image](url/to/image.png)")
        self.assertNotEqual(node, node2)

    def test_notEqTextType(self):
        node = TextNode("I'm a text node", TextType.LINK, "[link](https:boot.dev)")
        node2 = TextNode("I'm another one text node", TextType.IMAGE, "![image](url/to/image.png)")
        self.assertNotEqual(node, node2)

    def test_notEqUrl(self):
        node = TextNode("I'm a text node", TextType.LINK, "[link](https:boot.dev)")
        node2 = TextNode("I'm another one text node", TextType.IMAGE, "![image](url/to/image.png)")
        self.assertNotEqual(node, node2)

    def test_urlIsNone(self):
        node = TextNode("I'm a text node", TextType.CODE)
        self.assertIsNone(node.url)

    def test_urlNotNone(self):
        node = TextNode("I'm a text node", TextType.PLAIN, "Plain text")
        self.assertIsNotNone(node.url)

if __name__ == "__main__":
    unittest.main()