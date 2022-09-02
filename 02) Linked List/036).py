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
    ptr_to_head = node = Node(data=None)  # `ptr_to_head`: ref to return; `node`: for traversal
    for data in data_list:  # TC = O(nc)
        node.child = Node(data=data)  # create new child node with required data
        # Why child? Because it's asked in the question:
        # "The flattened list will be printed using the bottom pointer instead of the next pointer."
        node = node.child  # ++

    return ptr_to_head.child
    """
    # Without creating new LL:
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
