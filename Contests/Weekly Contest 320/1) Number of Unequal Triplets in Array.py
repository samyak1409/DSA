"""
https://leetcode.com/problems/number-of-unequal-triplets-in-array
"""


def unequal_triplets(nums: list[int]) -> int:
    """"""

    # 0) Brute-force (Nested Loops): TC = O(n^3); SC = O(1)
    # The constraints are very small. Can we try every triplet?
    # Yes, we can. Use three loops to iterate through all the possible triplets, ensuring the condition i < j < k holds.

    n = len(nums)
    ans = 0
    for i in range(n):
        num1 = nums[i]
        for j in range(i+1, n):
            num2 = nums[j]
            for k in range(j+1, n):
                num3 = nums[k]
                if num1 != num2 and num2 != num3 and num1 != num3:
                    # print([num1, num2, num3])  #debugging
                    ans += 1
    return ans

    # 1) Optimal (?): TC = O(n); SC = O(n)
    # https://leetcode.com/problems/number-of-unequal-triplets-in-array/discuss
