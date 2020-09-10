from typing import Any

class Stack:
    """A last-in-first-out (LIFO) stack of items.
    Stores data in last-in, first-out order. When removing an item from the
    stack, the most recently-added item is the one that is removed.
    """
    def __init__(self) -> None:
        """Initialize a new empty stack."""
        self._item = []

    def is_empty(self) -> bool:
        """Return whether this stack contains no items.
        >>> s = Stack()
        >>> s.is_empty()
        True
        >>> s.push('hello')
        >>> s.is_empty()
        False
        """

        if len(self._item) != 0:
            return False

        return True

    def push(self, item: Any) -> None:
        """Add a new element to the top of this stack.
        """
        self._item.append(item)

    def pop(self) -> Any:
        """Remove and return the element at the top of this stack.
        >>> s = Stack()
        >>> s.push('hello')
        >>> s.push('goodbye')
        >>> s.pop()
        'goodbye'
        """
        if len(self._item) == 0:
            return None

        item = self._item.pop()
        return item


def is_balanced(line: str) -> bool:
    """Return whether <line> contains balanced parentheses.

    Ignore square and curly brackets.

    >>> is_balanced('(a * (3 + b))')
    True
    >>> is_balanced('(a * (3 + b]]') # Note that the two ']'s don't matter
    False
    >>> is_balanced('1 + 2(x-y)}') # Note that the '}' doesn't matter
    True
    >>> is_balanced('3 - (x')
    False
    """
    parenthesis_stack = Stack()

    for character in line:
        # If the character is left parenthesis,
        if character == '(':
            # Store it in stack
            parenthesis_stack.push('(')
        # If the character is right parenthesis,
        elif character == ')':
            # Check for the non-emptiness of stack.
            if parenthesis_stack.is_empty():
                # if empty, return false.
                return False

            # If the list is not empty, then pop an element form stack.
            parenthesis_stack.pop()

    # Check parenthesis are balanced by checking stack is empty.
    if not parenthesis_stack.is_empty():
        return False

    return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()

