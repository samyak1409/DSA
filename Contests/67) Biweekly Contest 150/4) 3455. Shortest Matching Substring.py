"""
https://leetcode.com/problems/shortest-matching-substring
"""


def shortest_matching_substring(s: str, p: str) -> int:
    """"""

    # [WA]:
    # Input
    # s = 'madlogic'
    # p = '*adlogi*'
    # Output
    # 7
    # Expected
    # 6

    """
    from re import finditer

    p = p.replace('*', '.*?')  # `X*`: X, zero or more times
    # `?`: Reluctant quantifier (match as less as possible)
    # print(p)  # debug

    ans = float('inf')
    for m in finditer(p, s):
        ans = min(ans, len(m.group()))

    return ans if ans != float('inf') else -1
    """

    # [TLE]:
    # O(n^2)

    from re import finditer

    p = p.replace('*', '.*?')  # `X*`: X, zero or more times
    # `?`: Reluctant quantifier (match as less as possible)
    # print(p)  # debug

    ans = float('inf')
    for i in range(len(s)-(len(p)-6)+1):
        for m in finditer(p, s[i:]):
            ans = min(ans, len(m.group()))

    return ans if ans != float('inf') else -1
