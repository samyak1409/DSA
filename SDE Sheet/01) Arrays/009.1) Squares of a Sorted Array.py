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

    # 1) Time-Optimal (Two Pointers Traversing from Ends to Mid): TC = O(n); SC = O(n)
    # Like: https://github.com/samyak1409/DSA/blob/main/SDE%20Sheet/01%29%20Arrays/009%29%20Merge%20Sorted%20Array.py
    # https://leetcode.com/problems/squares-of-a-sorted-array/discuss/495394/C++:-Simplest-one-pass-two-pointers

    """
    n = len(nums)
    arr = []  # to store the results, we can't yield directly because results will be generated in reverse
    lo, hi = 0, n-1
    while lo <= hi:
        if abs(num1 := nums[lo]) >= abs(num2 := nums[hi]):
            arr.append(num1 ** 2)
            lo += 1
        else:
            arr.append(num2 ** 2)
            hi -= 1
    yield from arr[::-1]
    """

    # 2) Optimal (Two Pointers Traversing from Mid to Ends): TC = O(n); SC = O(1)
    # Solves the problem of `1)`.

    # Finding the middle index:
    min_val, mid = float('inf'), None
    for i, num in enumerate(nums):
        if (num := abs(num)) < min_val:
            min_val = num
            mid = i
    # mid = nums.index(min(nums, key=lambda x: abs(x)))  # one-liner but 2-pass

    # Traversing (from Mid to Ends) and Comparing:
    # https://github.com/samyak1409/DSA/blob/main/SDE%20Sheet/01%29%20Arrays/009%29%20Merge%20Sorted%20Array.py
    n = len(nums)
    lo, hi = mid, mid+1
    while lo > -1 and hi < n:
        if abs(num1 := nums[lo]) <= abs(num2 := nums[hi]):
            yield num1 ** 2
            lo -= 1
        else:
            yield num2 ** 2
            hi += 1
    '''
    while lo > -1:
        yield nums[lo] ** 2
        lo -= 1
    while hi < n:
        yield nums[hi] ** 2
        hi += 1
    '''
    # In short:
    # yield from map(lambda x: x**2, nums[lo:-1:-1] or nums[hi:])  # `[start:stop:step]`
    # Slicing is so problematic, run above line with `nums=[-5, -3, -2, -1]`. 😶 [WA]
    # Even https://stackoverflow.com/questions/509211/understanding-slicing doesn't mention (about) this problem.
    yield from map(lambda index: nums[index]**2, range(lo, -1, -1) or range(hi, n, 1))  # `[start:stop:step]`
    # Realizing that using indices is better actually, because SLICING MAKES NEW OBJECT, AND SO EXTRA MEMORY.
    # Above solves this problem as well! 🤩
