from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            if delimiter not in node.text:
                raise Exception(f"Invalid Markdown syntax : {delimiter}")
            else:
                delimiter_type = TextType
                match delimiter:
                    case "**":
                        delimiter_type = TextType.BOLD
                    case "_":
                        delimiter_type = TextType.ITALIC
                    case "`":
                        delimiter_type = TextType.CODE
                node_split = node.text.split(delimiter, 2)
                for i in range(0, len(node_split)):
                    match i:
                        case 0 | 2:
                            new_nodes.append(TextNode(node_split[i], TextType.TEXT))
                        case 1:
                            new_nodes.append(TextNode(node_split[i], delimiter_type))
    return new_nodes
                