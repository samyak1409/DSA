"""
https://leetcode.com/problems/move-zeroes
"""


def move_zeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    # 0) Brute-force (Find 0, Remove, Append): TC = O(n^2); SC = O(1)

    """
    for _ in range(nums.count(0)):  # O(n)
        nums.remove(0)  # O(n) (find+shift)
        nums.append(0)  # O(1)
    """

    # 1) Time-optimal (Extra array to save non-zeros): TC = O(n); SC = O(n)

    """
    # Filter non-zeros and store in new array:
    non_zeros = []
    for i in range(n := len(nums)):  # O(n); O(n)
        if nums[i]:
            non_zeros.append(nums[i])
    # Fill back:
    for i in range(nz := len(non_zeros)):  # put non-zeros in front; O(n); O(1)
        nums[i] = non_zeros[i]
    for i in range(nz, n):  # put zeros in back; O(n); O(1)
        nums[i] = 0
    """
    # Short:
    """
    # Filter non-zeros and store in new array:
    non_zeros = list(filter(None, nums))  # O(n); O(n)
    # Fill back:
    nums[:(nz := len(non_zeros))] = non_zeros  # put non-zeros in front; O(n); O(1)
    nums[nz:] = [0] * (len(nums)-nz)  # put zeros in back; O(n); O(n)
    """

    # 2) Optimal (Two Pointers): TC = O(n); SC = O(1)

    # 2.1) First copy non-zeros to front, then fill back with zeros:

    """
    i = 0  # index to put the next non-zero on
    # Loop on array:
    for j in range(n := len(nums)):
        if nums[j]:  # if we get a non-zero
            nums[i] = nums[j]  # copy to our non-zero index
            i += 1  # inc. non-zero index
    # Fill remaining indices with 0s:
    # nums[i:] = [0] * (n-i)
    # Above one-liner would take O(n) space, so basic loop:
    for j in range(i, n):
        nums[j] = 0
    # (Or `itertools.repeat` can be used.)
    """

    # Follow up: Could you minimize the total number of operations done?

    # 2.2) Using swapping, move non-zeros to front and zeros to back simultaneously:
    # "The total operations (array writes) that code does is number of non-0 elements. This gives us a much better
    # best-case (when most of the elements are 0) complexity than last solution. However, the worst-case (when all
    # elements are non-0) complexity for both the algorithms is same."
    # -https://leetcode.com/problems/move-zeroes/editorial/#approach-3-optimal-accepted

    i = 0
    for j in range(len(nums)):
        if nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
            i += 1
