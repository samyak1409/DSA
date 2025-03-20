"""
https://leetcode.com/problems/maximum-length-of-pair-chain
"""


def find_longest_chain(pairs: list[list[int]]) -> int:
    """"""

    # Same as:
    # https://github.com/samyak1409/DSA/blob/main/SDE%20Sheet/03%29%20Greedy%20Algorithm/043%29%20N%20Meetings%20in%20One%20Room.py

    # 1) Optimal (Greedy: Sort by "right" val): TC = O(n*log(n)); SC = O(n)
    # Why does greedy forms the longest chain? Because by sorting by "right" val, we're making sure that we pick the
    # pair which is ending earliest. So, we can chain the most pairs by doing that.

    ans = 0
    prev_rt = float('-inf')  # -inf so that any `lt` would be >
    for lt, rt in sorted(pairs, key=lambda pair: pair[1]):
        if lt > prev_rt:
            ans += 1  # this pair added to the chain
            prev_rt = rt  # update
    return ans
