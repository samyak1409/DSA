"""
https://leetcode.com/problems/valid-anagram/
"""


def isAnagram(s: str, t: str) -> bool:

    # Minor Optimization for every method:

    if len(s) != len(t):  # O(1)
        return False

    # 1) Naive: TC = O(n log n); SC = O(n)

    # return sorted(s) == sorted(t)

    # 3) Using HashMap: TC = O(n); SC = O(n)

    """
    hashmap1 = {}
    for char in s:
        hashmap1[char] = hashmap1.get(char, 0) + 1
    hashmap2 = {}
    for char in t:
        hashmap2[char] = hashmap2.get(char, 0) + 1
    return hashmap1 == hashmap2
    """

    # 2) Better: Average Case: TC = O(n); SC = O(1); Worst Case: TC = O(n log n); SC = O(n) (e.g. when s = "abc", t = "bbb")

    if sum(map(ord, s)) == sum(map(ord, t)):
        return sorted(s) == sorted(t)
    else:
        return False
