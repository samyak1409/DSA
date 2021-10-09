"""
https://leetcode.com/problems/longest-common-prefix/
"""


from typing import List


def longestCommonPrefix(strs: List[str]) -> str:

    # TC = O(mn); SC = O(n); where n = no. of strings in strs and m = length of the smallest string

    lcp = ''

    for tup in zip(*strs):  # * -> unpacking; TC = O(m), this loop will run m times

        # tup will occupy n space every iteration, so SC = O(n)

        if len(set(tup)) == 1:  # => all chars same; TC = O(n), set construction
            lcp += tup[0]

        else:
            break

    return lcp
