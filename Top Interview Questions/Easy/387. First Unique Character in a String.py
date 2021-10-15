"""
https://leetcode.com/problems/first-unique-character-in-a-string/
"""


def firstUniqChar(s: str) -> int:

    # 1) Brute Force: TC = O(n^2); SC = O(1)

    """
    for i, c in enumerate(s):

        count = 0
        for c_ in s:
            if c_ == c:
                count += 1
                if count > 1:
                    break
        if count == 1:
            return i

    return -1
    """

    # 2) Using Hash Table: TC = O(n); SC = O(1) (because of Q. constraint 2: "s consists of only lowercase English letters")

    ht = {}  # key = character, value = 1 if character is non-repeating else 0
    for c in s:
        if c in ht:
            ht[c] = 0
        else:
            ht[c] = 1
    print(ht)  # debug

    for c in s:
        if ht[c]:
            return s.index(c)
    return -1
