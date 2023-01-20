"""
https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array
"""


def difference_of_sum(nums: list[int]) -> int:
    """"""

    # 1) Brute-force = Optimal (Iterate and Sum): TC = O(n*log10(n)); SC = O(1)

    # 1.1) (One Pass): TC = O(n + n*log10(n)) {log10(n): no. of digits}; SC = O(1)
    # Use a simple for loop to iterate each number.
    # How you can get the digit for each number?

    """
    e_sum = d_sum = 0
    for num in nums:  # O(n * log10(n))
        e_sum += num
        while num:  # O(log10(n))
            d_sum += num % 10
            num //= 10
    return abs(e_sum - d_sum)
    """

    # 1.2) One Liner (Two Pass): TC = O(n + n*log10(n)) {log10(n): no. of digits}; SC = O(n)
    """
    return abs(sum(nums) - sum(map(int, ''.join(map(str, nums)))))
    # `sum(map(int, ''.join(map(str, nums)))))`: Convert each num into a str, join that str, iterate the joined str, and
    #                                            sum all the digits one by one.
    """

    # 1.2.1) One Liner (Two Pass): TC = O(n + n*log10(n)) {log10(n): no. of digits}; SC = O(1)

    """
    # return abs(sum(nums) - sum(map(lambda num: sum(map(int, str(num))), nums)))
    return abs(sum(nums) - sum(sum(map(int, str(num))) for num in nums))
    # `sum(sum(map(int, str(num))) for num in nums))`: Iterate on nums, for every num, convert the num into a str,
    #                                                  iterate on it and sum the digits one by one.
    #                                                  Finally, sum the sums found by this.
    """

    # 1.3) (One Pass): TC = O(n + n*log10(n)) {log10(n): no. of digits}; SC = O(1)

    e_sum = d_sum = 0
    for num in nums:  # O(n * log10(n))
        e_sum += num
        d_sum += sum(map(int, str(num)))  # O(log10(n))
    return abs(e_sum - d_sum)
