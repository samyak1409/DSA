"""
https://leetcode.com/problems/plus-one/
"""


from typing import List


def plusOne(digits: List[int]) -> List[int]:

    # Method 1 (Pythonic):

    # return list(map(int, str(int(''.join(map(str, digits)))+1)))

    # Method 2 (Generic):

    i = len(digits) - 1  # (reverse traversal)

    while i >= 0:

        if digits[i] != 9:  # addition without carry
            digits[i] += 1
            break

        else:  # addition with carry
            digits[i] = 0
            i -= 1
            if i == -1:  # no more MSBs
                digits.insert(0, 1)

    return digits
