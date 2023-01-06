"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    """"""

    # NOTE: All the following solutions are from
    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/019%29%20Two%20Sum.py
    # because this problem is just a subset of https://leetcode.com/problems/two-sum.

    # https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/discuss/51249/Python-different-solutions-(two-pointer-dictionary-binary-search).

    # 0) [TLE] Brute-force (Nested Loop): TC = O(n^2); SC = O(1)

    """
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i]+nums[j] == target:
                return [i+1, j+1]
    """

    # 1) Better (Binary Search): TC = O(n*log(n)); SC = O(1)

    """
    n = len(nums)
    # Taking every num one by one:
    for index1 in range(n):
        req_num2 = target - nums[index1]  # nums[index1] = num1
        # Finding the required_num2 using Binary Search:
        # https://en.wikipedia.org/wiki/Binary_search_algorithm#Procedure
        lo, hi = index1+1, n-1
        while lo <= hi:
            index2 = (lo+hi) // 2  # mid index
            num2 = nums[index2]
            if num2 == req_num2:
                return [index1+1, index2+1]
            elif num2 < req_num2:
                lo = index2 + 1
            else:  # (if num2 > req_num2)
                hi = index2 - 1
    """

    # Note: We can apply the HashMap solution to this problem as well, but not applying because
    # as the array is sorted, it doesn't make sense to use hashmap (=> use extra space).
    # Also, it's clearly mentioned in the problem: "Your solution must use only constant extra space."

    # 2) Optimal (Two-Pointers): TC = O(n); SC = O(1)

    # Finding the 2 nums using Two-Pointers:
    lo, hi = 0, len(nums)-1  # init
    while lo < hi:
        num1, num2 = nums[lo], nums[hi]
        if num1+num2 == target:
            return [lo+1, hi+1]
        elif num1+num2 < target:  # => we want greater sum
            lo += 1  # considering next num (larger) in right
        else:  # (if num1+num2 > target) => we want lesser sum
            hi -= 1  # considering next num (smaller) in left
