"""
https://leetcode.com/problems/make-array-non-decreasing
"""


def maximum_possible_size(nums: list[int]) -> int:
    """"""

    # 1) Optimal (Greedy, Loop): TC = O(n); SC = O(1)
    # Observations:
    # - We've to make the array non-decreasing (increasing or equal)
    # - `[2, 1]` If we've this, we've to make `1 >= 2`, or `2 <= 1`. In this problem, since the only allowed operation
    # is "select a subarray and replace it with a single element equal to its maximum value". Which means we can only do
    # `1 >= 2`.
    # - Greedy method to optimally do that is choosing the subarray `[nums[i-1], nums[i]]`, then since
    # `nums[i-1] > nums[i]`, replacing the subarray `nums[i-1], nums[i]` with `nums[i-1]`.
    # - The above thing is basically just = removing the element which is breaking our requirement "non-decreasing"
    # array. And hence, we can just count elements like those sequentially (that's the number of operations), and
    # subtract from the original array size, and that's the size of the final array.

    """
    # Cnt of bad elements:
    bad_cnt = 0
    # Prev element which is good (we can't use `nums[i-1]` as we go since we're not actually removing the bad elements,
    # but just counting):
    prev_good = float('-inf')  # init with `-inf` so that `num < prev_good` is False for the very first iteration
    for num in nums:
        if num < prev_good:
            bad_cnt += 1
            # no need to change `prev_good`, since it remains the same as current bad element `num` is being removed
        else:
            prev_good = num
    # Final arr size = initial arr size - bad elements:
    return len(nums) - bad_cnt
    """

    # We can just count the size of the final arr as we go:
    # And this turns out to be even easier as well.

    # Size of final arr:
    ans = 0
    # Prev element which is good (we can't use `nums[i-1]` as we go since we're not actually removing the bad elements,
    # but just counting):
    prev_good = float('-inf')  # init with `-inf` so that `num >= prev_good` is True for the very first iteration
    for num in nums:
        if num >= prev_good:
            ans += 1
            prev_good = num
    return ans
