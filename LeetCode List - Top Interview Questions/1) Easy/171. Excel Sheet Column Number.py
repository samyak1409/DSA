"""
https://leetcode.com/problems/excel-sheet-column-number
"""


def title_to_number(column_title: str) -> int:
    """"""

    # 1) Optimal (Traverse and Accumulate): TC = O(n); SC = O(1) {n: len(column_title)}

    # "This is similar to how the number 254 could be broken down as this: (2 x 10 x 10) + (5 x 10) + (4).
    # The reason we use 26 instead of 10 is that 26 is our base.
    # Think of this problem as the same way you'd manually take a binary string and calculate its decimal
    # representation.
    # Instead of being base 2 it is base 26."
    # -https://leetcode.com/problems/excel-sheet-column-number/solutions/52154/concise-java-solution-with-explanation

    # 1.1) Reverse Traversal:
    # 254 = (10**0 * 4) + (10**1 * 5) + (10**2 * 2)

    """
    num = 0
    for i in range(len(column_title)):
        num += (26 ** i) * (ord(column_title[~i]) - 64)
        # `26 ** i`: base; `i`: bit index
        # `ord(column_title[~i]) - 64`: letter value; `~i`: -i-1
    return num
    """

    # 1.2) Normal Traversal:
    # 254 ->
    #             0
    # 0 *10 + 2 = 2
    # 2 *10 + 5 = 25
    # 25*10 + 4 = 254

    num = 0
    for letter in column_title:
        num = (num * 26) + (ord(letter) - 64)
        # `num * 26`: left shift
        # `ord(letter) - 64`: letter value
    return num
