"""
https://leetcode.com/problems/find-subarrays-with-equal-sum
"""


def find_subarrays(nums: list[int]) -> bool:
    """"""

    # 1) Optimal (Sliding Window + HashSet): TC = O(n); SC = O(n)
    # Use a counter to keep track of the subarray sums.
    # Use a hashset to check if any two sums are equal.

    sum_ = nums[0] + nums[1]  # init: with 1st two nums
    sums = {sum_}  # save the sum
    for i in range(2, len(nums)):
        sum_ += -nums[i-2] + nums[i]  # remove the first num, and add the current num (slide window)
        if sum_ in sums:  # lookup
            return True
        sums.add(sum_)  # save
    # return False  # optional
