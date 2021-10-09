"""
https://leetcode.com/problems/climbing-stairs/
"""


def climbStairs(n: int) -> int:

    # Fibonacci Sequence: TC = O(n); SC = O(1)

    a = b = 1

    for _ in range(n):
        a, b = b, a + b

    return a

    # I was thinking of permutations or something, but thought of taking a look at the output in case some kind of sequence is forming, and YES.
