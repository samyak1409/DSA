"""
https://leetcode.com/problems/pass-the-pillow
"""


def pass_the_pillow(n: int, time: int) -> int:
    """"""

    # Maintain two integer variables, direction and i, where direction denotes the current direction in which the pillow
    # should pass, and `i` denotes an index of the person holding the pillow.
    # While time is positive, update the current index with the current direction. If the index reaches the end of the
    # line, multiply direction by - 1.
    # 0) Brute-force (Do the Passing): TC = O(time); SC = O(1)

    """
    pos = 1  # initially
    move = 1  # 1: move right, -1: move left
    for _ in range(time):  # O(time)
        # First, move:
        pos += move
        # Then, if at end of the line:
        if pos == n or pos == 1:
            # Change the direction of moving:
            move *= -1
    return pos
    """

    # 1) Optimal (Maths: %): TC = O(1); SC = O(1)
    # Better explanation than https://leetcode.com/problems/pass-the-pillow/solutions.

    # First, remove the complete cycles (when pillow reach back to 1):
    time %= (n-1) * 2

    # Then, if time < n => pillow will just be moved in the single direction and time will be over:
    if time < n:
        return time + 1  # (`+ 1` because start pos was 1)

    # Else, meaning direction will be changed and then the time will be over.
    # In this case we can compute the pos by:
    # `t - (n-1)`: moves in the opposite direction
    # `n - (t-(n-1))`: ans
    return 2*n - (time+1)
