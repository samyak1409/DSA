"""
https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured
"""


def capture_forts(forts: list[int]) -> int:
    """"""

    # 0) Brute-force (Nested Loop): TC = O(n^2); SC = O(1)
    # For each fort under your command, check if you can move the army from here.
    # If yes, find the closest empty positions satisfying all criteria.

    """
    n = len(forts)
    ans = 0
    for i in range(n):
        if (fort_i := forts[i]) != 0:  # start from our own fort (fort == 1) or empty fort (fort == -1)
            for j in range(i+1, n):
                if (fort_j := forts[j]) != 0:  # => reached at a non-enemy fort (i.e. either empty fort or our own fort)
                    if fort_j + fort_j == 0:  # verifying is the stop valid
                        ans = max(ans, j-i-1)  # update ans if required
                    break  # "The army travels over enemy forts only."
    return ans
    """

    # How can two-pointers be used to solve this problem optimally?

    # 1) Optimal: TC = O(n); SC = O(1)

    # 1.1) https://leetcode.com/problems/max-consecutive-ones Style:
    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/042%29%20Max%20Consecutive%20Ones.py

    """
    curr = max_ = 0  # streak
    for i in range(1, len(forts)-1):
        if forts[i] == 0:
            curr += 1
            if (left := forts[i-curr])+forts[i+1] == 0 and left:  # checking if the streak is surrounded by 1 and -1
                max_ = max(max_, curr)  # update ans
        else:
            curr = 0  # reset
    return max_
    """

    # 1.2)
    # Basically, we need to count zeros between the opposite non-zero elements (1 and -1, or -1 and 1).
    # https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/solutions/2947175/one-pass

    lt = 0  # init
    ans = 0
    for rt, fort in enumerate(forts):
        if fort != 0:  # if our own fort (fort == 1) or empty fort (fort == -1)
            if forts[lt] + fort == 0:  # checking if the streak is surrounded by 1 and -1
                ans = max(ans, rt-lt-1)  # update ans
            lt = rt  # update left
    return ans
