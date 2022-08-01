"""
https://leetcode.com/problems/4sum
"""


def four_sum(nums: list[int], target: int) -> list[list[int]]:
    """"""

    # 0) [TLE] Brute-force (Nested Loops & HashMap): TC = O(n^4); SC = O(n)

    # Core Logic: TC = O(n^4); SC = O(1)
    """
    n = len(nums)
    for a in range(n):
        for b in range(a+1, n):
            for c in range(b+1, n):
                for d in range(c+1, n):
                    if nums[a] + nums[b] + nums[c] + nums[d] == target:
                        yield [nums[a], nums[b], nums[c], nums[d]]
    """
    # But as we have to return an array of all the UNIQUE quadruplets, see Example 2:
    #     Input: nums = [2,2,2,2,2], target = 8
    #     Output: [[2,2,2,2]]
    #     Explanation:
    #     The only unique quadruplet is [2,2,2,2].
    # We will keep track of the quadruplets already added to the answer set and will not consider any quadruplet again:
    # TC = O(n*log(n) + n^4); SC = O(n+n)
    # IMP: Checkout:
    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/020%29%203Sum.py#L9
    nums = sorted(nums)  # (not modifying the input array but making a new variable (local))
    n = len(nums)
    quadruplet_set = set()  # for checking quadruplet's presence in O(1) time
    for a in range(n):
        for b in range(a+1, n):
            for c in range(b+1, n):
                for d in range(c+1, n):
                    if nums[a] + nums[b] + nums[c] + nums[d] == target:
                        quadruplet = [nums[a], nums[b], nums[c], nums[d]]
                        quadruplet_tuple = tuple(quadruplet)
                        if quadruplet_tuple not in quadruplet_set:
                            yield quadruplet
                            quadruplet_set.add(quadruplet_tuple)

    # We can implement 4Sum by wrapping 3Sum in another loop.
    # But wait - there is a catch.
    # If an interviewer asks you to solve 4Sum, they can follow up with 5Sum, 6Sum, and so on.
    # What they are really expecting at this point is a k_sum solution.
    # Therefore, we will focus on a generalized implementation here.
    # https://leetcode.com/problems/4sum/solution


# Similar Question: https://leetcode.com/problems/4sum-ii
