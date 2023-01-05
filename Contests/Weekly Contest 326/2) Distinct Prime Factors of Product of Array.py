"""
https://leetcode.com/problems/distinct-prime-factors-of-product-of-array
"""


def distinct_prime_factors(nums: list[int]) -> int:
    """"""

    # 1) Optimal (One by One Prime Factorization):
    # TC = O(n*v) {n: len(nums) <= 10^4 & v: nums[i] <= 1000};
    # SC = O(primes till v) {https://www.google.com/search?q=how+many+primes+are+there+till+1000}
    # Do not multiply all the numbers together, as the product is too big to store.
    # Think about how each individual number's prime factors contribute to the prime factors of the product of the
    # entire array.
    # Find the prime factors of each element in nums, and store all of them in a set to avoid duplicates.
    # https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/solutions/2977549/c-easy-to-understand

    distinct = set()
    for num in nums:
        # Prime Factorization: O(log(num)) if num is composite; O(num) if num is prime
        factor = 2
        while num != 1:
            if num % factor == 0:
                num //= factor
                distinct.add(factor)
            else:
                factor += 1
    return len(distinct)

    # Also see:
    # https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/solutions/2977286/large-prime-optimization
