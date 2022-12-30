"""
https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured
"""


def capture_forts(forts: list[int]) -> int:
    """"""

    n = len(forts)
    ans = 0
    for i in range(n):
        if forts[i] != 0:
            sum_ = forts[i]
            for j in range(i+1, n):
                if forts[j] != 0:
                    sum_ += forts[j]
                    if sum_ == 0:
                        ans = max(ans, j-i-1)
                    break
    return ans
