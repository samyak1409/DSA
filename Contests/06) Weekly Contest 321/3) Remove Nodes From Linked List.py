"""
https://leetcode.com/problems/remove-nodes-from-linked-list
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def remove_nodes(head: ListNode | None) -> ListNode | None:
    """"""

    # 1) Optimal (Copy Vals to an Array): TC = O(n); SC = O(n)
    # Iterate on nodes in reversed order.
    # When iterating in reversed order, save the maximum value that was passed before.

    # Save all the vals to an array:
    arr = []
    node = head  # for traversal
    while node:
        arr.append(node.val)
        node = node.next

    # Reverse traverse the array and mark the indices of the nodes which need to be removed:
    max_val = arr[-1]  # init
    for i in range(-2, -len(arr)-1, -1):
        if arr[i] < max_val:  # => node need to be removed
            arr[i] = 0  # marking the index
        else:  # (if arr[i] >= max_val)
            max_val = arr[i]  # update

    # Remove the nodes:
    to_head = node = ListNode(next_=head)  # to_head: dummy node ptr to head; node: for traversal
    for val in arr:
        if val == 0:  # marked val
            node.next = node.next.next  # change ptr to remove a node
        else:
            node = node.next  # ++
    return to_head.next

    # See more elegant methods: https://leetcode.com/problems/remove-nodes-from-linked-list/discuss
