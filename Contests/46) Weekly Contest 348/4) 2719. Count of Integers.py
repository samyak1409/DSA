"""
https://leetcode.com/problems/count-of-integers
"""


def count(num1: str, num2: str, min_sum: int, max_sum: int) -> int:
    """"""

    # 0) [TLE] Brute-force (Check all the numbers):
    # TC = O(n * log10(n)) ~= O(n); SC = O(log10(n)) ~= O(1) {since max(n) = 10^22}

    """
    ans = 0
    for num in range(int(num1), int(num2)+1):  # O(n)
        ans += min_sum <= sum(map(int, str(num))) <= max_sum  # TC = SC = O(log10(n))
    return ans % (10**9 + 7)
    """

    # 1) Sub-Optimal (Recursion + Memoization): TC = O(?); SC = O(?)
    # [Came up with this myself!!]
    # - So, the root problem why the above brute-force approach can't work here is because of the big range of numbers
    #   `1 <= num1 <= num2 <= 10^22`, if the range was not that big, it'd have worked as it's O(n) only.
    # - So, this was the intuition of this approach, we can't loop on num range, maybe we can loop on sum range, as it's
    #   very small: `1 <= min_sum <= max_sum <= 400`.
    # - Now, as we want to count all the nums in the range whose digit sum come in this sum range. So, what we can maybe
    #   do is for each sum, calculate all the nums in our num range whose sum is current sum.
    # - We'd calc. for different num of digits one by one. If our num range is [100, 99999], so this means we only
    #   need to for num len: 3, 4, 5. As nums with any other num len would be out of the range only.
    # - Now, how would we actually calc? We can try all the ways, using recursion. And we can add memoization to it.
    # - Also, we don't actually need sum range upto 400 as there in the constraint, since max num in num range is 10^22,
    #   num with max sum = 10**22 - 1 (as it'd have the most 9s); sum = 198.

    from functools import cache

    # Recursive Function:
    @cache
    def get_count(sum_left: int, len_left: int, min_len_call: bool, max_len_call: bool, msd: bool = False) -> int:
        """
        msd: on the first call, we can't allow 0 because it'd make our number x-1 len (e.g. 0143 = 143).

        min_len_call: as we'd have calls for multiple num lens, when the call is with min num len, we'd actually need to
                      take care of the starting range of digits to be allowed (e.g. `num1` = 69, we can't let the loop
                      below to start from 1 upto 5, and when we move on to the next digit place, we can only start from
                      9).

        max_len_call: same logic as above.
        """
        if sum_left < 0:  # -ve base case of recursion
            return 0
        if len_left == 0:  # +ve base case of recursion
            return sum_left == 0
        # Try all the allowed digits one by one for the next digit in our num whose sum should be `target_sum`:
        cnt = 0
        for digit in range(int(num1[-len_left]) if min_len_call else int(msd),
                           (int(num2[-len_left]) if max_len_call else 9) + 1):
            cnt += get_count(sum_left=sum_left-digit, len_left=len_left-1,
                             min_len_call=min_len_call and digit == int(num1[-len_left]),
                             max_len_call=max_len_call and digit == int(num2[-len_left]))
        return cnt

    ans = 0

    # Loop on sum range:
    for target_sum in range(min_sum, min(max_sum, 198) + 1):
        # We'd target num len one by one:
        for num_len in range(len(num1), len(num2) + 1):
            # (Following func would return the count of nums of len `num_len` which has digit sum `target_sum`.)
            ans += get_count(sum_left=target_sum, len_left=num_len,
                             min_len_call=num_len == len(num1), max_len_call=num_len == len(num2), msd=True)

    return ans % (10**9 + 7)

    # 2) Optimal (Digit DP): TC = O(?); SC = O(?)
    # Hints:
    # 1. Let f(n, l, r) denotes the number of integers from 1 to n with the sum of digits between l and r.
    # 2. The answer is f(num2, min_sum, max_sum) - f(num-1, min_sum, max_sum).
    # 3. You can calculate f(n, l, r) using digit dp.
    # https://leetcode.com/problems/count-of-integers/solutions
