from textnode import TextType, TextNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            text = node.text
            delimited_texts = extract_markdown_by_delimiter(text, delimiter)
            for delimited_text in delimited_texts:
                separator = f"{delimiter}{delimited_text}{delimiter}"
                split_index = text.find(separator)
                new_nodes.append(TextNode(text[:split_index], TextType.TEXT))
                new_nodes.append(TextNode(delimited_text, text_type))
                text = re.sub(rf".*?{re.escape(delimiter)}{re.escape(delimited_text)}{re.escape(delimiter)}", "", text, count=1)
            if text:
                new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

def extract_markdown_by_delimiter(text, delimiter):
    match delimiter:
        case "**":
            matches = list(re.findall(r"\*\*.*?\*\*", text))
            delimited_texts = [s.replace("**", "") for s in matches]
        case "_":
            matches = list(re.findall(r"\_.*?\_", text))
            delimited_texts = [s.replace("_", "") for s in matches]
        case "`":
            matches = list(re.findall(r"\`.*?\`", text))
            delimited_texts = [s.replace("`", "") for s in matches]
        case _:
            raise Exception("Invalid Markdown Syntax")
    return delimited_texts

def split_nodes_image(old_node):
    new_nodes = []
    for node in old_node:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            text = node.text
            images = extract_markdown_images(text)
            for image in images:
                separator = f"![{image[0]}]({image[1]})"
                split_index = text.find(separator)
                new_nodes.append(TextNode(text[:split_index], TextType.TEXT))
                new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
                text = re.sub(r".*?!\[.*?\]\(https?:\/\/.*?\)", "", text, count=1)
            if text:
                new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_node):
    new_nodes = []
    for node in old_node:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            text = node.text
            links = extract_markdown_links(text)
            for link in links:
                separator = f"[{link[0]}]({link[1]})"
                split_index = text.find(separator)
                new_nodes.append(TextNode(text[:split_index], TextType.TEXT))
                new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
                text = re.sub(r".*?(?<!!)\[.*?\]\(https?:\/\/.*?\)", "", text, count=1)
            if text:
                new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

def extract_markdown_images(text):
    matches = list(re.findall(r"(!\[.*?\])(\(https?:\/\/.*?\))", text))
    images = list(zip([i[0].replace("![", "").replace("]", "") for i in matches], [i[1].replace("(", "").replace(")", "") for i in matches]))
    return images

def extract_markdown_links(text):
    matches = list(re.findall(r"((?<!!)\[.*?\])(\(https?:\/\/.*?\))", text))
    links = list(zip([i[0].replace("[", "").replace("]", "") for i in matches], [i[1].replace("(", "").replace(")", "") for i in matches]))
    return links