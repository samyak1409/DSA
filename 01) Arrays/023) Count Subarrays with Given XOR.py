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
    count = 0
    for i in range(n):  # choose every element one by one
        xor_value = 0  # init
        for j in range(i, n):
            xor_value ^= arr[j]  # increase the length of sub-array
            if xor_value == x:  # if xor_value of sub-array arr[i:j+1] == x
                count += 1
    return count
    """

    # 1) Optimal (Prefix-XOR & HashMap): TC = O(n); SC = O(n)
    # Explanation: https://youtu.be/lO9R5CaGRPY

    from collections import Counter
    frequency = Counter()  # Counter for easy working with counts
    prefix_xor = 0
    frequency[prefix_xor] = 1  # initializing with "prefix_xor: 1" because:
    # dry run the algo with input (arr=[6, 6], x=6), you'll get the answer.
    count = 0
    for element in arr:
        prefix_xor ^= element
        # using the inverse logic:
        count += frequency[prefix_xor ^ x]  # ✔✔ if a pair is made with a prefix_xor, then it will also satisfy with any
        # & every previous occurrences of that particular prefix_xor
        # add/update frequency of prefix_xor:
        frequency[prefix_xor] += 1
    return count

    # Explanation of "inverse logic":
    # If at any iteration, (prefix_xor ^ x) = y is present in the hashmap,
    # this means that from index (index(y)+1) till current index i.e. index(element),
    # the sub-array's XOR is x, that's why we got current prefix_xor from y (if a ^ b = c, then a = b ^ c).
    # Solve this problem for complete understanding: https://leetcode.com/problems/subarray-sum-equals-k
    # (whose sub-problem is:
    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/022%29%20Largest%20Subarray%20with%200%20Sum.py)


# Similar Questions:
# https://www.codingninjas.com/codestudio/problems/920321
# https://leetcode.com/problems/subarray-sum-equals-k
# https://leetcode.com/problems/binary-subarrays-with-sum
# https://leetcode.com/problems/xor-queries-of-a-subarray
# https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum
# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum
