"""
https://leetcode.com/problems/wiggle-sort-ii
"""


def wiggle_sort(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    # 0) [WA] Brute-force (Sorting & Sequential Selection): TC = O(n*log(n)); SC = O(n)
    # Starting & Direction of Two Pointers: (leftmost & rightmost) to middle
    # WA because of the presence of duplicate numbers (would be correct for an array with unique numbers), see:
    # Input: [1,3,2,2,3,1]
    # stdout: [1,1,2,2,3,3]
    # Output: [1,3,1,3,2,2]
    # Expected: [2,3,1,3,1,2]

    """
    sorted_nums = sorted(nums)  # TC = O(n*log(n)); SC = O(n)
    print(sorted_nums)  #debugging
    n = len(nums)
    left, right = -1, n  # two pointers
    for i in range(n):  # TC = O(n); SC = O(1)
        if i % 2 == 0:  # even index
            nums[i] = sorted_nums[left := left+1]  # left++
        else:  # odd index
            nums[i] = sorted_nums[right := right-1]  # right--
        # nums[i] = sorted_nums[(left := left+1) if (i % 2 == 0) else (right := right-1)]  # one liner
    """

    # 1) Sub-Optimal (Sorting & Smart Sequential Selection): TC = O(n*log(n)); SC = O(n)
    # https://leetcode.com/problems/wiggle-sort-ii/discuss/77678/3-lines-Python-with-Explanation-Proof
    # Starting & Direction of Two Pointers: (mid to leftmost) & (rightmost to mid)
    # Example of the algorithm after sorting: (`|` indicates mid)
    # Even: nums = 1 1 2 | 2 3 3
    #    indices = 4 2 0 | 5 3 1 on which the nums will go for answer
    # Odd: nums = 1 2 3 4 | 5 6 7
    #   indices = 6 4 2 0 | 5 3 1 on which the nums will go for answer

    sorted_nums = sorted(nums)  # TC = O(n*log(n)); SC = O(n)
    # print(sorted_nums)  #debugging
    n = len(nums)
    small, big = (n+1)//2, n  # two pointers
    for i in range(n):  # TC = O(n); SC = O(1)
        if i % 2 == 0:  # even index
            nums[i] = sorted_nums[small := small-1]  # small--
        else:  # odd index
            nums[i] = sorted_nums[big := big-1]  # big--
        # nums[i] = sorted_nums[(small := small-1) if (i % 2 == 0) else (big := big-1)]  # one liner

    # Why do we need to reverse traverse? Because nums[0] is needed to be < nums[1].
    # ("Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....")
    # If this was not mandatory, i.e. nums[0] > nums[1] < nums[2] > nums[3].... was also accepted,
    # We could also do:
    # Even: nums = 1 1 2 | 2 3 3
    #    indices = 1 3 5 | 0 2 4 on which the nums will go for answer
    # Odd: nums = 1 2 3 | 4 5 6 7
    #   indices = 1 3 5 | 0 2 4 6 on which the nums will go for answer
    # Again :|, why do we need to consider the second_half first only, and then first_half?
    # Understand this yourself by taking: nums = 1 2 2 3

    # Follow Up: Can you do it in O(n) time and/or in-place with O(1) extra space?
    # 2) Optimal (): TC = O(n); SC = O(1)
    # https://leetcode.com/problems/wiggle-sort-ii/discuss/77684/Summary-of-the-various-solutions-to-Wiggle-Sort-for-your-reference
    # https://leetcode.com/problems/wiggle-sort-ii/discuss/77682/Step-by-step-explanation-of-index-mapping-in-Java
    # https://leetcode.com/problems/wiggle-sort-ii/discuss/77677/O(n)+O(1)-after-median-Virtual-Indexing
