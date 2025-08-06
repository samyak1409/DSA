"""
https://leetcode.com/problems/maximum-product-of-two-digits
"""


def max_product(n: int) -> int:
    """"""

    # 1) Brute-force (Sort & Pick Top 2): TC = O(d*log(d)); SC = O(d) {d = no. of digits in `n` = log10(n)}

    """
    s = sorted(str(n))
    return int(s[-1]) * int(s[-2])
    """

    # 2) Optimal (For loop: Track Top 2): TC = O(d); SC = O(d) {d = no. of digits in `n` = log10(n)}

    """
    arr = [int(d) for d in str(n)]

    mx, idx = float('-inf'), -1
    for i, d in enumerate(arr):
        if d > mx:
            mx, idx = d, i

    mx2 = float('-inf')
    for i, d in enumerate(arr):
        if i != idx and d > mx2:
            mx2 = d

    return mx * mx2
    """

    # Single Loop:

    mx, mx2 = float('-inf'), float('-inf')

    for d in str(n):
        d = int(d)
        if d > mx:
            mx, mx2 = d, mx
        elif d > mx2:
            mx2 = d

    return mx * mx2

    # This is the absolute best solution for this problem, even if the constraints are increased. (In terms of time.)
    # (Space can still be reduced to O(1) in the Optimal approach if we use div-mod for getting the next digit instead
    # of converting to string.)
