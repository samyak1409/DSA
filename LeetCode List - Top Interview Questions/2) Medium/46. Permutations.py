"""
https://leetcode.com/problems/permutations
"""


from collections.abc import Iterator


def permute(nums: list[int]) -> list[list[int]]:

    # 1) Something not supposed to be done in an interview: TC = O(n!); SC = O(n) (iterator is being used)

    """
    from itertools import permutations
    return permutations(nums)
    """

    # 2) Backtracking (Recursion, DFS): TC = O(n!); SC = O(n)

    def func(n: int) -> Iterator[list[int]]:
        if n:
            for i in range(n+1):
                nums[i], nums[n] = nums[n], nums[i]
                yield from func(n-1)  # recurse
                nums[i], nums[n] = nums[n], nums[i]
        else:  # base condition -> n = 0
            # print(nums)  #debugging
            yield nums  # "yield nums[:]" / "yield nums.copy()"

    yield from func(len(nums)-1)


# TEST:

print()

print(list(permute([1, 2, 3])))  # same nums being yielded again and again if not yielding a new copy of the list; why?
# TODO

print()

list(map(print, permute([1, 2, 3])))  # and here not, *awkward silence*
