"""
https://leetcode.com/problems/add-binary
"""


def add_binary(a: str, b: str) -> str:
    """"""

    # -1) Prohibited (Type Casting): TC = O(m+n) {len(a)+len(b)}; SC = O(1)
    # https://www.geeksforgeeks.org/python-program-to-add-two-binary-numbers

    """
    return bin(int(a, 2) + int(b, 2))[2:]  # bin to int, add ints, int to bin
    """

    # 1) Optimal (Reverse Traverse and Add): TC = O(max(m, n)); SC = O(max(m, n))
    # https://www.geeksforgeeks.org/program-to-add-two-binary-strings
    # https://leetcode.com/problems/add-binary/discuss/1679423/Well-Detailed-Explaination-Java-C%2B%2B-Python-oror-Easy-for-mind-to-Accept-it

    bigger_len = max(len(a), len(b))
    # Making the binary strings of same length by adding 0s on the left of the smaller binary string (if any):
    a, b = a.zfill(bigger_len), b.zfill(bigger_len)
    # Can also be done without this, by using the same paradigm we used in:
    # https://github.com/samyak1409/DSA/blob/main/02%29%20Linked%20List/029%29%20Add%20Two%20Numbers.py
    # Reverse Traverse and Add:
    char = {0: '0', 1: '1'}  # dict for type casting without using builtins
    output = []  # using a list because str is immutable, so appending to str will be O(n) again & again instead of O(1)
    carry = 0
    for i in range(-1, -bigger_len-1, -1):  # from LSB to MSB
        carry, sum_ = divmod((a[i], b[i], char[carry]).count('1'), 2)  # x//y, x%y
        output.append(char[sum_])
    if carry:  # from the MSB
        output.append(char[carry])
    return ''.join(output[::-1])
