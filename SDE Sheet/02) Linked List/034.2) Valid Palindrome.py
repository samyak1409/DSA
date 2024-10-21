"""
https://leetcode.com/problems/valid-palindrome
"""


def is_palindrome(s: str) -> bool:
    """"""

    # 1) Time-Optimal (Filter, then Match using Two Pointers): TC = O(n); SC = O(n)
    # -> Two Pass

    """
    s = [c.lower() for c in s if c.isalnum()]

    for i in range(len(s)//2):
        if s[i] != s[~i]:  # ~i = -i-1 (bit magic)
        # https://en.wikipedia.org/wiki/Bitwise_operation#NOT; https://wiki.python.org/moin/BitwiseOperators
            return False
    return True
    """

    # 2) Optimal (OTG Match (or Skip) using Two Pointers): TC = O(n); SC = O(1)
    # -> One Pass

    """
    lt, rt = 0, len(s)-1
    while lt < rt:
        c1, c2 = s[lt], s[rt]
        al_num1, al_num2 = c1.isalnum(), c2.isalnum()
        if al_num1 and al_num2:  # if both chars are alphanumeric
            if c1.lower() == c2.lower():  # match
                lt, rt = lt+1, rt-1
            else:  # chars unmatched
                return False
        else:  # skip non-alphanumeric char(s)
            if not al_num1:
                lt += 1
            if not al_num2:
                rt -= 1
    return True
    """
    # Conciser:
    lt, rt = 0, len(s)-1
    while lt < rt:
        c1, c2 = s[lt], s[rt]
        # skip non-alphanumeric char(s):
        if not c1.isalnum():
            lt += 1
        elif not c2.isalnum():
            rt -= 1
        elif c1.lower() == c2.lower():  # if no chars were non-alphanumeric, match
            lt, rt = lt+1, rt-1
        else:  # chars unmatched
            return False
    return True

    # How to define `isalnum`?
    # def isalnum(c: chr) -> bool: return ('A' <= c <= 'Z') or ('a' <= c <= 'z') or ('0' <= c <= '9')
    # https://en.wikipedia.org/wiki/ASCII#Printable_characters
