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

    # 1.1) Optimal (Modified Kadane's Algo): TC = O(n); SC = O(1)
    # https://leetcode.com/problems/maximum-product-subarray/discuss/48230/Possibly-simplest-solution-with-O(n)-time-complexity/160464
    # Basically the same algo as
    # https://github.com/samyak1409/DSA/blob/7171f3a12eef0353d41cc42981c1280d7bf720b7/01%29%20Arrays/004%29%20Maximum%20Subarray.py,
    # the only difference is the fact that in case of products:
    # -> smallest_product * a_negative_num = largest_product
    # -> largest_product * a_negative_num = smallest_product
    # So, we are handling this behaviour by keeping track of two extremes, viz. `maxi` and `mini` instead of just one
    # (like in `Maximum Subarray.py`).

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

    # 1.2) Optimal (Prefix & Suffix Product): TC = O(n); SC = O(1)
    # Calculate prefix product in A. Calculate suffix product in A. Return the max.
    # https://leetcode.com/problems/maximum-product-subarray/discuss/183483/JavaC++Python-it-can-be-more-simple
    # A way to understand the reason why the maximum subarray must be a prefix or suffix of the array:
    # suppose there's no 0 in the array:
    #     -> if number of negative number is odd, and left most is i and right most is j, then we can only either keep
    #        A[:j] or A[i+1:] to make it max
    #     -> if it's even, then we just multiply all the numbers.
    # 0 will divide the array to several separated subarrays
