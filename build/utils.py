import html as _html


def esc(s):
    """HTML-escape a string."""
    return _html.escape(str(s), quote=True)
