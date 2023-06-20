"""
https://leetcode.com/problems/add-strings
"""


def add_strings(num1: str, num2: str) -> str:
    """"""

    # All the solutions are (modifications of the solutions) from
    # https://github.com/samyak1409/DSA/blob/main/SDE%20Sheet/02%29%20Linked%20List/029.2%29%20Add%20Binary.py.

    # -1) Not Allowed (Type Casting): TC = O(m+n) {len(a)+len(b)}; SC = O(1)

    """
    return str(int(num1) + int(num2))  # str to int, add ints, int to str
    """

    # 1) Optimal (Reverse Traverse and Add): TC = O(max(m, n)); SC = O(max(m, n))
    # https://leetcode.com/problems/add-strings/discuss/90436/Straightforward-Java-8-main-lines-25ms

    bigger_len = max(len(num1), len(num2))

    # Making the strings of same length by adding 0s on the left of the smaller binary string (if any):
    num1, num2 = num1.zfill(bigger_len), num2.zfill(bigger_len)
    # Can also be done without this, by using the same paradigm we used in
    # https://github.com/samyak1409/DSA/blob/main/SDE%20Sheet/02%29%20Linked%20List/029%29%20Add%20Two%20Numbers.py,
    # but this is easier.

    # Reverse Traverse and Add:
    output = []  # using a list because str is immutable, so appending to str will be O(n) again & again instead of O(1)
    carry = 0
    for i in range(-1, -bigger_len-1, -1):  # from LSB to MSB
        num1_int, num2_int = ord(num1[i])-48, ord(num2[i])-48  # ord('0') = 48 so ord('0')-48 = 0 ... ord('9')-48 = 9
        carry, sum_ = divmod(num1_int+num2_int+carry, 10)  # x//y, x%y
        output.append(chr(sum_+48))  # chr(48) = '0', so chr(0+48) = '0' ... chr(9+48) = '9'
    if carry:  # from the MSB
        output.append(chr(carry+48))  # chr(48) = '0', so chr(0+48) = '0' ... chr(9+48) = '9'

    return ''.join(output[::-1])
