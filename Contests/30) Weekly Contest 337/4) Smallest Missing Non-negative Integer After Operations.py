"""
https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations
"""


def find_smallest_integer(nums: list[int], value: int) -> int:
    """"""

    # Think about using modular arithmetic.
    # If x = nums[i] (mod value), then we can make nums[i] equal to x after some number of operations.
    # How does finding the frequency of (nums[i] mod value) help?

    # 1) Optimal (Mod Op + HashMap): TC = O(n); SC = O(n)
    # https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/solutions/3313988/count-moduli

    from collections import Counter
    mod_counts = Counter(num % value for num in nums)
    # print(mod_counts)  #debugging

    ans = 0
    while mod_counts[ans % value]:
        mod_counts[ans % value] -= 1
        ans += 1
    return ans

    # Explanation:
    # First, we're doing `num % value`, then we're checking if `ans % value` is left in counts or not.
    # We're doing this to make sure that if `ans % value` is there in `mod_counts` for `num % value`, then this will
    # mean that we can make `num` equal to `ans` by adding/subtracting `value` to/from it some no. of times!
    # So, we do `ans += 1`.
