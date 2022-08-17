"""
https://leetcode.com/problems/count-good-meals
"""


def count_pairs(nums: list[int]) -> int:
    """"""

    # All the solutions are (modifications of the solutions) from
    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/019%29%20Two%20Sum.py.

    # 1) [WA] Sub-Optimal (Sorting & Two-Pointers): TC = O(n*log(n)); SC = O(n)
    # WA: Dry run the algo with input [1, 1, 1] to know the problem.

    """
    sorted_nums = sorted(nums)

    pairs = 0
    for target in map(lambda power: 2**power, range(22)):  # "0 <= nums[i] <= 2^20" => max pair sum =
        # 2^20 + 2^20 = 2^20 * (1+1) = 2^20 * 2 = 2^21
        # Finding all pairs using Two-Pointers:
        low, high = 0, len(nums)-1  # init
        while low < high:
            pair_sum = sorted_nums[low] + sorted_nums[high]
            if pair_sum == target:
                pairs += 1
                low, high = low+1, high-1  # continue for next nums
            elif pair_sum < target:  # => we want greater sum
                low += 1  # considering next num (larger) in right
            else:  # (if pair_sum > target) => we want lesser sum
                high -= 1  # considering next num (smaller) in left
    return pairs % 1000_000_007
    """

    # 2) Optimal (HashMap): TC = O(n); SC = O(n)

    """
    from collections import Counter

    pairs = 0
    for target in map(lambda power: 2**power, range(22)):  # "0 <= nums[i] <= 2^20" => max pair sum =
        # 2^20 + 2^20 = 2^20 * (1+1) = 2^20 * 2 = 2^21
        # Counter HashMap for easy working with the counts of nums:
        frequency = Counter()
        # Taking every num one by one and checking for required num in HashMap:
        for num in nums:
            pairs += frequency[target-num]  # `target-num` = required num for pair sum to be = target
            frequency[num] += 1
    return pairs % 1000_000_007
    """
    # Better:
    # https://leetcode.com/problems/count-good-meals/discuss/999119/Java-HashMap-Two-Sum-O(N)
    # https://leetcode.com/problems/count-good-meals/discuss/999170/Python3-frequency-table
    from collections import Counter

    targets = [2**power for power in range(22)]  # "0 <= nums[i] <= 2^20" => max pair sum = 2^20 + 2^20 =
    # 2^20 * (1+1) = 2^20 * 2 = 2^21
    # Counter HashMap for easy working with the counts of nums:
    frequency = Counter()
    pairs = 0
    # Taking every num one by one and checking for required num in HashMap for all the targets:
    for num in nums:
        """
        for target in targets:
            pairs += frequency[target-num]  # `target-num` = required num for pair sum to be = target
        """
        pairs += sum(map(lambda target: frequency[target-num], targets))
        frequency[num] += 1
    return pairs % 1000_000_007
