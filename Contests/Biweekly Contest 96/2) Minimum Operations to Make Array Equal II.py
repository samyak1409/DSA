"""
https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii
"""


def min_operations(nums1: list[int], nums2: list[int], k: int) -> int:
    """"""

    # What are the cases for which we cannot make nums1 == nums2?
    # For minimum moves, if nums1[i] < nums2[i], then we should never decrement nums1[i]. If nums1[i] > nums2[i], then
    # we should never increment nums1[i].

    # 1) Optimal (Track plus & minus): TC = O(n); SC = O(1)
    # https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii/solutions

    if k == 0:  # edge case: ZeroDivisionError
        return -1 if nums1 != nums2 else 0  # if k == 0 and nums1 != nums2: impossible to make equal

    p = n = 0  # plus, minus

    for x, y in zip(nums1, nums2):

        if (x-y) % k != 0:  # if remainder is there: impossible to make equal with respective difference
            return -1

        ops = (x-y) // k  # no. of times inc/dec required in order to make equal
        # print(x, y, ops)  #debugging
        if ops > 0:  # add ops to increment count
            p += ops
        elif ops < 0:  # add ops to decrement count
            n += -ops

    return p if p == n else -1
    # in one op, we have to inc as well as dec, so inc == dec
    # if inc != dec => diff no. of inc and dec count => but as we have to apply inc and dec in every op, not possible to
    # make nums1 & nums2 equal
