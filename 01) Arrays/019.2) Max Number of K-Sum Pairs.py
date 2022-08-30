"""
https://leetcode.com/problems/max-number-of-k-sum-pairs
"""


def max_operations(nums: list[int], k: int) -> int:
    """"""

    # All the solutions are (modifications of the solutions) from
    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/019%29%20Two%20Sum.py.

    # 1) Sub-Optimal (Sorting & Two-Pointers): TC = O(n*log(n)); SC = O(n)

    """
    sorted_nums = sorted(nums)

    ops = 0
    # Finding all the 2 nums using Two-Pointers:
    low, high = 0, len(nums)-1  # init
    while low < high:
        pair_sum = sorted_nums[low] + sorted_nums[high]
        if pair_sum == k:
            ops += 1
            low, high = low+1, high-1  # continue for next nums
        elif pair_sum < k:  # => we want greater sum
            low += 1  # considering next num (larger) in right
        else:  # (if pair_sum > k) => we want lesser sum
            high -= 1  # considering next num (smaller) in left
    return ops
    """

    # 2) Optimal (HashMap): TC = O(n); SC = O(n)
    # https://leetcode.com/problems/max-number-of-k-sum-pairs/discuss/2005922/Going-from-O(N2)-greater-O(NlogN)-greater-O(N)-%2B-MEME

    # Counter HashMap for easy working with the counts of nums:
    from collections import Counter
    frequency = Counter()
    ops = 0
    # Taking every num one by one and checking for required num in HashMap:
    for num in nums:
        req_num = k - num  # required num for pair sum to be = k
        if frequency[req_num]:  # if required num is there in our HashMap => k sum pair found
            ops += 1
            frequency[req_num] -= 1  # decrement the count of `req_num` as we have considered it in a pair
        else:
            frequency[num] += 1  # only increment the count of `num` if pair is not formed above
    return ops
