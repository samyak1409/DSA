"""
https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k
"""


def maximum_subarray_sum(nums: list[int], k: int) -> int:

    # 1) Optimal (Sliding Window + HashMap): TC = O(n); SC = O(n)
    # Which elements change when moving from the subarray of size k that ends at index i
    #                                     to the subarray of size k that ends at index i + 1?
    # Only two elements change, the element at i + 1 is added into the subarray,
    #                       and the element at i - k + 1 gets removed from the subarray.
    # Iterate through each subarray of size k and keep track of the sum of the subarray and the frequency of each
    # element.

    from collections import Counter
    freq = Counter()  # for easy working with elements' occurrences; SC = O(n)
    duplicates = 0
    cur_sum = max_sum = 0
    i = 0
    for j, num in enumerate(nums):  # TC = O(n)
        freq[num] += 1  # keep extending window to the right by 1 everytime
        duplicates += freq[num] >= 2  # update duplicate count
        cur_sum += num  # update current sum
        if j-i+1 == k:  # => reached required window size (condition 1: `The length of the subarray is k`)
            if not duplicates:  # => valid subarray (condition 2: `All the elements of the subarray are distinct`)
                max_sum = max(max_sum, cur_sum)  # update ans
            freq[(num := nums[i])] -= 1  # shrink window from left by 1
            i += 1
            duplicates -= freq[num] >= 1  # update duplicate count (tricky)
            cur_sum -= num  # update current sum
    return max_sum
