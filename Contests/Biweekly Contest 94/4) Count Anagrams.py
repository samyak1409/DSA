"""
https://leetcode.com/problems/count-anagrams
"""


def count_anagrams(s: str) -> int:
    """"""

    from math import factorial
    from collections import Counter

    ans = 1

    for word in s.split():
        ans *= factorial(len(word)) // (sum(map(factorial, filter(lambda val: val > 1, Counter(word).values()))) or 1)

    return ans
