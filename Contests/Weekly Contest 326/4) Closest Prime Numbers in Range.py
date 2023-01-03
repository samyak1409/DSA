"""
https://leetcode.com/problems/closest-prime-numbers-in-range
"""


def closest_primes(left: int, right: int) -> list[int]:
    """"""

    # Sieve of Eratosthenes
    n = right
    prime = [True] * (n+1)
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p*p, n+1, p):
                prime[i] = False
        p += 1
    # print(prime)  #debugging

    ans = [float('-inf'), float('inf')]
    i = max(left, 2)  # prime mummy penalty
    while i <= n:
        if prime[i]:
            j = i + 1
            while j <= n:
                if prime[j]:
                    if j-i < ans[1]-ans[0]:
                        ans[:] = [i, j]
                    break
                else:
                    j += 1
            i = j
        else:
            i += 1
    return ans if ans != [float('-inf'), float('inf')] else [-1, -1]
