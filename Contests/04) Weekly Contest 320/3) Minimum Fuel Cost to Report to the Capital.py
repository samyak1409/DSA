"""
https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital
"""


def minimum_fuel_cost(roads: list[list[int]], seats: int) -> int:
    """"""

    # 1) Optimal (Graph DFS): TC = O(n); SC = O(n)
    # Can you record the size of each subtree?
    # If n people meet on the same node, what is the minimum number of cars needed?
    # https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/solutions
