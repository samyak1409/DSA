"""
https://leetcode.com/problems/optimal-partition-of-string
"""


def partition_string(s: str) -> int:
    """"""

    # 1) Optimal (Greedy + HashSet): TC = O(n); SC = O(1) {s consists of only English lowercase letters.}
    # Try to come up with a greedy approach.
    # From left to right, extend every substring in the partition as much as possible.

    hashset = set()  # store unique chars of current substring
    partitions = 0
    for char in s:
        if char in hashset:  # => do partition
            partitions += 1
            hashset.clear()  # to store unique chars of next substring
        hashset.add(char)
    return partitions + 1  # = no. of substrings
