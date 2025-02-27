"""
https://leetcode.com/problems/sum-of-good-numbers
"""


def sum_of_good_numbers(nums: list[int], k: int) -> int:
    """"""

    # 1) Brute-force = Optimal (Loop): TC = O(n); SC = O(1)
    # So the main thing in the implementation is the order of the conditions:
    # We've 4 possibilities:
    # 1. Both indices exist.
    # 2. Only left index exist.
    # 3. Only right index exist.
    # 4. Neither of the indices exist.
    # So, we need to put the `if` statements in this order only.
    # Reason? Same as that in https://leetcode.com/problems/fizz-buzz.
    # And why are we putting the "element greater or not" lines in the inner block, because we want our if-else on the
    # basis of indices-existence only. Merge the conditions to one line and dry run to know.

    """
    ans = 0
    for i in range(n:=len(nums)):
        num = nums[i]
        if i-k >= 0 and i+k < n:
            if num > nums[i-k] and num > nums[i+k]:
                ans += num
        elif i-k >= 0:
            if num > nums[i-k]:
                ans += num
        elif i+k < n:
            if num > nums[i+k]:
                ans += num
        else:  # (if i-k < 0 and i+k >= n)
            ans += num
    return ans
    """

    # Turns out we can do it concisely using `or`:

    ans = 0
    for i in range(n:=len(nums)):
        num = nums[i]
        if (i-k < 0 or num > nums[i-k]) and (i+k >= n or num > nums[i+k]):
            ans += num
    return ans
