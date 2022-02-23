"""
https://leetcode.com/problems/valid-palindrome/
"""


def isPalindrome(s: str) -> bool:

    # 0) Helper func for all the algos:

    def is_alphanumeric(c: chr) -> bool:
        return ('a' <= c <= 'z') or ('0' <= c <= '9')  # https://en.wikipedia.org/wiki/ASCII#Printable_characters

    # 1) OTG Char By Char Matching: TC = O(n); SC = O(1)

    """
    l, r = 0, len(s)-1

    while l < r:

        x, y = s[l].lower(), s[r].lower()
        x_, y_ = is_alphanumeric(x), is_alphanumeric(y)

        if x_ and y_:  # if both chars are alphanumeric
            if x == y:  # equate
                l += 1
                r -= 1
            else:
                return False

        # skip char if not alphanumeric:
        if not x_:
            l += 1
        if not y_:
            r -= 1

    return True
    """

    # 2) Direct Equating: TC = O(n); SC = O(n)

    """
    s = ''.join(filter(is_alphanumeric, s.lower()))
    half = len(s) // 2
    return s[:half] == s[::-1][:half]
    # or simply:
    # return s == s[::-1]  # (O(n/2) = O(n))
    """

    # 3) Char By Char Matching: TC = O(n); SC = O(1)

    s = ''.join(filter(is_alphanumeric, s.lower()))

    for i in range(len(s)//2):

        if s[i] != s[-i-1]:
            return False

    return True
