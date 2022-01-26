"""
https://leetcode.com/problems/reverse-string/
"""


from typing import List


def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """

    # Two Pointer: TC = O(n); SC = O(1)

    for i in range(len(s)//2):
        s[i], s[-i-1] = s[-i-1], s[i]
