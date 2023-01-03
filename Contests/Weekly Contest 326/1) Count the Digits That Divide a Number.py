"""
https://leetcode.com/problems/count-the-digits-that-divide-a-number
"""


def count_digits(num: int) -> int:
    """"""

    ans = 0
    for d in str(num):
        ans += num % int(d) == 0
    return ans
