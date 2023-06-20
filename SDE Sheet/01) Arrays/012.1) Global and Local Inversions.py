"""
https://leetcode.com/problems/global-and-local-inversions
"""


def is_ideal_permutation(nums: list[int]) -> bool:
    """"""

    # Finding Local Inversions is straight-forward, the main part is finding Global Inversions.

    # 0) [TLE] Brute-force (Nested Loop to Find Global Inversions): TC = O(n^2); SC = O(1)

    """
    n = len(nums)

    # Find Local: O(n)
    '''
    local_inv = 0
    for i in range(n-1):
        if nums[i] > nums[i+1]:
            local_inv += 1
    '''
    local_inv = sum(nums[i] > nums[i+1] for i in range(n-1))

    # Find Global: O(n^2)
    '''
    global_inv = 0
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] > nums[j]:
                global_inv += 1
    '''
    global_inv = sum(map(sum, ((nums[i] > nums[j] for j in range(i+1, n)) for i in range(n))))

    return local_inv == global_inv
    """

    # 1) [TLE] Better (Merge Sort to Find Global Inversions): TC = O(n*log(n)); SC = O(n)

    """
    n = len(nums)

    # Find Local: O(n)
    '''
    local_inv = 0
    for i in range(n-1):
        if nums[i] > nums[i+1]:
            local_inv += 1
    '''
    local_inv = sum(nums[i] > nums[i+1] for i in range(n-1))

    # Find Global: O(n*log(n))
    # From https://github.com/samyak1409/DSA/blob/main/SDE%20Sheet/01%29%20Arrays/012%29%20Count%20Inversions.py:
    # Recursive Function:
    def get_count(array: list[int], length: int) -> int:
        if length > 1:
            # Step-1) Dividing:
            mid_index = length // 2
            left, right = array[:mid_index], array[mid_index:]
            count = get_count(array=left, length=mid_index) + get_count(array=right, length=length-mid_index)  # RECURSE
            # Step-2) Merging:
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    array[i+j] = left[i]
                    i += 1
                else:
                    array[i+j] = right[j]
                    j += 1
                    count += len(left)-i  # when element from right list (right[j]) is considered before all left[i:]
                    # => total len(left)-i inversions will be there (only for this particular right[j])
                    # EXPLANATION: https://youtu.be/kQ1mJlwW-c0?t=325
            array[i+j:] = left[i:] or right[j:]
            return count
        return 0  # for deepest (last) recursive calls (-> leaves of the recursion tree)
    global_inv = get_count(array=nums[:], length=n)  # [:] so that input array remains unmodified

    return local_inv == global_inv
    """

    # 2) Optimal (Find a "Non-Local Global Inversion"): TC = O(n); SC = O(1)
    # Smart! 👌
    # Solution 1 in:
    # https://leetcode.com/problems/global-and-local-inversions/discuss/113644/C++JavaPython-Easy-and-Concise-Solution
    # Intuition:
    # ALL LOCAL INVERSIONS ARE GLOBAL INVERSIONS.
    # So, if local inversions == global inversions => non-local global inversions will be = 0
    # i.e. we can't find nums[i] > nums[j] with i < j-1.
    # In other words, max(nums[i]) < nums[i+2].
    # So, to efficiently find one, traverse nums and keep the current biggest number cmax.
    # Then check the condition cmax < nums[i+2]

    """
    curr_max = -1  # init
    for i in range(len(nums)-2):
        curr_max = max(curr_max, nums[i])
        if curr_max > nums[i+2]:
            return False
    return True
    """

    # 2.1) Optimal (Find abs diff b/w num_at_i and num_that_should_be_at_i): TC = O(n); SC = O(1)
    # Solution 2 in:
    # https://leetcode.com/problems/global-and-local-inversions/discuss/113644/C++JavaPython-Easy-and-Concise-Solution
    # https://leetcode.com/problems/global-and-local-inversions/discuss/113656/My-3-lines-C++-Solution

    '''
    for i in range(len(nums)):
        if abs(nums[i]-i) > 1:  # if gap 2 or more => it's non-local global inversion
            return False
    return True
    '''
    return all(abs(nums[i]-i) <= 1 for i in range(len(nums)))  # True if all have gap = 0 or 1 else False
