"""
https://leetcode.com/problems/prime-subtraction-operation
"""


def prime_sub_operation(nums: list[int]) -> bool:
    """"""

    # Think about if we have many primes to subtract from nums[i]. Which prime is more optimal?
    # The most optimal prime to subtract from nums[i] is the one that makes nums[i] the smallest as possible and greater
    # than nums[i-1].

    # 1) Optimal (Greedy, Sieve of Eratosthenes + Binary Search): TC = O(n*log(n)); SC = O(n)
    # https://leetcode.com/problems/prime-subtraction-operation/solutions

    # i) Pre-process: Calculate the primes till 1000: TC = O(n*log(log(n))); SC = O(n)
    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes:
    # (https://www.geeksforgeeks.org/how-is-the-time-complexity-of-sieve-of-eratosthenes-is-nloglogn)
    n = 1000
    is_prime = [i > 1 for i in range(n+1)]  # [False, False, True, ... True]
    # print(is_prime)  #debugging
    for num in range(2, int(n**.5)+1):  # [2, √n]
        if is_prime[num]:
            for multiple in range(num*num, n+1, num):
                is_prime[multiple] = False
    # print(is_prime)  #debugging
    primes = [num for num, prime in enumerate(is_prime) if prime]
    # print(primes)  #debugging

    # ii) Main: TC = O(n * log(n)); SC = O(1)
    for i in range(len(nums)):

        # Binary search the biggest prime which can be subtracted: TC = O(log(n)); SC = O(1)
        # https://en.wikipedia.org/wiki/Binary_search_algorithm#Procedure_for_finding_the_rightmost_element:
        # See `Contests/Weekly Contest 331/3) House Robber IV.py` for more info about this paradigm.
        lo, hi = 0, len(primes)-1 + 1  # (imp: using indices)
        while lo < hi:
            mid = (lo+hi) // 2
            prime = primes[mid]
            if (i == 0 and nums[i] > prime) or nums[i]-prime > nums[i-1]:  # (`i == 0 and nums[i] > prime`: for index 0)
                # for this particular `prime`, it's possible, so let's try with a bigger `prime`
                lo = mid + 1
            else:  # we need a smaller `prime`
                hi = mid
        # Subtract:
        if hi:  # or lo
            # only subtracting if hi (or lo) != 0, if hi (or lo) == 0 => no prime satisfied (nums[i] <= prime[0])
            nums[i] -= primes[hi-1]  # or lo-1

        # Check if not strictly increasing:
        if i and nums[i] <= nums[i-1]:  # (`i and`: to avoid checking for index 0)
            return False

    # Can make nums a strictly increasing array using the ops.
    return True
