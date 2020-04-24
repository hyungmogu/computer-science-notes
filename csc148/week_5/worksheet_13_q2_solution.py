"""Linked List code we worked on in week 5.
=== CSC148 ===
Department of Computer Science,
University of Toronto

=== Module Description ===
This module contains the code for a linked list implementation with two classes,
LinkedList and _Node.

Code template we can use:

    curr = self._first
    while curr is not None:
        # ... curr.item ...
        curr = curr.next

"""
from __future__ import annotations

from typing import Any, Callable, Optional, Union


class _Node:
    """A node in a linked list.

    Note that this is considered a "private class", one which is only meant
    to be used in this module by the LinkedList class, but not by client code.

    === Attributes ===
    item:
        The data stored in this node.
    next:
        The next node in the list, or None if there are no more nodes.
    """
    item: Any
    next: Optional[_Node]

    def __init__(self, item: Any) -> None:
        """Initialize a new node storing <item>, with no next node.
        """
        self.item = item
        self.next = None  # Initially pointing to nothing


class LinkedList:
    """A linked list implementation of the List ADT.
    """
    # === Private Attributes ===
    # _first:
    #     The first node in the linked list, or None if the list is empty.
    _first: Optional[_Node]

    # This implementation of LinkedList has a fancier initializer
    # and a __str__ method that permit things like:
    #     >>> linky = LinkedList([1, 223, 30, 16])
    #     >>> print(linky)
    #     '[1 -> 223 -> 30 -> 16]'
    # You'll write these methods later.

    def append(self, item: Any) -> None:
        """Append <item> to the end of this list.
        """
        if self._first is None:
            self._first = _Node(item)
        else:
            curr = self._first
            while curr.next is not None:
                curr = curr.next
            curr.next = _Node(item)

    def print_items(self) -> None:
        """Print the items in this linked list.
        """
        curr = self._first
        while curr is not None:
            print(curr.item)
            curr = curr.next

    def __eq__(self, other: LinkedList) -> bool:
        """Return whether this list and the other list are equal.

        >>> lst1 = LinkedList([1, 2, 3])
        >>> lst2 = LinkedList([])
        >>> lst1.__eq__(lst2)
        False
        >>> lst2.append(1)
        >>> lst2.append(2)
        >>> lst2.append(3)
        >>> lst1.__eq__(lst2)
        True
        """
        curr1 = self._first
        curr2 = other._first
        while (curr1 is not None) and (curr2 is not None):
            # We know: (curr1 is not None) and (curr2 is not None).
            if curr1.item != curr2.item:
                return False
            else:
                curr1 = curr1.next
                curr2 = curr2.next
        # We know: not [(curr1 is not None) and (curr2 is not None)]
        assert (curr1 is None) or (curr2 is None)
        if (curr1 is None) and (curr2 is None):
            # They have the same lengths.
            # We already determined that no pair mismatched.
            # Therefore the 2 lists are equivalent.
            return True
        else:
            # They matched up to this point, but have
            # different lengths.
            return False
        # Equivalent:
        # return (curr1 is None) and (curr2 is None)

    def insert(self, index: int, item: Any) -> None:
        """Insert a the given item at the given index in this list.
        Raise IndexError if index > len(self) or index < 0.
        Note that adding to the end of the list is okay.

        >>> lst = LinkedList([1, 2, 3])
        >>> lst.insert(0,0)
        >>> str(lst)
        '[0 -> 1 -> 2 -> 3]'
        >>> lst.insert(1,10)
        >>> str(lst)
        '[0 -> 10 -> 1 -> 2 -> 3]'
        >>> lst.insert(5,10)
        >>> str(lst)
        '[0 -> 10 -> 1 -> 2 -> 3 -> 10]'
        """

        curr = self._first
        current_index = 0

        if index == 0:
            current_node = curr
            self._first = _Node(item)
            self._first.next = current_node
            return

        while curr is not None:
            if current_index != index - 1:
                curr = curr.next
                current_index += 1
                continue

            # 1. if index == len(self), then append to list
            # 2. if index < len(self), then insert value at index
            current_node = curr.next
            inserting_node = _Node(item)
            curr.next = inserting_node
            inserting_node.next = current_node
            return

        # 3. if index > len(self), raise IndexError
        raise IndexError

    # ===================== (Question 2, Worksheet 13) =========================
    def __getitem__(self, index: int) -> Any:
        """Return the item at position <index> in this list.
        Raise an IndexError if the <index> is out of bounds.
        Precondition: index >= 0.

        >>> lst = LinkedList([1, 2, 3])
        >>> print(lst[0])
        1
        >>> print(lst[1])
        2
        >>> print(lst[2])
        3
        >>> print(lst[3])
        Traceback (most recent call last):
            ...
        IndexError
        """

        curr = self._first
        i = 0

        while (curr is not None) and (i <= index):
            # 1. If index == 0, then return curr.item)
            if index == 0:
                return curr.item

            # 2. If index - 1 != i, then continue to next node
            if index - 1 != i:
                curr = curr.next
                i += 1
                continue

            # 3. If curr.next is none, then let it terminate naturally
            if curr.next is None:
                curr = curr.next
                i += 1
                continue

            # 4. If index - 1 == i, then return item of curr.next
            return curr.next.item

        raise IndexError
    # =========================================================================
























    def __init__(self, items: list) -> None:
        """Initialize a new linked list containing the given items.

        The first node in the linked list contains the first item
        in <items>.
        """
        if items == []:  # No items, and an empty list!
            self._first = None
        else:
            self._first = _Node(items[0])
            curr = self._first
            for item in items[1:]:
                curr.next = _Node(item)
                curr = curr.next

    def __str__(self) -> str:
        """Return a string representation of this list in the form
        '[item1 -> item2 -> ... -> item-n]'.

        >>> str(LinkedList([1, 2, 3]))
        '[1 -> 2 -> 3]'
        >>> str(LinkedList([]))
        '[]'
        """
        items = []
        curr = self._first
        while curr is not None:
            items.append(str(curr.item))
            curr = curr.next
        return '[' + ' -> '.join(items) + ']'


if __name__ == '__main__':

    import doctest
    doctest.testmod()
