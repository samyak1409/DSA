"""
https://leetcode.com/problems/node-with-highest-edge-score
"""


def edge_score(edges: list[int]) -> int:
    """"""

    # 1) Brute-force = Optimal (Frequency Array): TC = O(n); SC = O(n)
    # https://leetcode.com/problems/node-with-highest-edge-score/discuss/2422312/Counting
    # https://leetcode.com/problems/node-with-highest-edge-score/discuss/2422139/C++-oror-Easy-Solution-O(N)-oror-Without-Graph-oror-Counting

    # Count score:
    frequency = [0] * len(edges)  # init
    for score, edge in enumerate(edges):
        frequency[edge] += score

    # Find highest:
    highest, node = float('-inf'), None
    for edge, score in enumerate(frequency):
        if score > highest:
            highest = score
            node = edge
    return node
    # return frequency.index(max(frequency))
