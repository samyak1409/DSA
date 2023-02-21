"""
https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon
"""


def monkey_move(n: int) -> int:
    """"""

    # 1) Optimal (Reverse Count Ways + Fast Power (Exponentiation by Squaring)): TC = O(log2(n)); SC = O(1)
    # Try counting the number of ways in which the monkeys will not collide.
    # Read following for solution explanation and about wrong problem description (as of now):
    # https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/solutions/3111664/java-c-python-should-be-pow-2-n-4

    # [TLE] Normal Powering: TC = O(n)
    # Because max(n) == 10^9, normal powering is TLE.
    """
    return (2**n - 2) % 1000_000_007
    """

    # Exponentiation by Squaring: TC = O(log2(n))
    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/014%29%20Pow(x,%20n).py

    # Calculating total ways i.e. 2^n:
    base = 2
    total_ways = 1
    while n:
        if n & 1:  # if n is odd
            total_ways = (total_ways*base) % 1000_000_007  # multiply
            n -= 1
        base = (base*base) % 1000_000_007  # square
        n >>= 1  # n //= 2
        # Note that these mod in intermediates are must, without them, we'll run into TLE again, but why? Now the
        # solution is only O(log2(n)), and the fact that python doesn't have int limits, then what's the problem?
        # Because 2^n is an exponential growth, and max(n) == 10^9, so max(2^n) = 2^(10^9) which is as bigger than you
        # can imagine. So, even O(1) operation with that big number becomes slow!!
        # See the exponential growth ->
        # 2^(10^1) = 1024
        # 2^(10^2) = 1267650600228229401496703205376
        # 2^(10^3) =
        # 10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
        # :) okay bye.

    return (total_ways-2) % 1000_000_007
