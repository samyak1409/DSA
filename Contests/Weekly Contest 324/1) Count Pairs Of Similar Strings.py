"""
https://leetcode.com/problems/count-pairs-of-similar-strings
"""


def similar_pairs(words: list[str]) -> int:
    """"""

    count = {}
    ans = 0
    for word in words:
        word_ = tuple(sorted(set(x for x in word)))
        ans += count.get(word_, 0)
        count[word_] = count.get(word_, 0) + 1
    return ans
