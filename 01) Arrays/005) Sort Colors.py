"""
https://leetcode.com/problems/sort-colors
"""


def sortColors(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    # 0) Brute-force (Sorting): TC = O(n*log(n)); SC = O(n) {In Python, the sort() function is implemented using the Timsort algorithm, which has a worst-case space complexity of O(n)}

    """
    nums.sort()
    """

    # 1) Optimal (Counting Sort) (Two-pass): TC = O(n); SC = O(1)

    """
    from collections import Counter
    n = Counter(nums)  # TC = O(n); SC = O(1)
    # print(n)  #debugging

    nums[:] = [0]*n[0] + [1]*n[1] + [2]*n[2]  # O(n)
    # New Discovery: e.g. 2 is not there in nums, still n[2] will not give an error because n is a Counter object, and it handles that (by default returns 0 value if a key is not there)
    """

    # 2) Optimal (The "Running But Don't Know How" Algo) (One-pass): TC = O(n); SC = O(1)
    # https://leetcode.com/problems/sort-colors/discuss/26500/Four-different-solutions/160956

    """
    n2 = n1 = n0 = -1
    for num in nums:
        match num:
            case 2:
                n2 += 1
                nums[n2] = 2
            case 1:
                n2 += 1
                n1 += 1
                nums[n2] = 2
                nums[n1] = 1
            case 0:
                n2 += 1
                n1 += 1
                n0 += 1
                nums[n2] = 2
                nums[n1] = 1
                nums[n0] = 0
    """

    # 3) Optimal (Swapping) (One-pass): TC = O(n); SC = O(1)
    # https://en.wikipedia.org/wiki/Dutch_national_flag_problem
    # https://leetcode.com/problems/sort-colors/discuss/26472/Share-my-at-most-two-pass-constant-space-10-line-solution/25489; https://leetcode.com/problems/sort-colors/discuss/26481/Python-O(n)-1-pass-in-place-solution-with-explanation
    # The idea is to sweep all 0s to the left and all 2s to the right, then all 1s are left in the middle.

    i, low, high = 0, 0, len(nums)-1
    while i <= high:
        match nums[i]:
            case 0:
                nums[i], nums[low] = nums[low], nums[i]
                low += 1
                i += 1
            case 1:
                i += 1
            case 2:
                nums[i], nums[high] = nums[high], nums[i]
                high -= 1
