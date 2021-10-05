"""
https://leetcode.com/problems/pascals-triangle/
"""


from typing import List


def generate(num_rows: int) -> List[List[int]]:

    res = [[1], [1, 1]]  # initialization

    if num_rows in (1, 2):  # no summation
        return res[:num_rows]

    # Summation using a nested for loop:

    for i in range(1, num_rows-1):  # (num_rows-2) times

        res.append([1])  # (prefix)

        for j in range(i):  # (1 to num_rows-2) times
            res[i+1].append(res[i][j]+res[i][j+1])  # mid numbers' calc

        res[i+1].append(1)  # (suffix)

    return res
