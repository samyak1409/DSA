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
    k %= len(nums)  # remove duplicate rotations (as well as handle even if k is -ve)
    nums[:] = nums[-k:] + nums[:-k]
    """

    # Follow up: Could you do it in-place with O(1) extra space?
    # 1) Optimal (Reversal Algorithm): TC = O(n); SC = O(1)
    # https://leetcode.com/problems/rotate-array/discuss/54250/Easy-to-read-Java-solution
    # https://leetcode.com/problems/rotate-array/discuss/1730142/JavaC++Python-A-very-very-well-detailed-explanation
    # https://leetcode.com/problems/reverse-words-in-a-string can be solved using the same algorithm.
    # "Leet Code" --Reverse Whole String-> "edoC teeL" --Reverse Individual Words-> "Code Leet"

    # Helper Function:
    def reverse(array: list[int], start: int, end: int) -> None:
        while start < end:
            array[start], array[end] = array[end], array[start]  # swap first and last val
            start, end = start+1, end-1  # move pointers

    n = len(nums)
    k %= n  # remove duplicate rotations (as well as handle even if k is -ve)
    nums.reverse()
    reverse(array=nums, start=0, end=k-1)
    reverse(array=nums, start=k, end=n-1)

    # Articles with multiple solutions:
    # https://leetcode.com/problems/rotate-array/discuss/54277/Summary-of-C++-solutions
    # https://leetcode.com/problems/rotate-array/discuss/269948/4-solutions-in-python-(From-easy-to-hard)
    # https://leetcode.com/problems/rotate-array/discuss/54426/Summary-of-solutions-in-Python
