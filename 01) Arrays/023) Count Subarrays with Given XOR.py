"""
https://www.codingninjas.com/codestudio/problems/1115652
"""


def sub_arrays_xor(arr: list[int], x: int) -> int:
    """"""

    # 0) [TLE] Brute-force (Nested Loop): TC = O(n^2); SC = O(1)

    n = len(arr)
    count = 0
    for i in range(n):  # choose every element one by one
        xor_value = 0  # init
        for j in range(i, n):
            xor_value ^= arr[j]  # increase the length of sub-array
            if xor_value == x:  # if xor_value of sub-array arr[i:j+1] = x
                count += 1
    return count
