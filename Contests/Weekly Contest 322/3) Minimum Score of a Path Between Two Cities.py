"""
https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities
"""


def min_score(n: int, roads: list[list[int]]) -> int:
    """"""

    # 1) Optimal (Traverse Connected Component of `1`): TC = O(n); SC = O(n)
    # `The score of a path between two cities is defined as the minimum distance of a road in this path.
    # Return the minimum possible score of a path between cities 1 and n.`
    # Basically, we just need to return the minimum edge weight b/w the path from 1 to n.
    # But, wait, see this https://assets.leetcode.com/uploads/2022/10/12/graph22.png, the output will be 2,
    # because we can move around before going to n in order to minimize score!
    # So, that means, we just need to traverse all the vertices from `1` and return the minimum edge weight encountered!
    # Also, `The cities graph is not necessarily connected.`
    # But, `The test cases are generated such that there is at least one path between 1 and n.`
    # So, un-connected graph won't even matter! Only Connected Component of `1` will.
    # (https://en.wikipedia.org/wiki/Connected_component_(graph_theory))
    # For traversal, https://en.wikipedia.org/wiki/Graph_traversal#Graph_traversal_algorithms.
    # https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/solutions/2875034/python-c-connected-component-of-1-explained

    from collections import defaultdict, deque

    graph = defaultdict(dict)
    for u, v, w in roads:
        graph[u][v] = graph[v][u] = w

    dq = deque([1])  # for O(1) removal from left
    visited = set()  # for O(1) lookup
    min_weight = float('inf')  # init
    while dq:
        for node, weight in graph[dq.popleft()].items():
            if node not in visited:
                dq.append(node), visited.add(node)
            else:
                min_weight = min(min_weight, weight)
    return min_weight
