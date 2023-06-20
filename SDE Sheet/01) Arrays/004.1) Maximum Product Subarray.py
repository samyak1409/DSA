"""
https://leetcode.com/problems/maximum-product-subarray
"""


def max_product(nums: list[int]) -> int:
    """"""

    # 0) [TLE] Brute-force (Calculating product of all the possible sub-arrays): TC = O(n^2); SC = O(1)

    """
    n = len(nums)
    largest = float('-inf')  # because nums consists of integers
    for i in range(n):
        current = 1  # restart the sub-array formation from next element
        for j in range(i, n):
            current *= nums[j]  # increase the size of current sub-array by one element
            if current > largest:
                largest = current
    return largest
    """

    # 1) Optimal (Modified Kadane's Algo): TC = O(n); SC = O(1)

    # 1.1) Tracking Two Extremes:
    # https://leetcode.com/problems/maximum-product-subarray/discuss/48230/Possibly-simplest-solution-with-O(n)-time-complexity/160464
    # Basically the same algo as
    # https://github.com/samyak1409/DSA/blob/main/SDE%20Sheet/01%29%20Arrays/004%29%20Maximum%20Subarray.py,
    # the only difference is the fact that in case of products:
    # -> smallest_product * a_negative_num = largest_product
    # -> largest_product * a_negative_num = smallest_product
    # So, we are handling this behaviour by keeping track of two extremes, viz. `maxi` and `mini` instead of just one
    # (like `004) Maximum Subarray.py`).

    ans = maxi = mini = nums[0]  # init with the 1st value in the array
    for i in range(1, len(nums)):  # traverse
        num = nums[i]
        candidates = (maxi*num, mini*num, num)  # MOST IMP PART
        # `maxi*num` => continue the subarray including num which is +ve
        # `mini*num` => continue the subarray including num which is -ve
        # `num`      => resetting, starting a new subarray with num
        maxi, mini = max(candidates), min(candidates)  # update
        ans = max(ans, maxi)  # update
    return ans

    # 1.2) With Prefix & Suffix Product:
    # Calculate prefix product in A. Calculate suffix product in A. Return the max.
    # https://leetcode.com/problems/maximum-product-subarray/discuss/183483/JavaC++Python-it-can-be-more-simple
    # Let me try to give some explanations for this solution.
    # First, if there's no zero in the array, then the subarray with maximum product must start with the first element
    # or end with the last element. And therefore, the maximum product must be some prefix product or suffix product.
    # So in this solution, we compute the prefix product A and suffix product B, and simply return the maximum of A and
    # B.
    # Why? Here's the proof:
    # Say, we have a subarray A[i : j](i != 0, j != n) and the product of elements inside is P. Take P > 0 for example:
    # if A[i] > 0 or A[j] > 0, then obviously, we should extend this subarray to include A[i] or A[j]; if both A[i] and
    # A[j] are negative, then extending this subarray to include both A[i] and A[j] to get a larger product. Repeating
    # this procedure, and eventually we will reach the beginning or the end of A.
    # What if there are zeroes in the array? Well, we can split the array into several smaller ones. That's to say, when
    # the prefix product is 0, we start over and compute prefix product from the current element instead. And this is
    # exactly what A[i] *= (A[i - 1]) or 1 does.
    # -https://leetcode.com/problems/maximum-product-subarray/discuss/183483/JavaC++Python-it-can-be-more-simple/330117
