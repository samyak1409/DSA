"""
https://leetcode.com/problems/max-consecutive-ones
"""


def find_max_consecutive_ones(nums: list[int]) -> int:
    """"""

    # 1) Optimal (Iterate & Track): TC = O(n); SC = O(1)
    # You need to think about two things as far as any window is concerned.
    # One is the starting point for the window.
    # How do you detect that a new window of 1s has started?
    # The next part is detecting the ending point for this window.
    # How do you detect the ending point for an existing window?
    # If you figure these two things out, you will be able to detect the windows of consecutive ones.
    # All that remains afterward is to find the longest such window and return the size.
    # https://leetcode.com/problems/max-consecutive-ones/discuss/96693/Java-4-lines-concise-solution-with-explanation/101261

    max_streak = streak = 0  # init
    for num in nums:
        if num:
            streak += 1  # ++
            max_streak = max(max_streak, streak)  # update max
        else:
            streak = 0  # reset
    return max_streak


# Similar Questions:
# https://leetcode.com/problems/max-consecutive-ones-iii
# https://leetcode.com/problems/consecutive-characters
# https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros
# https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring
