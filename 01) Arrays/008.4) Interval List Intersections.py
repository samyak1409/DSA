"""
https://leetcode.com/problems/interval-list-intersections
"""


def interval_intersection(list1: list[list[int]], list2: list[list[int]]) -> list[list[int]]:
    """"""

    # 1) Optimal (Linearly Checking Intersections): TC = O(m+n); SC = O(1)
    # https://leetcode.com/problems/interval-list-intersections/solution
    # https://leetcode.com/problems/interval-list-intersections/discuss/647482/Python-Two-Pointer-Approach-+-Thinking-Process-Diagrams

    # Traversing like: https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/009%29%20Merge%20Sorted%20Array.py
    i = j = 0
    m, n = len(list1), len(list2)
    while i < m and j < n:
        interval1, interval2 = list1[i], list2[j]
        (start1, end1), (start2, end2) = interval1, interval2
        # Checking Intersection:
        bigger_start, smaller_end = max(start1, start2), min(end1, end2)
        # "The intersection of two closed intervals is a set of real numbers that are either empty or represented as a
        # closed interval. For example, the intersection of [1, 3] & [2, 4] is [2, 3]."
        if bigger_start <= smaller_end:  # if valid interval (will ignore e.g. [13, 12] because start > end)
            # print(interval1, interval2, [bigger_start, smaller_end])  #debugging
            yield [bigger_start, smaller_end]  # INTERSECTION
        # Moving to Next Interval:
        if end1 < end2:
            i += 1
        elif end1 > end2:
            j += 1
        else:  # (if end1 == end2)
            i, j = i+1, j+1
