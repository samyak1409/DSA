"""
https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1
"""


class Job:
    """
    Job class which stores profit and deadline.
    """
    def __init__(self, profit: int, deadline: int):
        self.profit = profit
        self.deadline = deadline


def job_scheduling(jobs: list[Job], n: int) -> list[int, int]:
    """"""

    # 1) Sub-Optimal (Greedy: Sort Profit in Decreasing, Do Job on Deadline): TC = O(n*log(n) + n^2); SC = O(n)
    # Thinking greedily: Sort the jobs to get the biggest profits first, then, do the job on its deadline!
    # By doing this what happens is we consider the biggest profits and do them on the deadline (if deadline is not
    # available, doing it as near as possible before deadline), so, we get max profit!
    # https://leetcode.com/discuss/interview-question/1065228/job-sequencing-problem
    # https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1 > Editorial > "Greedy approach for
    # job sequencing problem"
    # [Striver's Video Explanation](https://youtu.be/LjPx4wQaRIs)

    """
    jobs_done = max_profit = 0
    booked = [0] * max(job.deadline for job in jobs)  # 0: slot empty, 1: slot booked

    # Loop on jobs in decreasing sorted order of profit:
    for job in sorted(jobs, key=lambda job_: job_.profit, reverse=True):  # O(n*log(n)) {sorting} + O(n*n) {nested loop}
        # Going from deadline's slot to 1st slot (reverse): O(n)
        for slot in range(job.deadline-1, -1, -1):  # `-1` in `job.deadline-1`: because `time_slot` is 0-indexed
            if not booked[slot]:
                booked[slot] = 1
                jobs_done += 1
                max_profit += job.profit
                break

    return [jobs_done, max_profit]
    """

    # 2) Optimal (Greedy: Sort Deadline in Descending, Use Max Heap & Do the Job(s) w/ Max Profit out of the Only Jobs
    # which can be Done At That Time): TC = O(n*log(n)); SC = O(n)
    # What we're doing is: First, sorting the jobs in the descending order of their deadline, then traversing them, and
    # e.g. current deadline is 5 and next deadline is 3, this means the only job which can be done at 5 (or 4) is
    # current job, because as we're sorted in descending deadline, all the next jobs have earlier deadline!
    # And finally, using Max Heap to do the Job(s) w/ Max Profits out of the only Jobs which can be done at that time!
    # https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1 > Editorial > "Job sequencing
    # problem using Priority-Queue (Max-Heap)"

    from heapq import heappush, heappop

    jobs_done = max_profit = 0
    profits = []  # heap which will contain the profits

    # Get the sorted jobs in decreasing order of deadline: O(n*log(n))
    jobs = sorted(jobs, key=lambda job_: job_.deadline, reverse=True)

    # Loop the sorted jobs from start to end:
    for i in range(n):  # O(n*log(n))
        # Add the profit of current job to the heap:
        heappush(profits, -(job := jobs[i]).profit)  # O(log(n)); `-`: to get max-heap behaviour from min-heap
        # Add the top k (k = # of slots which can only be used by traversed jobs) profits to `max_profit`:
        for _ in range(job.deadline-(jobs[i+1].deadline if i+1 != n else 0)):  # `else 0`: for last iteration of `i`
            jobs_done += 1
            max_profit += -heappop(profits)  # O(log(n))
            if not profits:
                break  # slots may be left but all the traversed jobs are completed, so stop

    return [jobs_done, max_profit]

    # It can also be optimized using Disjoint Set Data Structure. Please refer to the below post for details.
    # https://www.cdn.geeksforgeeks.org/job-sequencing-using-disjoint-set-union
