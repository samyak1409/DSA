"""
https://leetcode.com/problems/longest-substring-without-repeating-characters
"""


def length_of_longest_substring(s: str) -> int:
    """"""

    # 0) Brute-force (Nested Loop & HashSet): TC = O(n^2); SC = O(1) because Q. constraint
    #                                                      "s consists of English letters, digits, symbols and spaces."

    n = len(s)
    longest = 0
    for i in range(n):
        occurred = set()  # for O(1) lookup
        count = 0
        for j in range(i, n):
            char = s[j]
            if char not in occurred:
                count += 1
                occurred.add(char)
            else:  # when a char is repeated
                break  # start the loop with next starting
        longest = max(longest, count)
    return longest
