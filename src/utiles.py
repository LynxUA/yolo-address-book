import textwrap


def wrap_text(text, width, initial_indent, subsequent_indent):
        return textwrap.fill(text, width=width, initial_indent=initial_indent, subsequent_indent=subsequent_indent)
