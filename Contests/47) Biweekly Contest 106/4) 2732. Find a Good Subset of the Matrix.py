"""
https://leetcode.com/problems/find-a-good-subset-of-the-matrix
"""


def good_subset_of_binary_matrix(grid: list[list[int]]) -> list[int]:
    """"""

    # 1) Optimal (Greedy, Sort):
    # TC = O(n*m + (n * 2^n) + (n * 2^2n)) = O(n * (m + 2^n + 2^2n)) = O(n * (m + 2^n * (1 + 2^n))) = O(n * (m + 2^2n))
    # SC = O((n * 2^n) + (n * 2^n) + n) = O(n * (2^n + 2^n + 1)) = O(n * 2^n)
    # [Came up with this myself!]
    # We need to have the column sum for every item to be <= half of number of rows we're taking.
    # If we're taking 1 row: max allowed column sum = 0
    #                 2                             = 1
    #                 3                             = 1
    #                 4                             = 2
    # Observation 1: As we can return any "good" subset of rows, it'd be the easiest for us to find the smallest one
    # (with the least number of rows), and the main observation is that if there are "good" subsets, then one subset
    # would form with 2 rows only. (And even one row only for the only case when all 0s row is present.)
    # Observation 2: Duplicate rows are disadvantage so we want unique rows only.
    # Observation 3: We can sort the rows by sum(row), and iterate and try to make pair with the following rows using
    # nested for loop to get the ans.
    # So, for following are the possible cases:
    # case 1: all 0s row is present, that's ans
    # case 2: at least two single 1s rows are present, that's ans
    # case 3: one single 1s row is there, try to pair it with every other row present
    # case 4: one by one try to make a pair of double 1s row with all the following upto triple 1s rows
    # case 5: ans not possible

    # Remove duplicates:
    hs = set(map(tuple, grid))  # TC = O(n*m); SC = O(n * 2^n)
    # Edge case: all 0s row is present:
    if (0,)*(n := len(grid[0])) in hs:
        return [grid.index([0]*n)]

    # For all the other cases:
    sorted_rows = sorted(hs, key=sum)  # TC = O((n * 2^n) + (2^n * log(2^n))) = O((n * 2^n) + (2^n * n)) = O(n * 2^n)
    # SC = O(n * 2^n)
    # Trying to make "good" pairs of two rows:
    for i in range((m := len(sorted_rows))-1):  # TC = O(2^n * (n + (2^n * n))) = O(2^n * (n * (1 + 2^n))) = O(n * 2^2n)
        # SC = O(n)
        curr_1_len = sum(row1 := sorted_rows[i])
        # `curr_1_len`: using for optimization: if n = 5, then we only need to go till double 1s rows in outer loop
        # and triple 1s rows in inner loop.
        for j in range(i+1, m):
            if curr_1_len+sum(row2 := sorted_rows[j]) > n:  # optimization
                break
            if all(val1+val2 <= 1 for val1, val2 in zip(row1, row2)):  # (max sum is 1 because we're making pairs of 2)
                return sorted([grid.index(list(row1)), grid.index(list(row2))])  # "Return ... in ascending order."
        if curr_1_len > n//2:  # optimization
            break
    # No "good" subset possible:
    return []
