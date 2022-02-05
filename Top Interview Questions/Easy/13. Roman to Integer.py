"""
https://leetcode.com/problems/roman-to-integer/
"""


def romanToInt(s: str) -> int:

    # Method 1 (Standard): TC = O(n); SC = O(1)

    """
    value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    ans = 0
    i = 0

    while i < len(s):

        if i+1 < len(s) and value[s[i]] < value[s[i+1]]:  # for those six instances where subtraction is used
            ans += value[s[i+1]] - value[s[i]]
            i += 2

        else:
            ans += value[s[i]]
            i += 1

    return ans
    """

    # Method 2 (Easier to Understand): TC = O(n); SC = O(1)

    value = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900, 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    ans = 0
    i = 0

    while i < len(s):

        try:  # https://docs.python.org/3.5/glossary.html#term-eafp
            ans += value[s[i:i+2]]
            i += 2

        except KeyError:
            ans += value[s[i]]
            i += 1

    return ans

    # Method 3 (Hold Up): TC = O(n); SC = O(1)

    # https://leetcode.com/problems/roman-to-integer/discuss/264743/Clean-Python-beats-99.78.
