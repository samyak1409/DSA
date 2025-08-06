"""
https://leetcode.com/problems/substring-matching-pattern
"""


def has_match(s: str, p: str) -> bool:
    """"""

    # 1) Optimal: TC = O(len(p)+len(s)); SC = O(len(p))
    # For complexity analysis (and more): https://chatgpt.com/share/67841dc9-04dc-800a-a7a5-8a55336759ce

    # 1.1) Regex:
    """
    import re
    return re.search(pattern=p.replace('*', '.*'), string=s) is not None
    # In regex, '.*' means: Any character, zero or more times.
    """

    # 1.2) Compare starting indices:
    # Greedy: Take the very first occurrence of `lt`, and the very last occurrence of `rt`.
    lt, rt = p.split('*')
    try:
        # `rt` should start after `lt` end:
        return s.rindex(rt) >= s.index(lt)+len(lt)
    except ValueError:
        # If any (or both) partitions are not there in the string:
        return False
