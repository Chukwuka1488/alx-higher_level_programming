#!/usr/bin/python3
def text_indentation(text):
    """
    Print a text with 2 new lines after '.', '?', and ':' characters.

    Args:
    text (str): The input text.

    Raises:
    TypeError: If text is not a string.

    Example:
    >>> text_indentation("Hello. How are you? I'm fine: thank you.")
    Hello.
    
    How are you?
    
    I'm fine: thank you.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = ['.', '?', ':']
    start = 0

    for i, char in enumerate(text):
        if char in chars:
            print(text[start:i + 1].strip())
            print()
            start = i + 1

    if start < len(text):
        print(text[start:].strip())
