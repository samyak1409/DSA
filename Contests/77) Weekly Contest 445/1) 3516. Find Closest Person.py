"""
https://leetcode.com/problems/find-closest-person
"""


def find_closest(x: int, y: int, z: int) -> int:
    """"""

    # 1) Optimal (If else): TC = O(1); SC = O(1)

    """
    if abs(z-x) < abs(z-y):
        return 1
    if abs(z-y) < abs(z-x):
        return 2
    return 0
    """

    # One-liner:
    return 1 if abs(z-x) < abs(z-y) else 2 if abs(z-y) < abs(z-x) else 0
