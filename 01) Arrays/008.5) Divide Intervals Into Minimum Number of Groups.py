"""
https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups
"""


def min_groups(intervals: list[list[int]]) -> int:
    """"""

    # 0) [TLE] Brute-force (Sort; For each interval, find the group linearly): TC = O(n^2); SC = O(n)

    """
    # Divide the intervals into groups sequentially:
    groups = []
    for interval in sorted(intervals):  # go through each interval one by one; O(n^2)
        # (Note: `sorted(intervals)` by default sorts on the basis of first value of each item, so no need of `key`.)
        for group in groups:  # search for the compatible group for this interval; O(n)
            if group[-1][1] < interval[0]:  # `group[-1]`: last interval in the group
                # => `interval` is not intersecting, so add in this group and stop
                group.append(interval)
                break
        else:  # if this interval is intersecting in all the groups, make a new group
            groups.append([interval])
    return len(groups)
    """

    # The main problem in this approach is the linear searching of the compatible group for every interval.
    # That's O(n) TC, if by anyway we reduce this to O(log(n)); we will get at the optimal TC i.e. O(n*log(n)),
    # because sorting the `intervals` take O(n*log(n)) anyway, and it gets accepted.
    # (Just submitting sorting part gives WA not TLE => O(n*log(n)) is accepted!)

    # 1) Optimal (Sort; For each interval, directly check for the group by keeping the groups sorted):
    # TC = O(n*log(n)); SC = O(n)
    # What we can do is:
    # 1) Will only keep interval[1] i.e. end values of intervals in `groups`.
    # 2) And, will keep `groups` sorted, so that we won't need to linear search whole `groups`, but checking the first
    #    value will only be required.

    # 1.0) Using normal array: O(n^2)
    """
    from bisect import insort

    # Divide the intervals into groups sequentially:
    groups = []
    for start, end in sorted(intervals):  # go through each interval one by one; O(n^2)
        '''
        if groups and groups[0] < start:  # => compatible group is there
            # updating the existing group with the new interval:
            groups.pop(0)  # removing
            insort(a=groups, x=end)  # adding, keeping it sorted
        else:  # => no compatible group is there
            insort(a=groups, x=end)  # so add a new group, keeping it sorted
        '''
        # Combined:
        if groups and groups[0] < start:
            groups.pop(0)  # O(n)
        insort(a=groups, x=end)  # O(log(n))
    return len(groups)
    """

    # 1.1) Using `deque` (https://docs.python.org/3.11/library/collections.html#collections.deque): O(n*log(n))
    """
    from collections import deque
    from bisect import insort

    # Divide the intervals into groups sequentially:
    groups = deque()
    for start, end in sorted(intervals):  # go through each interval one by one; O(n*log(n))
        if groups and groups[0] < start:
            groups.popleft()  # O(1)
        insort(a=groups, x=end)  # O(log(n))
    return len(groups)
    """

    # 1.2) Using Heap: O(n*log(n))
    # https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/solutions/2560020/min-heap
    from heapq import heappop, heappush

    # Divide the intervals into groups sequentially:
    groups = []
    for start, end in sorted(intervals):  # go through each interval one by one; O(n*log(n))
        if groups and groups[0] < start:
            heappop(groups)  # O(log(n))
        heappush(groups, end)  # O(log(n))
    return len(groups)

    # How is this (very) faster than `deque` one??
