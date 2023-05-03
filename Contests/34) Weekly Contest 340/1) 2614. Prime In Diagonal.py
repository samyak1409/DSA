"""
https://leetcode.com/problems/prime-in-diagonal
"""


def diagonal_prime(nums: list[list[int]]) -> int:
    """"""

    # Iterate over the diagonals of the matrix and check for each element.
    # Check if the element is prime or not in O(sqrt(n)) time.

    # 1) Brute-force = Optimal (Check for every val in diagonal using loop (Simple Primality Check, not Sieve)):
    # TC = O(n*2 * v^.5) {max = 600 * 2000 = 1e6}; SC = O(1)

    # Helper Function: O(v^.5) {v: val (nums[i][j]); max(v) = 4e6 => max(v^.5) = 2000}
    def is_prime(val: int) -> bool:
        if val < 2:
            return False
        for div in range(2, int(val**.5)+1):
            if val % div == 0:
                return False
        return True

    # Loop both diagonals: O(n*2) {n: length of a diagonal = len of a row = len of a col; max(n) = 300}
    ans = 0
    for i in range(n := len(nums)):
        for j in range(n):
            if i == j or i == n-j-1:
                # Check prime:
                if is_prime(num := nums[i][j]):
                    # Update ans if required:
                    ans = max(ans, num)
    return ans

    # Further optimization:
    # https://leetcode.com/problems/prime-in-diagonal/solutions/3395752/sieve
    # 1) Using Sieve? NO! Using sieve here will rather increase the TC to O(n*2 + max_v*log(log(max_v))) {max > 4e6}
    # 2) Using memoization/caching? Yes! Using a global HashMap so that we don't re-calc the primes that we've already
    #    checked in other test cases!
