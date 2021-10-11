"""
https://leetcode.com/problems/move-zeroes/
"""


from typing import List


def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    # 1) Brute Force: TC = O(n^2); SC = O(1)

    """
    for _ in range(nums.count(0)):  # O(n)
        nums.remove(0)  # O(n) (find + shift)
        nums.append(0)  # O(1)
    """

    # 2) Efficient (mine): TC = O(n); SC = O(1)

    i = j = 0

    for _ in range(len(nums)-1):  # replacing zeroes with next elements
        if nums[i] == 0:
            j += 1
        else:
            i += 1
        nums[i] = nums[i+j]

    print(nums)  # debug 👌

    for i in range(j):  # replacing last j elements with zeroes
        nums[-i-1] = 0

    # 3) Efficient (from "Discuss"): TC = O(n); SC = O(1)

    """
    zero = 0  # records the position of "0"
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1
    """
