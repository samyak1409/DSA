"""
https://leetcode.com/problems/valid-anagram/
"""


def isAnagram(s: str, t: str) -> bool:

    # Minor Optimization for every method:

    if len(s) != len(t):  # O(1)
        return False

    # 1) Naive: TC = O(n log n); SC = O(n)

    # return sorted(s) == sorted(t)

    # 2) Better: Average Case: TC = O(n); SC = O(1); Worst Case: TC = O(n log n); SC = O(n) (e.g. when s = "abc", t = "bbb")

    """
    if sum(map(ord, s)) == sum(map(ord, t)):
        return sorted(s) == sorted(t)
    else:
        return False
    """

    # 3) Using Hash Table: TC = O(n); SC = O(1) (because of Q. constraint 2: "s and t consist of lowercase English letters")

    ht1 = {}
    for char in s:
        ht1[char] = ht1.get(char, 0) + 1
    ht2 = {}
    for char in t:
        ht2[char] = ht2.get(char, 0) + 1
    return ht1 == ht2
