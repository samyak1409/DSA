"""
https://leetcode.com/problems/find-the-most-common-response
"""


def find_common_response(rs: list[list[str]]) -> str:
    """"""

    # If there were a definite types of responses, we could've used something like:

    """
    hm = {'bad': 0, 'good': 0, 'ok': 0}  # imp: already kept in sorted order
    mx = 0  # track most common count
    for arr in rs:
        for r in set(arr):
            hm[r] += 1
            mx = max(mx, hm[r])

    # Loop on our responses, and whichever count `c` match first with `mx` is the ans:
    for r, c in hm.items():
        if c == mx:
            return r
    """

    # But since there are indefinite types of responses in this question:

    # 1) Suboptimal (HashMap, Sort): TC = O(m*n*log2(m*n)); SC = O(m*n)
    # (In the worst case, every response there in the 2d array is distinct, hence `m*n`.)

    """
    from collections import defaultdict

    # `defaultdict` hm to easily count:
    freq = defaultdict(int)  # SC = O(m*n)
    # Count freq:
    for arr in rs:  # TC = O(m)
        for r in set(arr):  # TC = SC = O(n)
            freq[r] += 1

    # Sort by decreasing order of freq, increasing order of responses, and return the first val: TC = O(m*n*log2(m*n))
    return sorted(freq, key=lambda r: (-freq[r], r))[0]
    """

    # 2) Optimal (HashMap): TC = O(m*n); SC = O(m*n)
    # (In the worst case, every response there in the 2d array is distinct, hence `m*n`.)
    # We don't actually need to sort.
    # https://leetcode.com/problems/find-the-most-common-response/solutions/6689354/count-with-hashmap-c-python
    # https://leetcode.com/problems/find-the-most-common-response/solutions/6694634/python-elegant-short-hashmap

    """
    from collections import defaultdict

    # `defaultdict` hm to easily count:
    freq = defaultdict(int)  # SC = O(m*n)
    # Count freq:
    for arr in rs:  # TC = O(m)
        for r in set(arr):  # TC = SC = O(n)
            freq[r] += 1

    # First, get the maximum freq: # TC = SC = O(m*n)
    max_freq = max(freq.values())
    # Then return the smallest response (lexicographically) with that max freq: # TC = O(m*n)
    return min(r for r, c in freq.items() if c == max_freq)
    """

    # Concisely written:

    from collections import Counter

    # Count freq: TC = SC = O(m*n)
    freq = Counter(r for arr in rs for r in set(arr))
    # Return the response with max freq, if same, then min lexicographical value: TC = O(m*n)
    return min(freq, key=lambda r: (-freq[r], r))
