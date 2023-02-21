"""
https://leetcode.com/problems/maximum-value-of-a-string-in-an-array
"""


def maximum_value(strs: list[str]) -> int:
    """"""

    # 1) Optimal: TC = O(n); SC = O(1)
    # For strings comprising only of digits, convert them into integers. For strings comprising only of digits, convert
    # them into integers.
    # For all other strings, calculate their length.

    # 1.0) Try converting every str (EAFP):
    """
    ans = 0
    for s in strs:
        try:
            value = int(s)
        except ValueError:
            value = len(s)
        ans = max(ans, value)
    return ans
    """

    # 1.1) One liner using `str` method and list comprehension (not EAFP though):
    return max(int(s) if s.isdigit() else len(s) for s in strs)
