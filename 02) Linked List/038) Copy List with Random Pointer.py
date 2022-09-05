"""
https://leetcode.com/problems/copy-list-with-random-pointer
"""


from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val: int, next_: 'Node' = None, random: 'Node' = None):
        self.val = val
        self.next = next_
        self.random = random


def copy_random_list(head: Optional[Node]) -> Optional[Node]:
    """"""

    # 0) Brute-force (Using HashMap): TC = O(n); SC = O(n)

    # 0.1) Mapping using Indices:
    """
    node = head  # copy for traversing
    to_head2 = node2 = Node(val=0)  # `to_head2`: for easy pointing to head; `node2`: copy for traversing
    list1 = []  # list1[i] = random node of i-th node in original LL
    mapping = {}  # node: index -> node in original LL & it's index
    index = 0  # of LL node
    list2 = []  # list2[i] = random node of i-th node in copied LL
    while node:
        node2.next = Node(val=node.val)  # construct node with val
        list1.append(node.random)
        mapping[node] = index
        list2.append(node2.next)
        node, node2, index = node.next, node2.next, index+1  # ++
    mapping[None] = index
    list2.append(None)

    node2 = to_head2.next  # copy for traversing
    index = 0  # of LL node
    while node2:
        node2.random = list2[mapping[list1[index]]]  # point random
        node2, index = node2.next, index+1  # ++

    return to_head2.next
    """
    # 0.2) Easier (and Beautiful): Mapping Nodes Directly:
    # https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43488/Java-O(n)-solution
    # https://leetcode.com/problems/copy-list-with-random-pointer/discuss/811151/Extremely-simple-solution-using-C++
    """
    node = head  # copy for traversing
    copied = {None: None}  # original_node: copied_node
    while node:
        copied[node] = Node(val=node.val)  # construct node with val and save
        node = node.next  # ++

    node = head  # copy for traversing
    while node:
        copied[node].next = copied[node.next]  # point next
        copied[node].random = copied[node.random]  # point random
        node = node.next  # ++

    return copied[head]
    """

    # 1) Optimal (): TC = O(n); SC = O(1)

    pass


# Similar Question: https://leetcode.com/problems/clone-graph
