"""
https://leetcode.com/problems/maximum-star-sum-of-a-graph
"""


def max_star_sum(vals: list[int], edges: list[list[int]], k: int) -> int:
    """"""

    # 1) Almost-Optimal (Traverse edges and save all values in hashmap, then sort and choose biggest k vals):
    # TC = O(e + n*(e*log(e)+k)); SC = O(n * e) {e: edges.length}
    # A star graph doesn't necessarily include all of its neighbors.
    # For each node, sort its neighbors in descending order and take k max valued neighbors.
    # https://leetcode.com/problems/maximum-star-sum-of-a-graph/solutions/2897917/python-it-s-bidirectional-explained

    """
    neighbors = {node: [] for node in range(len(vals))}  # node num: list of vals of it's +ve neighbors
    for a, b in edges:  # O(e)
        if (val_b := vals[b]) > 0:  # imp: only taking vals that will increase the star sum ("AT MOST `k` edges")
            neighbors[a].append(val_b)
        # Similarly the other way around (as the graph is undirected i.e. bi-directional):
        if (val_a := vals[a]) > 0:  # imp: only taking vals that will increase the star sum ("AT MOST `k` edges")
            neighbors[b].append(val_a)

    ans = float('-inf')
    for node, neighbors in neighbors.items():  # O(n * (e*log(e)+k))
        ans = max(ans, vals[node]+sum(sorted(neighbors, reverse=True)[:k]))  # O(e*log(e) + k)
    return ans
    """

    # 1.1) Optimal (Traverse edges and save values greedily in hashmap using heap):
    # TC = O(e*log(k) + n) {e: edges.length}; SC = O(n * min(e, k))

    # Heap (PQ) to track the max vals in O(log(n)) (push & pop):
    from heapq import heappop, heappush

    neighbors = {node: [[], 0] for node in range(len(vals))}  # node num: [list of vals of it's +ve neighbors, star sum]
    for a, b in edges:  # O(e * log(k))
        if (val_b := vals[b]) > 0:  # imp: only taking vals that will increase the star sum ("AT MOST `k` edges")
            heappush(neighbors_a := neighbors[a][0], val_b)  # O(log(k))
            neighbors[a][1] += val_b
            if len(neighbors_a) > k:  # (== k+1)
                neighbors[a][1] -= heappop(neighbors_a)  # O(log(k))
        # Similarly the other way around (as the graph is undirected i.e. bi-directional):
        if (val_a := vals[a]) > 0:  # imp: only taking vals that will increase the star sum ("AT MOST `k` edges")
            heappush(neighbors_b := neighbors[b][0], val_a)  # O(log(k))
            neighbors[b][1] += val_a
            if len(neighbors_b) > k:  # (== k+1)
                neighbors[b][1] -= heappop(neighbors_b)  # O(log(k))

    ans = float('-inf')
    for node, (_, star_sum) in neighbors.items():  # O(n)
        ans = max(ans, vals[node]+star_sum)
    return ans
