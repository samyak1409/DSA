"""
https://leetcode.com/problems/choose-k-elements-with-maximum-sum
"""


def find_max_sum(nums1: list[int], nums2: list[int], k: int) -> list[int]:
    """"""

    # 1) Optimal (Sort, Heap, HashMap): TC = O(n*log(nk)); SC = O(n)
    # GOOD Q! Because of below edge case.
    # Intuition: Finding (at most) `k` elements > current element in `nums1` without sorting would be O(n^2).
    # But sorting would change the order, we need to pair the `nums1[i]` with `i` and `nums2[i]`.
    # Edge case:
    # Input: nums1 = [18,11,24,9,10,11,7,29,16], nums2 = [28,26,27,4,2,19,23,1,2], k = 1
    # Stdout: [[7,6,23],[9,3,4],[10,4,2],[11,1,26],[11,5,19],[16,8,2],[18,0,28],[24,2,27],[29,7,1]]
    # Output: [23,23,28,23,23,23,0,28,23]
    # Expected: [26,23,28,23,23,23,0,28,26]

    from heapq import heappush, heappop

    # Pair `nums1[i], i, nums2[i]` together: TC = SC = O(n)
    arr = [[n1, i, n2] for i, (n1, n2) in enumerate(zip(nums1, nums2))]
    # Sort by `nums1[i]` (as that's the first requirement: "Find all indices j where nums1[j] is less than nums1[i].")
    # in order to process in optimal time: TC = O(n*log(n)); SC = O(n)
    arr.sort(key=lambda x: x[0])
    # print(arr)  # debug

    ans = [0] * len(nums1)  # would be filled using saved `i`s while traversing through the sorted `arr`
    heap = []  # heap to track the biggest `k` elements efficiently; SC = O(k)
    curr_sum = 0  # track sum as we go
    seen = {}
    # Now, the base of this solution, after sorting, we can traverse on `nums1[i]` in ascending order, and maintain a
    # heap having top `k` elements, since all the next `n1`s > curr `n1`, we can have `nums2[i]` in the heap:
    for n1, i, n2 in arr:  # TC = O(n)
        # 1 WA (check submission) due to directly doing following (check edge case in above comments):
        # ans[i] = curr_sum
        # When next `n1` == curr `n1`, we can't consider curr `n2` in heap, but we still need to add in heap for any
        # next `n1` > curr `n1`, hence we use a hashmap:
        if n1 in seen:
            ans[i] = seen[n1]
        else:
            ans[i] = seen[n1] = curr_sum
        # Push `nums2[i]` for future, and update the sum: TC = log(k)
        heappush(heap, n2)
        curr_sum += n2
        # And if heap becomes bigger than `k`, pop the smallest element in the heap, and update sum: TC = log(k)
        if len(heap) > k:
            curr_sum -= heappop(heap)

    return ans
