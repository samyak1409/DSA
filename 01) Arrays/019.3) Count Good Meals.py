"""
https://leetcode.com/problems/count-good-meals
"""


def count_pairs(nums: list[int]) -> int:
    """"""

    # All the solutions are (modifications of the solutions) from
    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/019%29%20Two%20Sum.py.

    # 1) Optimal (HashMap): TC = O(n); SC = O(n)

    """
    from collections import Counter

    pairs = 0
    for target in map(lambda power: 2**power, range(22)):  # `0 <= nums[i] <= 2^20` => max pair sum =
        # 2^20 + 2^20 = 2^20 * (1+1) = 2^20 * 2 = 2^21
        # Counter HashMap for easy working with the counts of nums:
        freq = Counter()
        # Taking every num one by one and checking for required num in HashMap:
        for num in nums:
            pairs += freq[target-num]  # `target-num` = required num for pair sum to be = target
            freq[num] += 1
    return pairs % 1000_000_007
    """
    # Better:
    # https://leetcode.com/problems/count-good-meals/discuss/999119/Java-HashMap-Two-Sum-O(N)
    # https://leetcode.com/problems/count-good-meals/discuss/999170/Python3-frequency-table
    from collections import Counter

    targets = [2**power for power in range(22)]  # `0 <= nums[i] <= 2^20` => max pair sum =
    # 2^20 + 2^20 = 2^20 * (1+1) = 2^20 * 2 = 2^21
    # Counter HashMap for easy working with the counts of nums:
    freq = Counter()
    pairs = 0
    # Taking every num one by one and checking for required num in HashMap for all the targets:
    for num in nums:
        '''
        for target in targets:
            pairs += freq[target-num]  # `target-num` = required num for pair sum to be = target
        '''
        pairs += sum(map(lambda target: freq[target-num], targets))
        freq[num] += 1
    return pairs % 1000_000_007
