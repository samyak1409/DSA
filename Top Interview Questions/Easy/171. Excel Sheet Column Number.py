"""
https://leetcode.com/problems/excel-sheet-column-number/
"""


def titleToNumber(column_title: str) -> int:

    """
    ans = 0

    for i, letter in enumerate(column_title[::-1]):

        ans += (ord(letter)-64) * (26**i)  # (letter_number) * (26**letter_index)

    return ans
    """

    # Better ->

    ans = 0

    for letter in column_title:
        ans = (26*ans) + (ord(letter)-64)

    return ans
