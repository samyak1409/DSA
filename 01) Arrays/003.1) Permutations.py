"""
https://leetcode.com/problems/permutations
"""


def permute(nums: list[int]) -> list[list[int]]:
    """"""

    # 1) Optimal ("Next Permutation" n! Times): TC = (n! * n); SC = O(n)
    # NOTE: Following is the solution using the technique of finding "Next Permutation", though it shouldn't be solved
    # like this, but by Backtracking.

    from math import factorial

    nums = nums  # so that input array is not modified
    n = len(nums)
    for _ in range(factorial(n)):

        # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/003%29%20Next%20Permutation.py:
        done = False
        for i in range(n-1):  # finding first decreasing num (iterating from right to left)
            if nums[-i-2] < nums[-i-1]:
                decreasing_num = nums[-i-2]  # decreasing num found
                for j in range(i+1):  # finding number just larger than decreasing num (iterating from right to left)
                    if nums[-j-1] > decreasing_num:
                        just_larger = nums[-j-1]  # just larger number found
                        nums[-i-2], nums[-j-1] = just_larger, decreasing_num  # swapping the two
                        nums[-i-1:] = nums[-i-1:][::-1]  # reversing nums in the right
                        done = True
                        break
            if done:
                break
        if not done:
            nums.reverse()  # if nums is the last permutation itself

        yield nums
