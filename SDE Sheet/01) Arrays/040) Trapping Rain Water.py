"""
https://leetcode.com/problems/trapping-rain-water
"""


def trap(height: list[int]) -> int:
    """"""

    # My intuition was to use a stack:
    # If a shorter bar comes, push to the stack (and add to the answer),
    # if a longer bar comes, pop (and add to the answer) as long as the current bar is longer than the top bar in stack.
    # Failed to implement it.
    # However, solution using stack exists.

    # 1) Time-optimal (Think for each bars one by one; Prefix & Suffix Maxes): TC = O(n); SC = O(n)
    # This is less intuitive to come up with, but once you know the solution, it's very easy.
    # Idea: Just go one by one through the `height` arr, and think for each index, what would be the quantity of water,
    # and how can we calc. it?

    # Build prefix max arr:
    pre_mx = [0]
    for i in range((n:=len(height))-1):  # (runs n-1 times)
        pre_mx.append(max(pre_mx[-1], height[i]))
    # print(pre_mx)  # debug

    # Build suffix max arr:
    suf_mx = [0]
    for i in range(n-1, 0, -1):  # (runs n-1 times)
        suf_mx.append(max(suf_mx[-1], height[i]))
    suf_mx.reverse()
    # print(suf_mx)  # debug

    # Calc. ans. using the two arrays:
    ans = 0
    for i, h in enumerate(height):
        ans += max(min(pre_mx[i], suf_mx[i])-h, 0)
    return ans

    # Optimal (Same idea as `1)` + Two-Pointers): TC = O(n); SC = O(1)


# Similar Questions:
# https://leetcode.com/problems/container-with-most-water
# https://leetcode.com/problems/product-of-array-except-self
