"""
https://leetcode.com/problems/valid-anagram/
"""


def isAnagram(s: str, t: str) -> bool:

    # 0) Minor Optimization for every method:

    if len(s) != len(t):  # O(1)
        return False

    # 1) Naive (Using Sorting): TC = O(n log n); SC = O(n)

    """
    return sorted(s) == sorted(t)
    """

    # 1.1) Better: Average Case: TC = O(n); SC = O(1); Worst Case: TC = O(n log n); SC = O(n) (e.g. when s = "abc", t = "bbb")

    """
    return sum(map(ord, s)) == sum(map(ord, t)) and sorted(s) == sorted(t)
    """

    # 3) https://leetcode.com/problems/valid-anagram/discuss/66484/Accepted-Java-O(n)-solution-in-5-lines: TC = O(n); SC = O(1)

    # Note- Q. constraint 2: "s and t consist of lowercase English letters"

    """
    arr = [0] * 26
    for c in s:
        arr[ord(c)-97] += 1
    for c in t:
        arr[ord(c)-97] -= 1
    return arr == [0] * 26
    """

    # 2) Using Hash Table: TC = O(n); SC = O(1) (because of Q. constraint 2: "s and t consist of lowercase English letters")

    """
    ht1 = {}
    for char in s:
        ht1[char] = ht1.get(char, 0) + 1
    ht2 = {}
    for char in t:
        ht2[char] = ht2.get(char, 0) + 1
    return ht1 == ht2
    """

    from collections import Counter
    return Counter(s) == Counter(t)
