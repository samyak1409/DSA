"""
https://leetcode.com/problems/count-the-number-of-beautiful-subarrays
"""


def beautiful_subarrays(nums: list[int]) -> int:
    """"""

    # The solution of this question is just realizing that:
    # A subarray is beautiful if its xor is equal to zero.
    # Some explanations why:
    # https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/solutions/3286489/image-explanation-prefix-xor-complete-intuition
    # https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/solutions/3286256/count-subarrays-with-zero-xor
    # (Meme: https://leetcode.com/discuss/general-discussion/3286243/Weekly-Contest-336/1829731)

    # After that, the solution is basically the same as:
    # https://github.com/samyak1409/DSA/blob/main/SDE%20Sheet/01%29%20Arrays/023%29%20Count%20Subarrays%20with%20Given%20XOR.py

    # 1) Optimal (Prefix XOR + HashMap): TC = O(n); SC = O(n)
    # Compute the prefix xor for every index, then the xor of subarray [left, right] is equal to zero if
    # prefix_xor[left] ^ prefix_xor[right] == 0.
    # Iterate from left to right and maintain a hash table to count the number of indices equal to the current prefix
    # xor.

    from collections import Counter
    freq = Counter()
    pref_xor = 0
    freq[pref_xor] = 1
    count = 0

    for num in nums:
        pref_xor ^= num
        count += freq[pref_xor]
        freq[pref_xor] += 1

    return count
