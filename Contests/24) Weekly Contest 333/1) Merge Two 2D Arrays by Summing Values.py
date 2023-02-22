"""
https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values
"""


def merge_arrays(nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
    """"""

    # Use a dictionary/hash map to keep track of the indices and their sum values.

    # 1) Sub-Optimal (HashMap + Sort): TC = O((m+n)*log(m+n)); SC = O(m+n)
    # https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/solutions/3203773/using-map-very-simple-easy-to-understand-solution
    # https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/solutions/3205271/java-hashmap-explained

    """
    # Store nums1 in the HashMap for fast lookup:
    hm = {id_: val for id_, val in nums1}  # TC = O(m); SC = O(m)

    # Add nums2:
    for id_, val in nums2:  # TC = O(n); SC = O(n)
        hm[id_] = hm.get(id_, 0) + val

    # Sort and Return:
    return sorted(hm.items())  # TC = O((m+n)*log(m+n)); SC = O(m+n)
    """

    # But it's not benefiting from the fact that both the arrays are sorted.

    # 2) Optimal (Two Pointers): TC = O(m+n); SC = O(1)
    # https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/solutions/3203809/two-pointers

    # Merge Sorted Array:

    m, n = len(nums1), len(nums2)
    i = j = 0

    while i < m and j < n:

        num1, num2 = nums1[i], nums2[j]
        id1, id2 = num1[0], num2[0]

        if id1 == id2:
            yield [id1, num1[1]+num2[1]]
            i, j = i+1, j+1

        elif id1 < id2:
            yield num1
            i += 1

        else:  # (id1 > id2)
            yield num2
            j += 1

    # Leftovers:
    # yield from nums1[i:] or nums2[j:]  # linear space
    yield from (nums1[k] for k in range(i, m)) if i != m else (nums2[k] for k in range(j, n))  # constant space
