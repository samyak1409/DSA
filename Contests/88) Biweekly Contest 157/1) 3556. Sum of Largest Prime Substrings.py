"""
https://leetcode.com/problems/sum-of-largest-prime-substrings
"""


def sum_of_largest_primes(s: str) -> int:
    """"""

    # 1) Optimal (Nested Loop, Prime, Sort): TC = O(n^2); SC = O(n)
    # Since `len(s)` is small, just find all the substr of `s`, add the ones that are prime to a hashset to eliminate
    # duplicates, then sort and return the largest 3.

    from math import isqrt

    # Helper function:
    # Check each candidate for primality in O(sqrt(n)) time:
    def is_prime(x: int) -> bool:
        for d in range(2, isqrt(x)+1):
            if x % d == 0:
                return False
        return x > 1

    hs = set()
    # Iterate over all substrings of `s` to generate candidate numbers, store unique primes:
    for i in range(n:=len(s)):
        for j in range(i, n):
            if is_prime(num:=int(s[i:j+1])):
                hs.add(num)

    # Then sum the three largest (or all if fewer than three):
    return sum(sorted(hs, reverse=True)[:3])
