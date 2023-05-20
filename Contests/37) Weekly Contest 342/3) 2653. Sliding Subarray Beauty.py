"""
https://leetcode.com/problems/sliding-subarray-beauty
"""


def get_subarray_beauty(nums: list[int], k: int, x: int) -> list[int]:
    """"""

    # Try to maintain the frequency of negative numbers in the current window of size k.
    # The x^th smallest negative integer can be gotten by iterating through the frequencies of the numbers in order.

    # 1) Optimal (Sliding Window + Counting (using FreqArr / HashMap)): TC = O(n*50); SC = O(50)
    # -> This solution is possible only because of `-50 <= nums[i] <= 50`.
    # -> In fact, this Q. was about noticing the fact that `-50 <= nums[i] <= 50`, and implementing this algo.
    # Note: We're only storing negative nums, as they're only that we need.

    # 1.1) Using Frequency Array for Counting:

    """
    freq = [0] * 50
    i = 0

    for j, num in enumerate(nums):

        # Expand window:
        if num < 0:  # only store if it's -ve
            freq[num+50] += 1  # (`+50`: as indexing start from 0 only)

        if j-i+1 == k:  # when curr window size equals k
            
            # Finding the xth smallest integer linearly: TC = O(50)
            c = 0
            ans = 0
            for neg, frq in enumerate(freq):
                c += frq
                if c >= x:
                    ans = neg - 50
                    break
            yield ans

            # Shrink window:
            if nums[i] < 0:
                freq[nums[i]+50] -= 1
            i += 1
    """

    # 1.2) Using HashMap for Counting:

    freq = {neg: 0 for neg in range(-50, 0)}
    i = 0

    for j, num in enumerate(nums):

        # Expand window:
        if num < 0:  # only store if it's -ve
            freq[num] += 1

        if j-i+1 == k:  # when curr window size equals k

            # Finding the xth smallest integer linearly: TC = O(50)
            c = 0
            ans = 0
            for neg, frq in freq.items():
                c += frq
                if c >= x:
                    ans = neg
                    break
            yield ans

            # Shrink window:
            if nums[i] < 0:
                freq[nums[i]] -= 1
            i += 1
