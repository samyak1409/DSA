"""
https://leetcode.com/problems/remove-trailing-zeros-from-a-string
"""


def remove_trailing_zeros(num: str) -> str:
    """"""

    # 0) Brute-force (Trim and Re-assign while 0 in end): TC = O(n^2); SC = O(n)

    """
    while num[-1] == '0':  # O(n^2)
        num = num[:-1]  # O(n)
    return num
    """

    # 1.1) Optimal (Convert to List, Pop while 0 in end, Convert back to Str): TC = O(n); SC = O(n)
    # The main problem in above was str is immutable so the TC was rising, so converting str to a list.

    """
    num = list(num)  # O(n)
    while num[-1] == '0':  # O(n)
        num.pop()  # O(1)
    return ''.join(num)  # O(n)
    """

    # Find the last non-zero digit in num.
    # 1.2) Optimal (Count the 0s we've in the end in once, and Trim in once): TC = O(n); SC = O(n)

    """
    for i in range(len(num)-1, -1, -1):  # O(n)
        if num[i] != '0':
            return num[:i+1]  # O(n)
    """

    # 1.3) Optimal (Using Builtin): TC = O(n); SC = O(n)
    # This is something we'd use in real-world.

    return num.rstrip('0')  # O(n)
