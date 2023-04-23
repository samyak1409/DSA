"""
https://leetcode.com/problems/mice-and-cheese
"""


def mice_and_cheese(reward1: list[int], reward2: list[int], k: int) -> int:
    """"""

    # The intended solution uses greedy approach.

    # 1) Optimal (Greedy: Relative/Comparative Sorting): TC = O(n*log(n)); SC = O(n)
    # Using `zip` because those are just rewards for the same cheese for different mice.
    # So, they needed to be zipped if sorting.

    # [WA] Greedy: Direct Sorting:
    """
    # Sorting on the basis of chosen greedy criteria:
    r = sorted(zip(reward1, reward2), reverse=True)  # TC = O(n*log(n)); SC = O(n)
    
    # Sum and return the ans:
    # return sum(r1 for r1, _ in r[:k]) + sum(r2 for _, r2 in r[k:])
    return sum(r1 if i < k else r2 for i, (r1, r2) in enumerate(r))  # O(n)
    """

    # [AC] Greedy: Relative/Comparative Sorting: (Done this only in the contest ✅)
    # Why is this correct?
    # Because by doing the following, we're making sure that the `n-k` types of cheeses from reward2 that we have to
    # choose later, have the least diff with `k` types of cheeses from reward1, so that the loss is minimum!
    """
    # Sorting on the basis of chosen greedy criteria:
    r = sorted(zip(reward1, reward2), key=lambda tup: tup[1]-tup[0])  # TC = O(n*log(n)); SC = O(n)

    # Sum and return the ans:
    # return sum(r1 for r1, _ in r[:k]) + sum(r2 for _, r2 in r[k:])
    return sum(r1 if i < k else r2 for i, (r1, r2) in enumerate(r))  # O(n)
    """

    # One-liner:
    return sum(r1 if i < k else r2 for i, (r1, r2) in enumerate(sorted(zip(reward1, reward2), key=lambda r: r[1]-r[0])))

    # 2) Other way of thinking:
    # Imagine at first that the second mouse eats all the cheese, then we should choose k types of cheese with the
    # maximum sum of - reward2[i] + reward1[i].
    # https://leetcode.com/problems/mice-and-cheese/solutions/3368322/java-c-python-k-largest-a-i-b-i
