"""
https://leetcode.com/problems/sort-colors
"""


def sort_colors(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    # 0) Brute-force (Sorting): TC = O(n*log(n)); SC = O(n)
    # https://github.com/samyak1409/python-lab-assignments/blob/main/10/a.py

    """
    # Recursive Function:
    def merge_sort(arr: list[int]) -> None:
        arr_len = len(arr)
        if arr_len > 1:
            mid_index = arr_len // 2
            left, right = arr[:mid_index], arr[mid_index:]
            merge_sort(arr=left), merge_sort(arr=right)
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[i+j] = left[i]
                    i += 1
                else:
                    arr[i+j] = right[j]
                    j += 1
            arr[i+j:] = left[i:] or right[j:]

    merge_sort(arr=nums)  # passed reference
    """

    # 1.1) Optimal (Counting Sort) (Two-pass): TC = O(n); SC = O(1) {nums[i] is either 0, 1, or 2}

    """
    from collections import Counter
    from itertools import chain

    freq = Counter(nums)  # TC = O(n); SC = O(1)
    # print(freq)  #debugging

    # nums[:] = [0]*freq[0] + [1]*freq[1] + [2]*freq[2]  # TC = O(n); SC = O(n)
    # RHS will construct a new list and allocate it space
    nums[:] = chain([0]*freq[0], [1]*freq[1], [2]*freq[2])  # TC = O(n); SC = O(1)
    # Note: Let's assume 2 is not there in nums, still n[2] will not give an error because n is a Counter object, and it
    # handles that (by default returns 0 value if a key is not there).
    """

    # Follow up: Could you come up with a one-pass algorithm using only constant extra space?

    # 1.2) Optimal (?) (One-pass): TC = O(n); SC = O(1)
    # https://leetcode.com/problems/sort-colors/discuss/26500/Four-different-solutions/160956
    # Don't know how/why exactly is this working. Can someone explain me this?

    """
    i0 = i1 = i2 = -1  # indices at which last 0/1/2 was placed
    for num in nums:  # iterate on nums
        match num:
            case 0:
                nums[i2 := i2+1] = 2
                nums[i1 := i1+1] = 1
                nums[i0 := i0+1] = 0
            case 1:
                nums[i2 := i2+1] = 2
                nums[i1 := i1+1] = 1
            case 2:
                nums[i2 := i2+1] = 2
    """
    # Conciser:
    """
    i0 = i1 = i2 = -1
    for num in nums:
        nums[i2 := i2+1] = 2
        if num != 2:
            nums[i1 := i1+1] = 1
        if num == 0:
            nums[i0 := i0+1] = 0
    """

    # 1.3) Optimal (Three Pointers & Swapping) (One-pass): TC = O(n); SC = O(1)
    # The idea is to sweep all 0s to the left and all 2s to the right, then all 1s are left in the middle.
    # IMP: Based on the same concept we used in `1.2)` of
    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/041.1%29%20Remove%20Element.py.
    # https://en.wikipedia.org/wiki/Dutch_national_flag_problem
    # https://leetcode.com/problems/sort-colors/discuss/26481/Python-O(n)-1-pass-in-place-solution-with-explanation
    # https://leetcode.com/problems/sort-colors/discuss/26472/Share-my-at-most-two-pass-constant-space-10-line-solution/25489

    i, j, k = 0, 0, len(nums)-1
    while j <= k:
        match nums[j]:  # j is the main pointer
            case 0:  # if j -> 0, then we'll swap with i
                nums[j], nums[i] = nums[i], nums[j]
                i, j = i+1, j+1
            case 1:  # if j -> 1, then we just move forward, because 1s will be in the middle only
                j += 1
            case 2:  # and if j -> 2, then we'll swap with k
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
                # NOTE: we're not moving j forward in this case because the value we got from k can be 0/1 which still
                # needs to be checked


# Similar Question:
# https://leetcode.com/problems/sort-list
# https://leetcode.com/problems/wiggle-sort-ii
