"""
https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i
"""


def max_difference(s: str) -> int:
    """"""

    # 1) Optimal (Greedy, HashMap): TC = O(n); SC = O(26) {`s` consists only of lowercase English letters}
    # What we want basically is: most frequent odd freq char - least freq even freq char.

    from collections import Counter

    max_odd, min_even = 0, float('inf')

    for c, freq in Counter(s).items():
        if freq % 2:  # odd freq
            max_odd = max(max_odd, freq)
        else:  # even
            min_even = min(min_even, freq)

    return max_odd - min_even
