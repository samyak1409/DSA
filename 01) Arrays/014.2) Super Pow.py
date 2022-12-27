"""
https://leetcode.com/problems/super-pow
"""


def super_pow(a: int, b: list[int]) -> int:
    """"""

    # 1) Optimal (Exponentiation by Squaring): TC = O(log(n)); SC = O(log(n))
    # Like `1.2)` of https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/014%29%20Pow(x%2C%20n).py.

    """
    # Recursive Function:
    def my_pow(x, n):
        if n == 0:  # base case
            return 1  # recurse out
        return my_pow(x*x, n//2) if (n % 2 == 0) else x*my_pow(x*x, (n-1)//2)  # recurse in

    return my_pow(x=a, n=int(''.join(map(str, b)))) % 1337
    """

    # Strange: `1 <= b.length <= 2000` => max(b) = (10**2000)-1 and log2((10**2000)-1) = 6644 (approx)
    # Then why are we getting TLE?
    # Because the ans becomes bigger and bigger and so ops take more and more time.
    # We only need to return `ans` mod 1337 and not actual `ans`, so we can avoid expensive ops by using mod at every
    # step. God! Use this everytime in Qs where mod thing is given.

    # Recursive Function:
    def my_pow(x, n):
        if n == 0:  # base case
            return 1  # recurse out
        return my_pow(x*x % 1337, n//2) % 1337 if (n % 2 == 0) else x*my_pow(x*x % 1337, (n-1)//2) % 1337  # recurse in

    return my_pow(x=a, n=int(''.join(map(str, b))))

    # 2) Optimal (Maths Based): TC = O(?); SC = O(?)
    # https://leetcode.com/problems/super-pow/solutions
