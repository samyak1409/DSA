"""
https://leetcode.com/problems/the-number-of-beautiful-subsets
"""


def beautiful_subsets(nums: list[int], k: int) -> int:
    """"""

    # Sort the array nums and create another array cnt of size nums[i].
    # Use backtracking to generate all the beautiful subsets. If cnt[nums[i] - k] is positive, then it is impossible to
    # add nums[i] in the subset, and we just move to the next index. Otherwise, it is also possible to add nums[i] in
    # the subset, in this case, increase cnt[nums[i]], and move to the next index.

    # 1) Optimal (?): TC = O(?); SC = O(?)
    # https://leetcode.com/problems/the-number-of-beautiful-subsets/solutions

    pass
