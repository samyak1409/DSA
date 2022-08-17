"""
https://leetcode.com/problems/xor-queries-of-a-subarray
"""


def xor_queries(arr: list[int], queries: list[list[int]]) -> list[int]:
    """"""

    # Solution is based on the same concept used in:
    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/023%29%20Count%20Subarrays%20with%20Given%20XOR.py

    # 1) Optimal (Prefix-XOR): TC = (n); SC = O(n)
    # https://leetcode.com/problems/xor-queries-of-a-subarray/discuss/470787/JavaC%2B%2BPython-Straight-Forward-Solution

    # Forming Prefix-XOR Array:
    prefix_xor_arr = [0]  # init
    for num in arr:
        prefix_xor_arr.append(prefix_xor_arr[-1] ^ num)

    # Traverse Queries, Calc. Ans. and Yield:
    for (left, right) in queries:
        yield prefix_xor_arr[right+1] ^ prefix_xor_arr[left]  # using the same inverse logic
