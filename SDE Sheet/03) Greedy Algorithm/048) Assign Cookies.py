"""
https://leetcode.com/problems/assign-cookies
"""


def find_content_children(greeds: list[int], sizes: list[int]) -> int:
    """"""

    # 1) Optimal (Greedy: Sort): TC = O(m*log(m) + n*log(n)); SC = O(m+n)
    # Since we just want to take the number of children up, just give the minimum size of cookie to a children who can
    # take it.

    # Sort greed factors:
    greeds = sorted(greeds)
    i = 0
    child_cnt = len(greeds)
    # Iterate on sorted cookie sizes:
    for sz in sorted(sizes):
        # If this cookie can fulfill i-th child:
        if sz >= greeds[i]:
            # Move to the next child:
            i += 1
            # Break out if we've covered all children:
            if i == child_cnt:
                break
        # Move on to the next cookie.
    # We can use the index only to return the ans:
    return i

# Similar Questions:
# https://leetcode.com/problems/maximum-matching-of-players-with-trainers
