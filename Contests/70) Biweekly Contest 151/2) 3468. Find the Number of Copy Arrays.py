"""
https://leetcode.com/problems/find-the-number-of-copy-arrays
"""


def count_arrays(original: list[int], bounds: list[list[int]]) -> int:
    """"""

    # 1) Optimal (Loop, Find the least range): TC = O(n); SC = O(1)
    # [Came up with myself.]
    # Same as:
    # https://leetcode.com/problems/find-the-number-of-copy-arrays/solutions/6482086/c-java-diff-of-common-possible-interval
    # Observation: Since we want same diff between the elements, we can only +/- same value to all `original[i]` in
    # order to get our `copy` array(s).
    # We can find the minimum allowed lower and upper ranges across all `originals[i]`, and sum of that + 1 (for the
    # original array itself) would be our ans, with some edge cases as follows:

    # 1.1) [WA] Intuition: If we've negative value for an allowed range, we'd ignore that side, since we can't extend
    # our original arr in that particular direction. If both sides are negative, then return 0.

    """
    lower = upper = float('inf')

    # Find the minimum allowed lower and upper ranges across all `originals[i]`:
    for x, (u, v) in zip(original, bounds):
        lower, upper = min(lower, x-u), min(upper, v-x)
    print(lower, upper)  # debug

    ans = max(lower, 0) + max(upper, 0)
    return ans+1 if ans else ans
    """
    # WA:
    # Input: original = [2,76], bounds = [[93,110],[67,98]]
    # Output: 23
    # Expected: 0

    # 1.2) [WA] Intuition: We'll only consider the ans if we've both sides non-negative, else return 0.

    """
    lower = upper = float('inf')

    # Find the minimum allowed lower and upper ranges across all `originals[i]`:
    for x, (u, v) in zip(original, bounds):
        lower, upper = min(lower, x-u), min(upper, v-x)
    print(lower, upper)  # debug

    return lower+upper+1 if lower >= 0 and upper >=0 else 0
    """
    # WA:
    # Input: original = [3,25], bounds = [[9,80],[16,35]]
    # Output: 0
    # Expected: 5

    # 1.3) [AC] Intuition: If one negative side is there, then it needs to be added in the ans, since that's the amount
    # that needs to be subtracted since the bound[i][0] (i.e. i-th lower bound) > original[i]. And if `upper+lower+1` is
    # going -ve, means no copy arrays possible, return 0.

    lower = upper = float('inf')

    # Find the minimum allowed lower and upper ranges across all `originals[i]`:
    for x, (u, v) in zip(original, bounds):
        lower, upper = min(lower, x-u), min(upper, v-x)
    print(lower, upper)  # debug

    return max(upper+lower+1, 0)
