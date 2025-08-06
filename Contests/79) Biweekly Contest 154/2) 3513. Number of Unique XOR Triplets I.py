"""
https://leetcode.com/problems/number-of-unique-xor-triplets-i
"""


from math import log2


def unique_xor_triplets(nums: list[int]) -> int:
    """"""

    # 1) Optimal (Observing the Pattern; Maths): TC = O(1); SC = O(1)
    # [Came up with myself.]
    # Observation 1:
    # There are only 3 options:
    # - Triplet has all the same nums, e.g., `1,1,1`. Then the xor would be = the num itself. So total = len(nums).
    # - Triplet has two nums the same, e.g., `1,2,2`. In this case, the two nums which are repeated would be canceled,
    # hence the odd one would be left, but since those would already be covered in above, total = 0.
    # - Triplet has all the different nums, e.g. `1,2,3`. In this case total would be = ?.
    #
    # Next, trying to find a pattern:
    """
    from itertools import combinations
    from math import log2
    for n in range(1, 10):
        nums = [x for x in range(1, n+1)]
        hs = set(nums)
        for c in combinations(nums, 3):
            # print(c, c[0] ^ c[1] ^ c[2])
            hs.add(c[0] ^ c[1] ^ c[2])
        print('n:', n, 'ans:', len(hs))
    """
    # Pattern got: 2**(int(log2(n))+1)

    # Edge case, when `n` = 1 or 2, "triplets has all the three nums different" doesn't apply, so total = `n`.

    """
    n = len(nums)
    return n if n < 3 else 2**(int(log2(n))+1)
    """
    # Or:
    return n if (n:=len(nums)) < 3 else 2**(int(log2(n))+1)

    # Why does this pattern work?
    # https://leetcode.com/problems/number-of-unique-xor-triplets-i/solutions/6643510/java-python-3-2-liners-w-brief-explanation-and-analysis
    # [We're only talking about n >= 3 cases.]
    # - First, check observation 2: Max answer we can get is capped by the number of binary bits of `n`.
    # We can form every number possible in the current number of bits, e.g.:
    # Example 1: nums = [1, 2, 3]
    # number of bits = 2
    # All the numbers which can be formed using 2 bits:
    # 00 (0)
    # 01 (1)
    # 10 (2)
    # 11 (3)
    # 00 can be formed by 1^2^3
    # 01 can be formed by 1^1^1
    # 10 can be formed by 2^2^2
    # 11 can be formed by 3^3^3
    # Example 2: nums = [1, 2, 3, 4]
    # 2**(int(log2(n))+1) = 8
    # All the numbers in the range [0, 7] can be formed using `nums[i]^nums[j]^nums[k]`.
