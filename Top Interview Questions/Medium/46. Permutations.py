"""
https://leetcode.com/problems/permutations/
"""


from typing import List


def permute(nums: List[int]) -> List[List[int]]:

    # 1) Something not supposed to be done in an interview: TC = O(n!); SC = O(n) (iterator is being used)

    """
    from itertools import permutations
    return permutations(nums)
    """

    # 2) Backtracking (Recursion, DFS): TC = O(n!); SC = O(n)

    def func(n):
        if n:
            for i in range(n+1):
                nums[i], nums[n] = nums[n], nums[i]
                yield from func(n-1)  # recurse
                nums[i], nums[n] = nums[n], nums[i]
        else:  # base condition -> n = 0
            # print(nums)  # debug
            yield nums  # "yield nums[:]" / "yield nums.copy()"

    yield from func(len(nums)-1)


# TEST:

print()

print(list(permute([1, 2, 3])))  # same nums being yielded again and again if not yielding a new copy of the list; why? TODO

print()

list(map(print, permute([1, 2, 3])))  # and here not, *awkward silence*
