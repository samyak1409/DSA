"""
https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1
"""


def max_len(n: int, arr: list[int]) -> int:
    """"""

    # 0) [TLE] Brute-force (Nested Loop): TC = O(n^2); SC = O(1)

    """
    largest_len = 0
    for i in range(n):
        sum_ = 0  # init
        for j in range(i, n):
            sum_ += arr[j]  # increase the length of sub-array
            if sum_ == 0:  # whenever sum_ becomes 0, check the length of the sub-array
                largest_len = max(largest_len, j-i+1)
    return largest_len
    """

    # Sorting?
    # i) Sort the array
    # ii) Go to the integer which is closet to 0
    # iii) Use Two-Pointers to move left and right to find the largest sub-array with 0 sum
    # WRONG (Obviously): Sub-array means sub-array in the input array, sorting will change the order!

    # 1) Optimal (Prefix-Sum & HashSet): TC = O(n); SC = O(n)
    # Easy https://youtu.be/xmguZ6GbatA

    prefix_sum = 0
    hashset = {prefix_sum: -1}  # O(1) lookup
    # initializing with "prefix_sum: -1" because:
    # dry run the algo with input arr = [1, -1, 1, -1], you'll get your answer.
    longest_len = 0
    for i in range(n):  # O(n)
        prefix_sum += arr[i]
        if prefix_sum in hashset:  # O(1)
            longest_len = max(longest_len, i-hashset[prefix_sum])
        else:
            hashset[prefix_sum] = i
    return longest_len


# Similar Questions:
# https://leetcode.com/problems/subarray-sum-equals-k
# https://leetcode.com/problems/contiguous-array
