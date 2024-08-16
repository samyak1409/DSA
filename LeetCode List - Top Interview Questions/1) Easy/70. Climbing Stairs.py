"""
https://leetcode.com/problems/climbing-stairs
"""


def climb_stairs(n: int) -> int:

    # DP! https://youtu.be/Y0lT9Fck7qI?t=707: TC = O(n); SC = O(1)

    n1, n2 = 1, 1

    for _ in range(n-1):
        n1, n2 = n1+n2, n1

    return n1

    # https://leetcode.com/problems/climbing-stairs/discuss/25299/Basically-it's-a-fibonacci.

    # Note that fibonacci (https://leetcode.com/problems/fibonacci-number) can also be found by dividing by the golden
    # ratio.
    # [The magic of Fibonacci numbers | Arthur Benjamin](https://youtu.be/SjSHVDfXHQ4)
    # https://en.wikipedia.org/wiki/Fibonacci_number

    # 1 (init)
    # round(1 * 1.618) = 2
    # round(2 * 1.618) = 3
    # round(3 * 1.618) = 5
    # round(5 * 1.618) = 8
    # and so on...
