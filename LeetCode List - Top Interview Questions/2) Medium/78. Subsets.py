"""
https://leetcode.com/problems/subsets
"""


def subsets(nums: list[int]) -> list[list[int]]:

    # 1) https://leetcode.com/problems/subsets/solution/#:~:text=Algorithm: TC = O(2^n); SC = O(n)

    """
    from itertools import combinations

    for i in range(len(nums)+1):  # subsets of length 0 to n
        for subset in combinations(nums, i):
            yield subset
    """

    # 1.1) Implementing Combinations also; Using Backtracking (Recursion, DFS):

    """
    def func(list_: list, i: int) -> Iterator[list]:
        if len(list_) != l:
            for j in range(i, len(nums)):
                yield from func(list_+[nums[j]], j+1)  # recurse
        else:  # base condition -> subset of length l formed
            # print(list_)  #debugging
            yield list_

    for l in range(len(nums)+1):  # subsets of length 0 to n
        yield from func([], 0)  # will find subsets of length l
    """

    # 2) Iterative: TC = O(2^n) = SC

    """
    output = [[]]

    for num in nums:
        for prev in output[:]:  # or "for prev in output.copy():"; IMP- copying is mandatory
            output.append(prev+[num])

    return output
    """

    # 3) Using Bitmask (EASIEST!!): TC = O(2^n); SC = O(n)

    # https://leetcode.com/problems/subsets/solution/#approach-3-lexicographic-binary-sorted-subsets

    n = len(nums)
    for i in range(2**n):  # generate bitmask, from 0...00 to 1...11
        bitmask = bin(i)[2:].zfill(n)  # ("[2:]" for '0b'); 👌
        # print(bitmask)  #debugging
        yield [nums[i] for i in range(n) if int(bitmask[i])]
