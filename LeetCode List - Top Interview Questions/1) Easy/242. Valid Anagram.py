"""
https://leetcode.com/problems/valid-anagram
"""


def is_anagram(s: str, t: str) -> bool:
    """"""

    # 0) Brute-force (Sort): TC = O(n*log(n)); SC = O(n)

    """
    # Small optimization:
    if len(s) != len(t):  # O(1)
        return False

    return sorted(s) == sorted(t)
    """

    # 0.1) Optimized Brute-force (Checking ord sum before Sort):
    # Avg. Case: TC = O(n); SC = O(1)
    # Worst Case: TC = O(n*log(n)); SC = O(n) (e.g. s = "abc", t = "bbb")

    """
    if len(s) != len(t):  # O(1)
        return False

    # Added optimization on `0)`:
    return sum(map(ord, s)) == sum(map(ord, t)) and sorted(s) == sorted(t)
    """

    # 1) Optimal (HashMap): TC = O(n); SC = O(26) ("s and t consist of lowercase English letters")

    """
    if len(s) != len(t):  # O(1)
        return False

    hm1 = {}
    for char in s:
        hm1[char] = hm1.get(char, 0) + 1
    hm2 = {}
    for char in t:
        hm2[char] = hm2.get(char, 0) + 1
    return hm1 == hm2
    """
    # Pythonic:
    """
    from collections import Counter

    if len(s) != len(t):  # O(1)
        return False

    return Counter(s) == Counter(t)
    """

    # 1.1) Better: Array as HashMap:

    if len(s) != len(t):  # O(1)
        return False

    arr = [0] * 26
    for c in s:
        arr[ord(c)-97] += 1
    for c in t:
        arr[ord(c)-97] -= 1
    return arr == [0] * 26
