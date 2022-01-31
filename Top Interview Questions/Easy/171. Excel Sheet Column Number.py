"""
https://leetcode.com/problems/excel-sheet-column-number/
"""


def titleToNumber(column_title: str) -> int:  # TC = O(n); SC = O(1)

    """
    ans = 0
    for letter_index, letter in enumerate(column_title[::-1], start=0):
        ans += (ord(letter)-64) * (26**letter_index)  # (ord(letter)-64) => letter number
    return ans
    """

    # Better ->

    ans = 0
    for letter in column_title:
        ans *= 26
        ans += ord(letter)-64
    return ans

    # This is similar to how the number 254 could be broken down as this: (2 x 10 x 10) + (5 x 10) + (4).
    # The reason we use 26 instead of 10 is that 26 is our base.

    # Think of this problem as the same way you'd manually take a binary string and calculate its decimal representation.
    # Instead of being base 2 it is base 26.
