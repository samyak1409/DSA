"""
https://www.codingninjas.com/codestudio/problems/1112655
"""


# List Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.child = None

    def __del__(self):
        if self.next:
            del self.next


def flatten_linked_list(head: Node) -> Node:
    """"""

    # 0) Brute-force (Copy Vals to Array and Sort): TC = O(nc*log(nc)); SC = O(nc)
    # {n: total next nodes; c: average child nodes; nc: total nodes in the structure}
    # Same as `1)` of https://github.com/samyak1409/DSA/blob/main/SDE%20Sheet/02%29%20Linked%20List/027.1%29%20Sort%20List.py.

    # 0.0) Creating new LL:
    """
    # Save Values in an Array:
    vals = []
    while head:
        node = head  # copy for traversing child nodes
        while node:
            vals.append(node.data)
            node = node.child  # ++
        head = head.next  # ++

    # Create new LL with sorted vals:
    to_head = node = Node(data=None)  # `to_head`: ref to return; `node`: for traversal
    for val in sorted(vals):
        node.child = Node(data=val)  # create new child node with required val
        # Why child? Because it's asked in the question:
        # "The flattened list will be printed using the bottom pointer instead of the next pointer."
        node = node.child  # ++
    return to_head.child
    """

    # 0.1) Without creating new LL:
    """
    # Flatten the LL (Just attaching every next node to the current node's last child) and Save Values in an Array:
    vals = []
    node = head  # copy for traversing next nodes
    while node:  # one by one consider next nodes
        node2 = node  # copy for traversing child nodes
        while True:  # go all the way down and stop on last child (leaf node)
            vals.append(node2.data)  # save value
            if node2.child:
                node2 = node2.child  # ++
            else:
                break  # stop
        node2.child = node.next  # attach next node to the bottom of the current node
        node = node.next  # ++

    # Update Values to the LL:
    node = head  # copy for traversing child nodes
    for val in sorted(vals):
        node.data = val
        node = node.child  # ++
    return head
    """

    # 1) Optimal (Merge 2 LLs (n-1) Times): TC = O(nc); SC = O(1)
    # https://youtu.be/ysytSSXpAI0 - no need to do it from end to start 🤦

    while head.next:  # TC = O(nc)
        node1, node2, next_node = head, head.next, head.next.next  # init, init, save ref

        # Merging 2 LLs: TC = O(c)
        # `1.2)` of
        # https://github.com/samyak1409/DSA/blob/main/SDE%20Sheet/02%29%20Linked%20List/027%29%20Merge%20Two%20Sorted%20Lists.py:
        to_head = node = Node(data=None)  # `to_head` -> dummy node whose `child` will be the head of our flattened LL
        # `node` -> for traversing
        while node1 and node2:  # while both LLs have nodes left
            if node1.data < node2.data:
                node.child = node1  # merging
                node1 = node1.child  # ++
            else:  # (node1.data >= node2.data)
                node.child = node2  # merging
                node2 = node2.child  # ++
            node = node.child  # ++
        node.child = node1 or node2  # remaining node(s) from either side

        head, head.next = to_head.child, next_node  # head now = head of merged LL; attaching next node to it
    return head


# DUE TO SOME STUPID REASON, 1 TEST CASE ON CODING NINJAS IS THROWING TLE BUT THIS IS OPTIMAL APPROACH MAN!!! 🤦
# ACCEPTED ON GFG:


"""
https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1
"""


class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.bottom = None


def flatten(root: Node) -> Node:
    """"""

    # 1) Optimal (Merge 2 LLs (n-1) Times): TC = O(nc); SC = O(1)
    # https://youtu.be/ysytSSXpAI0 - no need to do it from end to start 🤦

    while root.next:  # TC = O(nc)
        node1, node2, next_node = root, root.next, root.next.next  # init, init, save ref

        # Merging 2 LLs: TC = O(c)
        # `1.2)` of
        # https://github.com/samyak1409/DSA/blob/main/SDE%20Sheet/02%29%20Linked%20List/027%29%20Merge%20Two%20Sorted%20Lists.py:
        to_root = node = Node(d=None)  # `to_root` -> dummy node whose `bottom` will be the root of our flattened LL
        # `node` -> for traversing
        while node1 and node2:  # while both LLs have nodes left
            if node1.data < node2.data:
                node.bottom = node1  # merging
                node1 = node1.bottom  # ++
            else:  # (node1.data >= node2.data)
                node.bottom = node2  # merging
                node2 = node2.bottom  # ++
            node = node.bottom  # ++
        node.bottom = node1 or node2  # remaining node(s) from either side

        root, root.next = to_root.bottom, next_node  # root now = root of merged LL; attaching next node to it
    return root
