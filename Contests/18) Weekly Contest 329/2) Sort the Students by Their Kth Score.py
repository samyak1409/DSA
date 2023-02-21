"""
https://leetcode.com/problems/sort-the-students-by-their-kth-score
"""


def sort_the_students(score: list[list[int]], k: int) -> list[list[int]]:
    """"""

    # "Insertion sort is widely used for small data sets, while for large data sets an asymptotically efficient sort is
    # used, primarily heapsort, merge sort, or quicksort."
    # - https://en.wikipedia.org/wiki/Sorting_algorithm#Popular_sorting_algorithms

    # 0) Brute-force (https://en.wikipedia.org/wiki/Sorting_algorithm#Simple_sorts): TC = O(n^2); SC = O(1)
    # Find the row with the highest score in the kth exam and swap it with the first row.
    # After fixing the first row, perform the same operation for the rest of the rows, and the matrix's rows will get
    # sorted one by one.

    # 1) Optimal (https://en.wikipedia.org/wiki/Sorting_algorithm#Efficient_sorts): TC = O(n*log(n)); SC = O(n)
    # (https://stackoverflow.com/questions/48759175/what-is-the-space-complexity-of-the-python-sort)
    # https://leetcode.com/problems/sort-the-students-by-their-kth-score/solutions/3083946/java-c-python-sort
    # https://leetcode.com/problems/sort-the-students-by-their-kth-score/solutions/3083914/java-python-3-short-codes-sort-by-the-kth-exam

    score.sort(key=lambda row: row[k], reverse=True)
    return score
