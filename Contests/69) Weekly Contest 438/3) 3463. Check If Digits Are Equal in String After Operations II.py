"""
https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-ii
"""


def has_same_digits(s: str) -> bool:
    """"""

    # 0) [TLE] Brute-force (Nested Loop): TC = O(n^2); SC = O(n)

    # 1) [TLE] Sub-optimal (Combinations Pattern): TC = O(); SC = O()
    # Intuition:
    # If we focus on the freq of every digit, that how many times it's coming, and if you've done pascal's triangle,
    # then you'd observe it's that only. I mean we can calculate the total number of times all the digits need to be
    # added using pattern observed from combinations formula (pascal's triangle).
    # This way, we don't need two loops (nested).
    # https://github.com/samyak1409/DSA/blob/65ac81f284a16301b7532e404d2a4b35f682560d/SDE%20Sheet/01%29%20Arrays/002%29%20Pascal%27s%20Triangle.py
    #
    # A very good explanation:
    # https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-ii/solutions/6458127/how-to-notice-that-it-s-pascal-s-triangle-and-compute-it-if-you-re-not-a-mathematician
    #
    # TLE: Because `multiplier` becomes way larger, even when python doesn't have int limits, it becomes so large, calc.
    # results in TLE.

    # Convert to correct data structure:
    s = [int(d) for d in s]

    lt, rt = s[0], s[1]
    multiplier = 1
    # Loop, and calculate the next multiplier (freq of the digit basically), and calc. the left and right digit:
    for i in range(1, n:=len(s)-1):
        multiplier = (multiplier*(n-i)) // i
        lt = (lt + s[i]*(multiplier % 10)) % 10
        rt = (rt + s[i+1]*(multiplier % 10)) % 10

    return lt == rt

    # 2) Optimal ("Obscure" Maths): TC = O(); SC = O()
    # https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-ii/solutions/6458127/how-to-notice-that-it-s-pascal-s-triangle-and-compute-it-if-you-re-not-a-mathematician
