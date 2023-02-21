"""
https://leetcode.com/problems/check-distances-between-same-letters
"""


def check_distances(s: str, distance: list[int]) -> bool:
    """"""

    # 1) Optimal (Frequency Array): TC = O(n); SC = O(n) but as "string s consisting of only lowercase English letters,
    # where each letter in s appears exactly twice", so TC = O(52) = O(1); SC = O(26) = O(1)
    # Create an integer array of size 26 to keep track of the first occurrence of each letter.
    # The number of letters between indices i and j is j - i - 1.

    # Calc Distances:
    real_distance = [-1] * 26  # real_distance[0] will be for 'a', and so on
    for i, letter in enumerate(s):
        if (i_old := real_distance[j := ord(letter)-97]) == -1:  # => letter's first occurrence
            real_distance[j] = i  # save index
        else:  # => letter's second occurrence
            real_distance[j] = i - i_old - 1  # save distance

    # Match Distances:
    for real, expected in zip(real_distance, distance):
        if real != -1 and real != expected:
            # `real != -1`: because "If the ith letter does not appear in s, then distance[i] can be ignored."
            return False
    return True
