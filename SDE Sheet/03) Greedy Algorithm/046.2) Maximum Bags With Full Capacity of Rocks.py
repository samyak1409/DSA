"""
https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks
"""


def maximum_bags(capacity: list[int], rocks: list[int], additional_rocks: int) -> int:
    """"""

    # Which bag should you fill completely first?
    # Can you think of a greedy solution?

    # 1) Optimal (Greedy: Fill those bags first which are just about to be filled): TC = O(n*log(n)); SC = O(n)
    # (This is an Easy Q, not Medium.)
    # https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/solutions/2643763/maximum-bags-with-full-capacity-of-rocks

    max_full_bags = 0

    for capacity_left in sorted([c-r for c, r in zip(capacity, rocks)]):
        if additional_rocks < capacity_left:
            break
        additional_rocks -= capacity_left  # fill the capacity_left, update additional_rocks
        max_full_bags += 1  # update count

    return max_full_bags
