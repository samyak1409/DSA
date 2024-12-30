"""
https://leetcode.com/problems/check-if-the-number-is-fascinating
"""


def is_fascinating(n: int) -> bool:
    """"""

    # 1) Optimal: TC = O(1); SC = O(1) {since "n consists of exactly 3 digits"}

    # 1.1) Using sorting: TC = O(d*log2(d)); SC = O(d) {d: no. of digits in n}
    """
    return ''.join(sorted(f'{n}{2*n}{3*n}')) == '123456789'
    """

    # 1.2) Using hashing: TC = O(d); SC = O(d) {d: no. of digits in n}
    s = f'{n}{2*n}{3*n}'
    hs = set(s)
    return '0' not in hs and len(s) == len(hs) == 9
