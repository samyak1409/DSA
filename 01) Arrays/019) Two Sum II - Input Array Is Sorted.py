"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
"""


def two_sum(numbers: list[int], target: int) -> list[int]:
    """"""

    # NOTE: All the following solutions are from
    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/019%29%20Two%20Sum%20.py
    # because this problem is just a subset of https://leetcode.com/problems/two-sum.

    # https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/discuss/51249/Python-different-solutions-(two-pointer-dictionary-binary-search).

    # 0) [TLE] Brute-force (Nested Loop): TC = O(n^2); SC = O(1)

    """
    n = len(numbers)
    for i in range(n):
        for j in range(i+1, n):
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
    """

    # 1) [TLE] Better (Binary Search): TC = O(n*log(n)); SC = O(1)

    """
    n = len(numbers)
    # Taking every num one by one:
    for index1 in range(n):
        required_num2 = target - numbers[index1]  # numbers[index1] = num1
        # Finding the required_num2 using Binary Search:
        low, high = index1+1, n-1
        while low <= high:
            index2 = (low+high) // 2  # mid index
            num2 = numbers[index2]
            if num2 == required_num2:
                return [index1+1, index2+1]
            elif num2 < required_num2:
                low += 1
            else:  # (if num2 > required_num2)
                high -= 1
    """

    # Note: We can apply the HashMap solution to this problem as well, but not applying because
    # "Your solution must use only constant extra space." - mentioned in the problem.

    # 2) Optimal (Two-Pointers): TC = O(n); SC = O(1)

    # Finding the 2 numbers using Two-Pointers:
    low, high = 0, len(numbers)-1  # initialization
    while low < high:
        num1, num2 = numbers[low], numbers[high]
        if num1 + num2 == target:
            return [low+1, high+1]
        elif num1 + num2 < target:  # => we want greater sum
            low += 1  # considering next num (larger) in right
        else:  # (if num1 + num2 > target) => we want lesser sum
            high -= 1  # considering next num (smaller) in left


# Similar Question: https://leetcode.com/problems/two-sum-iv-input-is-a-bst
