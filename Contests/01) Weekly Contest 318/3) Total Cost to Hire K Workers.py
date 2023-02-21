"""
https://leetcode.com/problems/total-cost-to-hire-k-workers
"""


def total_cost(costs: list[int], k: int, candidates: int) -> int:
    """"""

    # 0) [TLE] Brute-force (Did what's asked: Find min k times): TC = O(k*n); SC = O(n)

    """
    n = len(costs)
    indices_considered = set()  # for O(1) lookup; SC = O(n)
    total = 0

    for _ in range(k):  # "You will run k sessions and hire exactly one worker in each session."; TC = O(k*n)

        # "In each hiring session, choose the worker with the lowest cost from either the first candidates workers or
        # the last candidates workers.":
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

        if min_cost1 <= min_cost2:  # `=` because "Break the tie by the smallest index."
            index = index1
        else:  # (if min_cost2 < min_cost1)
            index = index2

        total += costs[index]
        indices_considered.add(index)

    return total
    """

    # 1) Optimal (Heap (Priority Queue)): TC = O(k*log(n)); SC = O(n)
    # Maintain two min-heaps: one for the left and one for the right.
    # Compare the top element from two heaps and remove the appropriate one.
    # Add a new element to the heap and maintain its size as k.
    # https://leetcode.com/problems/total-cost-to-hire-k-workers/solutions/2783147/python3-priority-queues/comments/1729099

    from heapq import heapify, heappop, heappush

    lt, rt = costs[:candidates], costs[max(len(costs)-candidates, candidates):]  # init heaps, SC = O(n)
    # For right heap `rt`, `max(len(costs)-candidates, candidates)` because it may be possible that
    # len(costs) < 2*candidates, in this case, we only add remaining elements to the right heap `rt`
    # as if we added some elements in both the heaps then those elements could be considered in the ans more than once.
    heapify(lt), heapify(rt)  # in order to get the min element in O(log(n)); TC = O(n)
    cost = 0
    i, j = candidates, len(costs)-candidates-1  # pointers to indicate which element to add next in the heaps
    for _ in range(k):  # "You will run k sessions and hire exactly one worker in each session."; TC = O(k*log(n))
        # "In each hiring session, choose the worker with the lowest cost from either the first candidates workers or
        # the last candidates workers.":
        if (not rt) or (lt and lt[0] <= rt[0]):  # `=` because "Break the tie by the smallest index.", and other
            # conditions in order to not get IndexError if either of lt or rt is empty.
            cost += heappop(lt)  # consider least cost; TC = O(log(n))
            if i <= j:  # making sure we do not consider any element if it's considered in the other heap
                heappush(lt, costs[i])  # as removed one element, adding next in order to keep the
                # heap size = candidates; TC = O(log(n))
                i += 1
        else:
            cost += heappop(rt)  # consider least cost; TC = O(log(n))
            if j >= i:  # making sure we do not consider any element if it's considered in the other heap
                heappush(rt, costs[j])  # as removed one element, adding next in order to keep the
                # heap size = candidates; TC = O(log(n))
                j -= 1
    return cost
