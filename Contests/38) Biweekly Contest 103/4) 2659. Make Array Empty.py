"""
https://leetcode.com/problems/make-array-empty
"""


def count_operations_to_empty_array(nums: list[int]) -> int:
    """"""

    # 0) [TLE] Brute-force (Simulation (using `deque` for fast add-remove at endpoints (FIFO))): TC = O(n^2); SC = O(n)
    # (505 / 514 testcases passed)

    """
    from collections import deque

    # Get the sorted nums:
    sorted_nums = sorted(nums)  # TC = O(n*log(n)); SC = O(n)
    i = 0

    nums = deque(nums)  # TC = SC = O(n)
    ops = 0

    while nums:  # while nums is not emptied; TC = O(n^2) {why?: dry run w/ nums=[5,4,3,2,1]}
        '''
        # "If the first element has the smallest value, remove it":
        if nums[0] == sorted_nums[i]:
            nums.popleft()
            i += 1
        # "Otherwise, put the first element at the end of the array":
        else:
            nums.append(nums.popleft())
        ops += 1
        '''
        # Shorter:
        # "If the first element has the smallest value, remove it":
        if (first := nums.popleft()) == sorted_nums[i]:
            i += 1
        # "Otherwise, put the first element at the end of the array":
        else:
            nums.append(first)
        ops += 1

    return ops
    """

    # Understand the order in which the indices are removed from the array.
    # We don’t really need to delete or move the elements, only the array length matters.
    # Upon removing an index, decide how many steps it takes to move to the next one.
    # Use a data structure to speed up the calculation.

    # 1) Optimal (?): TC = O(n*log(n)); SC = O(n)
    # Hard one.
    # https://leetcode.com/problems/make-array-empty/solutions

    pass
