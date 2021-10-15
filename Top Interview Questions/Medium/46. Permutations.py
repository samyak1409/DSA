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

    # 2) Backtracking (Recursion, DFS): TC = O(n!); SC = O(n*n!)

    p = []

    def func(n):
        if n:
            for i in range(n+1):
                nums[i], nums[n] = nums[n], nums[i]
                func(n-1)
                nums[i], nums[n] = nums[n], nums[i]
        else:
            print(nums)  # but while printing it's working without it also, WHY?? TODO
            p.append(nums[:])  # NOTE: without creating new object ("[:]" / ".copy()"), same nums is appending again and again

    func(len(nums)-1)
    return p
