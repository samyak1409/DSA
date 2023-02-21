"""
https://leetcode.com/problems/palindrome-number
"""


def is_palindrome(x: int) -> bool:
    """"""

    # 0) Brute-force (Convert to Sequence): TC = O(log10(x)); SC = O(log10(x))
    # (https://docs.python.org/3/glossary.html#term-sequence)
    # The first idea that comes to mind is to convert the number into string, and check if the string is a
    # palindrome, but this would require extra non-constant space for creating the string which is not allowed by the
    # problem description.

    """
    # Optimization:
    if x < 0:  # "From left to right, it reads -121. From right to left, it becomes 121-. ∴ it is not a palindrome."
        return False

    # Convert the Integer to an Sequence for Processing:
    x_str = str(x)  # or extract digit one by one using `% 10` and append to list (mutable sequence)
    # Check Palindrome using Two Pointers:
    for i in range(len(x_str)//2):
        if x_str[i] != x_str[~i]:
            return False
    return True
    """

    # Follow up: Could you solve it without converting the integer to a string?
    # 1) Optimal (Reverse Whole Integer): TC = O(log10(x)); SC = O(1)
    # Second idea would be reverting the number itself, and then compare the number with original number, if
    # they are the same, then the number is a palindrome.
    # Author: "Beware of overflow when you reverse the integer."
    # Le Me with Python: https://c.tenor.com/fBvQV_5Lp6UAAAAC/we-dont-do-that-here-black-panther.gif

    # Optimization:
    if x < 0:  # "From left to right, it reads -121. From right to left, it becomes 121-. ∴ it is not a palindrome."
        return False

    # Get Reversed x:
    x_copy, x_rev = x, 0
    while x_copy:
        x_rev = (x_rev * 10) + (x_copy % 10)
        x_copy //= 10
    # Return Comparison:
    return x == x_rev

    # For Other Languages:
    # Following the thoughts based on the second idea, to avoid the overflow issue of the reverted number, what if we
    # only revert half of the `int` number? After all, the reverse of the last half of the palindrome should be the same
    # as the first half of the number, if the number is a palindrome.
    # https://leetcode.com/problems/palindrome-number/solution
    # https://leetcode.com/problems/palindrome-number/discuss/785314/Python-3-greater-1-solution-is-89.20-faster.-2nd-is-99.14-faster.-Explanation-added
    # BUT WAIT:
    # WE DON'T NEED TO CONCERN THE OVERFLOW. When the reversed number overflows, it will become negative number which
    # will return false when compared with x. Source:
    # https://leetcode.com/problems/palindrome-number/discuss/5127/9-line-accepted-Java-code-without-the-need-of-handling-overflow/5915
