"""
https://leetcode.com/problems/count-ways-to-build-good-strings
"""


def count_good_strings(low: int, high: int, zero: int, one: int) -> int:
    """"""

    # 0) [TLE] Brute-force (Recursion: Find every possible string): TC = O(2^high); {branches ^ depth}
    #                                                               SC = O(high) {max depth of recursion stack}

    # Recursive Function:
    def recurse(length: int = 0):
        if length > high:  # base case: length exceeded
            return  # stop recursion from this node
        if length >= low:  # check if 1 good string constructed and continue
            count[0] += 1
        recurse(length+zero), recurse(length+one)  # recurse in (two edges of every node)

    count = [0]  # using `list` because `int` is immutable
    recurse()  # calc using recursion
    return count[0] % 1_000_000_007

    # 1) Optimal (DP): TC = O(?); SC = O(?)
    # Calculate the number of good strings with length less or equal to some constant x.
    # Apply dynamic programming using the group size of consecutive zeros and ones.
    # https://leetcode.com/problems/count-ways-to-build-good-strings/discuss
