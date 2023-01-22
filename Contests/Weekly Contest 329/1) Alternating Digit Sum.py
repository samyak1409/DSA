"""
https://leetcode.com/problems/alternating-digit-sum
"""


def alternate_digit_sum(n: int) -> int:
    """"""

    # The first step is to loop over the digits. We can convert the integer into a string, an array of digits, or just
    # loop over its digits.
    # Keep a variable sign that initially equals 1 and a variable answer that initially equals 0.
    # Each time you loop over a digit i, add sign * i to answer, then multiply sign by -1.

    # 1) Time Optimal (Convert to str and traverse): TC = O(log10(n)); SC = O(log10(n))

    """
    digits = str(n)
    sum_ = 0

    for i, d in enumerate(digits):
        '''
        if i % 2 == 0:
            sum_ += int(d)
        else:
            sum_ -= int(d)
        '''
        # One liner:
        sum_ += -int(d) if i % 2 else int(d)

    return sum_
    """

    # 2) Optimal (Get LSB one by one (by going right to left, not left to right)): TC = O(log10(n)); SC = O(1)
    # There is no way to get MSB in O(1).
    # (https://stackoverflow.com/questions/33947632/get-most-significant-digit-in-python)
    # But we can get LSB in O(1).
    # https://leetcode.com/problems/alternating-digit-sum/solutions/3083888/right-to-left

    sum_ = 0
    sign = 1

    while n:
        sum_ += (n % 10) * sign
        n //= 10
        sign *= -1

    return sum_ * -sign
    # digit: 1 2 3
    # sign:  + - +
    # if no. of digits is odd, no problem
    # digit: 1 2 3 4
    # sign:  - + - +
    # so as we can see, going right to left, we started from +, we ended with -, but we had to start from + (when going
    # left to right), so fixing this by multiplying `sum_` with the `-sign` again!
