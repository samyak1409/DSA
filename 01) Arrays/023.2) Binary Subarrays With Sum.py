"""
https://leetcode.com/problems/binary-subarrays-with-sum
"""


def num_subarrays_with_sum(nums: list[int], goal: int) -> int:
    """"""

    # All the solutions are (modifications of the solutions) from
    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/023%29%20Count%20Subarrays%20with%20Given%20XOR.py.

    # This problem can be categorized as sub-problem of https://leetcode.com/problems/subarray-sum-equals-k.

    # 1) Time-Optimal (Prefix Sum & HashMap): TC = O(n); SC = O(n)
    # https://leetcode.com/problems/subarray-sum-equals-k/solution/604490

    from collections import Counter
    frequency = Counter()  # Counter for easy working with counts
    prefix_sum = 0
    frequency[prefix_sum] = 1  # initializing with "prefix_sum: 1" because:
    # dry run the algo with input (nums=[6, 6], x=6), you'll get the answer.
    count = 0
    for num in nums:
        prefix_sum += num
        count += frequency[prefix_sum-goal]  # ✔✔ if a pair is made with a prefix_sum, then it will also satisfy with
        # any & every previous occurrences of that particular prefix_sum
        frequency[prefix_sum] += 1  # add/update frequency of prefix_sum
    return count

    # 2) Optimal (Three Pointers): TC = O(n); SC = O(1)
    # https://leetcode.com/problems/binary-subarrays-with-sum/solution/#approach-3-three-pointer
