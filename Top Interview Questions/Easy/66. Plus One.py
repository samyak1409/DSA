"""
https://leetcode.com/problems/plus-one/
"""


from typing import List


def plusOne(digits: List[int]) -> List[int]:

    # Method 1 (Pythonic): TC = O(n); SC = O(1)

    for i in str(int(''.join(map(str, digits)))+1):
        yield int(i)

    # Method 2 (Generic): TC = O(n); SC = O(1)

    """
    i = len(digits) - 1  # (reverse traversal)

    while i >= 0:  # O(n)

        if digits[i] != 9:  # addition without carry
            digits[i] += 1
            break

        else:  # addition with carry
            digits[i] = 0
            i -= 1
            if i == -1:  # no more MSBs
                digits.insert(0, 1)  # O(1) cause this case will only occur one time

    return digits
    """
