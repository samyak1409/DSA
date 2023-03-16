"""
https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score
"""


def max_score(nums: list[int]) -> int:
    """"""

    # Misread "The score of nums is the NUMBER of positive integers in the array prefix. Return the MAXIMUM score you
    # can achieve." to "The score of nums is the MAXIMUM of positive integers in the array prefix. Return the MAXIMUM
    # score you can achieve.", resulting in a penalty. 🤦
    '''
    return sum(n for n in nums if n > 0)
    '''
    # Bad luck was both the example testcases satisfied the ans of misunderstood approach. :|
    # I was not alone: https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/comments/1834566

    # 1) Optimal (Greedy: Sort in decreasing.): TC = O(n*log(n)); SC = O(n)
    # The best order of the array is in decreasing order.
    # Why?: +ve nums first, and then smallest -ve nums will give be the optimal order.
    # Sort the array in decreasing order and count the number of positive values in the prefix sum array.

    nums = sorted(nums, reverse=True)

    count = 0
    prefix_score = 0
    for num in nums:
        prefix_score += num
        if prefix_score <= 0:
            break
        count += 1
    return count
