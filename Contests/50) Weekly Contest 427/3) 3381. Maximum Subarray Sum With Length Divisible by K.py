"""
https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k
"""


def max_subarray_sum(nums: list[int], k: int) -> int:
    """"""

    # [WA] -1) Optimal (Prefix Sum): TC = O(n); SC = O(n)
    # - This was my first intuition.

    """
    # Build prefix sum array:
    ps = [0]
    for num in nums:
        ps.append(ps[-1]+num)
    # print(ps)  # debugging
    
    # Find the largest int in `ps[k:]`:
    max_ps, idx = float('-inf'), None
    for i in range(k, len(ps)):
        if (curr_ps := ps[i]) > max_ps:
            max_ps, idx = curr_ps, i
    
    # Then check on all `ps[idx-K]` {K is multiple of k} for max sum:
    max_sum = float('-inf')
    for i in range(idx-k, -1, -k):
        max_sum = max(max_sum, max_ps-ps[i])
    return max_sum
    """

    # At first, this solution might not only look correct, but also easy and good.
    # But it's VERY WRONG, e.g. consider a case when the very starting num is very big, next nums are small, but due to
    # that big num, `ps[-1]` is the largest int.
    # e.g. nums = [100, 1, 2]; k = 2
    # Output: 3; Expected: 101

    # 1) Optimal (Prefix Sum + Kadane's): TC = O(n); SC = O(n)
    # - This solution was smart and easy.
    # "Kadane's algorithm like in Maximum Subarray Sum, but instead of adding
    # the next element every time, we are adding the next k elements each time,
    # and starting from each 0 <= i < k, which covers all possible sub-arrays of
    # length divisible by k.
    # For example, if k = 4, we would do Kadane's on the prefix sum array on indices
    # 0, 4, 8, ..., then 1, 5, 9, ..., then 2, 6, 10, ..., then 3, 7, 11, ...,
    # always doing it until the end of the array."
    # -https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/solutions/6124522/prefix-sum-kadane/comments/2753895

    # Build prefix sum array:
    ps = [0]
    for num in nums:
        ps.append(ps[-1]+num)
    print(ps)  # debugging

    ans = float('-inf')
    for i in range(0, k):  # note that we only need to loop from 0 to k-1, other indices would be covered by these only
        # Kadane's (next 5 SLOCs):
        max_sum, curr_sum = float('-inf'), 0
        for j in range(i+k, len(ps), k):
            curr_sum += ps[j] - ps[j-k]  # add the sum
            max_sum = max(max_sum, curr_sum)  # update max if required
            curr_sum = max(curr_sum, 0)  # don't take negative sum forward
        ans = max(ans, max_sum)
    return ans
