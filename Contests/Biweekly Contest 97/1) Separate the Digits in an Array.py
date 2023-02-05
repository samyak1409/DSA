"""
https://leetcode.com/problems/separate-the-digits-in-an-array
"""


def separate_digits(nums: list[int]) -> list[int]:
    """"""

    # You can convert the integer into a string to do that easily.

    # 1) Optimal (Traverse nums and: `str` + `map` + `yield`): TC = O(no. of digits in `nums`); SC = O(1)

    for num in nums:
        yield from map(int, str(num))
