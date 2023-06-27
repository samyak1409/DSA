"""
https://leetcode.com/problems/find-the-distinct-difference-array
"""


def distinct_difference_array(nums: list[int]) -> list[int]:
    """"""

    # Which data structure will help you maintain distinct elements?
    # Iterate over all possible prefix sizes. Then, use a nested loop to add the elements of the prefix to a set, and
    # another nested loop to add the elements of the suffix to another set.

    # 1) Optimal (HashMap): TC = O(n); SC = O(n)
    # First of all to decide if HashSet would work, or we would need HashMap:
    # take nums = [3, 2, 3, 4, 2]
    # at i = 0: pre_set = {1}, suf_set = {2, 3, 4}
    # at i = 1: pre_set = {1, 2}, suf_set = {3, 4}
    # but as you can see that one more 2 is there at i = 4, so this implies that we need HashMap.
    # (We need exact counts.)

    from collections import Counter
    pre_count, suf_count = Counter(), Counter(nums)  # init

    for num in nums:
        # Update counts:
        pre_count[num] += 1
        suf_count[num] -= 1
        # Remove the element if it's count becomes 0:
        if suf_count[num] == 0:
            suf_count.pop(num)
        # Yield ans:
        yield len(pre_count) - len(suf_count)
