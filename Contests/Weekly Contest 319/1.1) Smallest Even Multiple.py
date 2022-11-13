"""
https://leetcode.com/problems/smallest-even-multiple
"""


def smallest_even_multiple(n: int) -> int: return n*2 if n % 2 else n  # or `return n * ((n % 2)+1)`
