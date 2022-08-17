"""
https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k
"""


def count_k_difference(nums: list[int], k: int) -> int:
    """"""

    # All the solutions are (modifications of the solutions) from
    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/019%29%20Two%20Sum.py.

    # 1) Optimal (HashMap): TC = O(n); SC = O(n)
    # https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/discuss/1501957/Java-Map-Solution-beats-98

    # Counter HashMap for easy working with the counts of nums:
    from collections import Counter
    frequency = Counter()
    pairs = 0
    # Taking every num one by one and checking for required nums in HashMap:
    for num in nums:
        pairs += frequency[num-k] + frequency[num+k]  # `num-k` & `num+k` = required num for pair diff to be = k
        # IMP: Why `-k` & `+k`? Take the input (nums=[1, 3, 2], k=1), so num=2 is k=1 away from num=1 as well as num=3.
        frequency[num] += 1
    return pairs

    # Also read:
    # https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/discuss/1471605/Counting-Sort
