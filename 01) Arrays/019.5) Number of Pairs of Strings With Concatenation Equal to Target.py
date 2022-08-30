"""
https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target
"""


def num_of_pairs(nums: list[str], target: str) -> int:
    """"""

    # All the solutions are (modifications of the solutions) from
    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/019%29%20Two%20Sum.py.

    # 1) Optimal (HashMap): TC = O(n); SC = O(n)

    # Counter HashMap for easy working with the counts of nums:
    from collections import Counter
    frequency = Counter()
    pairs = 0
    # Taking every num one by one and checking for required nums in HashMap:
    for num in nums:
        pairs += frequency[target.removeprefix(num)] + frequency[target.removesuffix(num)]
        # `target.removeprefix(num)` & `target.removesuffix(num)` = required num for pair concat to be = target, why? ->
        # Input: nums = ["777", "7"], target = "7777"
        # Output: 2
        # Explanation: Valid pairs are:
        # - (0, 1): "777" + "7"
        # - (1, 0): "7" + "777"
        frequency[num] += 1
    return pairs
