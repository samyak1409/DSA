"""
https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative
"""


def find_max_k(nums: list[int]) -> int:
    """"""

    # What data structure can help you to determine if an element exists?
    # Would a hash table help?
    # 1) Optimal (HashSet): TC = O(n); SC = O(n)

    hs = set()  # for O(1) lookup
    max_k = -1  # "If there is no such integer, return `-1`."
    for k in nums:
        if -k in hs:  # check
            max_k = max(max_k, abs(k))  # `abs(num)` because "Return the positive integer `k`."
        hs.add(k)  # save
    return max_k
