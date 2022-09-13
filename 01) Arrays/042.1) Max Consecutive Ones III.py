"""
https://leetcode.com/problems/max-consecutive-ones-iii
"""


def longest_ones(nums: list[int], k: int) -> int:
    """"""

    # 0) [TLE] Brute-force (Trying Every Combination Linearly): TC = O(n^2); SC = O(1)

    """
    # Helper Function (https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/042%29%20Max%20Consecutive%20Ones.py):
    def get_max_consecutive_ones(nums_: list[int]) -> int:
        max_streak = streak = 0  # init
        for num in nums_:
            if num:
                streak += 1  # ++
                max_streak = max(max_streak, streak)  # update max
            else:
                streak = 0  # reset
        return max_streak

    if not k:  # edge case: if k = 0, this question flattens to `042 Max Consecutive Ones.py`
        return get_max_consecutive_ones(nums)

    zeroes = nums.count(0)
    n = len(nums)
    if zeroes < k:  # optimization
        return n

    start = -1  # last index from where the flipping of 0s was started
    global_max = 0
    for _ in range(zeroes-k+1):  # no. of iterations needed to cover all the combinations
        # Get the modified nums by flipping `k` 0s:
        mod_nums = nums[:]
        flips = 0
        for i in range(start := nums.index(0, start+1), n):  # `nums.index(0, start+1)`: gets index to start from
            if flips == k:
                break
            if not mod_nums[i]:
                mod_nums[i] = 1
                flips += 1
        # Apply the basic O(n) "maximum number of consecutive 1's" finder on the modified nums:
        global_max = max(global_max, get_max_consecutive_ones(mod_nums))
    return global_max
    """
    # Wait, we don't need to actually flip and then calc., instead it can be done easily without it:
    """
    n = len(nums)
    max_streak = 0
    for start in range(n):
        # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/042%29%20Max%20Consecutive%20Ones.py, just with
        # `k` flips allowance:
        flips = 0
        streak = 0
        for i in range(start, n):
            if (num := nums[i]) or flips != k:
                streak += 1  # ++
                if not num:  # => came here by flipping
                    flips += 1
            else:  # stop as soon as we've no way to ↑ current streak (neither num is 1 nor flips are available)
                break
        max_streak = max(max_streak, streak)  # update max
    return max_streak
    """

    # 1) Optimal (Sliding Window): TC = O(n); SC = O(1)
    # Stating the obvious: In sliding window, once we go ahead we never go back!

    n = len(nums)
    i = j = 0
    max_streak = 0
    while j < n:  # while not reached at the end
        if (num := nums[j]) or k > 0:  # => either num is 1 or flips are available
            j += 1  # increase subarray
            if not num:  # => came here by flipping
                k -= 1
        else:  # => next num is 0 and flips are N/A
            if not nums[i]:  # the element we're discarding from our window is 0
                k += 1
            i += 1  # decrease subarray
        max_streak = max(max_streak, j-i)  # update max
    return max_streak
