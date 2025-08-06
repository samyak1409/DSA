"""
https://leetcode.com/problems/maximum-product-of-first-and-last-elements-of-a-subsequence
"""


def maximum_product(nums: list[int], m: int) -> int:
    """"""

    # 1) Optimal (Sliding Window, Prefix Min & Max): TC = O(n-m); SC = O(1)
    # Since we're talking about subsequence, we can go take any far distant elements, but the boundation is on closer
    # elements, e.g. see test case: `nums = [1, 3, -5, 5, 6, -4], m = 3`
    #
    # To find max prod of first and last elements of a subsequence of size `m`,
    # we iterate through `nums` considering each `nums[i]` as a potential last element.
    # For each `nums[i]`, best first element is either min or max num in valid prefix `nums[0...i-m+1]`.

    # Tracks min and max of first elements:
    mn, mx = float('inf'), float('-inf')
    ans = float('-inf')
    for i in range(m-1, len(nums)):
        # `nums[i-m+1]`, `nums[i]`: first and last element of current `m`-size subsequence ending at `i`
        # Update running min and max:
        mn, mx = min(mn, nums[i-m+1]), max(mx, nums[i-m+1])
        # Calc prod with both min and max first candidates:
        ans = max(ans, nums[i]*mn, nums[i]*mx)
    return ans
