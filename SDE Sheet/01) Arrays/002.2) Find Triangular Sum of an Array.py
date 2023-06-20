"""
https://leetcode.com/problems/find-triangular-sum-of-an-array
"""


def triangular_sum(nums: list[int]) -> int:
    """"""

    # 0) Brute-force (Calculate each row iteratively): TC = O(n^2); SC = O(n)

    # 1) Optimal (Calculate the Multipliers): TC = O(n); SC = O(1)
    # Each number in the array contributes to the final sum a certain number of times. We can visualize how to figure
    # out factors for each number using Pascal's triangle:
    # https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif    1
    #                                                                                  1   1
    #                                                                                1   2   1
    #                                                                              1   3   3   1
    #                                                                            1   4   6   4   1
    # For test case [1, 2, 3, 4, 5], we will get 1*1 + 2*4 + 3*6 + 4*4 + 5*1 = 1+8+18+16+5 = 48, or 8 after modulo 10.
    # Calculating the multipliers using:
    # https://github.com/samyak1409/DSA/blob/main/SDE%20Sheet/01%29%20Arrays/002.1%29%20Pascal%27s%20Triangle%20II.py
    # Multipliers will be nothing but n-th (len(nums)-th) row in Pascal's Triangle, why?
    # Because both, the triangle here and the Pascal's triangle, are based on the same base logic that new sum is
    # formed using the sum of two values above in the triangle.

    n = len(nums)
    multiplier = 1  # init
    ans = nums[0] * multiplier
    for i in range(1, n):
        multiplier = (multiplier*(n-i)) // i
        ans += nums[i] * multiplier
    return ans % 10

    # Runtime: 152 ms, faster than 98.89% of Python3 online submissions for Find Triangular Sum of an Array.
    # Memory Usage: 13.9 MB, less than 96.59% of Python3 online submissions for Find Triangular Sum of an Array.
