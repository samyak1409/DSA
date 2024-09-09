"""
https://leetcode.com/problems/plus-one
"""


def plus_one(digits: list[int]) -> list[int]:
    """"""

    # -1) Not Allowed (Type Cast to int): TC = O(n); SC = O(1)
    # Since there is no limit on the size of `int` in Python, we can just type cast our "large int represented as an int
    # array" to `int`.

    """
    plus_one = int(''.join(map(str, digits))) + 1
    # return list(map(int, str(plus_one)))
    # or:
    yield from map(int, str(plus_one))
    """

    # 1) Time-Optimal (HashSet & Reverse Iterate, Two-Pass): TC = O(n); SC = O(n)
    # We only need to insert a digit (`1`) to the array (at the beginning) if and only if ALL the digits are `9`.
    # If not, plus one would take the least significant non-9 digit, and we can return.

    """
    from itertools import repeat
    
    # Check if all are 9:
    if set(digits) == {9}:  # TC = SC = O(n)
        # If all are 9, we know the plus one would be 1 followed by 0 `len(digits)` times.
        # Inserting an element at index 0 in array costs O(n), instead we can just change the 0th index element, and
        # append a new element.
        digits[0] = 1
        # Changing all other (`digits[1:]`) 9s to 0s:
        # Using basic loop:
        # for i in range(1, len(digits)):
        #     digits[i] = 0
        # OR slice assignment:
        # digits[1:] = [0] * (len(digits)-1)
        # OR itertools.repeat:
        digits[1:] = repeat(0, len(digits)-1)  # O(n)
        digits.append(0)
    # Else we just need to handle carry (if LSB == 9):
    else:
        # Reverse iterate:
        for i in range(-1, -len(digits)-1, -1):  # O(n)
            # If current digit != 9, we can just plus one and break out:
            if digits[i] != 9:
                digits[i] += 1
                break
            # Else we need to make current digit (i.e. 9) as 0, and continue the loop:
            digits[i] = 0
    return digits
    """

    # 2) Optimal (Reverse Iterate, One-Pass): TC = O(n); SC = O(1)
    # Actually, we don't need to explicitly check if all the digits are 9s.
    # This is the solution in https://leetcode.com/problems/plus-one/solutions/24082/my-simple-java-solution, but
    # better.

    # Reverse iterate:
    for i in range(-1, -len(digits)-1, -1):  # O(n)
        # If current digit != 9, we can just plus one and return:
        if digits[i] != 9:
            digits[i] += 1
            return digits
        # Else we need to make current digit (i.e. 9) as 0, and continue the loop:
        digits[i] = 0
    # And if we get out of loop without returning would imply that all the digits were 9s, and we're still left with a
    # carry, so:
    # Make the first digit (which was 0 from above loop) to 1:
    digits[0] = 1
    # And append a 0:
    digits.append(0)
    return digits
