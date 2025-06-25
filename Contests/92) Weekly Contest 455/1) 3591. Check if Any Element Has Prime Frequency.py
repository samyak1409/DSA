"""
https://leetcode.com/problems/check-if-any-element-has-prime-frequency
"""


def check_prime_frequency(nums: list[int]) -> bool:
    """"""

    # 1) Optimal (HashMap, Trial division): TC = O(n * √freq); SC = O(n)

    from collections import Counter
    from math import isqrt

    # Helper function:
    # https://en.wikipedia.org/wiki/Prime_number#Trial_division
    def is_prime(x: int) -> bool:
        if x == 1:
            return False
        for i in range(2, isqrt(x)+1):
            # If divisible by any num `i` in the range [2, isqrt], then not prime:
            if x % i == 0:
                return False
        return True

    for freq in Counter(nums).values():
        if is_prime(x=freq):
            return True
    return False

    # Can also be done in O(n), just replace `range(2, isqrt(x)+1)` with `(2, 3, 5, 7)`.
    # https://leetcode.com/problems/check-if-any-element-has-prime-frequency/solutions/6871930/java-c-python-easy-and-concise-2-3-5-7
