"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii
"""


def remove_duplicates(nums: list[int]) -> int:
    """"""

    # Points to be noted:
    # -> Since it is impossible to change the length of the array in some languages, you must instead have the result be
    # placed in the first part of the array nums.
    # -> Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1)
    # extra memory.

    # 1) Optimal (Two-Pointers): TC = O(n); SC = O(1)
    # Similar to `1)` of
    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/041%29%20Remove%20Duplicates%20from%20Sorted%20Array.py.
    # https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/discuss/27976/3-6-easy-lines-C++-Java-Python-Ruby
    # (same algo, just the other way around)

    n = len(nums)
    i = -1
    for j in range(n):
        if j >= n-2 or nums[j] != nums[j+2]:  # `nums[j] != nums[j+2]`: checking is the `num[j]` not there at `num[j+2]`
            # in order to satisfy `each unique element appears AT MOST TWICE`;
            # `j >= n-2`: because for j >= n-2, there can't exist nums with occurrence > 2 (in the right)
            nums[i := i+1] = nums[j]
        # If these both conditions dissatisfy, just skip current num and move on to the next num.
    return i+1

    # "Just want to confirm, this solution can be easily generalized to "at most K duplicates", right?"
    # -https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/discuss/27976/3-6-easy-lines-C++-Java-Python-Ruby/27034
