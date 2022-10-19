"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array
"""


def remove_duplicates(nums: list[int]) -> int:
    """"""

    # Points to be noted:
    # -> Since it is impossible to change the length of the array in some languages, you must instead have the result be
    # placed in the first part of the array nums.
    # -> Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1)
    # extra memory.

    # 0) Brute-force (Using HashSet): TC = O(n); SC = O(n)

    """
    unique = set(nums)
    k = len(unique)
    nums[:k] = unique
    return k
    """
    # WA because `set` is unordered. Fixes:
    # https://stackoverflow.com/questions/480214/how-do-i-remove-duplicates-from-a-list-while-preserving-order
    # https://stackoverflow.com/questions/1653970/does-python-have-an-ordered-set
    """
    unique = set()
    i = -1
    for num in nums:
        if num not in unique:
            nums[i := i+1] = num
            unique.add(num)
    return i+1
    """
    # Or we can use `dict`, which preserves the order of insertion, and since the array is sorted, we'll be good to go!
    """
    from collections import Counter
    dict_ = Counter(nums)
    k = len(dict_)
    nums[:k] = dict_.keys()
    return k
    """

    # 1) Optimal (Two-Pointers): TC = O(n); SC = O(1)
    # https://leetcode.com/problems/remove-duplicates-from-sorted-array/solution

    """
    i = j = 0
    n = len(nums)
    while j <= n:
        if nums[j] != nums[i]:
            nums[i := i+1] = nums[j]
        j += 1
    return i+1
    """
    # We actually don't need while loop:
    """
    i = 0
    for j in range(len(nums)):
        if nums[j] != nums[i]:
            nums[i := i+1] = nums[j]
    return i+1
    """
    # Or:
    i = 0
    for num in nums:
        if num != nums[i]:
            nums[i := i+1] = num
    return i+1


# Similar Questions:
# https://leetcode.com/problems/remove-element
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii
