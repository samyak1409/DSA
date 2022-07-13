"""
https://leetcode.com/problems/find-the-duplicate-number
"""


from typing import List


def findDuplicate(nums: List[int]) -> int:
    """You must solve the problem without modifying the array nums and uses only constant extra space."""

    # 0.1) Brute-force (Sort and Traverse): TC = O(n*log(n)); SC = O(n)
    # Note: This approach uses extra space (sorting) so don't fulfill the problem requirement.
    # Since sorting will take O(n) space anyway, let's not modify the input array at least

    """
    sorted_nums = sorted(nums)
    for i in range(len(nums)):
        if sorted_nums[i] == sorted_nums[i+1]:
            return sorted_nums[i]
    """

    # 0.2) Brute-force (Using HashSet): TC = O(n); SC = O(n)

    """
    hash_set = set()
    for num in nums:  # TC = O(n)
        if num in hash_set:  # already in; TC = O(1)
            return num
        hash_set.add(num)  # SC = O(n)
    """

    # 1) Negating Numbers: TC = O(n); SC = O(1)
    # Note: This algorithm modifies the array temporarily.

    """
    for i in range(len(nums)):
        index = abs(nums[i])  # index to leave mark at; abs() because nums[i] can be a negated value
        if nums[index] < 0:  # value at "index" found negated => "index" (nums[i]) is the duplicate number!
            for j in range(i):  # turning the negated elements back positive; range(i) because elements were negated till here only
                nums[abs(nums[j])] *= -1
            # print(nums)  #debugging
            return index
        nums[index] *= -1  # leaving mark
        # print(nums)  #debugging
    """

    # 2) Maths (Sum of n terms) (WRONG ANSWER): TC = O(n); SC = O(1)
    # WA because nums can be = [2, 2, 2, 2, 2]
    # "Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive."
    # doesn't mean array will have all numbers from 1 to n and 1 number from the range repeating,
    # but means if the array has n + 1 numbers, every number will be between 1 and n!!
    # This was to clarify that array would never be = e.g. [2, 3, 3, 10]; => n+1 = 4 => n = 3; but 10 is not in the range [1, 3].

    """
    n = len(nums) - 1
    return sum(nums) - n * (n+1) // 2
    """

    # 3) Floyd's Cycle Detection Algo: TC = O(n); SC = O(1)
    # Cycle will be there for sure as the array contain duplicate for sure; we have to find the start point of cycle,
    # because start point will be the duplicate only for sure

    slow = fast = nums[0]  # start from start
    while True:  # imp: exit controlled (do-while) loop
        slow = nums[slow]  # next
        fast = nums[nums[fast]]  # next of next
        if slow == fast:  # cycle detected
            break
    slow2 = nums[0]
    while slow2 != slow:  # finding the start point of cycle
        slow2 = nums[slow2]
        slow = nums[slow]
    return slow2  # duplicate found
