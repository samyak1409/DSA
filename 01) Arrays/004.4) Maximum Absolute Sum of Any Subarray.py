"""
https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray
"""


def max_absolute_sum(nums: list[int]) -> int:
    """"""

    # 0) [TLE] Brute-force (Calculating for all sub-arrays): TC = O(n^2); SC = O(1)

    """
    n = len(nums)
    max_abs = 0  # because abs(sum(x)) >= 0
    for i in range(n):
        curr_sum = 0  # restart the sub-array formation from next element
        for j in range(i, n):
            curr_sum += nums[j]  # increase the size of current sub-array by one element
            max_abs = max(max_abs, abs(curr_sum))
    return max_abs
    """

    # 1.1) Optimal (Kadane's Algo): TC = O(n); SC = O(1)
    # What if we asked for maximum sum, not absolute sum?
    # It's a standard problem that can be solved by Kadane's algorithm.
    # The key idea is the max absolute sum will be either the max sum or the min sum.
    # So just run kadane twice, once calculating the max sum and once calculating the min sum.

    """
    curr_max = 0
    curr_min = 0
    max_sum = float('-inf')
    min_sum = float('+inf')
    for num in nums:
        curr_max += num
        curr_min += num
        max_sum = max(max_sum, curr_max)
        min_sum = min(min_sum, curr_min)
        curr_max = max(curr_max, 0)
        curr_min = min(curr_min, 0)
    return max(max_sum, -min_sum)
    """
    # Or just:
    # https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/discuss/1052471/C++Java:-Find-Max-and-Min-Sum
    max_sum = min_sum = max_abs_sum = 0
    for num in nums:
        max_sum = max(max_sum+num, 0)  # new_max_sum = max(old_max_sum+curr_num, 0); 0 means reset
        min_sum = min(min_sum+num, 0)  # new_min_sum = min(old_min_sum+curr_num, 0); 0 means reset
        max_abs_sum = max(max_abs_sum, max(max_sum, -min_sum))
    return max_abs_sum
    # We aren't tracking current sum, still why working? Because abs sum can't be < 0.

    # 1.2) Optimal (Prefix Sum): TC = O(n); SC = O(1)
    # Just find the maximum prefix sum and the minimum prefix sum. Return max - min.
    # https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/discuss/1052527/JavaC++Python-O(1)-Space
    # The proof idea behind the lee's intuition is using properties of modulus |a-b| = max(a,b) - min(a,b).
    # The sum of subarray arr[i:j]: S(i,j) = S(0,j) - S(0,i) and we want to maximize : |S(i,j)| = |S(0,j) - S(0,i)| =
    # max(S(0, i), S(0, j)) - min(S(0, i), S(0, j)) => max prefix sum - min prefix sum.
