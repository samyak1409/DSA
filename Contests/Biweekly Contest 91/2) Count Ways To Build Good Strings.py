"""
https://leetcode.com/problems/count-ways-to-build-good-strings
"""


def count_good_strings(low: int, high: int, zero: int, one: int) -> int:
    """"""

    # 0) [TLE] Brute-force (Recursion: Find every possible string): TC = O(2^high); {branches ^ depth}
    #                                                               SC = O(high) {max depth of recursion stack}

    # Recursive Function:
    def recurse(length: int = 0) -> int:
        if length > high:  # base case: length exceeded
            return 0  # stop recursion from this node
        x = 0
        if length >= low:  # if a good string is constructed, consider it and go ahead
            x = 1
        return x + recurse(length+zero) + recurse(length+one)  # recurse in (two edges of every node)

    return recurse() % 1_000_000_007  # calc using recursion

    # 1) Optimal (DP): TC = O(high); SC = O(high)
    # Calculate the number of good strings with length less or equal to some constant x.
    # Apply dynamic programming using the group size of consecutive zeros and ones.
    # https://leetcode.com/problems/count-ways-to-build-good-strings/solutions
