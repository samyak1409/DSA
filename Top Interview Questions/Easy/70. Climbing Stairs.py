"""
https://leetcode.com/problems/climbing-stairs/
"""


def climbStairs(n: int) -> int:

    # DP! https://youtu.be/Y0lT9Fck7qI?t=707: TC = O(n); SC = O(1)

    n1, n2 = 1, 1

    for _ in range(n-1):
        n1, n2 = n1+n2, n1

    return n1

    # https://leetcode.com/problems/climbing-stairs/discuss/25299/Basically-it's-a-fibonacci.
