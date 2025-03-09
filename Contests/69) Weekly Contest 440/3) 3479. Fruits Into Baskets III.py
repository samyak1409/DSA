"""
https://leetcode.com/problems/fruits-into-baskets-iii
"""


def num_of_unplaced_fruits(fruits: list[int], baskets: list[int]) -> int:
    """"""

    # 0) [TLE] Brute-force (Simulate: Nested Loop): TC = O(n^2); SC = O(n)

    """
    placed = 0
    for f in fruits:
        for i, b in enumerate(baskets):
            # If basket not already used, and can store current fruit:
            if b and b >= f:
                placed += 1
                baskets[i] = 0  # mark / flag
                break
    return len(fruits) - placed
    """

    # 1) Sub-optimal (Sqrt Decomposition): TC = O(n*sqrt(n)); SC = O(n)
    # Good approach!
    # https://leetcode.com/problems/fruits-into-baskets-iii/solutions/6515947/simple-o-nsqrt-n-solution-explained
    # How this algo battles the TLE is just that instead of traversing the whole baskets again and again, we'd only
    # traverse sqrt(n) times, and since each basket is sqrt(n) size, sorting is also not TLE. This is a mid-way between
    # both.

    from math import ceil, sqrt

    # sqrt decomposition
    bucket_sz = ceil(sqrt(len(fruits)))
    # idx -> baskets within [idx*bucket_sz, (idx+1)*bucket_sz)
    buckets = [[] for _ in range(bucket_sz)]
    for i, basket in enumerate(baskets):
        buckets[i//bucket_sz].append((basket, i))

    # sort each bucket, so that the last element is always the largest basket
    for bucket in buckets:
        bucket.sort()
    print(buckets)  # debug

    # assign fruits to baskets
    placed = 0
    for fruit in fruits:
        for bucket in buckets:
            # bucket contains a basket that can fit our fruit
            if bucket and bucket[-1][0] >= fruit:
                # find the lowest index basket which can fit our fruit
                chosen = min((i, basket) for basket, i in bucket if basket >= fruit)
                bucket.remove((chosen[1], chosen[0]))
                placed += 1
                break
    return len(fruits) - placed

    # 2) Optimal (Segment Tree): TC = O(n*log(n)); SC = O(n)
