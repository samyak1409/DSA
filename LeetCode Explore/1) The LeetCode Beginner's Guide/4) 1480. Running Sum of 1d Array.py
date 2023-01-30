"""
https://leetcode.com/problems/running-sum-of-1d-array
"""


def running_sum(nums: list[int]) -> list[int]:
    """"""

    # Think about how we can calculate the i-th number in the running sum from the (i-1)-th number.

    # 1) Optimal (Loop): TC = O(n); SC = O(1)

    """
    sum_, arr = 0, []
    for num in nums:
        arr.append(sum_ := sum_+num)
    return arr
    """

    # Using the prev element only:
    """
    sum_ = []
    for num in nums:
        sum_.append((sum_[-1] if sum_ else 0)+num)
    return sum_
    """

    # Directly yielding:
    """
    sum_ = 0
    for num in nums:
        yield (sum_ := sum_+num)
    """

    # https://leetcode.com/problems/running-sum-of-1d-array/solutions/686276/c-python-partial-sum:
    from itertools import accumulate
    yield from accumulate(nums)
