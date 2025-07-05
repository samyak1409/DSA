"""
https://leetcode.com/problems/partition-string
"""


def partition_string(s: str) -> list[str]:
    """"""

    # 1) Optimal (Simulate: Loop, HashMap): TC = O(n*sqrt(n)); SC = O(n)
    # Solution is straight-forward, time complexity analysis is not.
    # The time complexity of the algorithm is O(n*sqrt(n)).
    # This is because the work done to find each segment is proportional to the square of its length (O(l^2)).
    # A crucial insight is that to form a segment of length l, you must have previously formed segments for all of its
    # prefixes (lengths 1, 2, ..., L-1).
    # This limits the maximum possible segment length to be O(sqrt(n)).
    # Combining these facts, the total time complexity is bounded by N times the maximum segment length, resulting in
    # O(n*sqrt(n)).

    """
    curr = ''
    hs = set()
    ans = []

    for c in s:
        curr += c
        if curr not in hs:
            hs.add(curr)
            ans.append(curr)
            curr = ''

    return ans
    """

    # Since `dict` conserves the insertion order, we can just use `dict` instead of having to use `set` + `list`:

    curr, hm = '', {}
    for c in s:  # TC = O(n)
        curr += c  # TC = O(sqrt(n))
        if curr not in hm:
            hm[curr], curr = True, ''
    return list(hm)
