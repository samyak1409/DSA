"""
https://leetcode.com/problems/transformed-array
"""


def construct_transformed_array(nums: list[int]) -> list[int]:
    """"""

    # 1) Optimal (Simulation, Modulo Op): TC = O(n); SC = O(1)

    res = []

    for i, num in enumerate(nums):
        res.append(nums[(i+num) % len(nums)])

    return res
