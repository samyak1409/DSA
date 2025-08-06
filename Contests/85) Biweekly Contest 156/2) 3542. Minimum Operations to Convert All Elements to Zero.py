"""
https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero
"""


def min_operations(nums: list[int]) -> int:
    """"""

    # 1) Optimal (Monotonic Stack): TC = O(n); SC = O(n)
    # Observation: Since we can set min(subarray) = 0, if we want to set a num `x` = 0, there must not be any element
    # smaller than `x` in that subarray.
    # Hence, we can iterate on `nums`, and whenever a smaller number comes, we need to flush off all the larger numbers,
    # adding to the ans `cnt` variable.
    # Now, we just need to figure out how we can track this efficiently.

    """
    st = []
    cnt = 0
    for num in nums:
        # While the elements in the stack are larger than this num, we need to flush them to ans `cnt` var:
        while st and st[-1] > num:
            st.pop()
            cnt += 1
        # Now, after above, either `st[-1]` would be <= `num` or `st` would be empty, now we want to push `num` to the
        # stack, but we don't want to push if `st[-1] == num` (since we can "set all occurrences of the minimum
        # non-negative integer in that subarray to 0", and we want to minimize), and we don't want to push `0`:
        if num != 0 and ((st and st[-1] != num) or (not st)):
            st.append(num)

    # `st` would be left with unique nums which needed to be changed to 0:
    return cnt + len(st)
    """

    # CHATGPT-IMPROVED-COMMENTS VERSION OF ABOVE:

    # 1) Optimal (Monotonic Stack): TC = O(n); SC = O(n)
    # Observation: In one operation, we can set all occurrences of the *minimum* in a subarray to 0.
    # So to set a number `x` to 0, we must ensure there’s no smaller number in the selected subarray.
    #
    # Strategy:
    # We iterate over the array. Whenever a smaller number appears, we invalidate all previous larger
    # numbers (which are no longer optimal to process together), and we increment the operation count `cnt`.
    # To manage this efficiently, we use a monotonic stack that stores only relevant (and unique) candidates.

    st = []
    cnt = 0
    for num in nums:
        # Remove all larger numbers that came before `num` — they must be processed separately.
        while st and st[-1] > num:
            st.pop()
            cnt += 1
        # Skip pushing if `num` is 0 (already zeroed) or is a duplicate of the current top.
        if num != 0 and ((not st) or st[-1] != num):
            st.append(num)

    # Remaining values in `st` are unique, non-zero numbers still needing separate operations.
    return cnt + len(st)
