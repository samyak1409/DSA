"""
https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k
"""


def minimum_partition(s: str, k: int) -> int:
    """"""

    # 1) Optimal (Sliding Window): TC = O(n); SC = O(1)
    # https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k/solutions/2977270/greedy

    sub_str = 0
    parts = 1
    for digit in s:
        digit = int(digit)
        if digit > k:  # if single digit itself > k, then "The value of each substring <= k." is not possible
            return -1
        sub_str = sub_str*10 + digit  # increase the window size
        if sub_str > k:  # if sub_str goes > k, do partition
            parts += 1
            sub_str = digit
    return parts
