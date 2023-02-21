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
        '''
        if i % 2 == 0:  # even index
            nums[i] = sorted_nums[left := left+1]  # left++
        else:  # odd index
            nums[i] = sorted_nums[right := right-1]  # right--
        '''
        nums[i] = sorted_nums[(left := left+1) if (i % 2 == 0) else (right := right-1)]
    """

    # 1) Sub-Optimal (Sorting & Smart Sequential Selection): TC = O(n*log(n)); SC = O(n)
    # https://leetcode.com/problems/wiggle-sort-ii/discuss/77678/3-lines-Python-with-Explanation-Proof
    # Starting & Direction of Two Pointers: (mid to leftmost) & (rightmost to mid)
    # Example of the algorithm (after sorting): (`|` indicates mid)
    # Even: nums = 1 1 2 | 2 3 3
    #    indices = 4 2 0 | 5 3 1 on which the numbers will go
    # Odd: nums = 1 2 3 4 | 5 6 7
    #   indices = 6 4 2 0 | 5 3 1 on which the numbers will go

    sorted_nums = sorted(nums)  # TC = O(n*log(n)); SC = O(n)
    # print(sorted_nums)  #debugging
    n = len(nums)
    left, right = (n+1)//2, n  # two pointers
    for i in range(n):  # TC = O(n); SC = O(1)
        '''
        if i % 2 == 0:  # even index
            nums[i] = sorted_nums[left := left-1]  # left--
        else:  # odd index
            nums[i] = sorted_nums[right := right-1]  # right--
        '''
        nums[i] = sorted_nums[(left := left-1) if (i % 2 == 0) else (right := right-1)]

    # Why do we need to reverse traverse? To handle cases like this: nums = 1 2 2 3
    # When len(nums) is even and there are n/2 duplicates exactly in the middle.
    # If we don't reverse traverse:
    """
    sorted_nums = sorted(nums)  # TC = O(n*log(n)); SC = O(n)
    n = len(nums)
    left, right = -1, (n-1)//2  # two pointers
    for i in range(n):  # TC = O(n); SC = O(1)
        nums[i] = sorted_nums[(left := left+1) if (i % 2 == 0) else (right := right+1)]
    """
    # Wrong Answer
    # Input: [1,2,2,3]
    # Output: [1,2,2,3]
    # Expected: [2,3,1,2]

    # [ADDITIONAL]:
    # If `nums[0] > nums[1] < nums[2] > nums[3]...` was the required order instead of
    # `nums[0] < nums[1] > nums[2] < nums[3]...`, we would have chosen the first element from the right instead of left
    # (because of the obvious reason), as well as traversal would be straight instead of reversed (because of the same
    # reason why we reverse traversed in case of current Qn).
    # Even: nums = 1 1 2 | 2 3 3
    #    indices = 1 3 5 | 0 2 4 on which the numbers will go
    # Odd: nums = 1 2 3 | 4 5 6 7
    #   indices = 1 3 5 | 0 2 4 6 on which the numbers will go

    # Follow Up: Can you do it in O(n) time and/or in-place with O(1) extra space?
    # 2) Optimal (?): TC = O(n); SC = O(1)
    # https://leetcode.com/problems/wiggle-sort-ii/discuss/77684/Summary-of-the-various-solutions-to-Wiggle-Sort-for-your-reference
    # https://leetcode.com/problems/wiggle-sort-ii/discuss/77682/Step-by-step-explanation-of-index-mapping-in-Java
    # https://leetcode.com/problems/wiggle-sort-ii/discuss/77677/O(n)+O(1)-after-median-Virtual-Indexing
