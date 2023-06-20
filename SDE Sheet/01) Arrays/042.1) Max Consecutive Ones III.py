"""
https://leetcode.com/problems/max-consecutive-ones-iii
"""


def longest_ones(nums: list[int], k: int) -> int:
    """"""

    # 0) [TLE] Brute-force (Trying Every Combination Linearly): TC = O(n^2); SC = O(1)

    """
    # Helper Function (https://github.com/samyak1409/DSA/blob/main/SDE%20Sheet/01%29%20Arrays/042%29%20Max%20Consecutive%20Ones.py):
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
        # https://github.com/samyak1409/DSA/blob/main/SDE%20Sheet/01%29%20Arrays/042%29%20Max%20Consecutive%20Ones.py, just with
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

    # One thing's for sure, we will only flip a zero if it extends an existing window of 1s. Otherwise, there's no point
    # in doing it, right? Think Sliding Window!
    # Since we know this problem can be solved using the sliding window construct, we might as well focus in that
    # direction for hints. Basically, in a given window, we can never have > K zeros, right?
    # We don't have a fixed size window in this case. The window size can grow and shrink depending upon the number of
    # zeros we have (we don't actually have to flip the zeros here!).
    # The way to shrink or expand a window would be based on the number of zeros that can still be flipped and so on.
    # 1) Optimal (Sliding Window): TC = O(n); SC = O(1)
    # Stating the obvious: In sliding window, once we go ahead, we never go back!

    # 1.1) Intuitive & Easy but a bit Slower:
    """
    n = len(nums)
    i = j = 0
    max_streak = 0
    while j < n:  # while not reached at the end
        if (num := nums[j]) or k > 0:  # => either num is 1 or flips are available
            j += 1  # increase subarray
            max_streak = max(max_streak, j-i)  # update max
            if not num:  # => came here by flipping
                k -= 1
        else:  # => next num is 0 and flips are N/A
            if not nums[i]:  # the element we're discarding from our window is 0
                k += 1
            i += 1  # decrease subarray
    return max_streak
    """

    # 1.2) Tricky but Faster:
    # "Translation: Find the longest subarray with at most k zeros.
    # For each nums[j], try to find the longest subarray.
    # If nums[i] ~ nums[j] has zeros <= k, we continue to increment j.
    # If nums[i] ~ nums[j] has zeros > k, we increment i (as well as j)."
    # https://leetcode.com/problems/max-consecutive-ones-iii/discuss/247564/JavaC++Python-Sliding-Window
    # https://leetcode.com/problems/max-consecutive-ones-iii/discuss/719833/Python3-sliding-window-with-clear-example-explains-why-the-soln-works

    i, j = 0, -1
    for j in range(len(nums)):
        k -= 1-nums[j]  # `k -= 1 if nums[j] == 0 else 0`
        if k < 0:
            # num we just considered (we're automatically considering current num as j is moving continuously) was 0 and
            # k underflow-ed, so in order to keep the window size MAX only, increasing i
            k += 1-nums[i]  # `k += 1 if not nums[i] == 1 else 0`; the element we're discarding from our window is 0
            i += 1
    return j-i+1

    # Explanations on why this algorithm work:
    #
    # "I spent 20 minutes trying to understand this and I turned from "wtf is this code it can't be working" to "holy
    # it's genius". It's so intuitive, though I do think more explanation need to be added here for better
    # understanding.
    # Long story short: i, j is like a moving "memory" sliding frame. (Note: i, j definitely NOT the exact index for the
    # largest range!) Whenever there's a better choice, the span of the frame will fit for the larger range. So you can
    # directly return the final span/length of the frame as the final output.
    # More detailed version: as you can see from the code, j is constantly moving right. k here can be considered as the
    # remaining feasible amount of flips, and reflects the current range (i.e., from i to j). When k<0, it's not a
    # feasible solution and when k>=0, it'll be a feasible solution. If currently range is not yet a feasible solution
    # or better than current "memory" frame (i.e., k<0 judgement) , i will try follow up the j and j-i (the frame size)
    # remains unchanged, keeping the current maximum size intact. Whenever the flip count k of current range (i.e.,
    # still i to j) is greater or equals to 0, it means we can possibly expand our frame, and that's exactly what the
    # code does. (i remains unchanged since it will not go into k<0 clauses, and j keeps moving when k>=0).
    # Eventually, when j comes to the end, the "memory" frame will automatically (by design of course) give us the
    # maximum range throughout the array."
    # -https://leetcode.com/problems/max-consecutive-ones-iii/discuss/247564/JavaC++Python-Sliding-Window/326294
    #
    # "If k < 0, both i, j, will move forward together" <- that's the key!
    # -https://leetcode.com/problems/max-consecutive-ones-iii/discuss/247564/JavaC++Python-Sliding-Window/549451
    #
    # "For everyone who is confused about how this method works like I used to be, here is my explanation of the
    # solution:
    # Take nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3 for example.
    # We know the answer is 10 with subarray from nums[2] to nums[11].
    # Through the iteration of j, this subarray would be found while j = 11 and i = 2.
    # What happens then?
    # Well as we keep iterate j we will find out that j and i keep adding 1 in every iteration, which makes the distance
    # between j and i the same (and is the currently best).
    # The distance between `j` and `i` would change again if there is a longer subarray exist.
    # Try appending more 1s in nums you'll see.
    # In short:
    # We are looking for bigger window size, when we find one, we use this window to iterate till we find a larger one
    # (if any)."
    # -https://leetcode.com/problems/max-consecutive-ones-iii/discuss/247564/JavaC++Python-Sliding-Window/306089
