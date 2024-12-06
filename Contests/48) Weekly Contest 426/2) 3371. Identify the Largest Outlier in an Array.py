"""
https://leetcode.com/problems/identify-the-largest-outlier-in-an-array
"""


def get_largest_outlier(nums: list[int]) -> int:
    """"""

    # -1) [WA] Sub-optimal (Sort, Greedy): TC = O(n*log(n)); SC = (n)
    # If `nums` has non-negative ints only, then this would've worked.
    # Intuition:
    # If we sort nums, then all the bigger nums would be in the very end.
    # And, outlier can be any of the num, but sum would be the last one only.

    """
    nums.sort()  # O(n*log(n)); O(n)
    total_sum = sum(nums)

    # Edge case: Outlier can be any of the num, so it can be the biggest num as well, and only in that case, sum would
    # be second biggest num:
    if total_sum-nums[-1]-nums[-2] == nums[-2]:  # `nums[-1]`: outlier; `nums[-2]`: sum
        return nums[-1]
    # And for all the other cases, sum would be the last num only, and we will try every other num in decreasing order
    # to be the outlier:
    sum_ = nums[-1]
    total_sum -= sum_  # as sum is now fixed as the largest num, we can minus it here only
    for i in range(-2, -len(nums)-1, -1):  # O(n)
        if total_sum-nums[i] == sum_:  # `nums[i]`: outlier
            return nums[i]
    """

    # Hint 1: What will be the value of array sum if we remove the outlier from it?
    # Hint 2: Use hashmap to find occurrence of an element quickly.

    # 1) Optimal (HashMap, Basic Maths): TC = (n); SC = O(n)
    # If we remove the outlier, then the remaining total_sum would be 2x of sum.

    from collections import Counter

    freq = Counter(nums)
    total_sum = sum(nums)

    ans = -1001  # `-1000 <= nums[i] <= 1000`

    # One by one assume num as outlier:
    for num in nums:
        # Remove its freq:
        freq[num] -= 1
        # If (total_sum-num)/2 is there in nums, implies num is an outlier candidate:
        if freq.get((total_sum-num)/2):  # noqa
            ans = max(ans, num)
        # Add the freq back:
        freq[num] += 1

    return ans
