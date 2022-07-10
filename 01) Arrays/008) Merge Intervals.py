"""
https://leetcode.com/problems/merge-intervals
"""


from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:

    # 1) Brute-force = Optimal (Sorting + Linear Merge): TC = O(n*log(n)); SC = O(1)

    intervals.sort(key=lambda x: x[0])  # sort by start value of the intervals; TC = O(n*log(n))

    previous = intervals[0]
    for i in range(1, len(intervals)):  # TC = O(n)
        interval = intervals[i]
        if previous[1] >= interval[0]:  # => intervals are overlapping!
            previous[1] = max(previous[1], interval[1])  # merging
        else:
            yield previous  # adding the non-overlapping intervals to the output
            previous = interval  # saving the current interval in order to check if it can be merged with the following interval
    yield previous  # adding the last (overlapping/non-overlapping) interval to the output
