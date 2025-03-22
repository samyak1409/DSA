"""
https://leetcode.com/problems/minimum-number-of-operations-to-convert-time
"""


def convert_time(current: str, correct: str) -> int:
    """"""

    # Same logic as:
    # https://github.com/samyak1409/DSA/blob/main/SDE%20Sheet/03%29%20Greedy%20Algorithm/047%29%20Minimum%20Number%20of%20Coins.py
    # - "SO, GREEDY APPROACH WOULD WORK EVERYWHERE WHERE IN THE DENOMINATIONS, SUM OF *NO* TWO SMALLER DENOMINATIONS (SAME
    # OR DIFFERENT) IS GREATER THAN ANY BIGGER DENOMINATION."

    # 1) Optimal (Greedy: Start from Biggest Coin): TC = O(1); SC = O(1)

    # Straight-forward:

    """
    # Helper function:
    def get_minutes(t: str) -> int:
        h, m = map(int, t.split(":"))
        return h*60 + m

    # Convert to minutes:
    curr, corr = get_minutes(current), get_minutes(correct)

    ops = 0
    # Do increments/additions:
    for dt in (60, 15, 5, 1):
        multiplier = (corr-curr) // dt  # calc. no. of `dt` increments we can do
        curr += multiplier * dt
        ops += multiplier
        if curr == corr:
            break
    return ops
    """

    # Concise:

    # Helper function:
    def get_minutes(t: str) -> int:
        h, m = map(int, t.split(":"))
        return h*60 + m

    # Convert to minutes, get diff:
    diff = get_minutes(correct) - get_minutes(current)

    ops = 0
    # Do deductions:
    for dt in (60, 15, 5, 1):
        ops += diff // dt
        diff %= dt  # `diff %= dt` == `diff -= (diff//dt) * dt`
        if diff == 0:
            break
    return ops
