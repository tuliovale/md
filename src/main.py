from textnode import TextType, TextNode
def main():
    node = TextNode("This is a link", TextType.LINK, "http://jarvis")
    print(node.__repr__())


main()