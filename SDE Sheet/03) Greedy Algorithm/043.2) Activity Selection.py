"""
https://practice.geeksforgeeks.org/problems/activity-selection-1587115620/1
"""


def activity_selection(start: list[int], end: list[int]) -> int:
    """"""

    # Same as:
    # https://github.com/samyak1409/DSA/blob/main/SDE%20Sheet/03%29%20Greedy%20Algorithm/043%29%20N%20Meetings%20in%20One%20Room.py

    # https://en.wikipedia.org/wiki/Activity_selection_problem

    # 1) Optimal (Greedy: Sort by end time): TC = O(n*log(n)); SC = O(n)

    ans = 0
    prev_et = -1  # -1 so that any `st` would be >
    for et, st in sorted(zip(end, start)):
        if st > prev_et:
            ans += 1  # this activity selected
            prev_et = et  # update
    return ans
