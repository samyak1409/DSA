"""
https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes
"""


def max_distance(s: str, k: int) -> int:
    """"""

    # 1) Optimal (Try all four cases, Greedy): TC = O(4*n); SC = O(1)
    # It was easy and intuitive!! Failed to come up with in the contest, quickly came up with on the next day.
    # https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/solutions/6360032/diagonals

    """
    k_ = k  # copying for future ref
    ans = 0

    # Trying all four cases one by one:
    for hm in ({'N': 1, 'S': -1, 'E': 1, 'W': -1},
               {'N': 1, 'S': -1, 'E': -1, 'W': 1},
               {'N': -1, 'S': 1, 'E': 1, 'W': -1},
               {'N': -1, 'S': 1, 'E': -1, 'W': 1}):

        d = 0  # manhattan distance
        mx = 0  # max (manhattan distance) at any point of time, since the beginning
        # Iterate on `s`:
        for c in s:
            # If char is +ve:
            if hm[c] == 1:
                d += 1
                mx = max(mx, d)
            # If char is -ve:
            else:
                # If we've k left, we'd be greedy and turn it into +ve:
                # (IMP: Since we're asked the max distance since the beginning, we can greedily apply `k` changes asap.
                # Think why.)
                if k:
                    k -= 1
                    d += 1
                    mx = max(mx, d)
                # Else only, we need to consider the -ve:
                else:
                    d -= 1

        ans = max(ans, mx)  # take the max ans
        k = k_  # reset `k`

    return ans
    """

    # Concise:

    # BTW, as short as possible:
    """
    k_, ans = k, 0
    for hs in ({'N', 'E'}, {'N', 'W'},  {'S', 'E'}, {'S', 'W'}):
        d = mx = 0
        for c in s:
            d += 1 if c in hs or (k := k-1) >= 0 else -1
            mx = max(mx, d)
        ans, k = max(ans, mx), k_
    return ans
    """

    k_ = k  # copying for future ref
    ans = 0

    # Trying all four cases one by one:
    for hs in ({'N', 'E'}, {'N', 'W'},  {'S', 'E'}, {'S', 'W'}):

        d = 0  # manhattan distance
        mx = 0  # max (manhattan distance) at any point of time, since the beginning
        # Iterate on `s`:
        for c in s:
            # If char is +ve,
            # OR
            # If we've k left, we'd be greedy and turn it into +ve:
            # (IMP: Since we're asked the max distance since the beginning, we can greedily apply `k` changes asap.
            # Think why.)
            if c in hs or (k := k-1) >= 0:
                d += 1
                mx = max(mx, d)
            # If char is -ve AND no `k` left, we need to consider the -ve:
            else:
                d -= 1

        ans = max(ans, mx)  # take the max ans
        k = k_  # reset `k`

    return ans
