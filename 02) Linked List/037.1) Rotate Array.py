"""
https://leetcode.com/problems/rotate-array
"""


def rotate(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    # Follow up:
    # Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.

    # 0) Brute-force (Pop and Insert at Start One by One k%n times): TC = O(k%n * n); SC = O(1)

    """
    for _ in range(k % len(nums)):
        nums.insert(0, nums.pop())  # O(n)
    """

    # 1) Time-Optimal (Add 2 Sliced Lists): TC = O(n); SC = O(n)
    # https://leetcode.com/problems/rotate-array/discuss/54294/My-solution-by-using-Python

    """
    k %= len(nums)  # remove duplicate rotations
    nums[:] = nums[-k:] + nums[:-k]
    """

    # Follow up: Could you do it in-place with O(1) extra space?
    # 1) Optimal (): TC = O(n); SC = O(1)

    pass
