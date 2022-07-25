"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
"""


def twoSum(numbers: list[int], target: int) -> list[int]:
    """"""

    # NOTE: All the following solutions are from https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/019%29%20Two%20Sum.py
    # because this problem is just a subset of https://leetcode.com/problems/two-sum.

    # 0) (TLE) Brute-force (Nested Loop): TC = O(n^2); SC = O(1)

    n = len(numbers)
    for i in range(n):
        for j in range(i+1, n):
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
