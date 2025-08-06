"""
https://leetcode.com/problems/button-with-longest-push-time
"""


def button_with_longest_time(events: list[list[int]]) -> int:
    """"""

    # 1) Optimal (Iterate; HashSet): TC = O(n) {n = len(events)}; SC = O(1)

    prev_t = 0  # ("The time for the first button is simply the time at which it was pressed.")
    max_diff = 0
    ans = float('inf')

    # Iterate on events:
    for i, t in events:  # TC = O(n)
        # If curr diff is >= max diff:
        if (diff := t-prev_t) >= max_diff:
            # If curr diff > max diff, we got a longer push time, reset ans:
            if diff > max_diff:
                ans = float('inf')
            # "If multiple buttons have the same longest time, return the button with the smallest index":
            ans = min(ans, i)
            # Update the max diff to new diff:
            max_diff = diff
        # Update the prev time on every iteration:
        prev_t = t

    return ans
