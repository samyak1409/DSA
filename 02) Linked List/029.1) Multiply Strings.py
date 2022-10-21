"""
https://leetcode.com/problems/multiply-strings
"""


def multiply(num1: str, num2: str) -> str:
    """"""

    # -1) Not Allowed (Type Casting & Direct Multiplication): TC = O(m+n); SC = O(1)

    """
    return str(int(num1) * int(num2))
    """

    # 1) No Type Casting but Direct Multiplication: TC = O(m+n); SC = O(m+n)

    """
    # Helper Function:
    def to_int(num_str: str) -> int:
        num = 0
        for digit_chr in num_str:
            num = (num * 10) + ord(digit_chr) - 48  # ord('0') = 48 so ord('0')-48 = 0 ... ord('9')-48 = 9
        return num

    # Convert into Integer and Calc. the Product:
    product = to_int(num_str=num1) * to_int(num_str=num2)

    # Convert into String:
    output = []  # using a list because str is immutable, so appending to str will be O(n) again & again instead of O(1)
    while product:
        digit = product % 10  # digit at unit place
        output.append(chr(digit+48))  # chr(48) = '0', so chr(0+48) = '0' ... chr(9+48) = '9'
        product //= 10

    return ''.join(output[::-1]) or '0'  # `or '0'` -> handles the edge case (num1="0", num2="0")
    """

    # 2) No Type Casting & No Direct Multiplication: TC = O(m*n); SC = O(m+n)
    # 123 * 456 = 6*123 + 50*123 + 400*123

    # Convert into Integer and Calc. the Product:
    product = 0
    for i in range(len(num2)):
        digit1 = ord(num2[~i]) - 48  # ~i = -i-1 (bit magic); ord('0') = 48 so ord('0')-48 = 0 ... ord('9')-48 = 9
        # print(digit1)  #debugging
        sub_product = 0
        for j in range(len(num1)):
            digit2 = ord(num1[~j]) - 48  # ~j = -j-1 (bit magic); ord('0') = 48 so ord('0')-48 = 0 ... ord('9')-48 = 9
            # print(digit2)  #debugging
            sub_product += 10**j * digit2*digit1
        product += 10**i * sub_product

    # Convert into String:
    output = []  # using a list because str is immutable, so appending to str will be O(n) again & again instead of O(1)
    while product:
        digit = product % 10  # digit at unit place
        output.append(chr(digit+48))  # chr(48) = '0', so chr(0+48) = '0' ... chr(9+48) = '9'
        product //= 10

    return ''.join(output[::-1]) or '0'  # `or '0'` -> handles the edge case (num1="0", num2="0")

    # Also Read:
    # https://leetcode.com/problems/multiply-strings/solution
    # https://leetcode.com/problems/multiply-strings/discuss/17605/Easiest-JAVA-Solution-with-Graph-Explanation
