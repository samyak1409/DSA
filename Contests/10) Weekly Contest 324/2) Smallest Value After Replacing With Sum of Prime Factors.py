"""
https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors
"""


def smallest_value(n: int) -> int:
    """"""

    # 1) Optimal (Prime Factorization till get a Prime):
    # TC = O(log(n)^2) if n is composite;
    #      O(n) if n is prime;
    # Source: https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number
    # https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/solutions/2923624/c-simple-prime-factorization/comments/1739612
    # SC = O(1)
    #
    # Every time you replace n, it will become smaller until it is a prime number, where it will keep the same value
    # each time you replace it.
    # n decreases logarithmically, allowing you to simulate the process.
    # To find the prime factors, iterate through all numbers less than n from least to greatest and find the maximum
    # number of times each number divides n.
    # https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/solutions/2923847/simple-java-prime-factorization
    # "The idea of this solution relies on the fact that a number is not less than the sum of its primes. Equality is
    # attained for the prime numbers themselves and also for the number 4. Thus, we can iteratively decompose n into
    # primes and compute their sum until the sequence stabilizes."
    # -https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/solutions/2923506/python-c-prime-factorization-explained

    """
    # Helper Function:
    def is_prime(x: int) -> bool:
        for y in range(2, int(x**.5)+1):
            if x % y == 0:
                return False
        return True

    if n == 4:  # exception: sum_of_prime_factors(n) = n
        return n

    # Simulating the Process:
    while not is_prime(n):
        # Finding all the prime factors:
        pf = 2  # prime_factor
        s = 0  # sum
        while n != 1:
            if n % pf == 0:  # if divisible, it's a prime factor
                n //= pf  # divide
                s += pf  # add
            else:  # else increment
                pf += 1
        # Replacing:
        n = s
    return n
    """

    # Turns out that we don't need to check if a number is prime or not and continue the process till we get n two times
    # in a row, also, this handles the exception n == 4 implicitly:

    prev_n = n
    while True:  # O(log(n) * log(n)) if n is composite; O(1 * n) if n is prime
        # Finding all the prime factors:
        pf = 2  # prime_factor
        s = 0  # sum
        while n != 1:  # O(log(n)) if n is composite; O(n) if n is prime
            if n % pf == 0:  # if divisible, it's a prime factor
                n //= pf  # divide
                s += pf  # add
            else:  # else increment
                pf += 1
        # Replacing:
        n = s
        if n == prev_n:  # => we got same n two times in a row => this is a prime or 4, in either case we need to stop
            return n
        prev_n = n  # update
