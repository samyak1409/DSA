"""
https://leetcode.com/problems/count-the-number-of-square-free-subsets
"""


def square_free_subsets(nums: list[int]) -> int:
    """"""

    # There are 10 primes before number 30.
    # Label primes from {2, 3, … 29} with {0,1, … 9} and let DP(i, mask) denote the number of subsets before index: i
    # with the subset of taken primes: mask.
    # If the mask and prime factorization of nums[i] have a common prime, then it is impossible to add to the current
    # subset, otherwise, it is possible.

    # 1) Optimal (?): TC = O(?); SC = O(?)
    # https://leetcode.com/problems/count-the-number-of-square-free-subsets/solutions

    pass
