def left_count(s: str) -> int:
    """
    Return the number of "(" in s
    """
    return s.count("(")

def double_count(s: str) -> int:
    """
    Return the number of "((" plus number of "))", including possible
    overlaps.
    """
    return (len([s[i:] for i in range(len(s)) if s[i:].startswith("((")])
    + len([s[:i] for i in range(len(s) + 1) if s[:i].endswith("))")]))

def left_surplus(s: str, i: int) -> int:
    """
    Return the number of "(" minus the number of ")"
    in s[:i]
    """
    return s.count("(", 0, i) - s.count(")", 0, i)

def max_left_surplus(s: str) -> int:
    """
    Return the maximum left surplus for all prefixes of s.
    """
    return max([left_surplus(s, i) for i in range(len(s))] + [0])