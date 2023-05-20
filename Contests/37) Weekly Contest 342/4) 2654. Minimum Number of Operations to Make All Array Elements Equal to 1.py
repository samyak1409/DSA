"""
https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1
"""


def min_operations(nums: list[int]) -> int:
    """"""

    # Note that if you have at least one occurrence of 1 in the array, then you can make all the other elements equal
    # to 1 with one operation each.
    # Try finding the shortest subarray with a gcd equal to 1.

    # 1) Optimal (Maths): TC = O(n^2); SC = O(1)
    # Read the QnA:
    # https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/solutions/3445725/explained-easy-gcd-and-intuition

    from math import gcd

    # Edge Case: If 1 is already there:
    if ones := nums.count(1):
        return len(nums)-ones

    ops = float('inf')  # init; min no. of ops to make gcd of any sub-array = 1

    # Checking for all sub-arrays: O(n^2)
    for i in range(n := len(nums)):

        g = nums[i]  # init

        for j in range(i+1, n):
            if (g := gcd(g, nums[j])) == 1:
                ops = min(ops, j-i)
                break  # breaking coz next j will obv be > current j

    # Now, that we've got min no. of ops to make gcd of any sub-array = 1, `+n-1` to make remaining elements = 1 using
    # current 1:
    return ops+n-1 if ops != float('inf') else -1
    # At first, you may have a doubt that what is the proof that making all other elements 1 using the 1 we have got
    # will be optimal (as we have to minimize the no. of ops).
    # But we don't need to prove anything, because bruh, we need to update all other elements, so that simply takes x
    # ops anyway (for making x nums = 1).

    # Follow-up:
    # The O(n) time complexity solution works, but could you find an O(1) constant time complexity solution?
    # WDYM??
