"""
https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1
"""


def job_sequencing(deadline: list[int], profit: list[int]) -> list[int]:
    """"""

    # -1) [WA] Optimal (Greedy, Sort): TC = O(n*log(n)); SC = O(n)

    # -1.1) Greedy: I'd take the most profit first.
    # Intuition: Since we want the max profit, this is the brute-force comes to the mind very first.
    # Sorting: (Profit Decreasing, Deadline Increasing)
    # WA: deadline = [1, 2], profit = [100, 200]
    # Output = [1, 200]
    # Expected = [2, 300]
    """
    jobs_done = max_profit = 0
    for p, d in sorted(zip(profit, deadline), key=lambda tup: (-tup[0], tup[1])):
        # If this deadline has not passed:
        if d > jobs_done:
            # Do the job:
            max_profit += p
            jobs_done += 1
    return [jobs_done, max_profit]
    """

    # -1.2) Greedy: I'd take the most profit first, but going by increasing order of deadline.
    # Intuition: We take the max profit job from each deadline.
    # Sorting: (Deadline Increasing, Profit Decreasing)
    # WA: deadline = [1, 2, 2], profit = [100, 200, 300]
    # Output = [2, 400]
    # Expected = [2, 500]
    """
    jobs_done = max_profit = 0
    for d, p in sorted(zip(deadline, profit), key=lambda tup: (tup[0], -tup[1])):
        # If this deadline has not passed:
        if d > jobs_done:
            # Do the job:
            max_profit += p
            jobs_done += 1
    return [jobs_done, max_profit]
    """

    # Remark: This is why these classic greedy problems are tricky, since they look very straight-forward at first.

    # 1) [TLE] Sub-Optimal (Greedy, Sort, Slotting): TC = O(n*log(n) + n^2); SC = O(n)
    # This is the fix of approach `-1.1)`.
    # Approach: Sort the jobs to get the biggest profits first, then, do the job as close as possible to its
    # deadline, in order to preserve space for other potential jobs.
    # Sorting: (Profit Decreasing, Deadline Decreasing)
    # Note that we do not compulsorily need deadline sorting in this approach, just profit sorting.
    # Striver: https://youtu.be/QbwltemZbRg
    # Abdul Bari: https://youtu.be/zPtI8q9gvX8

    """
    jobs_done = max_profit = 0
    slots = [0] * (max(deadline)+1)  # 0: slot empty, 1: slot booked; `+1`: to make 1-indexed

    # Iterate in decreasing order of profit:
    for p, d in sorted(zip(profit, deadline), key=lambda tup: (-tup[0], -tup[1])):
        # Going from deadline's slot to first slot:
        for day in range(d, 0, -1):
            # If slot empty:
            if slots[day] == 0:
                max_profit += p
                jobs_done += 1
                slots[day] = 1
                break

    return [jobs_done, max_profit]
    """

    # 2) Optimal (Greedy, Sort, Max Heap): TC = O(n*log(n)); SC = O(n)
    # Approach: Sort the jobs in the descending order of their deadline, then traverse them, and
    # e.g. current deadline is 5 and next deadline is 3, this means the only job which can be done at 5 (or 4) is
    # current job, because as we're sorted in descending deadline, all the next jobs have earlier deadline.
    # So, use max heap and do the `k` job(s) with top profits out of the only jobs which can be done at that time.
    # Sorting: (Deadline Decreasing, Profit Decreasing)
    # Note that we do not compulsorily need profit sorting in this approach, just deadline sorting.

    from heapq import heappush, heappop

    jobs_done = max_profit = 0
    profits = []  # heap

    # Get the sorted jobs:
    jobs = sorted(zip(deadline, profit), key=lambda tup: (-tup[0], -tup[1]))

    # Iterate:
    for i in range(n:=len(jobs)):
        # Push this profit to heap:
        heappush(profits, -jobs[i][1])  # `-`: to get max-heap behaviour from min-heap
        # Do `k` top profit jobs (where `k` = this deadline - next deadline = `jobs[i][0]-jobs[i+1][0]`) which are
        # optimal to do now only:
        for _ in range(jobs[i][0]-(jobs[i+1][0] if i+1 != n else 0)):  # (`else 0`: for last iteration of `i`)
            max_profit += -heappop(profits)  # take the top profit out of current available
            jobs_done += 1
            if not profits:
                break  # days may be left but all the traversed jobs are done, so stop

    return [jobs_done, max_profit]

    # 2.1)
    # This can also be done using sorting order: (Deadline Increasing, Profit Decreasing)
    # - https://www.geeksforgeeks.org/job-sequencing-problem/#expected-approach-using-priority-queue-on-logn-time-and-on-space
    # - https://www.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1 > Editorial > "Expected Approach"
    # But above looked more intuitive to me.
