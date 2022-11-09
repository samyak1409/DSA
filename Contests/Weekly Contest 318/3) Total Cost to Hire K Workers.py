"""
https://leetcode.com/problems/total-cost-to-hire-k-workers
"""


def total_cost(costs: list[int], k: int, candidates: int) -> int:
    """"""

    # 0) [TLE] Brute-force (Did what's asked: Find min k times): TC = O(k*n); SC = O(n)

    n = len(costs)
    indices_considered = set()  # for O(1) lookup; SC = O(n)
    total = 0

    for _ in range(k):  # `You will run k sessions and hire exactly one worker in each session.`; TC = O(k*n)

        # `In each hiring session, choose the worker with the lowest cost from either the first candidates workers or
        # the last candidates workers.`:
        min_cost1, index1, count = float('inf'), None, 0
        for i in range(n):  # TC = O(n)
            if i not in indices_considered:
                if (cost := costs[i]) < min_cost1:
                    min_cost1, index1 = cost, i  # update min_cost and save its index
                if (count := count+1) == candidates:
                    break  # stop
        min_cost2, index2, count = float('inf'), None, 0
        for i in range(n-1, -1, -1):  # TC = O(n)
            if i not in indices_considered:
                if (cost := costs[i]) < min_cost2:
                    min_cost2, index2 = cost, i  # update min_cost and save its index
                if (count := count+1) == candidates:
                    break  # stop

        if min_cost1 < min_cost2:
            index = index1
        elif min_cost2 < min_cost1:
            index = index2
        else:  # =
            index = min(index1, index2)  # `Break the tie by the smallest index.`

        total += costs[index]
        indices_considered.add(index)

    return total

    # 1) Optimal (Heap (Priority Queue)): TC = O(?); SC = O(?)
    # https://leetcode.com/problems/total-cost-to-hire-k-workers/discuss
