"""
https://leetcode.com/problems/first-missing-positive
"""


def first_missing_positive(nums: list[int]) -> int:
    """"""

    # Think about how you would solve the problem in non-constant space. Can you apply that logic to the existing space?
    # We don't care about duplicates or non-positive integers.
    # Remember that O(2n) = O(n).

    # 0) Brute-force (HashSet): TC = O(n); SC = O(n_) (n_: no. of +ve ints in arr)

    # Pass 1: Hash
    positives = set(num for num in nums if num > 0)
    # Pass 2: Search
    min_positive = 1  # init
    while min_positive in positives:
        min_positive += 1
    return min_positive

    # 1) Optimal (?): TC = O(n); SC = O(1)
    # https://leetcode.com/problems/first-missing-positive/discuss/17071/My-short-c++-solution-O(1)-space-and-O(n)-time
    # https://leetcode.com/problems/first-missing-positive/discuss/17080/Python-O(1)-space-O(n)-time-solution-with-explanation
    # https://leetcode.com/problems/first-missing-positive/discuss/17214/Java-simple-solution-with-documentation
