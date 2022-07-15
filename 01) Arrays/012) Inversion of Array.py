"""
https://practice.geeksforgeeks.org/problems/inversion-of-array-1587115620/1
"""


from typing import List


def inversionCount(arr: List[int], n: int) -> int:
    """"""

    # 0) Brute-force (Two Loops) (TLE): TC = O(n^2); SC = O(1)

    count = 0
    for i in range(n):  # go through all the elements in the array one by one
        for j in range(i+1, n):  # for every element, check for all the elements on the right
            if arr[j] < arr[i]:  # "Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j."
                count += 1
    return count
