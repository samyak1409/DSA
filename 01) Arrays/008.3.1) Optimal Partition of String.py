"""
https://leetcode.com/problems/optimal-partition-of-string
"""


def partition_string(s: str) -> int:
    """"""

    # 1) Optimal (HashSet): TC = O(n); SC = O(1) {s consists of only English lowercase letters.}

    hashset = set()  # store unique chars of current substring
    partitions = 0
    for char in s:
        if char in hashset:  # => do partition
            partitions += 1
            hashset.clear()  # to store unique chars of next substring
        hashset.add(char)
    return partitions + 1  # = no. of substrings
