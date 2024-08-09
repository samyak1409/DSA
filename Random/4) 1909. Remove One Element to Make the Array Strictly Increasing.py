"""
https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing
"""


def can_be_increasing(nums: list[int]) -> bool:
    """"""

    # No.2 Least Accepted Easy Question
    # (https://leetcode.com/problemset/all/?difficulty=EASY&sorting=W3sic29ydE9yZGVyIjoiQVNDRU5ESU5HIiwib3JkZXJCeSI6IkFDX1JBVEUifV0%3D)

    # For each index i in nums remove this index.
    # If the array becomes sorted return true, otherwise revert to the original array and try different index.

    # 0) Brute-force (Remove every num one by one and Check): TC = O(n^2); SC = O(1)

    """
    for i in range(n := len(nums)):  # loop on indices from start to end

        possible = True
        prev = None

        # Check if removing nums[i] make the array strictly increasing:
        for j in range(n):
            if j != i:  # skip i-th index so that it behaves like we have removed the nums[i] w/o actually doing so
                if prev and prev >= nums[j]:
                    possible = False  # even after removing nums[i], array is not strictly increasing
                    break
                prev = nums[j]  # update prev

        if possible:
            return True

    return False
    """

    # 1) Optimal (Figure out removing which index (out of two) will be correct): TC = O(n); SC = O(1)
    # "When we find a drop, we check if the current number nums[i] is greater than the number before the previous one
    # nums[i-2]:
    #            - If so, the number nums[i-1] needs to be removed.
    #            - Otherwise, the current number needs to be removed (nums[i]).
    # And, of course, we return false if we find a second drop."
    # -https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/solutions/1299306/two-conditions

    """
    removed = None  # index at which num is removed

    for i in range(1, len(nums)):  # start from index 1 and go till the end

        # If encountered not strictly increasing:
        if nums[i] <= nums[i-1 if i-1 != removed else i-2]:
            # `i-1 if (i-1 != removed) else i-2`: handling the case when an index is removed, so for following elements,
            # `i-1` changes to `(i-1)-1` = `i-2`

            if removed is not None:  # we've already removed a num
                return False  # so

            # Main Part: Deciding which num to remove:
            '''
            if i == 1 or nums[i] > nums[i-2]:  # `i == 1`: for the lil edge case
                removed = i-1
            else:
                removed = i
            '''
            removed = i-1 if i == 1 or nums[i] > nums[i-2] else i

    return True
    """
    # OR:
    removed = None  # will save index of num which is removed

    for i in range(len(nums)-1):  # loop from start to end-1

        if nums[i+1] <= nums[i if i != removed else i-1]:  # check if not strictly inc
            # `i if i != removed else i-1` instead of `i` because:
            # when a num is removed, for next iteration, it should be ignored

            if removed is not None:  # if we already have a drop
                return False  # then not possible

            # Ignore a num greedily:
            '''
            if i == 0 or nums[i+1] > nums[i-1]:  # (`i == 0` handles the edge case)
                removed = i
            else:
                removed = i + 1
            '''
            removed = i if i == 0 or nums[i+1] > nums[i-1] else i+1

    return True

    # Why do we NOT need to check both, for the smaller num out of the two which is still bigger than nums[i-1]?
    # [Also: Why do we want smaller, because greedy!]
    # Because we are facing a drop, implying nums[i+1] <= nums[i]. So, we just need to check nums[i+1], if it is >
    # num[i-1], if it is we do not need to check nums[i] and remove nums[i], as we already know nums[i+1] <= nums[i].
    # Otherwise, we just remove nums[i+1] as it's <= nums[i-1].
