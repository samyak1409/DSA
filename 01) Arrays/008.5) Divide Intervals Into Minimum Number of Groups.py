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
    #    value will only be required. Why? Because the first value will be the least end of them all, and
    #    -> if it's < than current interval start this means we can add the current interval to this group, and we'll
    #       update the end, and
    #    -> if it's not, that mean no other following `end` will be < than current interval start (because obviously
    #       groups is sorted), in this case we'll just create a new group.
    #    For keeping `groups` sorted, we can use `bisect.insort`, but, "The insort() functions are O(n) because the
    #    logarithmic search step is dominated by the linear time insertion step."
    #    -https://docs.python.org/3.11/library/bisect.html#performance-notes, so this will lead us to O(n^2) again,
    #    Then what can we do? Heaps (Priority Queues)! O(log(n)) Push & Pop.
    #    (https://stackoverflow.com/questions/38806202/whats-the-time-complexity-of-functions-in-heapq-library#:~:text=heapq%20is%20a%20binary%20heap%2C%20with%20O(log%20n)%20push%20and%20O(log%20n)%20pop.)
    # https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/solutions/2560020/min-heap

    from heapq import heappop, heappush

    # Divide the intervals into groups sequentially:
    groups = []
    for start, end in sorted(intervals):  # go through each interval one by one; O(n*log(n))
        if groups and groups[0] < start:
            heappop(groups)  # O(log(n))
        heappush(groups, end)  # O(log(n))
    return len(groups)
