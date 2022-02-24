"""
https://leetcode.com/problems/longest-common-prefix/
"""


from typing import List


def longestCommonPrefix(strs: List[str]) -> str:

    # Best from https://leetcode.com/problems/longest-common-prefix/solution & https://leetcode.com/problems/longest-common-prefix/discuss:

    # Vertical Scanning (Pythonic): TC = O(mn); SC = O(n); where m = len(LCP) to be (<= len(min(strs, key=len))) and n = len(strs)

    lcp = ''

    for tup in zip(*strs):  # '*' -> unpacking; this loop will run m times, so TC = O(m)

        # tup will occupy n space on every iteration, so SC = O(n)

        if len(set(tup)) == 1:  # => all chars same; set construction, so TC = O(n)
            lcp += tup[0]

        else:
            break

    return lcp
