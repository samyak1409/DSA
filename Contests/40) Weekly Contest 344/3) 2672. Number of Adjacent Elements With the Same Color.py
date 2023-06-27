"""
https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color
"""


def color_the_array(n: int, queries: list[list[int]]) -> list[int]:
    """"""

    # Since at each query, only one element is being recolored, we just need to focus on its neighbors.
    # If an element that is changed on the i-th query had the same color as its right element answer decreases by 1.
    # Similarly, contributes its left element too.
    # After changing the color, if the element has the same color as its right element answer increases by 1.
    # Similarly, contributes its left element too.

    # 1) Optimal (Counting Neighbours): TC = O(n); SC = O(n)

    nums = [0] * n  # "Initially, all elements are uncolored (has a value of 0)."
    ans = 0

    # Loop on queries:
    for i, color in queries:
        # Only if current color != 0 (0 represents uncolored element):
        if nums[i]:
            # Decrease the count for left and right if the color is same as the current element (as the color is going
            # to be overwritten):
            ans -= (i-1 >= 0 and nums[i-1] == nums[i]) + (i+1 < n and nums[i+1] == nums[i])
        # Color the index:
        nums[i] = color
        # Increase the count for left and right if the color is same as the current element:
        ans += (i-1 >= 0 and nums[i-1] == nums[i]) + (i+1 < n and nums[i+1] == nums[i])
        # Yield ans:
        yield ans
