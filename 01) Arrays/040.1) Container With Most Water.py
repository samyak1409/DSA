"""
https://leetcode.com/problems/container-with-most-water
"""


def max_area(height: list[int]) -> int:
    """"""

    # https://leetcode.com/problems/container-with-most-water/solution

    # If you simulate the problem, it will be O(n^2) which is not efficient.
    # 0) [TLE] Brute-force (Find for all possible containers): TC = O(n^2); SC = O(1)
    # Note: Brute force approaches are often included because they are intuitive starting points when solving a problem.
    # However, they are often expected to receive Time Limit Exceeded since they would not be accepted in an interview
    # setting.

    """
    n = len(height)
    ans = 0  # area can't be negative
    for left in range(n):
        for right in range(left+1, n):
            ans = max(ans, (right-left) * min(height[left], height[right]))  # area = width * height
            # `right-left`: width of the container & `min(height[left], height[right])`: height of the container
    return ans
    """

    # 1) Optimal (Two-Pointers): TC = O(n); SC = O(1)
    # Try to use two-pointers. Set one pointer to the left and one to the right of the array. Always move the pointer
    # that points to the lower line.
    # How does this approach work?
    # Initially we consider the area constituting the exterior most lines.
    # Now, to maximize the area, we need to consider the area between the lines of larger lengths.
    # If we try to move the pointer at the longer line inwards, we won't gain any increase in area, since it is limited
    # by the shorter line.
    # But moving the shorter line's pointer could turn out to be beneficial, as per the same argument, despite the
    # reduction in the width.
    # This is done since a relatively longer line obtained by moving the shorter line's pointer might overcome the
    # reduction in area caused by the width reduction.
    # Proof: https://leetcode.com/problems/container-with-most-water/solution/201204

    pass
