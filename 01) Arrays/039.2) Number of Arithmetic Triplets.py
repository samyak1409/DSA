"""
https://leetcode.com/problems/number-of-arithmetic-triplets
"""


def arithmetic_triplets(nums: list[int], diff: int) -> int:
    """"""

    # All the solutions are (modifications of the solutions) from
    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/039%29%203Sum.py

    # 0.1) Brute-force (3 Loops): TC = O(n^3); SC = O(1)
    # The constraints are small enough for brute force.
    # We can use three loops, each iterating through the array to go through every possible triplet.
    # Be sure to not count duplicates.

    # 0.2) Brute-force (2 Loops): TC = O(n^2); SC = O(1)

    """
    count = 0
    for i in range(n := len(nums)):  # loop on every num one by one
        # for every num, check the two required nums linearly which are fixed (by diff) to form arithmetic tuple:
        req_num = nums[i] + diff  # `nums[i]`: num1; `req_num`: num2
        last_left = False  # to stop once triplet is formed
        for j in range(i+1, n):
            if (num := nums[j]) == req_num:
                if last_left:  # => triplet formed
                    count += 1  # add count
                    break  # start with new num1
                req_num = num + diff  # now `req_num`: num3
                last_left = True
            elif num > req_num:
                break
    return count
    """

    # 1) Better (Traverse & Binary Search): TC = O(n*log(n)); SC = O(1)

    """
    # Helper Function:
    def index(x: int, lo: int = 0, hi: int = len(nums)-1) -> (int, None):
        # https://en.wikipedia.org/wiki/Binary_search_algorithm#Procedure
        while lo <= hi:
            y = nums[(mid := (lo+hi)//2)]
            if y == x:
                return mid
            elif y < x:
                lo = mid + 1
            else:  # (if y > x)
                hi = mid - 1

    count = 0
    # Traverse every num as num1:
    for i, num1 in enumerate(nums):
        # Find num2 & num3 using Binary Search:
        if j := index(x=(num2 := num1+diff), lo=i+1):
            if index(x=num2+diff, lo=j+1):  # `num2+diff`: num3
                count += 1
    return count
    """

    # 2) Optimal (Traverse & Hashing): TC = O(n); SC = O(n)
    # https://leetcode.com/problems/number-of-arithmetic-triplets/discuss/2392136/C++-Easy-Hashmap-solution-or-with-explanation
    # https://leetcode.com/problems/number-of-arithmetic-triplets/discuss/2390635/JavaPython-3-HashSet-O(n)-codes-w-analysis.
    # https://leetcode.com/problems/number-of-arithmetic-triplets/discuss/2390637/Check-n-diff-and-n-2-*-diff

    hashset = set()
    count = 0
    # Traverse every num as num3:
    for num3 in nums:
        # Find num2 & num1 using Hashing:
        if (num2 := num3-diff) in hashset and num2-diff in hashset:  # `num2-diff` = num1
            count += 1
        hashset.add(num3)  # adding after checking ✅
    return count
