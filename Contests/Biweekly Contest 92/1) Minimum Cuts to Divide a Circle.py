"""
https://leetcode.com/problems/minimum-cuts-to-divide-a-circle
"""


def number_of_cuts(n: int) -> int:
    """"""

    # 1) Optimal (Recognize the Pattern): TC = O(1); SC = O(1)
    # Think about odd and even values separately.
    # When will we not have to cut the circle at all?

    if n == 1:  # edge case
        return 0

    return n if n % 2 else n // 2

    # Explanation:
    # https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/discuss/2850445/JavaC++Python-Easy-and-Concise
