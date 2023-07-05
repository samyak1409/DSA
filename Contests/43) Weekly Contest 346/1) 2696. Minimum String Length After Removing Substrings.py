"""
https://leetcode.com/problems/minimum-string-length-after-removing-substrings
"""


def min_length(s: str) -> int:
    """"""

    # Can we use brute force to solve the problem?
    # Repeatedly traverse the string to find and remove the substrings “AB” and “CD” until no more occurrences exist.

    # 0) Brute-force (Simulation): TC = O(n^2); SC = O(n)

    """
    while 'AB' in s or 'CD' in s:
        s = s.replace('AB', '').replace('CD', '')
    return len(s)
    """

    # 1) Optimal (Stack): TC = O(n); SC = O(n)
    # Cool how stack solves the problem so elegantly!

    stack = [None]  # init w/ a val to save from StackUnderflow
    for c in s:
        if (c == 'B' and stack[-1] == 'A') or (c == 'D' and stack[-1] == 'C'):
            stack.pop()  # 'AB' or 'CD' formed and removed
        else:
            stack.append(c)
    return len(stack) - 1
