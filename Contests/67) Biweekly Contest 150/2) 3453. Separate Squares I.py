"""
https://leetcode.com/problems/separate-squares-i
"""


def separate_squares(squares: list[list[int]]) -> float:
    """"""

    # Minimization (Optimization) Problem

    # 1) Optimal (Binary Search): TC = O(log2(10**9 + 10**6) * n); SC = O(1)
    # [Came up with myself; My implementation]
    # Intuition: Can we binary search the `y` of the horizontal line?

    # Helper function: O(n)
    def get_diff() -> float:
        # Straight-forward calculation:
        sum_below = sum_above = 0
        for _, y_start, h in squares:
            if y_start >= y_line:
                sum_above += h * h
            elif y_start + h <= y_line:
                sum_below += h * h
            else:  # if `y_line` is splitting the square:
                sum_below += (y_line - y_start) * h
                sum_above += (y_start + h - y_line) * h
        # print('sum_below, sum_above', sum_below, sum_above)  # debug
        return sum_below - sum_above

    # Init:
    # min_y, max_y = 0, 10**9 + 10**6
    # max_y = `10**9` since "0 <= xi, yi <= 10^9"
    #    + `10**6` since "The total area of all the squares will not exceed 10^12."

    # (Optional) Optimized Init:
    min_y, max_y = float('inf'), 0
    for _, y, l in squares:
        min_y, max_y = min(min_y, y), max(max_y, y+l)
    
    ans = None
    min_diff = float('inf')
    while min_y <= max_y:  # O(log2(10**9 + 10**6))
        # print('min_y, max_y', min_y, max_y)  # debug
        y_line = (min_y+max_y) / 2
        # print('y_line', y_line)  # debug
        diff = get_diff()
        # print('diff', diff)  # debug
        # We're tracking the min diff. of `sum_below - sum_above` (across the search, the `y_line` which results in the
        # least absolute min diff. would be our answer):
        if (abs_diff := abs(diff)) <= min_diff:
            ans = y_line
            # print('ans', ans)  # debug
            min_diff = abs_diff
        # Update the search range:
        if diff >= 0:  # (if sum_below >= sum_above)
            max_y = y_line - .00001
        else:  # (if sum_below < sum_above)
            min_y = y_line + .00001
        # `.00001` since "Answers within 10^-5 of the actual answer will be accepted.".

    # print('=> min_y > max_y', min_y, max_y)  # debug
    return ans

    # Another implementation:
    # https://youtu.be/Qi-tGtmZL2w
    # https://leetcode.com/problems/separate-squares-i/solutions/6426084/precision-binary-search
