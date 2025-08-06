"""
https://leetcode.com/problems/path-existence-queries-in-a-graph-i
"""


def path_existence_queries(n: int, nums: list[int], max_diff: int, queries: list[list[int]]) -> list[bool]:
    """"""

    # 1) Optimal (HashMap: Grouping based on max_diff): TC = O(n+q); SC = O(n)
    # Intuition:
    #   Nodes can be grouped together if the diff b/w consecutive nums is <= max_diff.
    #   If two nodes belong to the same group, a path exists between them.
    # Approach:
    #   - Init a hashmap to assign group leaders.
    #   - Iterate through nums:
    #       - If the diff b/w curr and prev num > max_diff, start a new group.
    #       - Else, assign the curr idx to the curr group.
    #   - For each query, check if both indices belong to the same group.

    curr_leader = 0
    hm = {0: curr_leader}  # (node: node leader)
    # (note that these are node indices from nums)
    # Grouping:
    for i in range(1, n):
        # Group break, new node component would start:
        if nums[i]-nums[i-1] > max_diff:
            curr_leader = i  # change the leader
        hm[i] = curr_leader

    # For the indices, if they both belong to the same group leader, that means they're in the same connected component:
    # ans = []
    # for i1, i2 in queries:
    #     ans.append(hm[i1]==hm[i2])
    # return ans
    # Or just:
    return [hm[i1]==hm[i2] for i1, i2 in queries]

    # ALSO, IMP NOTE:
    # This type of problems generally comes under https://leetcode.com/problem-list/union-find.
    # aka DSU https://en.wikipedia.org/wiki/Disjoint-set_data_structure
