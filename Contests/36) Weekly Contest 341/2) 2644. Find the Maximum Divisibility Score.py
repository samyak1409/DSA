"""
https://leetcode.com/problems/find-the-maximum-divisibility-score
"""


def max_div_score(nums: list[int], divisors: list[int]) -> int:
    """"""

    # Consider counting for each element in divisors the count of elements in nums divisible by it using bruteforce.
    # After counting for each divisor, take the one with the maximum count. In case of a tie, take the minimum one of
    # them.

    # 1) Brute-force = Optimal (Calc. for every divisor): TC = O(n*d); SC = O(d)

    ans, max_score = None, -1  # -1 so that even 0 > -1 and so `ans` is updated w/ some real val.

    for div in set(divisors):  # set to avoid checking for duplicates

        if (score := sum(num % div == 0 for num in nums)) > max_score:
            ans, max_score = div, score  # update ans
        elif score == max_score:
            ans = min(ans, div)  # "If there is more than one int with the max score, return the min of them."

    return ans

    # Additional: https://leetcode.com/problems/find-the-maximum-divisibility-score/submissions/945200004
