"""
https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k
"""


def min_operations(nums: list[int], k: int) -> int:
    """"""

    # Hint 1: Handle the case when the array contains an integer less than k
    # Hint 2: Start by performing operations on the highest integer
    # Hint 3: You can perform an operation on the highest integer using the second-highest, an operation on the
    # second-highest using the third-highest, and so forth.
    # Hint 4: The answer is the number of distinct integers in the array that are larger than k.

    # 1) Optimal (HashSet): TC = O(n); SC = O(n)

    # Edge case: If any of the num is < k, then we can't make it = k (because it's < k, and we can only change nums
    # which are greater than current num):
    if min(nums) < k:
        return -1

    # There are 3 possibilities:
    # a) min(nums) < k: we'd return from above.
    # b) min(nums) == k: we'd need len(set(nums))-1 ops.
    # c) min(nums) > k (implying k not in nums): we'd need len(set(nums)) ops.
    return len(set(nums)) - int(min(nums) == k)
