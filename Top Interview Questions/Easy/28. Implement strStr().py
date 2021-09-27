"""
https://leetcode.com/problems/implement-strstr/
"""


def strStr(haystack: str, needle: str) -> int:

    # Brute Force: O(nm)

    """
    if len(needle) > len(haystack):
        return -1

    if haystack == '':
        return 0

    for i in range(0, len(haystack)-len(needle)+1):

        for n, h in zip(needle, haystack[i:]):
            if n != h:
                break
        else:
            return i

    return -1
    """

    # Using Built-in Method: O(n)

    return haystack.find(needle)
