"""
https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1
"""


def maximum_meetings(start: list[int], end: list[int]) -> int:
    """"""

    # 1) Optimal (Greedy: Sort by end time): TC = O(n*log(n)); SC = O(n)
    # Why are we sorting on the basis of end time?
    # Because:
    # 1) As we have to maximize the meeting count, we want to schedule the meeting which is ending earlier before.
    # 2) If we sort on the basis of start time, we won't know if the end time is low or high, it's not limited (capped),
    # but if sort on the basis of end time, as start time < end time, so we know that it's limited (capped)!
    # [Striver's Video Explanation](https://youtu.be/II6ziNnub1Q)

    ans = 0
    prev_et = -1  # -1 so that any `st` would be >
    for et, st in sorted(zip(end, start)):
        if st > prev_et:
            ans += 1  # this meeting scheduled
            prev_et = et  # update
    return ans


# Similar Questions:
# https://leetcode.com/problems/maximum-length-of-pair-chain
# https://practice.geeksforgeeks.org/problems/activity-selection-1587115620/1
