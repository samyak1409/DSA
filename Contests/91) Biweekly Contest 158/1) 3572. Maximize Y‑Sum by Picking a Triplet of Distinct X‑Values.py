"""
https://leetcode.com/problems/maximize-ysum-by-picking-a-triplet-of-distinct-xvalues
"""


def max_sum_distinct_triplet(x: list[int], y: list[int]) -> int:
    """"""

    # 1) Suboptimal (HashMap, Sort): TC = O(n*log2(n)); SC = O(n)

    # HashMap from `x` to its largest `y`:
    hm = {}
    for k, v in zip(x, y):  # TC = SC = O(n)
        hm[k] = max(hm.get(k, 0), v)

    # If triplet exists, return sum of vals:
    if len(hm) >= 3:
        return sum(sorted(hm.values(), reverse=True)[:3])  # TC = O(n*log2(n)); SC = O(n)

    return -1

    # 2) Optimal (3 vars and iterate): TC = O(n); SC = O(1)
    # https://leetcode.com/problems/maximize-ysum-by-picking-a-triplet-of-distinct-xvalues/solutions/6820841/three-solutions-multiple-language-beats-100-o-n-time-o-1-space
