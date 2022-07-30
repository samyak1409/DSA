"""
https://practice.geeksforgeeks.org/problems/inversion-of-array-1587115620/1
"""


def inversion_count(arr: list[int], n: int) -> int:
    """"""

    # 0) [TLE] Brute-force (Two Loops): TC = O(n^2); SC = O(1)

    """
    count = 0
    for i in range(n):  # go through all the elements in the array one by one
        for j in range(i+1, n):  # for every element, check for all the elements on the right
            if arr[j] < arr[i]:  # "Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j."
                count += 1
    return count
    """

    # 1) Optimal (Using Merge Sort): TC = O(n*log(n)); SC = O(n)
    # Prerequisite: https://github.com/samyak1409/python-lab-assignments/blob/main/10/a.py (Merge Sort Algorithm)

    def get_count(array: list[int], length: int) -> int:
        count = 0
        if length > 1:
            # Step-1) Dividing:
            mid_index = length // 2
            left, right = array[:mid_index], array[mid_index:]
            count = get_count(array=left, length=mid_index) + get_count(array=right, length=length-mid_index)
            # Step-2) Merging:
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    array[i+j] = left[i]
                    i += 1
                else:
                    array[i+j] = right[j]
                    j += 1
                    count += (len(left)-i)  # when element from right list (right[j]) is considered before all left[i:]
                    # => total len(left)-i inversions will be there (only for this particular right[j])
            array[i+j:] = left[i:] or right[j:]
        return count

    return get_count(array=arr.copy(), length=n)  # copy() so that input array remains unmodified
