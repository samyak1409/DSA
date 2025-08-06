"""
https://leetcode.com/problems/maximum-subarray-with-equal-products
"""


def max_length(nums: list[int]) -> int:
    """"""

    # 1) Brute-force (Simulate: Calc. for all sub-arrays): TC = O(n^2); SC = O(1) {assuming lcm, gcd are ~ O(1)}

    """
    from math import lcm, gcd

    ans = 0
    # Outer loop:
    for i in range(n := len(nums)):
        # Init the variables with first element:
        p = l = g = nums[i]
        if p == l*g:
            ans = max(ans, 1)
        # Inner loop (starting with +1):
        for j in range(i+1, n):
            # Update the vars:
            p *= nums[j]
            l = lcm(l, nums[j])
            g = gcd(g, nums[j])
            # Update ans. if condition satisfies:
            if p == l*g:
                ans = max(ans, j-i+1)
    return ans
    """

    # OR:

    from math import lcm, gcd

    ans = 0
    # Outer loop:
    for i in range(n := len(nums)):
        # Init the variables with their default vals (vals with no effect on vars):
        p, l, g = 1, 1, 0
        # Inner loop:
        for j in range(i, n):
            # Update the vars, and update ans. if condition satisfies:
            if (p := p*nums[j]) == (l := lcm(l, nums[j])) * (g := gcd(g, nums[j])):
                ans = max(ans, j-i+1)
    return ans
