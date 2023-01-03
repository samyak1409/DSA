"""
https://leetcode.com/problems/distinct-prime-factors-of-product-of-array
"""


def distinct_prime_factors(nums: list[int]) -> int:
    """"""

    hs = set()

    for num in nums:
        f = 2
        while num != 1:
            if num % f == 0:
                num //= f
                hs.add(f)
            else:
                f += 1

    return len(hs)
