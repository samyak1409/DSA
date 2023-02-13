"""
https://leetcode.com/problems/build-array-from-permutation
"""


def build_array(nums: list[int]) -> list[int]:
    """"""

    # No.1 Most Accepted Easy Question
    # (https://leetcode.com/problemset/all/?difficulty=EASY&sorting=W3sic29ydE9yZGVyIjoiREVTQ0VORElORyIsIm9yZGVyQnkiOiJBQ19SQVRFIn1d)

    # Just apply what's said in the statement.
    # Notice that you can't apply it on the same array directly since some elements will change after application

    # 1) Brute-force = Optimal (Do as said.): TC = O(n); SC = O(1)

    """
    return [nums[nums[i]] for i in range(len(nums))]
    """

    # 1.1) Using Generator:
    # Benefit?: Not using space even for returning the output.

    yield from (nums[nums[i]] for i in range(len(nums)))
