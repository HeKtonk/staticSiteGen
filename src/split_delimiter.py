from textnode import TextType, TextNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    markdownType = ["","**","_","`"]
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            if (delimiter in markdownType) and (node.text.count(delimiter) % 2) == 0:
                if node.text.count(delimiter) != 0:
                    node_split = node.text.split(delimiter, 2)
                    for i in range(0, len(node_split)):
                        match i:
                            case 0 | 2:
                                new_nodes.append(TextNode(node_split[i], TextType.TEXT))
                            case 1:
                                new_nodes.append(TextNode(node_split[i], text_type))
                else:
                    new_nodes.append(node)
            else:
                raise Exception("Invalid Markdown Syntax")
    return new_nodes

def extract_markdown_images(text):
    regex = "!\[.*?\]\(https?:\/\/\w\.([A-Z]|[a-z]|[0-9]|-)+\.([a-z]|[0-9]){2,3}\/([A-Z]|[a-z]|[0-9]|[-_/])+\.([A-Z]|[a-z]){3,4}\)"
    matches = re.findall()

def extract_markdown_links(text):
    regex = "\[.*?\]\(https?:\/\/www\.([A-Z]|[a-z]|[0-9]|-)+\.([a-z]|[0-9]){2,3}([A-Z]|[a-z]|[0-9]|[-_/@])*\)"
    pass