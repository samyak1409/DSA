"""
https://leetcode.com/problems/majority-element/
"""


from typing import List


def majorityElement(nums: List[int]) -> int:

    # Boyer-Moore Voting Algorithm (https://www.cs.utexas.edu/~moore/best-ideas/mjrty/) 💘: TC = O(n); SC = O(1)

    """
    candidate = None
    votes = 0

    for num in nums:

        if votes == 0:
            candidate = num  # reset

        votes += 1 if (num == candidate) else -1

    return candidate
    """

    # By sorting: TC = O(n log n); SC = O(n) (-_- why the hell is following faster as well as lighter than the above one)

    return sorted(nums)[len(nums)//2]
