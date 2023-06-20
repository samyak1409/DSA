"""
https://leetcode.com/problems/remove-element
"""


def remove_element(nums: list[int], val: int) -> int:
    """"""

    # Points to be noted:
    # -> Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative
    # order of the elements may be changed.
    # -> Since it is impossible to change the length of the array in some languages, you must instead have the result be
    # placed in the first part of the array nums.
    # -> Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1)
    # extra memory.

    # 0) Brute-force (Copy all the elements to the left): TC = O(n^2); SC = O(1)

    """
    n = len(nums)
    i = 0
    while i < n:
        if nums[i] == val:
            for j in range(i+1, n):  # shift all the elements in right to 1 left
                nums[j-1] = nums[j]
            n -= 1  # ∵ elements are shifted to 1 left
        else:
            i += 1  # skip the num which is != val
    return i
    """

    # 1) Optimal (Two-Pointers): TC = O(n); SC = O(1)

    # 1.1) Copy Required Elements to the Left: TC = O(2n); SC = O(1)
    # https://leetcode.com/problems/remove-element/solution/#approach-1-two-pointers
    # Almost same as `1)` of
    # https://github.com/samyak1409/DSA/blob/main/SDE%20Sheet/01%29%20Arrays/041%29%20Remove%20Duplicates%20from%20Sorted%20Array.py.

    """
    i = -1
    for num in nums:
        if num != val:
            nums[i := i+1] = num
    return i+1
    """

    # 1.2) Move Elements to Remove to the End by Swapping: TC = O(n); SC = O(1)
    # -> "The relative order of the elements may be changed."
    # https://leetcode.com/problems/remove-element/solution/#approach-2-two-pointers-when-elements-to-remove-are-rare

    i, j = 0, len(nums)-1
    while i <= j:  # why `=`? dry run the algo w/o `=` on input (nums=[1], val=1) to get it
        if nums[i] == val:
            nums[i], nums[j] = nums[j], nums[i]  # swap (putting element to remove in the end)
            j -= 1
        else:
            i += 1  # imp: to not ↑ `i` when swapping is done, because we don't know what came from the end to `i`, so
            # we need to check that too
    return i
