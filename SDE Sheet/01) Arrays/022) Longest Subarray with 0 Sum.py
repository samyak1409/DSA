"""
https://www.codingninjas.com/codestudio/problems/920321
"""


def longest_subarray_with_0_sum(arr: list[int]) -> int:
    """"""

    # 0) [TLE] Brute-force (Nested Loop): TC = O(n^2); SC = O(1)

    """
    n = len(arr)
    ans = 0
    for i in range(n):  # choose every element one by one
        sum_ = 0  # init
        for j in range(i, n):
            sum_ += arr[j]  # increase the length of sub-array
            if sum_ == 0:  # whenever sum_ becomes 0, check the length of the sub-array
                ans = max(ans, j-i+1)
    return ans
    """

    # Sorting?
    # i) Sort the array
    # ii) Go to the integer which is closet to 0
    # iii) Use Two-Pointers to move left and right to find the largest sub-array with 0 sum
    # WRONG (Obviously): Sub-array means sub-array of original array, sorting will change the order!
    # It's possible in case like Two Sum (see `1.2)` of
    # https://github.com/samyak1409/DSA/blob/main/SDE%20Sheet/01%29%20Arrays/019%29%20Two%20Sum.py) (basically where
    # order doesn't matter, e.g. subset), but not in the case of subarray/substring or subsequence (where order
    # matters).

    # 1) Optimal (Prefix-Sum & HashMap): TC = O(n); SC = O(n)
    # Easy https://youtu.be/xmguZ6GbatA

    ps = 0
    index = {ps: -1}  # for O(1) lookup; initializing with `ps: -1` because:
    # dry run the algo with input arr = [1, -1, 1, -1] to know
    ans = 0
    for i, num in enumerate(arr):  # O(n)
        ps += num
        if (leftmost := index.get(ps)) is not None:  # => this prefix sum has occurred before; O(1)
            ans = max(ans, i-leftmost)  # `i-leftmost` = length of 0 sum subarray
        else:  # this prefix sum has occurred 1st time
            index[ps] = i  # save
    return ans


# Similar Questions:
# https://www.codingninjas.com/codestudio/problems/1115652
# https://leetcode.com/problems/continuous-subarray-sum
# https://leetcode.com/problems/contiguous-array
