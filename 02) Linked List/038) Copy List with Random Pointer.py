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
    to_new_head = new_node = Node(val=0)  # `to_new_head`: for easy pointing to head; `new_node`: copy for traversing
    old_randoms = []  # old_randoms[i] = random node of i-th node in original LL
    mapping = {}  # node: index -> node in original LL & it's index
    index = 0  # of LL node
    new_randoms = []  # new_randoms[i] = random node of i-th node in copied LL
    while node:
        new_node.next = Node(val=node.val)  # construct new node with val
        old_randoms.append(node.random)
        mapping[node] = index
        new_randoms.append(new_node.next)
        node, new_node, index = node.next, new_node.next, index+1  # ++
    mapping[None] = index
    new_randoms.append(None)

    new_node = to_new_head.next  # copy for traversing
    index = 0  # of LL node
    while new_node:
        new_node.random = new_randoms[mapping[old_randoms[index]]]  # point random
        new_node, index = new_node.next, index+1  # ++

    return to_new_head.next
    """
    # 0.2) Easier (and Beautiful): Mapping Nodes Directly:
    # Just iterate the linked list and create copies of the nodes on the go. Since a node can be referenced from
    # multiple nodes due to the random pointers, ensure you are not making multiple copies of the same node.
    # You may want to use extra space to keep old_node ---> new_node mapping to prevent creating multiple copies of the
    # same node.
    # https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43488/Java-O(n)-solution
    # https://leetcode.com/problems/copy-list-with-random-pointer/discuss/811151/Extremely-simple-solution-using-C++
    """
    node = head  # copy for traversing
    new = {None: None}  # original_node: copied_node
    while node:
        new[node] = Node(val=node.val)  # construct new node with val and save
        node = node.next  # ++

    node = head  # copy for traversing
    while node:
        new[node].next = new[node.next]  # point next
        new[node].random = new[node.random]  # point random
        node = node.next  # ++

    return new[head]
    """

    # 1) Optimal (Just Attach New Nodes in Right of Old Nodes): TC = O(n); SC = O(1)
    # We can avoid using extra space for old_node ---> new_node mapping by tweaking the original linked list. Simply 
    # interweave the nodes of the old and copied list. For example: Old List: A -> B -> C -> D InterWeaved List: 
    # A -> A' -> B -> B' -> C -> C' -> D -> D'
    # The interweaving is done using next pointers, and we can make use of inter-weaved structure to get the correct
    # reference nodes for random pointers.
    # https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43491/A-solution-with-constant-space-complexity-O(1)-and-linear-time-complexity-O(N)
    # https://leetcode.com/problems/copy-list-with-random-pointer/discuss/1059181/C++-or-Three-Pass-or-O(n)-0ms-Beats-100-or-Explanation-(with-example)

    # Step 1) Create and Attach:
    node = head  # copy for traversing
    while node:
        new_node = Node(val=node.val)  # construct new node with val
        node.next, new_node.next = new_node, node.next  # and attach to next of old node
        node = new_node.next  # +2

    # Step 2) Link Random Pointers (for which we're doing all this):
    node = head  # copy for traversing
    while node:
        node.next.random = node.random.next if node.random else None  # point random; BEAUTIFUL!;
        # `node.random.next if node.random else None` -> handling when node.random points to None
        node = node.next.next  # +2

    # Step 3) Detach and Link Next Pointers:
    '''
    new_head = head.next  # save ref to return before detachment
    node = head  # copy for traversing
    while node:
        node.next, node.next.next = node.next.next, node.next.next.next if node.next.next else None  # detach and point
        # next; `node.next.next.next if node.next.next else None` -> handling last node
        node = node.next  # +2

    return new_head
    '''
    # Why above one is not working? [Create PR]
    # "AttributeError: 'NoneType' object has no attribute 'next'
    #     node.next, node.next.next = node.next.next, node.next.next.next if node.next.next else None"
    to_new_head = new_node = Node(val=0)  # `to_new_head`: for easy pointing to head; `new_node`: copy for traversing
    node = head  # copy for traversing
    while node:
        node.next, new_node.next = node.next.next, node.next  # detach and point
        node, new_node = node.next, new_node.next  # +2

    return to_new_head.next


# Similar Question: https://leetcode.com/problems/clone-graph
