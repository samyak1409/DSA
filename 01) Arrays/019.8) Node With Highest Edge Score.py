"""
https://leetcode.com/problems/node-with-highest-edge-score
"""


def edge_score(edges: list[int]) -> int:
    """"""

    # 1) Brute-force = Optimal (Frequency Array): TC = O(n); SC = O(n)
    # Create an array arr where arr[i] is the edge score for node `i`.
    # How does the edge score for node edges[i] change? It increases by `i`.
    # The edge score may not fit within a standard 32-bit integer.
    # Le Me with Python: "We don't do that here."
    # https://leetcode.com/problems/node-with-highest-edge-score/discuss/2422312/Counting
    # https://leetcode.com/problems/node-with-highest-edge-score/discuss/2422139/C++-oror-Easy-Solution-O(N)-oror-Without-Graph-oror-Counting

    # Count score:
    scores = [0] * len(edges)  # init
    for score, node in enumerate(edges):
        scores[node] += score

    # Find highest:
    max_score, ans = -1, None
    for node, score in enumerate(scores):
        if score > max_score:
            max_score = score
            ans = node
    return ans
    # return scores.index(max(scores))
