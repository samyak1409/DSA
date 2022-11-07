"""
https://leetcode.com/problems/apply-operations-to-an-array
"""


def apply_operations(nums: list[int]) -> list[int]:
    """"""

    # 1) Optimal (OTG Yield Non-Zero Vals & Yield Zeroes in the End): TC = O(n); SC = O(1)

    """
    n = len(nums)
    non_zeroes = 0

    # Go through all till last-1:
    for i in range(n-1):
        if (num := nums[i]) == nums[i+1]:  # `If nums[i] == nums[i+1]`
            if num:  # (only if num != 0)
                yield num*2  # `multiply nums[i] by 2`
                nums[i+1] = 0  # `set nums[i+1] to 0`
                non_zeroes += 1
        else:
            if num:  # (only if num != 0)
                yield num
                non_zeroes += 1
    # Last one:
    if num := nums[-1]:  # (only if num != 0)
        yield num
        non_zeroes += 1

    # Remaining Zeroes:
    for _ in range(n-non_zeroes):
        yield 0
    """

    # Shortened:

    n = len(nums)
    non_zeroes = 0

    for i in range(n):
        if num := nums[i]:  # (only if num != 0)
            # `Apply Operations`:
            try:
                if num == nums[i+1]:  # `If nums[i] == nums[i+1]`
                    num *= 2  # `multiply nums[i] by 2`
                    nums[i+1] = 0  # `set nums[i+1] to 0`
            except IndexError:  # for last i, `nums[i+1]` will raise IndexError
                pass  # (we don't have to apply any op for the last num)
            yield num
            non_zeroes += 1

    # Remaining Zeroes:
    for _ in range(n-non_zeroes):
        yield 0
