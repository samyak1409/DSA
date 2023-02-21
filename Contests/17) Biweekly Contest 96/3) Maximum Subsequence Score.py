"""
https://leetcode.com/problems/maximum-subsequence-score
"""


def max_score(nums1: list[int], nums2: list[int], k: int) -> int:
    """"""

    # How can we use sorting here?
    # Try sorting (in descending order) the two arrays based on second array.
    # Loop through nums2 and compute the max product given the minimum is nums2[i]. Update the answer accordingly.

    # 1) Optimal (Sort (by 2nd Array in Decreasing Order) + MinHeap): TC = O(n*log(n)); SC = O(n)
    # This solution is tricky!!!! To understand this, read below explanations and then dry run on Example 1
    # (nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3), and you'll get it!
    # https://leetcode.com/problems/maximum-subsequence-score/solutions/3082106/java-c-python-priority-queue
    # https://leetcode.com/problems/maximum-subsequence-score/solutions/3082373/min-heap

    from heapq import heappush, heappop

    top_k, sum_ = [], 0  # `top_k`: hold top k nums1, `sum_`: track sum of those top k nums1
    ans = 0

    # Traverse nums1[i], nums2[j] acc. to nums2 sorted in reverse:
    for n1, n2 in sorted(zip(nums1, nums2), key=lambda tup: tup[1], reverse=True):

        # Add num1 to the heap, and increment sum:
        heappush(top_k, n1)
        sum_ += n1

        # If top_k get k+1 elements:
        if len(top_k) > k:
            # Remove min(top_k), and decrement sum:
            sum_ -= heappop(top_k)

        # Whenever top_k has exactly k elements:
        if len(top_k) == k:
            # Update ans. with sum_of_top_k_till_now_from_nums1 * curr_min_from_nums2:
            ans = max(ans, sum_*n2)

    return ans
