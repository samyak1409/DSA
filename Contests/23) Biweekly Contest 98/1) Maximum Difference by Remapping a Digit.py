"""
https://leetcode.com/problems/maximum-difference-by-remapping-a-digit
"""


def min_max_difference(num: int) -> int:
    """"""

    # 1) Optimal (Try replacing each digit one by one to 9 to get Max, and 0 to get Min):
    # TC = O(10 * log10(n)) = O(log10(n)); SC = O(log10(n))
    # "remap one of the 10 possible digits (0 to 9) to another digit"
    # So, we'll get the MAX num by remapping one of the digit to 9,
    # and we'll get the MIN num by remapping one of the digit to 0.

    """
    # Convert int num to str num in order to replace digits easily:
    num = str(num)  # TC = SC = O(log10(n))
    # Make a set of digits (i.e. unique) to traverse on:
    digits = set(num)  # TC = SC = O(10)

    # One by one replace each digit with 9 & 0 to get the max & min num respectively, and return the diff:
    return max(int(num.replace(d, '9')) for d in digits) - min(int(num.replace(d, '0')) for d in digits)
    # TC = O(10 * log10(n)); SC = O(log10(n))
    """

    # 2) Optimal (Greedy): TC = O(log10(n)); SC = O(log10(n))
    # Remap the first non-nine digit to 9 to obtain the maximum number.
    # Remap the first non-zero digit to 0 to obtain the minimum number.

    # Convert int num to str num in order to replace digits easily:
    num = str(num)  # TC = SC = O(log10(n))

    # Find the first non-nine digit:
    i = 0
    while num[i] == '9':  # TC = O(log10(n)); SC = O(1)
        i += 1
        if i == len(num):  # if num consists only of 9s, ans = num only
            return int(num)

    # Replace and return the diff:
    return int(num.replace(num[i], '9')) - int(num.replace(num[0], '0'))  # TC = SC = O(log10(n))
