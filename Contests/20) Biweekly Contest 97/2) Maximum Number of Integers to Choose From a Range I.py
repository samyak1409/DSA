"""
https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i
"""


def max_count(banned: list[int], n: int, max_sum: int) -> int:
    """"""

    # 1) Optimal (HashSet + Greedy): TC = O(n); SC = O(n)
    # Keep the banned numbers (that are less than n) in a set.
    # Loop over the numbers from 1 to n and if the number is not banned, use it.
    # Keep adding numbers while they are not banned, and their sum is less than k.

    # banned = set(banned)
    # Lil Better:
    banned = set(num for num in banned if num <= n)  # since "The chosen integers have to be in the range [1, n]."

    count = 0
    cur_sum = 0
    for num in range(1, n+1):
        if num not in banned:
            if (cur_sum := cur_sum+num) <= max_sum:
                count += 1
            else:
                break
    return count
