"""
https://leetcode.com/problems/teemo-attacking
"""


def find_poisoned_duration(time_series: list[int], duration: int) -> int:
    """"""

    # 1) Optimal: TC = O(n); SC = O(1)

    # 1.0) Using concept of `008 Merge Intervals.py`:
    # Not much appreciable because next solutions are more intuitive (if you don't attempt this question keeping in mind
    # that it's Similar of `008 Merge Intervals.py`) as well as fast.
    """
    n = len(time_series)
    # Forming the Time Intervals:
    for i in range(n):
        time_series[i] = [time_series[i], time_series[i]+duration-1]
    # Merging Overlapping Intervals in order to calc. Distinct Poisoned Durations:
    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/008%29%20Merge%20Intervals.py
    poisoned_duration = 0
    prev = time_series[0]
    for i in range(1, n):
        curr = time_series[i]
        if curr[0] <= prev[1]:  # => intervals are overlapping!
            prev[1] = max(prev[1], curr[1])  # merging
        else:
            poisoned_duration += prev[1]-prev[0]+1  # adding the non-overlapping intervals to the output
            prev = curr  # updating previous in order to check if it can be merged with the following interval
    return poisoned_duration + prev[1]-prev[0]+1  # adding the last (overlapping/non-overlapping) interval to the output
    """
    # OTG Forming the Time Intervals and Merging Overlapping Intervals in order to calc. Distinct Poisoned Durations:
    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/008%29%20Merge%20Intervals.py
    """
    poisoned_duration = 0
    prev = [time_series[0], time_series[0]+duration-1]
    for i in range(1, len(time_series)):
        curr = [time_series[i], time_series[i]+duration-1]
        if curr[0] <= prev[1]:  # => intervals are overlapping!
            prev[1] = max(prev[1], curr[1])  # merging
        else:
            poisoned_duration += prev[1]-prev[0]+1  # adding the non-overlapping intervals to the output
            prev = curr  # updating previous in order to check if it can be merged with the following interval
    return poisoned_duration + prev[1]-prev[0]+1  # adding the last (overlapping/non-overlapping) interval to the output
    """

    # 1.1) Add duration for current attack time, then while doing the same for next, un-consider any overlapping
    # poisoned duration from the previous attack:
    """
    poisoned_duration = 0
    prev = -1  # point of time at which the previous attack's poison ended; init with -1 coz `0 <= time_series[i]`
    for t in time_series:  # t: point of time (e.g. 1st sec.) at which attack will start
        '''
        poisoned_duration += duration
        if prev >= t:  # if overlapping poisoned duration
            poisoned_duration -= prev-t+1  # subtract it
        '''
        poisoned_duration += duration - max(prev-t+1, 0)  # `- max(prev-t+1, 0)`: subtract overlapping poisoned duration
        prev = t + duration - 1  # update
    return poisoned_duration
    """

    # 1.2) "If he attacks again before the poison effect ends, the timer for it resets, and the poison effect will end
    # `duration` seconds after the new attack."
    # Exactly doing this:
    # Poisoned duration is nothing but `duration` seconds from an attack start point, but if new attack starts when the
    # poison from the last attack is still there, then the remaining `duration` will just become 0.
    # https://leetcode.com/problems/teemo-attacking/solution

    poisoned_duration = 0
    for i in range(len(time_series)-1):  # traverse all the attack start points other than last
        poisoned_duration += min(duration, time_series[i+1]-time_series[i])  # poisoned_duration will just be the
        # minimum of normal_poison_duration and the distance b/w next attack start and current attack start
    return poisoned_duration + duration if time_series else 0  # adding the duration which is for the last attack only
    # if time_series is not empty (which is edge case)
