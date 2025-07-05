"""
https://leetcode.com/problems/minimum-adjacent-swaps-to-alternate-parity
"""


def min_swaps(nums: list[int]) -> int:
    """"""

    # Hardest Q1 ever.
    # https://leetcode.com/discuss/post/6869421/biweekly-contest-159-by-leetcode-lsz3

    # 0) [TLE] Brute-force (Nested Loop): TC = O(n^2); SC = O(1)

    """
    pass
    """

    # 1) Optimal (Greedy: Track Indices): TC = O(n); SC = O(1)
    # Observation:
    # If abs diff of even and odd elements in nums > 1, then impossible to rearrange.
    # Only if it's 0 or 1, then it's always possible.
    # Now, we just need to figure out how to calc the MINIMUM swaps.
    # Approach:
    # If diff is 0, then it's possible to arrange by starting with either parity. Since we want min, we need to calc for
    # both and return the min.
    # If diff is 1, then it's only possible to arrange by starting with the parity which is greater.
    # Now, to actually calc, we compare current-indices of even (or odd) nums to target-indices of even (or odd) nums.
    # (Why do we need to compare only even or only odd, why not both? Because fixing the positions of either
    # automatically fixes the positions of other.)
    # The sum of abs diff between them is the ans.
    # But the main question is how?
    # Because by doing above what we're actually doing is greedily moving any element
    # that is not at its correct position, to the nearest correct position. And, since we're not asked to actually swap
    # but just tell the min swaps cnt, we don't need to swap, but just count.

    from collections.abc import Generator
    # https://docs.python.org/3/library/typing.html#annotating-generators-and-coroutines

    # Calc freq:
    even = odd = 0
    for num in nums:
        if num % 2:
            odd += 1
        else:
            even += 1

    # Not possible only if:
    if (diff := abs(even-odd)) > 1:
        return -1

    # Helper: Returns the sum of index differences:
    def f(curr: Generator[int]) -> int:
        # `range(0, n, 2)`: target indices
        return sum(abs(i1-i2) for i1, i2 in zip(curr, range(0, n, 2)))
        # Side note:
        # if `diff == 0`, `n` would always be even; and e.g. if `n` = `4`, `range(0, n, 2)` = `[0, 2]`
        # if `diff == 1`, `n` would always be odd; and e.g. if `n` = `5`, `range(0, n, 2)` = `[0, 2, 4]`

    n = len(nums)

    if diff == 0:
        # Minimum of (starting with even, starting with odd):
        return min(f(curr=(i for i in range(n) if nums[i] % 2 == 0)), f(curr=(i for i in range(n) if nums[i] % 2)))

    # if diff == 1:
    if even > odd:
        return f(curr=(i for i in range(n) if nums[i] % 2 == 0))
    else:
        return f(curr=(i for i in range(n) if nums[i] % 2))
