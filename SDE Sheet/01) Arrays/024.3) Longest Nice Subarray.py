"""
https://leetcode.com/problems/longest-nice-subarray
"""


def longest_nice_subarray(nums: list[int]) -> int:
    """"""

    # Hints:
    # 1) What is the maximum possible length of a nice subarray?
    # 2) The length of the longest nice subarray cannot exceed 30. Why is that?
    # Why????

    # 1) Optimal (Sliding Window w/ Bitwise AND of Every Pair): TC = O(n); SC = O(1)

    i = j = 0  # [start, end]
    n = len(nums)
    ans = 0
    while j != n:
        # For every `j`, go from `i` to `j-1` and check if it satisfies the condition (Bitwise AND == 0):
        for k in range(i, j):  # one by one from left to right
            if nums[j] & nums[k] != 0:  # if condition doesn't satisfy
                i += 1  # shrink the window (imp: not shrinking all the way to `j`, because ans. in b/w can exist)
                break  # stop for this subarray, next we'll start from `i+1` but same `j`
                # not incrementing `j` here because we've not considered all the `i`s for this `j`
        else:  # condition satisfied, => new "nice" subarray found
            ans = max(ans, j-i+1)  # update ans if required
            j += 1
    return ans

    # You might think at first, that how's this working because we're not checking for every pair on considering a new
    # element, but only checking the pairs with that element.
    # Because we've had already checked for remaining pairs in the last iteration, and then only we reached on current
    # iteration with current subarray on the first place!

    # Diff. solutions: https://leetcode.com/problems/longest-nice-subarray/solutions
