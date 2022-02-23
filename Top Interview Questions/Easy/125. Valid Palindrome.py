"""
https://leetcode.com/problems/valid-palindrome/
"""


def isPalindrome(s: str) -> bool:

    # 1) Direct Equating: TC = O(n); SC = O(n)

    """
    s = ''.join(filter(lambda c: c.isalnum(), s.lower()))
    half = len(s) // 2
    return s[:half] == s[::-1][:half]
    # or simply:
    # return s == s[::-1]  # (O(n/2) = O(n))
    """

    # 2) Char By Char Matching: TC = O(n); SC = O(1)

    """
    s = ''.join(filter(lambda c: c.isalnum(), s.lower()))

    for i in range(len(s)//2):

        if s[i] != s[-i-1]:
            return False

    return True
    """

    # 3) OTG Char By Char Matching: TC = O(n); SC = O(1)

    l, r = 0, len(s)-1

    while l < r:

        if s[l].isalnum() and s[r].isalnum():  # if both chars are alphanumeric

            if s[l].lower() == s[r].lower():  # equate
                l += 1
                r -= 1
            else:
                return False

        # skip char if not alphanumeric:
        if not s[l].isalnum():
            l += 1
        if not s[r].isalnum():
            r -= 1

    return True

    # how to define "isalnum":
    # def isalnum(c: chr) -> bool: return ('a' <= c <= 'z') or ('0' <= c <= '9')  # https://en.wikipedia.org/wiki/ASCII#Printable_characters
