"""
https://leetcode.com/problems/valid-palindrome/
"""


def isPalindrome(s: str) -> bool:

    s = ''.join(filter(lambda char: (65 <= ord(char) <= 90) or (48 <= ord(char) <= 57), s.upper()))

    # Method 1 (char by char matching): TC = O(n); SC = O(1)

    """
    for i in range(len(s)//2):

        if s[i] != s[-i-1]:
            return False

    return True
    """

    # Method 2 (direct equating): TC = O(n); SC = O(n)

    half = len(s) // 2
    return s[:half] == s[-1:-half-1:-1]  # reversed
