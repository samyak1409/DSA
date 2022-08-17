"""
https://leetcode.com/problems/number-of-arithmetic-triplets
"""


def arithmetic_triplets(nums: list[int], diff: int) -> int:
    """"""

    # 0) Brute-force (3 Loops): TC = O(n^3); SC = O(1)
    # The constraints are small enough for brute force.
    # We can use three loops, each iterating through the array to go through every possible triplet.
    # Be sure to not count duplicates.

    # 1) Optimal (Traverse & Binary Search): TC = O(n*log(n)); SC = O(1)

    def index(x: int, arr: list[int], start: int = None, end: int = None) -> (int, None):
        """Using Binary Search"""
        lo, hi = start or 0, end or len(arr)-1
        while lo <= hi:
            mid = (lo+hi) // 2
            y = arr[mid]
            if y < x:
                lo = mid + 1
            elif y > x:
                hi = mid - 1
            else:  # (if y == x)
                return mid

    count = 0
    # Traverse every num as num1:
    for i, num1 in enumerate(nums):
        # Find num2 & num3 using Binary Search:
        if j := index(x=(num2 := num1+diff), arr=nums, start=i+1):
            if index(x=num2+diff, arr=nums, start=j+1):  # `num2+diff` = num3
                count += 1
    return count
