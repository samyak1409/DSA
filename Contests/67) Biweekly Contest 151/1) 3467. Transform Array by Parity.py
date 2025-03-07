"""
https://leetcode.com/problems/transform-array-by-parity
"""


def transform_array(nums: list[int]) -> list[int]:
    """"""

    # Assuming modifying the input array only is not required since we're asked to return the modified array.

    # 1) Sub-optimal (Replaces, Sort): TC = O(n*log(n)); SC = O(n)

    # return sorted(num % 2 for num in nums)
    # Or using bitwise:
    """
    return sorted(num & 1 for num in nums)
    """

    # 2) Optimal (Count): TC = O(n); SC = O(1)

    even_cnt = sum(num % 2 == 0 for num in nums)
    return [0 if i < even_cnt else 1 for i in range(len(nums))]
