"""
https://leetcode.com/problems/missing-number
"""


def missing_number(nums: list[int]) -> int:
    """"""

    # 0.1) Brute-force (Loop on n and Lookup): TC = O(n^2); SC = O(1)

    # 0.2) Brute-force (Sort and Traverse): TC = O(n*log(n)); SC = O(n)

    # 1) Time-Optimal Brute-force (HashSet + Loop on n and Lookup): TC = O(n); SC = O(n)

    # Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

    # 2) Optimal: TC = O(n); SC = O(1)

    # 2.2) Bit Manipulation: XOR:
    # https://leetcode.com/problems/missing-number/discuss/69791/4-Line-Simple-Java-Bit-Manipulate-Solution-with-Explaination

    """
    ans = (n := len(nums))
    for i in range(n):
        ans ^= nums[i] ^ i
    return ans
    """

    # "For people who don't understand this solution: what he's doing is he's using the bitwise XOR operator to single
    # out the missing number.
    # How? First, we need to understand the properties of XOR:
    # Firstly, XOR-ing a number by itself results in 0. So if we have 1 ^ 1, this will equal 0.
    # Secondly, XOR is commutative and associative - what this means is we can re-order our XOR operations in any way
    # we want, and it will result in the same value we would have if we didn't.
    # Finally, a number XOR-ed by 0 will result in the same number unchanged. So, essentially, by XOR-ing all the
    # numbers from 0 to n, and all the numbers in the array, we will end up XOR-ing 2 of every number except for the
    # missing one.
    # As we know, it doesn't matter which order we XOR these numbers in - as long as we XOR 2 of the same number, it
    # will result in 0. So eventually we will get 0 ^ the missing number, which, due to the third property I mentioned,
    # will simply equal the missing number.
    # If you're not convinced as to how these properties work, I'd recommend taking a quick look as to how they work."
    # -https://leetcode.com/problems/missing-number/discuss/69777/C++-solution-using-bit-manipulation/196136

    # 2.1) Maths: Sum of n terms:

    n = len(nums)
    return n*(n+1)//2 - sum(nums)
