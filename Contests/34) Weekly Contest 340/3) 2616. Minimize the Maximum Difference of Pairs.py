"""
https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs
"""


def minimize_max(nums: list[int], p: int) -> int:
    """"""

    # Can we use dynamic programming here?
    # To minimize the answer, the array should be sorted first.
    # The recurrence relation is fn(i, x) = min(fn(i+1, x), max(abs(nums[i]-nums[i+1]), fn(i+2, p-1)), and fn(0,p) gives
    # the desired answer.

    # 1) Optimal (MinMax? BS!): TC = O(n*log(n) + log2(max(nums[-1]-nums[0]))*n); SC = O(n)
    # https://github.com/samyak1409/DSA/blob/main/Contests/21%29%20Weekly%20Contest%20331/3%29%20House%20Robber%20IV.py
    # https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/solutions

    # Helper Function:
    def check(val: int) -> bool:
        # Check if making `p` pairs w/ diff <= `val` is possible or not:
        p_formed = 0
        i = 0
        while p_formed != p:  # O(n)
            try:  # EAFP
                if nums[i+1]-nums[i] <= val:
                    p_formed += 1
                    i += 2  # these two are taken, so
                else:
                    i += 1  # take case (nums=[1, 1, 1, 2, 2], p=2)
            except IndexError:  # traversed whole array, failed to make `p` pairs w/ diff <= `val`
                return False
        return True

    nums = sorted(nums)  # O(n*log(n)); O(n)

    # https://en.wikipedia.org/wiki/Binary_search_algorithm#Procedure_for_finding_the_leftmost_element:
    lo, hi = 0, nums[-1]-nums[0] + 1
    while lo < hi:  # O(log2(10^9)) = O(30) = O(1) {max(nums[-1]-nums[0]) == 10^9)
        guess = (lo + hi) // 2
        if check(guess):  # current guess val is valid, let's see if we can get a smaller valid val
            hi = guess
        else:  # p_formed < p, guess was invalid, we need a larger val
            lo = guess + 1
    return lo  # or hi
