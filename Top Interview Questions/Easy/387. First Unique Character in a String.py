"""
https://leetcode.com/problems/first-unique-character-in-a-string/
"""


def firstUniqChar(s: str) -> int:

    # 1) Brute Force: TC = O(n^2); SC = O(1)

    """
    for i, c in enumerate(s):
        if s.count(c) == 1:
            return i

    return -1
    """

    # 2) Using Hash Table: TC = O(n); SC = O(1) (because of Q. constraint 2: "s consists of only lowercase English letters")

    """
    from collections import Counter
    ht = Counter(s)

    for i, c in enumerate(s):
        if ht[c] == 1:
            return i
    return -1    
    """

    ht = {}  # key = chr, value = 1 if chr is non-repeating else 0
    for c in s:
        if c in ht:  # O(1) coz ht will have 26 items at max
            ht[c] = 0
        else:
            ht[c] = 1
    print(ht)  # debug

    for i, c in enumerate(s):
        if ht[c]:
            return i
    return -1
