"""
https://leetcode.com/problems/teemo-attacking
"""


def find_poisoned_duration(time_series: list[int], duration: int) -> int:
    """"""

    # 1) Optimal (Forming Intervals, Merging, Calculating): TC = O(n); SC = O(1)

    """
    n = len(time_series)
    # Forming the Time Intervals:
    for i in range(n):
        time_series[i] = [time_series[i], time_series[i]+duration-1]

    # Merging Overlapping Intervals in order to calc. Distinct Poisoned Durations:
    # https://github.com/samyak1409/DSA/blob/7cbe5e00f474eb6a0aee5e0b58d66296a59604c3/01%29%20Arrays/008%29%20Merge%20Intervals.py#L41
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
    # https://github.com/samyak1409/DSA/blob/7cbe5e00f474eb6a0aee5e0b58d66296a59604c3/01%29%20Arrays/008%29%20Merge%20Intervals.py#L41
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

    # Also see: https://leetcode.com/problems/teemo-attacking/solution
