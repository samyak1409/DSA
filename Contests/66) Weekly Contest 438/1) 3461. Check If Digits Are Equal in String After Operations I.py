"""
https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i
"""


def has_same_digits(s: str) -> bool:
    """"""

    # 0) Brute-force (Simulate: Loop): TC = O(n^2); SC = O(n)

    """
    # Convert to correct data structure:
    s = [int(d) for d in s]

    # "until it has exactly two digits":
    while len(s) != 2:
        # Operation:
        s = [(s[i]+s[i+1])%10 for i in range(len(s)-1)]
        # print(s)  # debug

    return s[0] == s[1]
    """

    # From `3463.` (Problem 3 of this contest):

    # 1) Sub-optimal (Combinations Pattern): TC = O(n); SC = O(n)
    # But, TC is not actually O(n) as `n` grows bigger. Check Problem 3. :(

    # Convert to correct data structure:
    s = [int(d) for d in s]

    lt, rt = s[0], s[1]
    multiplier = 1
    # Loop, and calculate the next multiplier (freq of the digit basically), and calc. the left and right digit:
    for i in range(1, n:=len(s)-1):
        multiplier = (multiplier*(n-i)) // i
        print(multiplier)
        lt = (lt + s[i]*(multiplier % 10)) % 10
        rt = (rt + s[i+1]*(multiplier % 10)) % 10

    return lt == rt
