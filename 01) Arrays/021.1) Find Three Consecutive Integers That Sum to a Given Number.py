"""
https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number
"""


def sum_of_three(num: int) -> list[int]:
    """"""

    # Notice that if a solution exists, we can represent them as x-1, x, x+1. What does this tell us about the number?
    # Notice the sum of the numbers will be 3x. Can you solve for x?

    # 1) Brute-force = Optimal (Maths): TC = O(1); SC = O(1)

    if num % 3 == 0:
        mid = num // 3
        return [mid-1, mid, mid+1]
