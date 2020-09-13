from typing import Union, List, Optional

def add_one(obj: Union[int, List]) -> None:
    """Add one to every number stored in <obj>. Do nothing if <obj> is an int.
    If <obj> is a list, *mutate* it to change the numbers stored.
    >>> lst0 = 1
    >>> add_one(lst0)
    >>> lst0
    1
    >>> lst1 = []
    >>> add_one(lst1)
    >>> lst1
    []
    >>> lst2 = [1, [2, 3], [[[5]]]]
    >>> add_one(lst2)
    >>> lst2
    [2, [3, 4], [[[6]]]]
    """

    if isinstance(obj, int):
        pass
    else:
        for i in range(len(obj)):
            if isinstance(obj[i], int):
                obj[i] += 1
            else:
                add_one(obj[i])


if __name__ =='__main__':
    import doctest
    doctest.testmod()