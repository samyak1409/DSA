"""
https://leetcode.com/problems/closest-equal-element-queries
"""


def solve_queries(nums: list[int], queries: list[int]) -> list[int]:
    """"""

    # 1) Optimal (HashMap, Greedy): TC = O(n); SC = O(n)

    min_dist, first_idx, last_idx = {}, {}, {}
    # (Preprocess) Calc. minimum distance for all the indices in `nums`: TC = O(n); SC = O(n)
    for i, num in enumerate(nums):
        # If `num` is not seen before:
        if num not in first_idx:  # (or `if num not in last_idx`)
            # Init w/ `inf` so that any actual distance is smaller than this:
            min_dist[i] = float('inf')
            # Update:
            first_idx[num] = last_idx[num] = i
        # We've seen num before:
        else:
            # Curr index min dist = curr index - last index:
            min_dist[i] = i - (l := last_idx[num])
            # We also need to update the min_dist at last index considering the dist till curr index:
            # Last index min dist = min of (last index min dist, curr index min dist):
            min_dist[l] = min(min_dist[l], min_dist[i])
            # Update:
            last_idx[num] = i
            # Now, assuming the curr index is the last index of `num`, we also want to consider the circular dist:
            # Indices shouldn't be the same:
            if (l := last_idx[num]) != (f := first_idx[num]):
                min_dist[l] = min(min_dist[l], len(nums)-l+f)
                min_dist[f] = min(min_dist[f], len(nums)-l+f)
                # `len(nums)-l+f`: circular dist from l to f
    print(min_dist)  # debug

    # Return ans: TC = O(q); SC = O(1)
    return [min_dist[q] if min_dist[q] != float('inf') else -1 for q in queries]
