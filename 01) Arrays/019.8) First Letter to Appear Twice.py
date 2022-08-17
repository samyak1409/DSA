"""
https://leetcode.com/problems/first-letter-to-appear-twice
"""


def repeated_character(s: str) -> str:
    """"""

    # Optimal (HashSet): TC = O(n); SC = O(1) {"s consists of lowercase English letters."}

    appeared = set()
    # Iterate through the string from left to right. Keep track of the elements you have already seen in a set.
    for c in s:
        # If the current element is already in the set, return that element.
        if c in appeared:
            return c
        appeared.add(c)
