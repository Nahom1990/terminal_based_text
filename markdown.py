from dataclasses import dataclass
from typing import Dict,Iterable,List,Optional

from markdown_it import MarkdownIt

from .console import Console,ConsoleOptions, StyledText
from .style import Style

@dataclass
class MarkdownHeading:
    """A markdown document heading"""

    test:str
    level:int
    width:int

    def __console__(self)->str:
        pass

class Markdown:
    """Render markdown to the console."""

    def __init__(self, markup: str) -> None:
        self.markup = markup

    def __console_render__(
        self, console: Console, options: ConsoleOptions
    ) -> Iterable[StyledText]:

        width = options.max_width
        
        # 1. Initialize the modern markdown-it parser
        md_parser = MarkdownIt()
        
        # 2. Parse the markup into a linear list of tokens
        tokens = md_parser.parse(self.markup)

        rendered: List[StyledText] = []
        append = rendered.append
        stack = [Style()]

        style: Optional[Style]

        for token in tokens:
            # Handle block-level structures containing text elements
            if token.type == "inline":
                if token.children:
                    for child in token.children:
                        # Extract structural type (e.g., 'em_open', 'text', etc.)
                        node_type = child.type
                        
                        # Handle base text contents
                        if node_type == "text":
                            style = stack[-1].apply(console.get_style("markdown.text"))
                            append(StyledText(child.content, style))
                            
                        # Handle formatting start tags (e.g., strong_open, em_open)
                        elif node_type.endswith("_open"):
                            clean_type = node_type.replace("_open", "")
                            style = console.get_style(f"markdown.{clean_type}")
                            if style is not None:
                                stack.append(stack[-1].apply(style))
                            else:
                                stack.append(stack[-1])
                                
                        # Handle formatting end tags (e.g., strong_close, em_close)
                        elif node_type.endswith("_close"):
                            if len(stack) > 1:
                                stack.pop()

            # Handle paragraph spacing
            elif token.type == "paragraph_close":
                append(StyledText("\n\n", stack[-1]))
                
            # Handle block-level code blocks/fences directly
            elif token.type in ("fence", "code_block"):
                style = console.get_style("markdown.code") or stack[-1]
                append(StyledText(token.content, style))

        print(rendered)
        return rendered


markup = """*hello*, **world**!

# Hi

```python
code
```

"""

if __name__ == "__main__":
    from .console import Console

    console = Console()
    md = Markdown(markup)

    console.print(md)
    # print(console.render_spans())