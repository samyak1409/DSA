"""
https://leetcode.com/problems/concatenation-of-array
"""


def get_concatenation(nums: list[int]) -> list[int]:
    """"""

    # No.2 Most Accepted Easy Question
    # (https://leetcode.com/problemset/all/?difficulty=EASY&sorting=W3sic29ydE9yZGVyIjoiREVTQ0VORElORyIsIm9yZGVyQnkiOiJBQ19SQVRFIn1d)

    # Build an array of size 2*n and assign num[i] to ans[i] and ans[i+n].

    # 1) Optimal (Do as said.): TC = O(2n) = O(n); SC = O(1)

    """
    return nums + nums
    """

    """
    n = len(nums)
    ans = [None] * (2*n)
    for i in range(n):
        ans[i] = ans[i+n] = nums[i]
    return ans
    """

    # 1.1) Using Generator:
    # Benefit?: Not using space even for returning the output.

    from itertools import chain
    yield from chain(nums, nums)
