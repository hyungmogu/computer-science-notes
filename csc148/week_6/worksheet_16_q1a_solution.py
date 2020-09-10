from typing import Union, List

def nested_list_contains(obj: Union[int, List], item: int) -> bool:
    """Return whether the given item appears in <obj>.
    Note that if <obj> is an integer, this function checks whether
    <item> is equal to <obj>.

    >>> nested_list_contains(1,1)
    True
    >>> nested_list_contains(1,2)
    False
    """

    if isinstance(self, int):
        return obj == item