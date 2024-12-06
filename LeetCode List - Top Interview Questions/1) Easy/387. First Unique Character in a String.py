"""
https://leetcode.com/problems/first-unique-character-in-a-string
"""


def first_uniq_char(s: str) -> int:
    """"""

    # 0) [TLE] Brute-force (Loop and Count): TC = O(n^2); SC = O(1)
    # Loop, count occurrence, return first char with count = 1.

    """
    for i, c in enumerate(s):  # O(n)
        if s.count(c) == 1:  # O(n)
            return i
    return -1
    """

    # 1) Optimal (Loop, Count, Save to HashMap): TC = O(26*n) = O(n); SC = O(26) = O(1)
    # Optimization of approach `0)` using hashmap.

    """
    hm = {}
    for i, c in enumerate(s):  # O(n)
        if hm.get(c) is None:
            hm[c] = s.count(c)  # O(n), but because of the above `if` condition, this line would run max 26 times
        if hm[c] == 1:
            return i
    return -1
    """

    # 2) Optimal (HashMap): TC = O(n); SC = O(26) = O(1)
    # Make a hashmap first, and then return the first char with occurrences = 1.

    from collections import Counter
    hm = Counter(s)  # O(n); O(26)

    # If `Counter` didn't preserve insertion order, then we would've done:
    '''
    for i, c in enumerate(s):  # O(n)
        if hm[c] == 1:
            return i
    return -1
    '''

    # But as it does (just like `dict`), we can also do:
    for c, x in hm.items():  # O(n)
        if x == 1:
            return s.index(c)
    return -1
