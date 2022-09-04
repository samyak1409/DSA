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

    # 0) [TLE] Brute-force (Copy Vals to Array and Sort): TC = O(nc*log(nc)); SC = O(nc)
    # {n: total next nodes; c: average child nodes; nc: total nodes in the structure}
    # https://github.com/samyak1409/DSA/blob/c2ed7891e7156a319cb7c13f801769034e981b9d/02%29%20Linked%20List/027.1%29%20Sort%20List.py#L35

    # Creates a new LL:
    """
    from bisect import insort

    # Insert Values in Array keeping it Sorted:
    data_list = []  # SC = O(nc)
    while head:  # TC = O(nc*log(nc))
        node = head  # copy for traversing child nodes
        while node:  # TC = O(c*log(nc))
            insort(a=data_list, x=node.data)  # TC = O(log(nc))
            node = node.child  # ++
        head = head.next  # ++

    # Create new LL with required data:
    to_head = node = Node(data=None)  # `to_head`: ref to return; `node`: for traversal
    for data in data_list:  # TC = O(nc)
        node.child = Node(data=data)  # create new child node with required data
        # Why child? Because it's asked in the question:
        # "The flattened list will be printed using the bottom pointer instead of the next pointer."
        node = node.child  # ++

    return to_head.child
    """
    # Without creating new LL:
    """
    from bisect import insort

    # Flatten the LL (Unsorted): (Just attaching every next node to the current node's last child)
    node = head  # copy for traversing next nodes
    while node:  # one by one consider next nodes; TC = O(nc)
        node2 = node  # copy for traversing child nodes
        node = node.next  # ++
        node2.__del__()  # will delete it's `next` pointer
        while node2.child:  # go all the way down; TC = O(c)
            node2 = node2.child  # ++
        node2.child = node  # attach in the bottom

    # Insert Values in Array keeping it Sorted:
    node = head  # copy for traversing child nodes
    data_list = []  # SC = O(nc)
    while node:  # TC = O(nc*log(nc))
        insort(a=data_list, x=node.data)  # TC = O(log(nc))
        node = node.child  # ++

    # Update Values to the LL:
    node = head  # copy for traversing child nodes
    for data in data_list:  # TC = O(nc)
        node.data = data
        node = node.child  # ++

    return head
    """

    # 1) Optimal (Merge 2 LLs (n-1) Times): TC = O(nc); SC = O(1)
    # https://youtu.be/ysytSSXpAI0 - no need to do it from end to start 🤦

    while head.next:  # TC = O(nc)
        node1, node2, next_node = head, head.next, head.next.next  # init, init, save ref
        node1.__del__(), node2.__del__()  # will delete their `next` pointers

        # Merging 2 LLs: TC = O(c)
        # https://github.com/samyak1409/DSA/blob/c2ed7891e7156a319cb7c13f801769034e981b9d/02%29%20Linked%20List/027%29%20Merge%20Two%20Sorted%20Lists.py#L75:
        to_head = node = Node(data=None)  # `to_head` -> dummy node whose next will be the head of our flattened LL
        # `node` -> not using head for traversing because we've to return it
        while node1 and node2:  # while both LLs have nodes left
            if node1.data < node2.data:
                node.child = node1  # changing ptr
                node1 = node1.child  # ++
            else:  # (node1.data >= node2.data)
                node.child = node2  # changing ptr
                node2 = node2.child  # ++
            node = node.child  # ++
        node.child = node1 or node2  # remaining node(s)

        head, head.next = to_head.child, next_node  # head now = head of merged LL; attaching it to next node
    return head


# DUE TO SOME STUPID REASON, 1 TEST CASE IS FAILING ON CODING NINJAS AND OJ IS SAYING TLE BUT THIS IS OPTIMAL APPROACH
# MAN!!! 🤦
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
        # node1.__del__(), node2.__del__()  # will delete their `next` pointers

        # Merging 2 LLs: TC = O(c)
        # https://github.com/samyak1409/DSA/blob/c2ed7891e7156a319cb7c13f801769034e981b9d/02%29%20Linked%20List/027%29%20Merge%20Two%20Sorted%20Lists.py#L75:
        to_root = node = Node(d=None)  # `to_root` -> dummy node whose next will be the root of our flattened LL
        # `node` -> not using root for traversing because we've to return it
        while node1 and node2:  # while both LLs have nodes left
            if node1.data < node2.data:
                node.bottom = node1  # changing ptr
                node1 = node1.bottom  # ++
            else:  # (node1.data >= node2.data)
                node.bottom = node2  # changing ptr
                node2 = node2.bottom  # ++
            node = node.bottom  # ++
        node.bottom = node1 or node2  # remaining node(s)

        root, root.next = to_root.bottom, next_node  # root now = root of merged LL; attaching it to next node
    return root