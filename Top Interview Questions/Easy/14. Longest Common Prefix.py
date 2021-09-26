"""
https://leetcode.com/problems/longest-common-prefix/
"""


from typing import List


def longestCommonPrefix(strs: List[str]) -> str:

    lcp = ''

    for tup in zip(*strs):

        if len(set(tup)) == 1:  # => all chars same
            lcp += tup[0]

        else:
            break

    return lcp
