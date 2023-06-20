"""
https://practice.geeksforgeeks.org/problems/activity-selection-1587115620/1
"""


def activity_selection(n: int, start: list[int], end: list[int]) -> int:
    """"""

    # Same as:
    # https://github.com/samyak1409/DSA/blob/main/SDE%20Sheet/03%29%20Greedy%20Algorithm/043%29%20N%20Meetings%20in%20One%20Room.py

    # https://en.wikipedia.org/wiki/Activity_selection_problem

    # 1) Optimal (Greedy: Sort by end time): TC = O(n*log(n)); SC = O(n)

    count = 0
    prev_et = None
    for st, et in sorted(zip(start, end), key=lambda tup: tup[1]):
        if prev_et is None or st > prev_et:
            count += 1  # this meeting scheduled
            prev_et = et  # update
    return count


# Similar Questions:
# https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1
