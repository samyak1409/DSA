"""
https://leetcode.com/problems/minimum-impossible-or
"""


def min_impossible_or(nums: list[int]) -> int:
    """"""

    # "Some numbers are impossible to build using the other numbers with or operator. Think about them"
    # -https://leetcode.com/problems/minimum-impossible-or/discussion

    # "My observations:
    # x1 | x2 | x3 .... >= min(x1, x2, x3 ....)
    # x1 | x2 | x3 .... <= x1 + x2 + x3 + ....
    # Not able to understand further, can someone give a tip?"
    # -https://leetcode.com/problems/minimum-impossible-or/discussion
    # "The way you thought is right, and is the 1 way everyone else must have thought, but it doesn't help here, the
    # other way to think is binary.
    # Represent the numbers in binary (but why would this come in mind? because the op we're talking about here is
    # bitwise) and try to make 1 to n (where n is the ans, i.e., min num that can't be made) from any nums, and you'll
    # notice something."
    # -https://leetcode.com/problems/minimum-impossible-or/discussion (My)

    # Think about forming numbers in the powers of 2 using their bit representation.
    # The minimum power of 2 not present in the array will be the first number that could not be expressed using the
    # given operation.

    # 1) Return the first (min) power of 2 which is not there in nums:
    # https://leetcode.com/problems/minimum-impossible-or/solutions/3201924/explained-two-solutions-with-without-extra-space-very-simple-easy-to-understand
    # https://leetcode.com/problems/minimum-impossible-or/solutions/3201897/java-c-python-pow-of-2
    # https://leetcode.com/problems/minimum-impossible-or/solutions/3201880/lowest-missing-bit-o-n-o-1

    # 1.1) Sub-Optimal (Using Sorting): TC = O(n*log(n)); SC = O(n)
    # Solution 1 in:
    # https://leetcode.com/problems/minimum-impossible-or/solutions/3201924/explained-two-solutions-with-without-extra-space-very-simple-easy-to-understand

    """
    nums = sorted(nums)  # TC = O(n*log(n)); SC = O(n)
    ans = 1  # init
    for num in nums:  # TC = O(n)
        if num > ans:  # we came ahead, and `ans`, i.e. a power of 2 was not in nums, so stop
            break
        if num == ans:  # time to ans *= 2
            ans <<= 1
        # else do nothing
    return ans
    """

    # 1.2) Time-Optimal (Using HashSet): TC = O(n + log2(m)) (where m is max(nums[i]), which is 10^9 here); SC = O(n)
    # Solution 2 in:
    # https://leetcode.com/problems/minimum-impossible-or/solutions/3201924/explained-two-solutions-with-without-extra-space-very-simple-easy-to-understand
    # https://leetcode.com/problems/minimum-impossible-or/solutions/3201897/java-c-python-pow-of-2

    """
    nums = set(nums)  # TC = SC = O(n)
    ans = 1
    while ans in nums:  # TC = O(log2(m))
        ans <<= 1  # ans *= 2
    return ans
    """

    # 1.3) Optimal (Using HashMap Smartly):
    # TC = O(n + log2(m)) (where m is max(nums[i]), which is 10^9 here); SC = O(log2(m))
    # https://leetcode.com/problems/minimum-impossible-or/solutions/3201880/lowest-missing-bit-o-n-o-1

    powers_of_2 = set(num for num in nums if (num & num-1 == 0))  # TC = O(n); SC = O(log2(m))
    # `num & num-1 == 0`: best way to check if a +ve int is a power of two or not
    # Notice this condition is the only change in this code from the above one which improved the SC from linear to
    # logarithmic!
    ans = 1
    while ans in powers_of_2:  # TC = O(log2(m))
        ans <<= 1  # ans *= 2
    return ans
