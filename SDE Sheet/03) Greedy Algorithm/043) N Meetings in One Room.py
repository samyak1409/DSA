"""
https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1
"""


def maximum_meetings(n: int, start: list[int], end: list[int]) -> int:
    """"""

    # 1) Optimal (Greedy: Sort by end time): TC = O(n*log(n)); SC = O(n)
    # Why are we sorting on the basis of end time?
    # Because:
    # 1) As we have to maximize the meeting count, we want to schedule the meeting which is ending earlier before.
    # 2) If we sort on the basis of start time, we won't know if the end time is low or high, it's not limited (capped),
    # but if sort on the basis of end time, as start time < end time, so we know that it's limited (capped)!
    # [Striver's Video Explanation](https://youtu.be/II6ziNnub1Q)

    count = 0
    prev_et = None
    for st, et in sorted(zip(start, end), key=lambda tup: tup[1]):
        if prev_et is None or st > prev_et:
            count += 1  # this meeting scheduled
            prev_et = et  # update
    return count


# Similar Questions:
# https://practice.geeksforgeeks.org/problems/activity-selection-1587115620/1
