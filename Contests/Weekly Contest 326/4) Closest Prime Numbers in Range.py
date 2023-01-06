"""
https://leetcode.com/problems/closest-prime-numbers-in-range
"""


# Sieve of Eratosthenes (https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes):
# https://github.com/samyak1409/python-lab-assignments/blob/main/5/a.py
# TC = O(n*log(log(n))); SC = O(n) {n is fixed here = 10^6}
# https://www.geeksforgeeks.org/how-is-the-time-complexity-of-sieve-of-eratosthenes-is-nloglogn
# We use Sieve of Eratosthenes to find all primes <= 10^6.
# We store those primes in a global array, so we can reuse it between test cases.

n = 10 ** 6  # "1 <= left <= right <= 10^6"
is_prime = [i > 1 for i in range(n+1)]  # [0, 1, 2 ... n]
for num in range(2, int(n**.5)+1):  # [2, √n]
    if is_prime[num]:
        for multiple in range(num*num, n+1, num):
            is_prime[multiple] = False
# print(is_prime)  #debugging


def closest_primes(left: int, right: int) -> list[int]:
    """"""

    # 1) Optimal (Sieve of Eratosthenes):
    # TC = O(n*log(log(n))) {where n = 10^6; only single time for all the test cases} + O(right-left);
    # SC = O(n) {across any and every test case}
    # Use Sieve of Eratosthenes to mark numbers that are primes.
    # Iterate from right to left and find pair with the minimum distance between marked numbers.

    # About optimization:
    # "Difference between two consecutive primes is called Prime Gap.
    # There is only one gap of 1 (3 - 2).
    # There are many primes with the gap of 2 - they are called twin primes.
    # So, we exit early if we find a gap < 3, which improves runtime to 0 ms."
    # -https://leetcode.com/problems/closest-prime-numbers-in-range/solutions/2977256/sieve-of-eratosthenes

    """
    prev_prime = None
    ans = []
    for num_ in range(left, right+1):
        if is_prime[num_]:
            if prev_prime and (not ans or num_-prev_prime < ans[1]-ans[0]):
                ans[:] = prev_prime, num_
                if ans[1]-ans[0] < 3:  # optimization
                    return ans
            prev_prime = num_
    return ans or [-1, -1]
    """
    # Or:
    prev_prime = float('-inf')
    ans = [float('-inf'), float('inf')]
    for num_ in range(left, right+1):
        if is_prime[num_]:
            if (gap := num_-prev_prime) < ans[1]-ans[0]:
                ans[:] = prev_prime, num_
                if gap < 3:  # optimization
                    return ans  # (wrong warning)
            prev_prime = num_
    return ans if ans != [float('-inf'), float('inf')] else [-1, -1]

    # Read more: https://leetcode.com/problems/closest-prime-numbers-in-range/solutions
