"""
https://leetcode.com/problems/make-k-subarray-sums-equal
"""


def make_sub_k_sum_equal(arr: list[int], k: int) -> int:
    """"""

    # DISCLAIMER: This is marked as Medium, but is definitely a Hard.

    # Think about gcd(n, k). How will it help to calculate the answer?
    # indices i and j are in the same group if gcd(n, k) mod i = gcd(n, k) mod j. Each group should have equal elements.
    # Think about the minimum number of operations for each group
    # The minimum number of operations for each group equals the summation of differences between the elements and the
    # median of elements inside the group.

    # 1) Optimal (Math (GCD) + Greedy + Sorting + Math (Median)): TC = O(n*log(n)); SC = O(n)
    # a) Recognize the basic pattern.
    # b) [Hardest Part] Realize the involvement of GCD.
    # c) Divide in buckets.
    # d) [Also Tricky] Greedily (using median not mean) equalize them.
    # Read following for understanding:
    # https://leetcode.com/problems/make-k-subarray-sums-equal/solutions/3366442/python3-find-median-of-each-gcd-defined-subarray-w-examples
    # https://leetcode.com/problems/make-k-subarray-sums-equal/solutions/3367765/explaining-like-you-are-five-years-old
    # https://leetcode.com/problems/make-k-subarray-sums-equal/solutions/3366373/k-cycles

    # [WA] Using Mean as Greedy Criteria:
    # Input: arr = [2,10,9]; k = 1
    # Output: 10
    # Expected: 8

    """
    from math import gcd
    gcd = gcd(n := len(arr), k)

    min_ops = 0
    for i in range(gcd):
        bucket = [arr[j] for j in range(i, n, gcd)]
        mean = round(sum(bucket)/len(bucket))
        min_ops += sum(abs(num-mean) for num in bucket)
    return min_ops
    """

    # Using Median as Greedy Criteria:
    # https://leetcode.com/problems/make-k-subarray-sums-equal/solutions/3366373/k-cycles/comments/1850476

    from math import gcd
    gcd = gcd(n := len(arr), k)

    min_ops = 0
    for i in range(gcd):
        bucket = sorted(arr[j] for j in range(i, n, gcd))
        median = bucket[len(bucket)//2]  # why is this working for even len cases also?
        min_ops += sum(abs(num-median) for num in bucket)
    return min_ops
