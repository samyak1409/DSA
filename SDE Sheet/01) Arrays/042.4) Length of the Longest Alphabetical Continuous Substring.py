"""
https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring
"""


def longest_continuous_substring(s: str) -> int:
    """"""

    # What is the longest possible continuous substring?
    # The size of the longest possible continuous substring is at most 26, so we can just brute force the answer.
    # 1) Brute-force = Optimal (Nested Loop to check for every char, taking every char as start one by one):
    # TC = O(26n) = O(n); SC = O(1)

    # 1.1) Optimal (Sliding Window): TC = O(n); SC = O(1)

    current = longest = 1  # init
    for i in range(1, len(s)):
        if ord(s[i]) == ord(s[i-1])+1:  # if consecutive letters
            current += 1  # ++
            if current == 26:  # optional optimization (as the longest possible continuous substring is at most 26)
                return current
            longest = max(longest, current)  # update
        else:
            current = 1  # reset
    return longest
