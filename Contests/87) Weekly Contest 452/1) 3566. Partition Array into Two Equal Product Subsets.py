"""
https://leetcode.com/problems/partition-array-into-two-equal-product-subsets
"""


def check_equal_partitions(nums: list[int], target: int) -> bool:
    """"""

    # 1) Brute-force = Suboptimal (Combinations):
    # TC = O(n * comb(n, r) * r) {r: [1, n-1]}
    #    = O(n * 2^n) {https://chatgpt.com/share/685420d2-ef48-800a-b3b2-2d754df68a7d}
    # SC = O(n)
    # (I did this during the contest.)
    # [Easy]
    # Trying all the subsets of each length from 1 to n-1.

    """
    from itertools import combinations

    # Total product of `nums`:
    p = 1
    for num in nums:
        p *= num

    # One by one from 1 to n-1:
    for r in range(1, len(nums)):  # O(n)
        # Loop on all the `r` length combinations:
        for c in combinations(nums, r):  # O(comb(n, r)) {r: [1, n-1]}
            # print(c)  # debug
            # And check if the product of `c` and remaining product is coming as equal:
            p1, p2 = p, 1
            for num in c:  # O(r)
                p1 //= num
                p2 *= num
                if p1 < target or p2 > target:
                    break
            # print('ans', p1, p2)  # debug
            if p1 == p2 == target:
                return True
    return False
    """

    # "i thought of calculating the product of whole array and check if its root matches with the target, until this test case hit me: `nums = [4, 4, 4], target = 8`"
    # -https://leetcode.com/problems/partition-array-into-two-equal-product-subsets/description/comments/3015447
    # Above statement looks correct on first read, but the test case can be used to understand why this solution would not work. However:
    # "Your statement is actually true, but it serves as an early return. there is a second check: you need to visit each subsets, and return if some subproduct is equal to the target."
    # -https://leetcode.com/problems/partition-array-into-two-equal-product-subsets/description/comments/3022053/?parent=3015447
    # So, to repeat:
    # "If the square root of the entire product of nums is not equal to the target, then the array cannot be partitioned equally.
    # If we find a subproduct that is equal to the target, then the complementary subproduct is guaranteed to be equal. (1st statement must be true)."
    # -https://leetcode.com/problems/partition-array-into-two-equal-product-subsets/description/comments/3016659

    from math import isqrt
    from itertools import combinations

    # Total product of `nums`:
    p = 1
    for num in nums:
        p *= num

    # Early return optimization:
    if isqrt(p) != target:
        return False

    # One by one from 1 to n-1:
    for r in range(1, len(nums)):  # O(n)
        # Loop on all the `r` length combinations:
        for c in combinations(nums, r):  # O(comb(n, r)) {r: [1, n-1]}
            # print(c)  # debug
            # And check if the product of `c` is coming equal to `target`:
            p = 1
            for num in c:  # O(r)
                p *= num
                if p > target:
                    break
            # print('ans', p)  # debug
            if p == target:
                return True
    return False

    # 2) Time-optimal (Recursion: Backtracking): TC = O(2^n); SC = O(n) {recursion stack}
    # [Easy]

    # 3) Optimal (Bit Manipulation: Bitmask): TC = O(2^n); SC = O(1)
    # [Easy]
