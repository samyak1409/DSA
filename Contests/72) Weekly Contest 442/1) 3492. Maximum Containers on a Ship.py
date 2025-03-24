"""
https://leetcode.com/problems/maximum-containers-on-a-ship
"""


def max_containers(n: int, w: int, mx: int) -> int:
    """"""

    # 1) Optimal (Maths): TC = O(1); SC = O(1)

    """
    # If the full deck's weight is within the limit, use all slots; otherwise, fit within max weight.
    return n*n if n*n*w <= mx else mx//w
    """

    # Or just:

    # The ship can hold at most `n*n` containers, but weight capacity limits it to `mx//w`.
    return min(n*n, mx//w)
