"""
https://leetcode.com/problems/degree-of-an-array
"""


def find_shortest_sub_array(nums: list[int]) -> int:
    """"""

    # 0) Brute-force (Calc. degree of whole array, Calc. degree of all the subarrays, Return length of the smallest
    # subarray with same degree): TC = O(n^2); SC = O(n)

    # 1) Optimal (Store [Frequencies, LeftMost & RightMost Indices] in HashMap): TC = O(n); SC = O(n)
    # https://leetcode.com/problems/degree-of-an-array/solution
    # https://leetcode.com/problems/degree-of-an-array/discuss/124317/JavaC++Python-One-Pass-Solution

    # Two Pass:
    """
    # Pass 1: Calculate the Degree of Array, and every num's [frequency, leftmost_index, rightmost_index]:
    hashmap = {}  # num: [frequency, leftmost_index, rightmost_index]
    degree = 0  # maximum frequency of any element
    for index, num in enumerate(nums):
        if num not in hashmap:
            hashmap[num] = [1, index, index]  # add [frequency, leftmost_index, rightmost_index]
        else:
            hashmap[num][0] += 1  # update frequency
            hashmap[num][2] = index  # update rightmost_index
        degree = max(degree, hashmap[num][0])  # update degree if required
    # print(hashmap, degree)  #debugging

    # Pass 2: Find length of the smallest subarray with same Degree:
    min_len = len(nums)  # length of the smallest subarray with same degree
    for (frequency, leftmost_index, rightmost_index) in hashmap.values():
        if frequency == degree:
            min_len = min(min_len, rightmost_index-leftmost_index+1)
    return min_len
    """
    # One Pass:
    hashmap = {}  # num: [frequency, leftmost_index, rightmost_index]
    degree = 0  # maximum frequency of any element
    min_len = len(nums)  # length of the smallest subarray with same degree
    for index, num in enumerate(nums):
        # Add/Update Frequencies & Indices:
        if num not in hashmap:
            hashmap[num] = [1, index, index]  # add [frequency, leftmost_index, rightmost_index]
        else:
            hashmap[num][0] += 1  # update frequency
            hashmap[num][2] = index  # update rightmost_index
        # Update Degree and Minimum Length:
        frequency, leftmost_index, rightmost_index = hashmap[num]
        if frequency == degree:  # => found another candidate with same degree
            min_len = min(min_len, rightmost_index-leftmost_index+1)
            # update `min_len` if this candidate forms less length
        elif frequency > degree:  # => found a candidate with higher degree
            degree = frequency  # update degree
            min_len = rightmost_index-leftmost_index+1  # now `min_len` = length with this candidate
    return min_len
