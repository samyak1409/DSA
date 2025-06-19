"""
https://leetcode.com/problems/find-minimum-log-transportation-cost
"""


def min_cutting_cost(n: int, m: int, k: int) -> int:
    """"""

    # 1) Optimal (Simulate): TC = O(1); SC = O(1)

    """
    # Only three cases are possible:
    # If both are less, no extra cost:
    if n <= k and m <= k:
        return 0
    # If both are more:
    if n > k and m > k:
        return (n-k)*k + (m-k)*k
    # If one of them is more:
    return (max(n, m) - k) * k
    """

    # Turns out case 2 would not be there:
    # "There are two logs of lengths n and m units, which need to be transported in three trucks where **[EACH TRUCK CAN
    # CARRY ONE LOG]** with length at most k units."
    # "The input is generated such that it is always possible to transport the logs."

    # Only two cases are possible:
    # If both are less, no extra cost:
    if n <= k and m <= k:
        return 0
    # If one of them is more:
    return (max(n, m) - k) * k
