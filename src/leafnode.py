from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if value is None:
            raise ValueError("Value is required for LeafNode.")
        super().__init__(tag=tag, value=value, children=[], props=props)

    def to_html(self):
        if self.tag is None:
            return self.value
        props_str = self.props_to_html()
        if props_str:
            return f'<{self.tag}{props_str}>{self.value}</{self.tag}>'
        return f"<{self.tag}>{self.value}</{self.tag}>"