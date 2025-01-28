"""
https://leetcode.com/problems/maximum-frequency-after-subarray-operation
"""


def max_frequency(nums: list[int], k: int) -> int:
    """"""

    # 1) Optimal (Fix a target from 1 to 50, apply kadane): TC = O(50 * n); SC = O(50)
    # If we notice the constraints `1 <= nums[i] <= 50; 1 <= k <= 50`, we can actually try all the nums as target to
    # convert to k. And then see which target gives us the most freq. Using kadane's algo.
    # https://www.youtube.com/watch?v=OZwYStLC8J4

    best_overall = 0
    # Loop on only nums which are present in `nums` (instead of looping on 1 to 50):
    for target in set(nums):  # O(50)
        # Kadane considering `target` as `+1`, `k` as `-1`, and ignoring all the other nums:
        curr = 0
        best = 0
        for num in nums:  # O(n)
            if num == k:
                curr -= 1
                if curr < 0:
                    curr = 0
            elif num == target:
                curr += 1
                best = max(best, curr)
        best_overall = max(best_overall, best)
    # Return best conversion count + count of already k:
    return best_overall + nums.count(k)  # O(n)
