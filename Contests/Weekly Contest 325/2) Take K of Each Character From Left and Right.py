"""
https://leetcode.com/problems/take-k-of-each-character-from-left-and-right
"""


def take_characters(s: str, k: int) -> int:
    """"""

    a = b = c = 0  # removal count

    i, j = 0, len(s)-1

    while a < k or b < k or c < k:

        if i > j:
            return -1

        c1, c2 = s[i], s[j]

        if globals()[c1] < k:
            globals()[c1] += 1
            i += 1

        elif globals()[c2] < k:
            globals()[c2] += 1
            j -= 1

    return a+b+c
