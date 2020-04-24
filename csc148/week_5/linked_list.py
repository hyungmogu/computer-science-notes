"""Linked List code we worked on in week 5.

Homework:
- write the __get_item__ method, which is discussed at the end of one
  of our worksheets and is ready for you, commented out below.
- review the insert method.
    - Do you understand the "parallel" assignment statement in the first
      if-statement (and also at the end of the method)?  Could you express it
      as two separate assignments? Be careful about ordering them or you may
      lose track of a node.
    - Notice that we stopped at the node *before* where we wanted to insert.
      Do you understand why?
    - Try rewriting this using the technique of stopping at the spot
      where we want to insert, but keeping also a reference to the "previous"
      node?
    - What do we know after the while loop ends, and how does that determine
      what we do next?
- complete the remove method.  Don't forget to test it with at least the
  doctest examples.

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

    # def __getitem__(self, index: int) -> Any:
    #     """Return the item at position <index> in this list.
    #
    #     Raise IndexError if <index> is >= the length of this list.
    #
    #     >>> linky = LinkedList([100, 4, -50, 13])
    #     >>> linky[0]          # Equivalent to linky.__getitem__(0)
    #     100
    #     >>> linky[2]
    #     -50
    #     >>> linky[100]
    #     Traceback (most recent call last):
    #     IndexError
    #     """
    #     pass

    # def pop(self, index: int) -> Any:
    #     """Remove and return the item at position <index>.
    #
    #     Raise IndexError if index >= len(self) or index < 0.
    #
    #     >>> lst = LinkedList([1, 2, 10, 200])
    #     >>> lst.pop(1)
    #     2
    #     >>> lst.pop(2)
    #     200
    #     >>> lst.pop(148)
    #     Traceback (most recent call last):
    #     IndexError
    #     >>> lst.pop(0)
    #     1
    #     """
    #     pass

    def remove(self, item: Any) -> None:
        """Remove the FIRST occurrence of <item> in this list.

        Do nothing if this list does not contain <item>.
        (Note: Python lists actually raise a ValueError.)

        >>> lst = LinkedList([1, 2, 3])
        >>> lst.remove(2)
        >>> str(lst)
        '[1 -> 3]'
        >>> lst.remove(2)
        >>> str(lst)
        '[1 -> 3]'
        >>> lst.remove(3)
        >>> str(lst)
        '[1]'
        >>> lst.remove(1)
        >>> str(lst)
        '[]'
        >>> lst.remove(1)
        >>> str(lst)
        '[]'
        """
        # Find the place to make the change (if any).
        prev = None
        curr = self._first
        # Stopping conditions:
        #   Stop if a) curr is None OR
        #   Stop if b) curr.item == item
        # Continue if:
        #   not (a or b)
        #   (not a) and (not b)
        while (curr is not None and curr.item != item):
            prev, curr = curr, curr.next
        # We know that
        #   not (curr is not None and curr.item != item)
        #   curr is None OR curr.item == item

        # If a change is needed, make the change.




























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

    def __getitem__(self, )

if __name__ == '__main__':
    # import python_ta
    # python_ta.check_all()

    import doctest
    doctest.testmod()
