"""
https://leetcode.com/problems/longest-common-prefix
"""


def longest_common_prefix(strs: list[str]) -> str:
    """"""

    # 1) Optimal (2 Loops): TC = O(mn); SC = O(1) {m = len(LCP) to be (<= len(min(strs, key=len))), n = len(strs)}

    """
    lcp = []  # list instead of str for mutability
    i = 0  # index of char one by one
    while True:
        hs = set()  # to save only uniques
        try:  # if index error occurs, means we've traversed the shortest str, so time to stop
            for string in strs:
                hs.add(string[i])
        except IndexError:
            break
        if len(hs) == 1:  # if all the chars were same
            lcp.append(hs.pop())
            i += 1  # now next char
        else:
            break
    return ''.join(lcp)
    """

    # 1.1) Time-optimal (Using zip and unpacking):
    # TC = O(mn); SC = O(1) {m = len(LCP) to be (<= len(min(strs, key=len))), n = len(strs)}
    # This method is a trade-off between space complexity and code complexity.

    lcp = []  # list instead of str for mutability
    for char_tup in zip(*strs):  # loop on char tuples; TC = O(m); SC = O(n)
        if len(set(char_tup)) == 1:  # if all chars same; TC = O(n)
            lcp.append(char_tup[0])
        else:
            break
    return ''.join(lcp)
