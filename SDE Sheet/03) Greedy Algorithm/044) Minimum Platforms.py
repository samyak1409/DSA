"""
https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1
"""


def minimum_platform(arr: list[int], dep: list[int]):
    """"""

    # 0) Brute-force (Sort on arrival time; Linear Search; Greedy): TC = O(n^2); SC = O(n)
    # Intuitive: So, to solve this problem, what one would do in real world is:
    # First train comes, so platform 1.
    # Second train comes, if first train has left, platform 1, else new platform.
    # Third train comes, check one by one on each of the platform, and whichever is empty, put this train on that. If no
    # platform is empty, one more platform is needed.
    # And so on.
    # So, we need to sort on the basis on arrival time of the train. (Sorting on the basis of departure time would be
    # WA.) And sorting on arrival time is pretty intuitive too, and that's what we'd do in real world to get the minimum
    # no. of platforms using this approach.

    """
    pass
    """

    # 1) Sub-optimal: TC = O(n*log(n)); SC = O(n)

    # 1.1) (Intuitive) Sort on arrival time; Min Heap; Greedy:
    # This approach is an improvement on `0)`.
    # If we keep a min heap of departure times of the trains, we can compare the upcoming train's arrival time with the
    # min departure time in heap. If at > min(dt), we do not need a new platform, else we do.
    # Why min heap? Because it'd be optimal to put upcoming train to the platform which is emptied the earliest.
    # By using heap we're reducing the platform finding time from O(n) (linear search) to O(log(n)).

    """
    from heapq import heappush, heappop

    dt_heap = []

    # Iterate on sorted trains (based on arrival time):
    for at, dt in sorted(zip(arr, dep)):
        # If this train's `at` > minimum `dt` on our current platforms:
        if dt_heap and at > dt_heap[0]:  # (`dt_heap[0]` gives min of `dt_heap`)
            # Then we can put this train to existing platform (`pop` + `push` outside `if`):
            heappop(dt_heap)
        # Else, we need to assign one more platform (just `push`):
        heappush(dt_heap, dt)

    # At the end, return len of total assigned platforms:
    return len(dt_heap)
    """

    # 1.2) Sort together on the basis of time:
    # Not very intuitive to come up with, but very easy after knowing.
    # Approach Explanation: https://youtu.be/AsGzwR_FWok?t=534

    """
    from itertools import chain

    ans = platforms = 0
    # Loop on sorted events: `(t, event)` where `t` = timestamp, `event` = `0` (means arrival) or `1` (means departure):
    # e.g. arr = [1000, 1200], dep = [1500, 1300]
    # sorted events = (1000, 0), (1200, 0),  (1300, d), (1500, d)
    # So, at 1000, platforms += 1, so 1
    # at 1200, platforms += 1, so 2
    # at 1300, platforms -= 1, so 1
    # at 1500, platforms -= 1, so 0
    # So, at any point of time, max = 2 = ans.
    # (Also, note that we want to make sure that when `at` == `dt`, `at` comes before. Reason to use `0` for `at`.)
    for t, event in sorted(chain([(at, 0) for at in arr], [(dt, 1) for dt in dep])):
        if event == 0:  # arrival
            platforms += 1
            ans = max(ans, platforms)
        else:  # departure
            platforms -= 1
    return ans
    """


    # 2) Optimal (Counting Sort + `1.2)`): TC = O(n); SC = O(2359)
    # Just using counting sort as sorting to the approach `1.2)`.

    # WA due to the edge case when `at` == `dt`:
    """
    # Array init:
    events = [0] * (2359+1)
    # Counting:
    for time in arr:
        events[time] = 1
    for time in dep:
        events[time] = -1
    # Process:
    ans = platforms = 0
    for event in events:
        platforms += event
        ans = max(ans, platforms)
    return ans
    """

    # So, we can't directly use `int`, since for a particular index, both `at` & `dt` can be there, so using `list`:
    # Array init:
    events = [[] for _ in range(2359+1)]
    # Counting:
    for time in arr:
        events[time].append(1)
    for time in dep:
        events[time].append(-1)
    # Process:
    ans = platforms = 0
    for event in events:
        for e in event:
            platforms += e
            ans = max(ans, platforms)
    return ans

    # This approach can also be called Sweep Line Algorithm (https://en.wikipedia.org/wiki/Sweep_line_algorithm).
    # Article:
    # https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/#expected-approach-using-sweep-line-algorithm-on-time-and-o1-auxiliary-space
    # Video:
    # https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1 > Editorial > Video
