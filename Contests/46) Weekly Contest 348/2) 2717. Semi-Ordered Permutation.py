"""
https://leetcode.com/problems/semi-ordered-permutation
"""


def semi_ordered_permutation(nums: list[int]) -> int:
    """"""

    # 1) Optimal (Calc. Distance): TC = O(n); SC = O(1)
    # We don't actually need to swap and count, we can just calc. by the distance.
    # No. of swaps required to move a num from its src to dst = idx(dst) - idx(src)
    # Just one imp. thing to catch (edge case), if index of n < index of 1, then we'd need to subtract 1 from our ans.
    # because there would be a point when they'd cross each other, in that case one swap would be swapping both closed
    # to their respective dst.

    idx_1, idx_n = nums.index(1), nums.index(n := len(nums))
    return idx_1 + (n - idx_n - 1) - (idx_1 > idx_n)
