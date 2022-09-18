"""
https://leetcode.com/problems/longest-turbulent-subarray
"""


def max_turbulence_size(arr: list[int]) -> int:
    """"""

    # 1) Optimal (Sliding Window): TC = (n); SC = O(1)
    # https://leetcode.com/problems/longest-turbulent-subarray/solution

    max_size = size = 1  # 1 and not 0 because for array [a, b] if a < b then the turbulence is 1 but size of turbulent
    # array is 2
    last = ''  # will track the last sign (doesn't matter at first, both signs will be considered)
    for i in range(len(arr)-1):
        x, y = arr[i], arr[i+1]
        if x < y:
            if last == '<':  # if same sign as last
                size = 1  # reset
            size, last = size+1, '<'  # update
        elif x > y:
            if last == '>':  # if same sign as last
                size = 1  # reset
            size, last = size+1, '>'  # update
        else:  # if x == y => no turbulence
            size, last = 1, ''  # reset
        max_size = max(max_size, size)  # update
    return max_size
