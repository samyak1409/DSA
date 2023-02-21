"""
https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps
"""


def number_of_ways(start_pos: int, end_pos: int, k: int) -> int:
    """"""

    # Similar to:
    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/017%29%20Unique%20Paths.py

    # 0) [TLE] Brute-force (Recursion to check every possible ways):
    # TC = O(2^k) (branches = 2; max_depth = k); SC = O(k) {recursion stack}

    """
    # Recursive Function:
    def recurse(pos: int = start_pos, moves_left: int = k) -> int:
        # Base Case (Moved k times):
        if moves_left == 0:  # "exactly k steps"
            return pos == end_pos  # return 1 if we are on the end_pos after this particular path & recurse out
        # Recurse in:
        return recurse(pos-1, moves_left-1) + recurse(pos+1, moves_left-1)  # move left & right
    
    return recurse() % 1_000_000_007
    """

    # 1) Sub-Optimal (Recursion w/ Memoization):
    # TC = O(k^2) (how? because we can have at most k * k unique combinations of the two parameters of our memoized
    # recursion function viz. `pos` and `moves_left`); SC = O(k^2 + k) {memoization + recursion stack}

    """
    # Recursive Function:
    @cache
    def recurse(pos: int = start_pos, moves_left: int = k) -> int:
        # Base Case (Moved k times):
        if moves_left == 0:  # "exactly k steps"
            return pos == end_pos  # return 1 if we are on the end_pos after this particular path & recurse out
        # Recurse in:
        return (recurse(pos-1, moves_left-1) + recurse(pos+1, moves_left-1)) % 1_000_000_007  # move left & right
    
    return recurse()
    """

    # 1) Optimal (Combinatorics): TC = O(k*log(k)); SC = O(1)
    # How many steps to the left and to the right do you need to make exactly?
    # Does the order of the steps matter?
    # Use combinatorics to find the number of ways to order the steps.

    # "With one step, you can move either one position to the left, or one position to the right."
    # "perform exactly k steps."
    # => left_moves + right_moves = k  ...(1)
    # "reach the position endPos starting from startPos"
    # => right_moves - left_moves = end_pos - start_pos  ...(2)
    # Now, if we add eqn 1 & 2:
    # => 2 * right_moves = k + end_pos-start_pos
    # => right_moves = (k + end_pos-start_pos) // 2
    # And, if we find the ways in which we can select the right_moves out of the total moves which we have to make i.e.
    # k, we'll get the ans! (like https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/017%29%20Unique%20Paths.py)
    # Source:
    # https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/solutions/2527381/java-c-python-math-solution-o-klogk

    from math import comb

    gap = end_pos - start_pos

    if gap % 2 != k % 2:  # if gap is even and steps is odd, or vice versa, then there can't be any way
        return 0

    return comb(k, (k+gap)//2) % 1_000_000_007
