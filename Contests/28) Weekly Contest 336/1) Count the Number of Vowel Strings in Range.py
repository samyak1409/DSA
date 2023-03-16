"""
https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range
"""


def vowel_strings(words: list[str], left: int, right: int) -> int:
    """"""

    # Consider iterating over all strings from left to right and use an if condition to check if the first character and
    # last character are vowels.

    # 1) Optimal (Loop): TC = O(n); SC = O(1)

    count = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for i in range(left, right+1):
        word = words[i]
        if word[0] in vowels and word[-1] in vowels:
            count += 1
    return count
