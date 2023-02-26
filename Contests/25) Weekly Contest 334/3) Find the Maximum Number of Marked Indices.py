"""
https://leetcode.com/problems/find-the-maximum-number-of-marked-indices
"""


def max_num_of_marked_indices(nums: list[int]) -> int:
    """"""

    # Think about how to check that performing k operations is possible.
    # To perform k operations, it’s optimal to use the smallest k elements and the largest k elements and think about
    # how to match them.
    # It’s optimal to match the ith the smallest number with the k-i + 1 largest number.
    # Now we need to binary search on the answer and find the greatest possible valid k.

    # We can do it without the binary search too:
    # 1) Optimal (Greedy + Two Pointers): TC = O(n*log(n)); SC = O(n)
    # INTUITION FOR THIS PROBLEM IS TRICKY, BUT SOLUTION IS EASY.
    # Greedy: Sort the array.
    # At most n // 2 pairs can be made, so try making pairs of `i` with `j`, `i` starting from 0, `j` starting from
    # (n+1)//2.
    # Now, this part is also little tricky that why starting the `j` from (n+1)//2 and not n//2 or (n//2)+1.
    # Take some examples and figure out yourself (it's easy, hint: involves greediness).
    # https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/solutions/3231114/two-pointers

    nums = sorted(nums)

    n = len(nums)
    i = 0
    for j in range((n+1)//2, n):  # `j` will always move
        if 2*nums[i] <= nums[j]:  # if pair forming
            i += 1  # `i` will only move when pair for `i` found
    return i*2  # no. of pairs
