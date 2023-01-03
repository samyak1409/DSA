"""
https://leetcode.com/problems/count-the-digits-that-divide-a-number
"""


def count_digits(num: int) -> int:
    """"""

    # 1) Brute-force = Optimal: O(1); SC = O(1)
    # https://leetcode.com/problems/count-the-digits-that-divide-a-number/solutions/2977336/two-approaches

    # 1.1)
    # Use mod by 10 to retrieve the least significant digit of the number.
    # Divide the number by 10, then round it down so that the second least significant digit becomes the least
    # significant digit of the number.
    # Use your language’s mod operator to see if a number is a divisor of another.

    # 1.2)
    # Or just convert the number to string.
    # Use your language’s mod operator to see if a number is a divisor of another.

    """
    ans = 0
    for d in str(num):
        ans += num % int(d) == 0
    return ans
    """
    # Using list comprehension:
    return sum(num % int(d) == 0 for d in str(num))
