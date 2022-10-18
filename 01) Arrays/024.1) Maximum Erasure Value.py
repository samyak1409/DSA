"""
https://leetcode.com/problems/maximum-erasure-value
"""


def maximum_unique_subarray(nums: list[int]) -> int:
    """"""

    # All the solutions are (modifications of the solutions) from
    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/024%29%20Longest%20Substring%20Without%20Repeating%20Characters.py.

    # 0) Brute-force (Check all the Subarrays using Nested Loop & HashSet): TC = O(n^2); SC = O(n)

    # 1) Optimal (Sliding Window + Prefix Sum + HashMap): TC = O(n); SC = O(n)
    # https://leetcode.com/problems/maximum-erasure-value/discuss/2140577/An-Interesting-Optimisation-or-JAVA-Explanation

    prefix_sums = [0]  # init
    last_index = {}  # for O(1) lookup
    start = 0
    max_score = 0
    for index, num in enumerate(nums):
        prefix_sums.append(prefix_sum := prefix_sums[-1]+num)
        if (last := last_index.get(num)) is not None:  # => num has occurred before also
            start = max(start, last+1)  # moving the start to last_index[num]+1 if start is not already ahead of it
        max_score = max(max_score, prefix_sum-prefix_sums[start])
        # `prefix_sum-prefix_sums[start]` = sum(arr[start:index+1])
        last_index[num] = index  # add/update last index of num to the hashmap
    return max_score
