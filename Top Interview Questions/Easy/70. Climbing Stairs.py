"""
https://leetcode.com/problems/climbing-stairs/
"""


def climbStairs(n: int) -> int:

    # Fibonacci Sequence:

    a = b = 1

    for _ in range(n):
        a, b = b, a + b

    return a

    # I was going for permutations, but I thought of taking a look at the output in case some kind of sequence is forming, and YES.
