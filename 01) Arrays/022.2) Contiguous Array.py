"""
https://leetcode.com/problems/contiguous-array
"""


def find_max_length(nums: list[int]) -> int:
    """"""

    # All the solutions are (modifications of the solutions) from
    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/022%29%20Longest%20Subarray%20with%200%20Sum.py.

    # 1) Optimal (0s to -1s; Prefix Sum & HashMap): TC = O(n); SC = O(n)

    n = len(nums)
    # 0s to -1s:
    for i in range(n):
        if nums[i] == 0:
            nums[i] = -1
    # And now the question has been transformed to: `022 Longest Subarray with 0 Sum.py`

    # Prefix Sum Algorithm:
    prefix_sum = 0
    leftmost_index = {prefix_sum: -1}  # for O(1) lookup; initializing with `prefix_sum: -1` because:
    # dry run the algo with input arr = [1, -1, 1, -1], you'll get the answer.
    max_len = 0
    for index in range(n):
        prefix_sum += nums[index]
        if (leftmost := leftmost_index.get(prefix_sum)) is not None:  # => this prefix_sum has occurred before
            max_len = max(max_len, index-leftmost)  # `index-leftmost` = length of 0 sum subarray
        else:  # this prefix_sum has occurred 1st time
            leftmost_index[prefix_sum] = index  # save `prefix_sum: index`

    # -1s back to 0s (Good Practice):
    for i in range(n):
        if nums[i] == -1:
            nums[i] = 0

    return max_len
