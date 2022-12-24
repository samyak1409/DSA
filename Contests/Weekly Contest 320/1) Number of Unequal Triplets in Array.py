"""
https://leetcode.com/problems/number-of-unequal-triplets-in-array
"""


def unequal_triplets(nums: list[int]) -> int:
    """"""

    # 0) Brute-force (3 Loops): TC = O(n^3); SC = O(1)
    # The constraints are very small. Can we try every triplet?
    # Yes, we can. Use three loops to iterate through all the possible triplets, ensuring the condition i < j < k holds.

    """
    n = len(nums)
    ans = 0
    for i in range(n):
        num1 = nums[i]
        for j in range(i+1, n):
            num2 = nums[j]
            for k in range(j+1, n):
                num3 = nums[k]
                if num1 != num2 and num2 != num3 and num1 != num3:  # or `if len(set([num1, num2, num3])) == 3:`
                    # print([num1, num2, num3])  #debugging
                    ans += 1
    return ans
    """

    # 1) Better (2 Loops and HashMap): TC = O(n^2); SC = O(n)

    from collections import Counter
    freq, total = Counter(), 0  # `Counter` for easy working
    ans = 0
    # Reverse Traversal to satisfy "0 <= i < j < k < nums.length" while using HashMap:
    for j in range(len(nums)-2, 0, -1):  # from 2nd last index to index `1`
        # Save num3 to HashMap for future lookup:
        freq[nums[j+1]] += 1  # j+1 -> k, nums[j+1] -> num3
        total += 1
        num2 = nums[j]
        for i in range(j-1, -1, -1):  # from j-1 to 0th index
            num1 = nums[i]
            # Following to satisfy "nums[i] != nums[j], nums[i] != nums[k], and nums[j] != nums[k]" and count ans:
            if num1 != num2:
                ans += total - (freq[num2] + freq[num1])  # this is only adding triplet count to ans. by removing all
                # the num2 and num1 so that only those are left are bound to be distinct to num2 and num1, so = num3
    return ans

    # 1) Optimal (?): TC = O(n); SC = O(n)
    # https://leetcode.com/problems/number-of-unequal-triplets-in-array/solutions
