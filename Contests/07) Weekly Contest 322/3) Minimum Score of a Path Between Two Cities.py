"""
https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities
"""


def min_score(n: int, roads: list[list[int]]) -> int:
    """"""

    # 1) Optimal (Traverse (Search) (Connected Component of) `1`): TC = O(n); SC = O(n)
    # Basically, we just need to return the minimum edge weight b/w the path from 1 to n.
    # But, see this https://assets.leetcode.com/uploads/2022/10/12/graph22.png, the output will be 2,
    # i.e. we can move around before going to n in order to minimize score!
    # So, that means, we just need to traverse all the vertices from `1` and return the minimum edge weight encountered!
    # Also, "The cities graph is not necessarily connected."
    # But, "The test cases are generated such that there is at least one path between 1 and n."
    # So, un-connected graph won't even matter! Only Connected Component of `1` will.
    # https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/solutions/2875034/python-c-connected-component-of-1-explained

    # "It is straightforward to compute the components of a finite graph in linear time (in terms of the numbers of the
    # vertices and edges of the graph) using either breadth-first search or depth-first search. In either case, a search
    # that begins at some particular vertex `v` will find the entire component containing `v` (and no more) before
    # returning. All components of a graph can be found by looping through its vertices, starting a new breadth-first or
    # depth-first search whenever the loop reaches a vertex that has not already been included in a previously found
    # component." -https://en.wikipedia.org/wiki/Connected_component_(graph_theory)#Algorithms

    # "Note. — If each vertex in a graph is to be traversed by a tree-based algorithm (such as DFS or BFS), then the
    # algorithm must be called at least once for each connected component of the graph. This is easily accomplished by
    # iterating through all the vertices of the graph, performing the algorithm on each vertex that is still unvisited
    # when examined." -https://en.wikipedia.org/wiki/Graph_traversal#Graph_traversal_algorithms

    pass
