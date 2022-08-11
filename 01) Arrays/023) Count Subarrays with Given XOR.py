"""
https://www.codingninjas.com/codestudio/problems/1115652
"""


def sub_arrays_xor(arr: list[int], x: int) -> int:
    """"""

    # This problem is solved using the same core logic as
    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/022%29%20Largest%20Subarray%20with%200%20Sum.py.

    # Properties of XOR:
    # A ^ 0 = A
    # A ^ A = 0

    # 0) [TLE] Brute-force (Nested Loop): TC = O(n^2); SC = O(1)

    """
    n = len(arr)
    ans = 0
    for i in range(n):  # choose every element one by one
        xor_value = 0  # init
        for j in range(i, n):
            xor_value ^= arr[j]  # increase the length of sub-array
            if xor_value == x:  # if xor_value of sub-array arr[i:j+1] == x
                ans += 1
    return ans
    """

    # 1) Optimal (Prefix-XOR & HashMap): TC = O(n); SC = O(n)
    # Explanation: https://youtu.be/lO9R5CaGRPY

    prefix_xor = 0
    ans = 0
    frequency = {prefix_xor: 1}  # for O(1) lookup; initializing with "prefix_xor: 1" because:
    # dry run the algo with input (arr=[6, 6], x=6), you'll get the answer.
    for element in arr:  # O(n)
        prefix_xor ^= element
        # using the inverse logic:
        if (freq := frequency.get(prefix_xor ^ x)) is not None:  # O(1)
            ans += freq  # ✔✔ if a pair is made with a prefix_xor, then it will also satisfy with any/every previous
            # occurrences of that particular prefix_xor
        # add/update frequency of prefix_xor:
        frequency[prefix_xor] = frequency.get(prefix_xor, 0) + 1
    return ans

    # Explanation of "inverse logic":
    # If at any iteration, (prefix_xor ^ x) = y is present in the hashmap,
    # this means that from index (index(y)+1) till current index i.e. index(element),
    # the sub-array's XOR is x, that's why we got current prefix_xor from y (if a ^ b = c, then a = b ^ c).
    # Solve this problem for complete understanding: https://leetcode.com/problems/subarray-sum-equals-k
    # (whose sub-problem is:
    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/022%29%20Largest%20Subarray%20with%200%20Sum.py)
