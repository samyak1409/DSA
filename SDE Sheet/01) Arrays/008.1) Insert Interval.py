"""
https://leetcode.com/problems/insert-interval
"""


def insert(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    """"""

    # 1) Optimal (Liner - Insert & Merge): TC = O(n); SC = O(1)
    # https://leetcode.com/problems/insert-interval/discuss

    n = len(intervals)
    # Inserting the New Interval:
    for i in range(n):
        if intervals[i][0] > new_interval[0]:
            intervals.insert(i, new_interval)
            break
    else:  # handling edge cases: if intervals = [] or interval[-1][0] <= new_interval[0]
        intervals.append(new_interval)

    # Merging Any Overlapping Intervals (if formed after insertion):
    # https://github.com/samyak1409/DSA/blob/main/SDE%20Sheet/01%29%20Arrays/008%29%20Merge%20Intervals.py
    prev = intervals[0]
    for i in range(1, n+1):
        curr = intervals[i]
        if curr[0] <= prev[1]:  # => intervals are overlapping!
            prev[1] = max(prev[1], curr[1])  # merging
        else:
            yield prev  # adding the non-overlapping intervals to the output
            prev = curr  # updating previous in order to check if it can be merged with the following interval
    yield prev  # adding the last (overlapping/non-overlapping) interval to the output
