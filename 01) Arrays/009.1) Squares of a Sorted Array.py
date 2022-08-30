"""
https://leetcode.com/problems/squares-of-a-sorted-array
"""


def sorted_squares(nums: list[int]) -> list[int]:
    """"""

    # 0) Brute-force (Sorting): TC = O(n*log(n)); SC = O(n)

    """
    yield from map(lambda x: x**2, sorted(nums, key=lambda x: abs(x)))
    """

    # Follow up: Squaring each element and sorting the new array is very trivial,
    # could you find an O(n) solution using a different approach?

    # 1) Time-Optimal (Two Pointers & Traversal from Ends to Mid): TC = O(n); SC = O(n)
    # Like:
    # https://github.com/samyak1409/DSA/blob/7cbe5e00f474eb6a0aee5e0b58d66296a59604c3/01%29%20Arrays/009%29%20Merge%20Sorted%20Array.py#L32
    # https://leetcode.com/problems/squares-of-a-sorted-array/discuss/495394/C%2B%2B%3A-Simplest-one-pass-two-pointers

    """
    n = len(nums)
    arr = []  # to store the results, we can't yield directly because we're generating the results in opposite order
    lo, hi = 0, n-1
    while lo <= hi:
        num1, num2 = nums[lo], nums[hi]
        if abs(num1) >= abs(num2):
            arr.append(num1 ** 2)
            lo += 1
        else:
            arr.append(num2 ** 2)
            hi -= 1
    yield from arr[::-1]
    """

    # 2) Optimal (Two Pointers & Traversal from Mid to Ends): TC = O(n); SC = O(1)
    # Solves the problem of `1)`.

    # Finding the middle index:
    # mid = nums.index(min(nums, key=lambda x: abs(x)))
    min_val, mid = float('inf'), None
    for i, num in enumerate(map(lambda x: abs(x), nums)):
        if num < min_val:
            min_val = num
            mid = i
    yield nums[mid] ** 2

    # Traversing (from Mid to Ends) and Comparing:
    # https://github.com/samyak1409/DSA/blob/7cbe5e00f474eb6a0aee5e0b58d66296a59604c3/01%29%20Arrays/009%29%20Merge%20Sorted%20Array.py#L32
    n = len(nums)
    lo, hi = mid-1, mid+1
    while lo >= 0 and hi < n:
        num1, num2 = nums[lo], nums[hi]
        if abs(num1) <= abs(num2):
            yield num1 ** 2
            lo -= 1
        else:
            yield num2 ** 2
            hi += 1
    while lo >= 0:
        yield nums[lo] ** 2
        lo -= 1
    while hi < n:
        yield nums[hi] ** 2
        hi += 1
