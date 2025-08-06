"""
https://leetcode.com/problems/zero-array-transformation-iv
"""


def min_zero_array(nums: list[int], queries: list[list[int]]) -> int:
    """"""

    # 0) Brute-force (Pick + Not Pick: Recursion): TC = O(n * 2^q); SC = O(q) {n=len(nums), q=len(queries)}
    # Basic pick + not-pick implementation using recursion.

    """
    # Recursive Function: TC = O(2^q); SC = O(q)
    def get_min_q(num_left: int, q:int = 0) -> int | float:
        # +ve Base case: Reduced to 0:
        if num_left == 0:
            return q
        # -ve: Reached out of `queries` without making 0:
        if q == q_len:
            return float('inf')

        l, r, v = queries[q]
        # If allowed to choose this `v` (if in range) and `v` <= num:
        if l <= num_i <= r and num_left >= v:
            # Try both, pick & not pick:
            return min(get_min_q(num_left-v, q+1), get_min_q(num_left, q+1))
        # Else we can only skip picking:
        else:
            return get_min_q(num_left, q+1)

    q_len = len(queries)
    ans = -1
    # Calc. min `q` for each num: O(n)
    for num_i, num in enumerate(nums):
        # Max of which would be the min `q` for the whole `nums`:
        ans = max(ans, get_min_q(num))
    # If any of the num can't be reduced to 0, it'd be `inf`, so return -1, else return the min `q` for whole arr:
    return ans if ans != float('inf') else -1
    """

    # 1) Sub-optimal (Pick + Not Pick: Recursion + Memo):
    # TC = O(n * max(nums)*q); SC = O(max(nums)*q + q) {n=len(nums), q=len(queries)}
    # This approach is literally just adding `@cache` to the brute-force and moving the recursive function inside the
    # `for` loop for caching local for `nums[i]`s.
    # Idea reference:
    # https://leetcode.com/problems/zero-array-transformation-iv/solutions/6541300/c-java-dp-pick-not-to-pick-with-intuition-to-reach-the-solution
    #
    # I came up with brute-force myself in the contest, but couldn't figure out how to add caching because of the range
    # barrier (`l <= num_i <= r`), missed AC by tiny-tiny change, would've gotten very good rank after long.

    from functools import cache

    q_len = len(queries)
    ans = -1
    # Calc. min `q` for each num: O(n)
    for num_i, num in enumerate(nums):

        # Recursive Function w/ caching: TC = O(max(nums)*q); SC = O(max(nums)*q + q)
        @cache
        def get_min_q(num_left: int, q:int = 0) -> int | float:
            # +ve Base case: Reduced to 0:
            if num_left == 0:
                return q
            # -ve: Reached out of `queries` without making 0:
            if q == q_len:
                return float('inf')

            l, r, v = queries[q]
            # If allowed to choose this `v` (if in range) and `v` <= num:
            if l <= num_i <= r and num_left >= v:
                # Try both, pick & not pick:
                return min(get_min_q(num_left-v, q+1), get_min_q(num_left, q+1))
            # Else we can only skip picking:
            else:
                return get_min_q(num_left, q+1)

        # Max of which would be the min `q` for the whole `nums`:
        ans = max(ans, get_min_q(num))

    # If any of the num can't be reduced to 0, it'd be `inf`, so return -1, else return the min `q` for whole arr:
    return ans if ans != float('inf') else -1
