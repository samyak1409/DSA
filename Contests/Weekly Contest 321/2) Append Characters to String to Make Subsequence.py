"""
https://leetcode.com/problems/append-characters-to-string-to-make-subsequence
"""


def append_characters(s: str, t: str) -> int:
    """"""

    # 1) Optimal (Traverse and Find): TC = O(len(s)); SC = O(1)
    # Find the longest prefix of t that is a subsequence of s.
    # Use two variables to keep track of your location in s and t. If the characters match, increment both variables.
    # Otherwise, only increment the variable for s.
    # The remaining characters in t must be appended to the end of s.

    chars_left = len(t)
    i = 0  # for traversing t
    for c in s:  # traverse s to find t[i] in it subsequently
        if t[i] == c:
            i, chars_left = i+1, chars_left-1  # go to next char in t
            if chars_left == 0:  # => t is already a subsequence of s
                break  # or `return 0`
    return chars_left
