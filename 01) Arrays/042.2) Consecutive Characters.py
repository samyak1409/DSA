"""
https://leetcode.com/problems/consecutive-characters
"""


def max_power(s: str) -> int:
    """"""

    # 1) Optimal (Traverse and Get): TC = O(n); SC = O(1)
    # https://leetcode.com/problems/consecutive-characters/solution
    # https://leetcode.com/problems/consecutive-characters/discuss/635269/JavaPython-3-Simple-code-w-brief-explanation-and-analysis.
    # Extra: https://leetcode.com/problems/consecutive-characters/discuss/635241/Python-One-line

    """
    max_streak = streak = 0
    last_char = None
    for char in s:
        if char == last_char:
            streak += 1
        else:
            last_char, streak = char, 1  # reset
        max_streak = max(max_streak, streak)
    return max_streak
    """
    # Concise:
    max_streak, streak, last_char = 0, 0, None
    for char in s:
        if char != last_char:
            last_char, streak = char, 0  # reset
        max_streak = max(max_streak, (streak := streak+1))
    return max_streak
