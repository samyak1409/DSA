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
    # "If n == 1, no need to cut,
    # return 0.
    #
    # If n is odd like n == 3,
    # cannot cut on diameter.
    # need to cut one by one,
    # return n
    #
    # If n is even like n == 6,
    # we can cut on diameter.
    # It's same as cut into n = 3 but cut on diameter,
    # so return n / 2."
    # -https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/discuss/2850445/JavaC++Python-Easy-and-Concise
