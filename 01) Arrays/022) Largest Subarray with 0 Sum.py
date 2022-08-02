"""
https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1
"""


def max_len(n: int, arr: list[int]) -> int:
    """"""

    # 0) [TLE] Brute-force (Nested Loop): TC = O(n^2); SC = O(1)

    largest_len = 0
    for i in range(n):
        sum_ = 0  # init
        for j in range(i, n):
            sum_ += arr[j]  # increase the length of sub-array
            if sum_ == 0:  # whenever sum_ becomes 0, check the length of the sub-array
                largest_len = max(largest_len, j-i+1)
    return largest_len


# Similar Questions:
# https://leetcode.com/problems/subarray-sum-equals-k
# https://leetcode.com/problems/contiguous-array
