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

    for i in range(len(nums)):
        index = abs(nums[i])  # index to leave mark at; abs() because nums[i] can be a negated value
        if nums[index] < 0:  # value at "index" found negated => "index" (nums[i]) is the duplicate number!
            for j in range(i):  # making back the negated elements positive; range(i) because elements were negated till here only
                nums[abs(nums[j])] *= -1
            # print(nums)  #debugging
            return index
        nums[index] *= -1  # leaving mark
        # print(nums)  #debugging
