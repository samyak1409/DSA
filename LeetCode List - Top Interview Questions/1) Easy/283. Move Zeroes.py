"""
https://leetcode.com/problems/move-zeroes
"""


def move_zeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    # 1) Brute Force: TC = O(n^2); SC = O(1)

    """
    for _ in range(nums.count(0)):  # O(n)
        nums.remove(0)  # O(n) (find + shift)
        nums.append(0)  # O(1)
    """

    # 2) Brute Force: TC = O(n); SC = O(n)

    """
    store = []  # stores non-zero numbers
    for num in filter(None, nums):
        store.append(num)
    for i in range(len(store)):  # put the non-zero numbers in the front
        nums[i] = store[i]
    for i in range(len(nums)-len(store)):  # put the zeros in the back
        nums[-i-1] = 0
    """

    # 2.1) Efficient: TC = O(n); SC = O(1)

    """
    front = 0
    for i in range(len(nums)):  # copying the non-zero numbers to the front
        if nums[i] != 0:  # if num is non-zero
            nums[front] = nums[i]  # copy num to the front
            front += 1  # inc front
    for i in range(len(nums)-front):  # filling the end indices with 0
        nums[-i-1] = 0
    """

    # 3) Efficient: TC = O(n); SC = O(1)

    """
    zeroes = 0
    for i in range(len(nums)):  # copying the non-zero numbers to the front
        if nums[i] == 0:
            zeroes += 1
        else:  # non-zero
            nums[i-zeroes] = nums[i]  # copy num to the front
    for i in range(zeroes):  # filling the end indices with 0
        nums[-i-1] = 0
    """

    # 4) Best (in terms of no. of ops): TC = O(n); SC = O(1)

    zero = 0  # records the index of 0
    for i in range(len(nums)):
        if nums[i] != 0:  # num non-zero
            nums[i], nums[zero] = nums[zero], nums[i]  # swap
            zero += 1
