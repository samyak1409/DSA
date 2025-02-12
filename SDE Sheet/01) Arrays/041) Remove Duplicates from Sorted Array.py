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

    # 0) Brute-force (Using HashSet/HashMap): TC = O(n); SC = O(n)

    # https://stackoverflow.com/questions/480214/how-do-i-remove-duplicates-from-a-list-while-preserving-order
    # https://stackoverflow.com/questions/1653970/does-python-have-an-ordered-set
    """
    hs = set()
    i = -1
    for num in nums:
        if num not in hs:
            nums[i:=i+1] = num
            hs.add(num)
    return i+1
    """
    # Or we can use `dict`, which preserves the order of insertion, and since the array is sorted, we'll be good to go!
    """
    from collections import Counter
    hm = Counter(nums)
    k = len(hm)
    nums[:k] = hm.keys()
    return k
    """

    # 1) Optimal: TC = O(n); SC = O(1)

    # 1.1) Intuitive: While loop + Two-pointers:
    # [Came up with myself.]
    # Basic idea: If curr num == prev num, we need a num from the right to place at curr, else we can go ahead.

    """
    i = 1
    j = 2
    n = len(nums)
    # While we've not traversed the whole arr:
    while j < n:
        # If curr num is <= prev (we need `<` as well, dry run on [0,0,1,1,1,2,2,3,3,4] to know why):
        if nums[i] <= nums[i-1]:
            # Copy from the right:
            nums[i] = nums[j]
            # Increment `j` (as nums[j] is already copied, and we need unique nums):
            j += 1
        # If curr num > prev, then we can just go ahead:
        else:
            i += 1
            # But, only ++j if `i` has become = to `j` (dry run on [0,0,0,1,1,2,3,4,4] to know why):
            if i == j:
                j += 1

    # Loop once more to find k:
    for i in range(1, n):
        if nums[i] <= nums[i-1]:
            return i
    """

    # Hints:
    # 1. In this problem, the key point to focus on is the input array being sorted. As far as duplicate elements are
    # concerned, what is their positioning in the array when the given array is sorted? Look at the image below for the
    # answer. If we know the position of one of the elements, do we also know the positioning of all the duplicate
    # elements?
    # https://assets.leetcode.com/uploads/2019/10/20/hint_rem_dup.png
    # 2. We need to modify the array in-place and the size of the final array would potentially be smaller than the size
    # of the input array. So, we ought to use a two-pointer approach here. One, that would keep track of the current
    # element in the original array and another one for just the unique elements.
    # 3. Essentially, once an element is encountered, you simply need to BYPASS its duplicates and move on to the next
    # unique element.

    # 1.1) For loop + Two-pointers:
    # Not intuitive, but easy after realizing how it's working.
    # Idea: Focus on putting the unique nums one by one at the beginning of arr, just traverse the arr, and whenever a
    # new num is found, save to current `i`, and increment it.

    i = 0  # IMP: this is the index till which the numbers are unique
    # (including itself, so currently, it says nums[0] is unique, which is true)
    # Iterate:
    for num in nums:
        # If we find a num `num` which is not same as our latest unique num `nums[i]`, implies we've a new unique num,
        # so, we can copy `num` to `nums[i+1]`, ++i, and continue with the loop:
        if num != nums[i]:
            # nums[i+1] = num
            # i += 1
            # Or just:
            nums[i:=i+1] = num
    # Since `i` is the index of last unique num, `i+1` is the num of unique nums we've in the arr:
    return i+1


# Similar Questions:
# https://leetcode.com/problems/remove-element
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii
