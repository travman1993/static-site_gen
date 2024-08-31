from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children):
        if tag is None:
            raise ValueError("A tag is required for ParentNode.")
        if children is None or len(children) == 0:
            raise ValueError("Children are required for ParentNode.")
        super().__init__(tag=tag, value=None, children=children, props={})

    def to_html(self):
        if self.tag is None:
            raise ValueError("A tag is required for ParentNode.")
        if not self.children:
            raise ValueError("Children are required for ParentNode.")
        children_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}>{children_html}</{self.tag}>"