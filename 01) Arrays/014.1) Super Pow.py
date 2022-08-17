"""
https://leetcode.com/problems/super-pow
"""


def super_pow(a: int, b: list[int]) -> int:
    """"""

    # 0) [TLE] Brute-force (Exponentiation by Squaring):  TC = O(log(n)); SC = O(log(n))

    def my_pow(x, n):
        """
        https://github.com/samyak1409/DSA/blob/d81aed952797c645eedf2032ba8537fafb3412a9/01%29%20Arrays/014%29%20Pow(x%2C%20n).py#L111
        """
        if n == 0:  # base case
            return 1  # recurse out
        return my_pow(x*x, n//2) if (n % 2 == 0) else x*my_pow(x*x, (n-1)//2)  # recurse in

    return my_pow(x=a, n=int(''.join(map(str, b)))) % 1337
