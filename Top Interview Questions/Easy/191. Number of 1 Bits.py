"""
https://leetcode.com/problems/number-of-1-bits/
"""


def hammingWeight(n: int) -> int:  # TC = O(log n); SC = O(1)

    return bin(n).count('1')  # deci -> bin and then counting occurrences
