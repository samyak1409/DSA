"""
https://leetcode.com/problems/k-items-with-the-maximum-sum
"""


def k_items_with_maximum_sum(num_ones: int, num_zeros: int, num_neg_ones: int, k: int) -> int:
    """"""

    # It is always optimal to take items with the number 1 written on them as much as possible.
    # If k > numOnes, after taking all items with the number 1, it is always optimal to take items with the number 0
    # written on them as much as possible.
    # If k > numOnes + numZeroes we are forced to take `k - numOnes - numZeroes` -1s.

    # 0) Brute-force (Greedy: Loop): TC = O(k); SC = O(1)

    """
    max_sum = 0

    for _ in range(k):
        if num_ones:
            max_sum += 1
            num_ones -= 1
        elif num_zeros:
            num_zeros -= 1
        elif num_neg_ones:
            max_sum -= 1
            num_neg_ones -= 1

    return max_sum
    """

    # 1) Optimal (Greedy: Maths): TC = O(1); SC = O(1)
    # https://leetcode.com/problems/k-items-with-the-maximum-sum/solutions/3342004/one-liner

    # If k can be filled by only using 1s and 0s:
    if k <= num_ones+num_zeros:
        return min(num_ones, k)

    # Else just subtract the number of remaining k (after filling all the 1s & 0s) because they will be filled by -1s:
    return num_ones - (k-(num_ones+num_zeros))
