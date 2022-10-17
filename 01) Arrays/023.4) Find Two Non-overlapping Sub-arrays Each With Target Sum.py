"""
https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum
"""


def min_sum_of_lengths(arr: list[int], target: int) -> int:
    """"""

    # Let's create two arrays prefix and suffix where prefix[i] is the minimum length of sub-array ends before i and has
    # sum = k, suffix[i] is the minimum length of sub-array starting at or after i and has sum = k.
    # The answer we are searching for is min(prefix[i] + suffix[i]) for all values of i from 0 to n-1 where
    # n == arr.length.
    # If you are still stuck with how to build prefix and suffix, you can store for each index i the length of the
    # sub-array starts at i and has sum = k or infinity otherwise, and you can use it to build both prefix and suffix.

    # https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/discuss
