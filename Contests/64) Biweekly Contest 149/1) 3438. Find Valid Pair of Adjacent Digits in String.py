"""
https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string
"""


def find_valid_pair(s: str) -> str:
    """"""

    # 1) Optimal (Count Freq, Iterate on adjacent chars):
    # TC = O(n); SC = O(9) {s only consists of digits from '1' to '9'}

    """
    from collections import Counter

    freq = Counter(s)  # TC = O(n); SC = O(9)

    for i in range(len(s)-1):  # O(n)
        c1, c2 = s[i], s[i+1]
        if c1 != c2 and freq[c1] == int(c1) and freq[c2] == int(c2):
            return c1 + c2
    return ''
    """

    # Using `itertools.pairwise`:

    from collections import Counter
    from itertools import pairwise

    freq = Counter(s)  # TC = O(n); SC = O(9)

    for c1, c2 in pairwise(s):  # O(n)
        if c1 != c2 and freq[c1] == int(c1) and freq[c2] == int(c2):
            return c1 + c2
    return ''
