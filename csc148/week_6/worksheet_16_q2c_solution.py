from typing import Union, List, Optional


def first_at_depth(obj: Union[int, List], d: int) -> Optional[int]:
    """Return the first (leftmost) item in <obj> at depth <d>.
    Return None if there is no item at depth <d>.
    Precondition: d >= 0.

    >>> first_at_depth(1,2)
    >>> first_at_depth(1,0)
    1
    >>> first_at_depth([1,2,[3,4,[5,6]]],1)
    1
    >>> first_at_depth([1,2,[3,4,[5,6]]],3)
    5
    >>> first_at_depth([1,2,[3,4,[5,6]]],4)
    >>> first_at_depth([[1,2,[3]],4,[[5],6]],3)
    3
    """

    if isinstance(obj, int):
        if d != 0:
            return None
        return obj

    else:
        for sublist in obj:
            result = first_at_depth(sublist, d - 1)

            if result:
                return result

        return None

if __name__ =='__main__':
    import doctest
    doctest.testmod()