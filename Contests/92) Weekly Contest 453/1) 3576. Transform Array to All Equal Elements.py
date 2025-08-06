"""
https://leetcode.com/problems/transform-array-to-all-equal-elements
"""


def can_make_equal(nums: list[int], k: int) -> bool:
    """"""

    # 1) Optimal (Try converting to both, iteratively left to right (Greedy)): TC = O(n); SC = O(n)

    # Helper:
    def f(arr: list[int], target: int, ops_left: int) -> bool:
        # Iterate left to right:
        for i in range(n-1):
            # If curr el != target, means it needs to be converted:
            if arr[i] != target:
                arr[i], arr[i+1] = -arr[i], -arr[i+1]
                # If at any point, `k` exceeds, means not possible, so return early:
                if (ops_left := ops_left-1) == -1:
                    return False
        # At the end, check if the last element == target, then only all arr[i] == target:
        return arr[-1] == target

    n = len(nums)
    # We need to try both converting to 1 and -1:
    return f(nums[:], 1, k) or f(nums[:], -1, k)
