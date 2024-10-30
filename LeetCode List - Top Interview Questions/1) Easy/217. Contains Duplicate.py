"""
https://leetcode.com/problems/contains-duplicate
"""


def contains_duplicate(nums: list[int]) -> bool:
    """"""

    # https://leetcode.com/problems/contains-duplicate/solutions

    # 0.1) Brute-force (Nested Loop): TC = O(n^2); SC = O(1)

    # 0.2) Brute-force (Sort): TC = O(n*log(n)); SC = O(n)

    """
    sorted_nums = sorted(nums)
    for i in range(len(sorted_nums)-1):
        if sorted_nums[i] == sorted_nums[i+1]:
            return True
    return False
    """

    # 1) Optimal (HashSet): TC = O(n); SC = O(n)

    """
    hs = set()
    for num in nums:
        if num in hs:
            return True
        hs.add(num)
    return False
    """

    # Or just use len:
    return len(nums) != len(set(nums))
