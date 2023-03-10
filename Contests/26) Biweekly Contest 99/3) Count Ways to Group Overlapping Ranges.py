"""
https://leetcode.com/problems/count-ways-to-group-overlapping-ranges
"""


def count_ways(ranges: list[list[int]]) -> int:
    """"""

    # Can we use sorting here?
    # Sort the ranges and merge the overlapping ranges. Then count number of non-overlapping ranges.
    # How many ways can we group these non-overlapping ranges?

    # 1) Optimal (Find the number of non-overlapping ranges, Return 2^it): TC = O(n*log(n)); SC = O(n)
    # i) Count non-overlapping ranges (Similar to https://leetcode.com/problems/merge-intervals)
    # ii) Return total no. of ways these non-overlapping ranges can be grouped in 2 (Ways = 2 ^ count)
    # https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/solutions/3256371/java-c-python-sort-solution

    ans = 1
    prev_end = -1
    for (start, end) in sorted(ranges):  # loop on sorted ranges
        if start > prev_end:  # if not overlapping
            ans = ans*2 % 1000_000_007  # multiply by 2; mod on every iteration to avoid overflow (TLE for Python)
        prev_end = max(prev_end, end)  # update for next
    return ans
