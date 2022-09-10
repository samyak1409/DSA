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
    #
    # How does this approach work?
    # Initially we consider the area constituting the exterior most lines.
    # Now, to maximize the area, we need to consider the area between the lines of larger lengths.
    # If we try to move the pointer at the longer line inwards, we won't gain any increase in area, since it is limited
    # by the shorter line.
    # But moving the shorter line's pointer could turn out to be beneficial, as per the same argument, despite the
    # reduction in the width.
    # This is done since a relatively longer line obtained by moving the shorter line's pointer might overcome the
    # reduction in area caused by the width reduction.
    #
    # Understanding the proof of this algorithm is way harder than the algorithm itself, so linking some more good
    # proof-explanations following:
    #
    # "I found a lot of the discussion and proof about this quite opaque, but one thing helped it finally clicked for me
    # (which is sort of proof by contradiction I guess)
    # You have two heights H_left and H_right, and H_right < H_left, then we know we have two choices, we want to move
    # one of them. If we move the larger one, we cannot increase the height for the simple reason that we are always
    # limited by the shortest, and we would be decreasing j-i, the width as well.
    # To clarify: let's say we kept the shortest forever, what would happen? Well, j-i would decrease, and either we
    # come across a taller block, which doesn't matter because our shorter one we kept only mattered, or we find a
    # shorter one, in which case that one matters.
    # Either way we end up with a smaller area, so we must move the shorter one because moving the larger one cannot
    # give an increase in area."
    # -https://leetcode.com/problems/container-with-most-water/solution/201204
    #
    # "Idea / Proof:
    # The widest container (using first and last line) is a good candidate, because of its width. Its water level is the
    # height of the smaller one of first and last line.
    # All other containers are less wide and thus would need a higher water level in order to hold more water.
    # The smaller one of first and last line doesn't support a higher water level and can thus be safely removed from
    # further consideration."
    # -https://leetcode.com/problems/container-with-most-water/discuss/6100/Simple-and-clear-proofexplanation
    #
    # "Frankly speaking, this "proof" is insufficient to prove that the optimal solution will be considered in the
    # movement of left and right indices."
    # -https://leetcode.com/problems/container-with-most-water/discuss/6100/Simple-and-clear-proofexplanation/253484
    # "Not sure how it's unclear. Maybe I have a blind spot here because I've seen and done this stuff too often...
    # The smaller end wall is now useless, and its removal doesn't have any effect on the other walls. So if there's a
    # better solution, it's still in the game. The same argument applies throughout the game, at each step. So in the
    # end, you must've at some point considered the optimal solution.
    # Consider a simpler problem. Let's say there's a table with a bunch of closed boxes. You're told there's a number
    # in each box, and you're asked to find the largest number. So you open some first box, remember its number, and
    # then throw that box away. Then you open some other box. If its number is larger than the one before, you remember
    # this new number instead. And then you throw that box away. And so on. Until you went through all boxes. In code,
    # that might look like this:
    # max = 0
    # i = 0
    # while i < number_of_boxes:
    #     if number_in_box[i] > max:
    #         max = number_in_box[i]
    #     i = i + 1
    # print(max)
    # Are you here also wondering whether the optimal solution might be missed? If yes, then why? If no, then what's the
    # difference to the water problem? The box problem is simpler, but the process is the same as the water one. You
    # consider a new option, you update your current "best", you remove something that can't give you something better
    # anymore, and you move on. If you have seen the overall optimum already, then you have seen it already and remember
    # it until the end. And if not, it's still in the game. So it will be found at some point. Really the only thing you
    # need to show is that you don't make a mistake when you reduce the problem, which is what I did in my post."
    # -https://leetcode.com/problems/container-with-most-water/discuss/6100/Simple-and-clear-proofexplanation/427495
    #
    # "what will happen for the h[i] == h[j]?"
    # -https://leetcode.com/problems/container-with-most-water/discuss/6090/Simple-and-fast-C++C-with-explanation/136098
    # "Both must move inside and find a higher height. Because if we only move either of them inside, the minimum height
    # don't change (to be accurate, don't increase, but can decrease), while the width decreases, then less water can be
    # held."
    # -https://leetcode.com/problems/container-with-most-water/discuss/6090/Simple-and-fast-C++C-with-explanation/230471

    left, right = 0, len(height)-1
    ans = 0  # area can't be negative
    while left < right:
        left_wall, right_wall = height[left], height[right]
        ans = max(ans, (right-left) * min(left_wall, right_wall))  # area = width * height
        # `right-left`: width of the container & `min(left_wall, right_wall)`: height of the container
        if left_wall < right_wall:
            left += 1
        elif right_wall < left_wall:
            right -= 1
        else:  # (if left_wall == right_wall)
            left, right = left+1, right-1
    return ans
