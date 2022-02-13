"""
https://leetcode.com/problems/two-sum/
"""


from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:

    # 0) Brute-force (TLE): TC = O(n^2); SC = O(1)

    """
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i]+nums[j] == target:
                return [i, j]
    """

    # 1) Tried Sorting + Binary Search but didn't work out. (TC = O(n log n); SC = O(n))

    # 2) Hash Map: TC = O(n); SC = O(n)

    """
    hashmap = {}  # num: index
    for i, num in enumerate(nums):
        hashmap[num] = i

    for i, num in enumerate(nums):
        i_req = hashmap.get(target-num)  # target-num = required num; i_req -> index of required num
        if i_req is not None and i_req != i:
            return [i, i_req]
    """

    # 2.1) Hash Map (Single-pass): TC = O(n); SC = O(n)

    hashmap = {}  # num: index
    for i, num in enumerate(nums):
        i_req = hashmap.get(target-num)  # target-num = required num; i_req -> index of required num
        if i_req is not None:
            return [i, i_req]
        hashmap[num] = i
