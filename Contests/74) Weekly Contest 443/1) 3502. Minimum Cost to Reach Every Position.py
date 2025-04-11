"""
https://leetcode.com/problems/minimum-cost-to-reach-every-position
"""


from itertools import accumulate


def min_costs(cost: list[int]) -> list[int]:
    """"""

    # 1) Optimal (Prefix Arr): TC = O(n); SC = O(1)
    # Read the description and do not see the examples, it'd sound like a LC medium.

    """
    ans = [float('inf')]
    for c in cost:
        ans.append(min(ans[-1], c))
    return ans[1:]
    """

    # One-liner:

    return list(accumulate(iterable=cost, func=min))
