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

    # 1) Optimal (Kadane's Algo): TC = O(n); SC = O(1)
    # What if we asked for maximum sum, not absolute sum?
    # It's a standard problem that can be solved by Kadane's algorithm.
    # The key idea is the max absolute sum will be either the max sum or the min sum.
    # So just run kadane twice, once calculating the max sum and once calculating the min sum.
    # `1.0)` of https://github.com/samyak1409/DSA/blob/main/SDE%20Sheet/01%29%20Arrays/004%29%20Maximum%20Subarray.py will work!
    # Why? Because here we're allowed to choose an empty subarray as answer if max abs sum < 0.
    # "Return the maximum absolute sum of any (POSSIBLY EMPTY) subarray of nums."

    """
    maxi = curr = 0
    for num in nums:
        curr = max(curr+num, 0)
        maxi = max(maxi, curr)
    mini = curr = 0
    for num in nums:
        curr = min(curr+num, 0)
        mini = min(mini, curr)
    return max(maxi, -mini)
    """
    # Combined:
    """
    maxi = mini = curr_maxi = curr_mini = 0
    for num in nums:
        curr_maxi, curr_mini = max(curr_maxi+num, 0), min(curr_mini+num, 0)
        maxi, mini = max(maxi, curr_maxi), min(mini, curr_mini)
    return max(maxi, -mini)
    """
    # Minor Improvement:
    # https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/discuss/1052471/C++Java:-Find-Max-and-Min-Sum
    ans = curr_maxi = curr_mini = 0
    for num in nums:
        curr_maxi, curr_mini = max(curr_maxi+num, 0), min(curr_mini+num, 0)
        ans = max(ans, max(curr_maxi, -curr_mini))
    return ans

    # Another Solution:
    # Optimal (Prefix Sum): TC = O(n); SC = O(1)
    # Just find the maximum prefix sum and the minimum prefix sum. Return max - min.
    # https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/discuss/1052527/JavaC++Python-O(1)-Space
    # The proof idea behind the lee's intuition is using properties of modulus |a-b| = max(a,b) - min(a,b).
    # The sum of subarray arr[i:j]: S(i,j) = S(0,j) - S(0,i) and we want to maximize : |S(i,j)| = |S(0,j) - S(0,i)| =
    # max(S(0, i), S(0, j)) - min(S(0, i), S(0, j)) => max prefix sum - min prefix sum.
    # -https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/discuss/1052527/JavaC++Python-O(1)-Space/1060161
