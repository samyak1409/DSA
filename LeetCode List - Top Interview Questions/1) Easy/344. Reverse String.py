"""
https://leetcode.com/problems/reverse-string
"""


def reverse_string(s: list[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """

    # Two Pointer: TC = O(n); SC = O(1)

    for i in range(len(s)//2):
        s[i], s[-i-1] = s[-i-1], s[i]
