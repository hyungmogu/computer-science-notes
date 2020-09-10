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

if __name__ == '__main__':
    import doctest
    doctest.testmod()