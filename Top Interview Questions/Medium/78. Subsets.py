"""
https://leetcode.com/problems/subsets/
"""


from typing import List


def subsets(nums: List[int]) -> List[List[int]]:

    # 1) https://leetcode.com/problems/subsets/solution/#:~:text=Algorithm: TC = O(2^n); SC = O(n)

    """
    from itertools import combinations

    for i in range(len(nums)+1):  # subsets of length 0 to n
        for subset in combinations(nums, i):
            yield subset
    """

    # 1.1) Implementing Combinations also; Using Backtracking (Recursion, DFS):

    """
    def func(iterable, i):
        if len(iterable) != l:
            for j in range(i, len(nums)):
                yield from func(iterable+[nums[j]], j+1)
        else:  # subset of length l formed
            # print(iterable)  # debug
            yield iterable

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

    # https://leetcode.com/problems/subsets/solution/#:~:text=Approach%203%3A%20Lexicographic%20(Binary%20Sorted)%20Subsets

    n = len(nums)
    for i in range(2**n):  # generate bitmask, from 0...00 to 1...11
        bitmask = bin(i)[2:].zfill(n)  # ("[2:]" for '0b'); 👌
        print(bitmask)  # debug
        yield [nums[i] for i in range(n) if int(bitmask[i])]
