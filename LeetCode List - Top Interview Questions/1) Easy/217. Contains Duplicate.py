"""
https://leetcode.com/problems/contains-duplicate
"""


def contains_duplicate(nums: list[int]) -> bool:

    # https://leetcode.com/problems/contains-duplicate/discuss/60858/Possible-solutions.

    # Using HashSet: TC = O(n); SC = O(n)
    # https://leetcode.com/problems/contains-duplicate/discuss/60850/One-line-solution-in-python

    return len(nums) != len(set(nums))
