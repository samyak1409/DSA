"""
https://leetcode.com/problems/implement-strstr/
"""


def strStr(haystack: str, needle: str) -> int:

    # Brute Force: TC = O(nm); SC = O(1)

    """
    if len(needle) > len(haystack):
        return -1

    if haystack == '':
        return 0

    for i in range(0, len(haystack)-len(needle)+1):  # O(n)

        for n, h in zip(needle, haystack[i:]):  # O(m)
            if n != h:
                break
        else:
            return i

    return -1
    """

    # Using Built-in Method: TC = O(n); SC = O(1)

    return haystack.find(needle)

    # Its implementation (standard string matching algorithms):


