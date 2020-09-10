from typing import Union, List, Optional


def first_at_depth(obj: Union[int, List], d: int) -> Optional[int]:
    """Return the first (leftmost) item in <obj> at depth <d>.
    Return None if there is no item at depth <d>.
    Precondition: d >= 0.

    >>> first_at_depth(1,2)
    None
    """

    if isinstance(obj, int):
        return None