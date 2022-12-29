"""
https://leetcode.com/problems/clone-graph
"""


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: 'Node') -> 'Node':
    """"""
