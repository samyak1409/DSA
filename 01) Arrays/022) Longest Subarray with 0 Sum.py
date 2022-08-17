"""
https://www.codingninjas.com/codestudio/problems/920321
"""


def longest_subarray_with_0_sum(arr: list[int]) -> int:
    """"""

    # 0) [TLE] Brute-force (Nested Loop): TC = O(n^2); SC = O(1)

    """
    n = len(arr)
    longest_len = 0
    for i in range(n):  # choose every element one by one
        sum_ = 0  # init
        for j in range(i, n):
            sum_ += arr[j]  # increase the length of sub-array
            if sum_ == 0:  # whenever sum_ becomes 0, check the length of the sub-array
                longest_len = max(longest_len, j-i+1)
    return longest_len
    """

    # Sorting?
    # i) Sort the array
    # ii) Go to the integer which is closet to 0
    # iii) Use Two-Pointers to move left and right to find the largest sub-array with 0 sum
    # WRONG (Obviously): Sub-array means sub-array of original array, sorting will change the order!
    # It's possible in case like Two Sum (see:
    # https://github.com/samyak1409/DSA/blob/268cbaaf16b5d5441e5ffd3544abf190c3ca2b94/01%29%20Arrays/019%29%20Two%20Sum.py#L51),
    # but not in the case of subarrays / subsequences (basically contiguous).

    # 1) Optimal (Prefix-Sum & HashMap): TC = O(n); SC = O(n)
    # Easy https://youtu.be/xmguZ6GbatA

    prefix_sum = 0
    leftmost_index = {prefix_sum: -1}  # for O(1) lookup; initializing with "prefix_sum: -1" because:
    # dry run the algo with input arr = [1, -1, 1, -1], you'll get the answer.
    longest_len = 0
    for index in range(len(arr)):  # O(n)
        prefix_sum += arr[index]
        if (leftmost := leftmost_index.get(prefix_sum)) is not None:  # O(1); => this prefix_sum has occurred before
            longest_len = max(longest_len, index-leftmost)  # `index-leftmost` = length of 0 sum subarray
        else:  # this prefix_sum has occurred 1st time
            leftmost_index[prefix_sum] = index  # save `prefix_sum: index`
    return longest_len


# Similar Questions:
# https://www.codingninjas.com/codestudio/problems/1115652
# https://leetcode.com/problems/continuous-subarray-sum
# https://leetcode.com/problems/contiguous-array
