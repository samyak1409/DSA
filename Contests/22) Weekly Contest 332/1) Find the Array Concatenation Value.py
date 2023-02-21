"""
https://leetcode.com/problems/find-the-array-concatenation-value
"""


def get_array_concat_val(nums: list[int]) -> int:
    """"""

    # Consider simulating the process to calculate the answer
    # Iterate until the array becomes empty. In each iteration, concatenate the first element to the last element and
    # add their concatenation value to the answer.
    # Don’t forget to handle cases when one element is left in the end, not two elements.

    # 1) Optimal (Two Pointers + String Conversion): TC = O(n); SC = O(1)

    """
    val = 0
    i, j = 0, len(nums)-1

    while i < j:
        # Pick from left and right:
        # val += int(str(nums[i])+str(nums[j]))  # O(1) since "1 <= nums[i] <= 10^4"
        val += int(f'{nums[i]}{nums[j]}')
        i, j = i+1, j-1

    # If an element is left:
    if i == j:
        val += nums[i]  # or nums[j]

    return val
    """

    # 1.1) Avoiding String Conversion using Maths:
    # https://leetcode.com/problems/find-the-array-concatenation-value/solutions/3174246/pow-and-log

    from math import log10

    val = 0
    i, j = 0, len(nums)-1

    while i < j:
        # Pick from left and right:
        val += nums[i] * (10 ** (int(log10(nums[j]))+1)) + nums[j]
        # `int(log10(nums[j]))+1`: no. of digits in `nums[j]`
        i, j = i+1, j-1

    # If an element is left:
    if i == j:
        val += nums[i]  # or nums[j]

    return val
