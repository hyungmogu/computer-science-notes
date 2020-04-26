from typing import Union, List


def nested_list_contains(obj: Union[int, List], item: int) -> bool:
    """Return whether the given item appears in <obj>.
    Note that if <obj> is an integer, this function checks whether
    <item> is equal to <obj>.

    >>> nested_list_contains([4,2,2,[6,5,7,[8]]],8)
    True
    >>> nested_list_contains([4,2,2,[6,5,7,[8]]],9)
    False
    """

    if isinstance(self, int):
        return obj == item
    else:
        # ==================== (Solution) =======================
        for sublist in obj:
            result = nested_list_contains(sublist, item)

            if result:
                return result

        return False
        # =======================================================