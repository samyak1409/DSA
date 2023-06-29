"""
https://leetcode.com/problems/sum-in-a-matrix
"""


def matrix_sum(nums: list[list[int]]) -> int:
    """"""

    # Same as: Contests/09) Weekly Contest 323/1) Delete Greatest Value in Each Row.py
    # https://github.com/samyak1409/DSA/blob/main/Contests/09%29%20Weekly%20Contest%20323/1%29%20Delete%20Greatest%20Value%20in%20Each%20Row.py

    # Sort the numbers in each row in decreasing order.
    # The answer is the summation of the max number in every column after sorting the rows.

    # 1) Optimal (Sort, Get Max, Sum): TC = O(m * n*log(n)); SC = O(m*n) {m = rows; n = columns}

    # Sort:
    '''
    for row in nums:
        row.sort()
    '''
    nums = [sorted(row) for row in nums]  # this way, input is not modified

    '''
    score = 0
    for i in range(len(nums[0])):
        score += max(row[i] for row in nums)
    return score
    '''
    # One liner:
    return sum(max(row[i] for row in nums) for i in range(len(nums[0])))
