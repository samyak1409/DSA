"""
https://leetcode.com/problems/merge-intervals
"""


def merge(intervals: list[list[int]]) -> list[list[int]]:
    """"""

    # 0) [WA] Brute-force (Spilling the nums of all the intervals): TC = O(n^2); SC = O(n)
    # Tried a different logic but failed only and only due to the following case:
    # When intervals do not overlap but are contiguous. e.g.: [[1, 4], [5, 6]]
    # Following algorithm can't differentiate between the test cases [[1, 5], [4, 6]] and [[1, 4], [5, 6]]
    # And returns the same output for the both.

    """
    arr_start, arr_end = float('inf'), float('-inf')
    for interval in intervals:  # getting smallest and largest number among all intervals; TC = O(n)
        arr_start, arr_end = min(arr_start, *interval), max(arr_end, *interval)

    arr_len = arr_end - arr_start + 1
    arr = [False] * arr_len  # initialize an array with all `False`(s); SC = O(n)
    for interval in intervals:  # TC = O(n^2)
        start, end = interval[0]-arr_start, interval[1]-arr_start
        arr[start:end+1] = [True] * (end-start+1)  # insert `True` at all the indices which lie in an interval

    i = 0
    while i < arr_len:  # TC = O(n)
        if arr[i]:  # starting of an interval
            i_ = i  # saving start point
            while i+1 < arr_len and arr[i+1]:  # while interval continues
                i += 1
            yield [i_+arr_start, i+arr_start]  # [start, end] of the merged interval
        i += 1
    """

    # 1) Brute-force = Optimal (Sorting + Linear Merge): TC = O(n*log(n)); SC = O(n) {In Python, sorting is implemented
    # using the Timsort algorithm, which has a worst-case space complexity of O(n)}
    # https://leetcode.com/problems/merge-intervals/solution/#approach-2-sorting

    intervals = sorted(intervals, key=lambda interval: interval[0])  # sort by start value of the intervals;
    # new local var created

    prev = intervals[0]
    for i in range(1, len(intervals)):
        curr = intervals[i]
        if curr[0] <= prev[1]:  # => intervals are overlapping!
            prev[1] = max(prev[1], curr[1])  # merging
        else:
            yield prev  # adding the non-overlapping intervals to the output
            prev = curr  # updating previous in order to check if it can be merged with the following interval
    yield prev  # adding the last (overlapping/non-overlapping) interval to the output

    # [Extra]:
    # Not exactly related to this problem, just a new discovery about "Python":
    # From https://leetcode.com/problems/merge-intervals/discuss/21227/7-lines-easy-Python/21250, found this:
    # For sequences like List, `a += b` is not same as `a = a + b`.
    # `_ += _` will actually try to extend the current sequence with the sequence in RHS, whereas `_ = _ + _` will just
    # behave as expected.
    """
    a, b = [1, 2], [3, 4]
    print(id(a))  # 2002675308992
    a += b
    print(a)  # [1, 2, 3, 4]
    print(id(a))  # 2002675308992
    a = a + b
    print(a)  # [1, 2, 3, 4]
    print(id(a))  # 2002674932608
    """
    # Crazy Stuff 🤯
    # https://stackoverflow.com/questions/2347265/why-does-behave-unexpectedly-on-lists
    # https://stackoverflow.com/questions/6951792/a-b-not-the-same-as-a-a-b
    # https://stackoverflow.com/questions/57025897/concatenation-using-the-and-operators-in-python


# Similar Questions:
# https://leetcode.com/problems/insert-interval
# https://leetcode.com/problems/teemo-attacking
# https://leetcode.com/problems/partition-labels
# https://leetcode.com/problems/interval-list-intersections
# https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups
