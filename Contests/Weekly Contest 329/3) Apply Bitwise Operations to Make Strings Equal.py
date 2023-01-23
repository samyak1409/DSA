"""
https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal
"""


def make_strings_equal(s: str, target: str) -> bool:
    """"""

    # Think of when it is impossible to convert the string to the target.
    # If exactly one of the strings is having all 0’s, then it is impossible. And it is possible in all other cases. Why
    # is that true?

    # 1) Optimal (Observe possible inputs and outputs): TC = O(n); SC = O(1)
    # This question was all about solving through observation!!
    # https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/solutions/3083831/java-c-python-1-line-check-1
    # https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/solutions/3083931/java-python-3-analysis-results-short-codes
    # Best explanation: https://youtu.be/KJasELfxWqE

    #     i j  OR  XOR
    # a)  0 0   0   0
    # b)  0 1   1   1
    # c)  1 0   1   1
    # d)  1 1   1   0
    #
    # Note that case c and d are basically the same because i and j can be used interchangeably!

    # If s has all zeroes, they can't be changed!
    if '1' not in s:
        return s == target

    # If we reach here => '1' in s.
    # If '1' in s, but target has all zeroes => we can't change those 1s to 0s.
    if '1' not in target:
        return False

    # If these are not the cases, then s can always be changed to t using some no. of steps!
    return True
