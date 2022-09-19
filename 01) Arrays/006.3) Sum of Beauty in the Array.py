"""
https://leetcode.com/problems/sum-of-beauty-in-the-array
"""


def sum_of_beauties(nums: list[int]) -> int:
    """"""

    # 0) [TLE] Brute-force: TC = O(n^2); SC = O(1)

    # 1) Optimal (Prefix & Suffix Array): TC = O(n); SC = O(n)
    # Easy.
    # Use suffix/prefix arrays.
    # prefix[i] records the maximum value in range (0, i-1) inclusive.
    # suffix[i] records the minimum value in range (i+1, n-1) inclusive.
    # https://leetcode.com/problems/sum-of-beauty-in-the-array/discuss

    # We can also do this: Instead of saving max/min in array, directly save (partial) beauty for left & right, and then
    # the beauties will just be min of two partial-beauties.
    """
    n = len(nums)
    beauty_for_left, beauty_for_right = [0]*(n-2), [0]*(n-2)
    max_in_left, min_in_right = float('-inf'), float('inf')
    for i in range(1, n-1):
        if nums[i] > (max_in_left := max(max_in_left, nums[i-1])):
            beauty_for_left[i-1] = 2
        elif nums[i] > nums[i-1]:
            beauty_for_left[i-1] = 1
        if nums[~i] < (min_in_right := min(min_in_right, nums[~(i-1)])):
            beauty_for_right[~(i-1)] = 2
        elif nums[~i] < nums[~(i-1)]:
            beauty_for_right[~(i-1)] = 1
    # print(beauty_for_left, beauty_for_right)  #debugging

    return sum(min(tup) for tup in zip(beauty_for_left, beauty_for_right))
    """

    n = len(nums)
    max_in_left = [nums[0]]  # init prefix array with leftmost value
    min_in_right = [nums[-1]]  # init suffix array with rightmost value
    for i in range(1, n-2):
        max_in_left.append(max(max_in_left[i-1], nums[i]))
        min_in_right.append(min(min_in_right[i-1], nums[~i]))  # ~i = -i-1 (bit magic)
        # https://en.wikipedia.org/wiki/Bitwise_operation#NOT; https://wiki.python.org/moin/BitwiseOperators
    min_in_right.reverse()
    # print(max_in_left, min_in_right)  #debugging

    # As per the question:
    beauty_sum = 0
    for i in range(1, n-1):
        if max_in_left[i-1] < nums[i] < min_in_right[i-1]:
            beauty_sum += 2
        elif nums[i-1] < nums[i] < nums[i+1]:
            beauty_sum += 1
    return beauty_sum
