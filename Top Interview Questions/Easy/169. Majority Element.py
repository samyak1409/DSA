"""
https://leetcode.com/problems/majority-element/
"""


from typing import List


def majorityElement(nums: List[int]) -> int:

    # 1) Brute Force: TC = O(n^2); SC = O(1)

    """
    for num in nums:
        if nums.count(num) > len(nums)//2:
            return num
    """

    # 2) HashMap: TC = O(n); SC = O(n)

    """
    from collections import Counter
    counts = Counter(nums)
    return max(counts.keys(), key=counts.get)  # max(counts.keys(), key=lambda num: counts[num])
    """
    # 2.1) Better:
    """
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > len(nums) // 2:
            return num
    """

    # 3) Sorting: TC = O(n log n); SC = O(n)

    """
    return sorted(nums)[len(nums)//2]
    """

    # 4) Randomization (https://leetcode.com/problems/majority-element/solution): TC = O(n); SC = O(1)

    """
    from random import choice
    while True:
        rand_num = choice(seq=nums)
        if nums.count(rand_num) > len(nums)//2:
            return rand_num
    """

    # 5) Boyer-Moore Voting Algorithm (https://www.cs.utexas.edu/~moore/best-ideas/mjrty) 💘: TC = O(n); SC = O(1)

    major, major_votes = None, 0  # init
    for new_num in nums:  # traverse
        if major_votes == 0:  # reset
            major, major_votes = new_num, 1
        else:  # votes ++ or --
            major_votes += (1 if (new_num == major) else -1)
    return major  # ans
