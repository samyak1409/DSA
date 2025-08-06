"""
https://leetcode.com/problems/minimum-cost-to-make-arrays-identical
"""


def min_cost(arr: list[int], brr: list[int], k: int) -> int:
    """"""

    # 1) Optimal (Greedy, Sort): TC = O(n*log(n)); SC = O(n) {sort}
    # Good tricky question!
    # At first this question would feel very hard due to:
    # "Split arr into any number of contiguous sub-arrays and rearrange these sub-arrays in any order. This operation
    # has a fixed cost of k."
    # But, the realization that if we can do that, we can just also rearrange every single element in `arr`, to be as
    # close as the elements in `brr`. That'd give the minimum absolute-difference. (Greedy)
    # And how can we do that? Easily by sorting both the arrays.
    # So, we'd have two cases:
    # - Abs diff without sorting. (If the arrays are already sorted, we don't need to use `k`.)
    # - Abs diff after sorting. +k.

    """
    # Get cost without sorting:
    c1 = 0
    for i in range(n := len(arr)):
        c1 += abs(arr[i]-brr[i])

    # Sort:
    arr, brr = sorted(arr), sorted(brr)  # (using `sorted()` instead of `sort()` to avoid modifying the input)
    # Get cost after sorting:
    c2 = k
    for i in range(n):
        c2 += abs(arr[i]-brr[i])

    # Return min:
    return min(c1, c2)
    """

    # Concise:

    # Helper function: Calc. cost:
    def cost(a: list[int], b: list[int]) -> int: return sum(abs(a[i]-b[i]) for i in range(len(a)))

    # Get cost without & after sorting, return min:
    return min(cost(arr, brr), k+cost(sorted(arr), sorted(brr)))
