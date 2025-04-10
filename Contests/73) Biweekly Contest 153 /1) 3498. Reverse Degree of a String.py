"""
https://leetcode.com/problems/reverse-degree-of-a-string
"""


def reverse_degree(s: str) -> int:
    """"""

    # 1) Optimal (Simulate: Loop): TC = O(n); SC = O(1)

    ans = 0
    for i, c in enumerate(s, start=1):
        ans += (26-(ord(c)-ord('a'))) * i
    return ans
