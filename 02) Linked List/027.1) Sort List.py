"""
https://leetcode.com/problems/sort-list
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def sort_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """"""

    # 0) [TLE] Brute-force (Insertion Sort): TC = O(n^2); SC = O(1)

    """
    start = head  # copy for traversal
    while start:  # outer loop (for start)
        node = start  # copy for traversal
        min_val, min_val_node = float('inf'), None
        while node:  # inner loop (for finding the minimum value)
            if node.val < min_val:
                min_val, min_val_node = node.val, node  # save
            node = node.next  # ++
        start.val, min_val_node.val = min_val, start.val  # swap value
        start = start.next  # ++
    return head
    """

    # 1) Brute-force = Time-Optimal (Copy Vals to Array and Sort): TC = O(n*log(n)); SC = O(n)

    # Insert Values in Array:
    node = head  # copy for traversal
    vals = []  # SC = O(n)
    while node:  # TC = O(n)
        vals.append(node.val)
        node = node.next  # ++
    # Sort the Array:
    vals.sort()  # TC = O(n*log(n)); SC = O(n)
    # Update Values to the LL:
    node = head  # copy for traversal
    for val in vals:  # TC = O(n)
        node.val = val
        node = node.next  # ++
    return head

    # 2.1) (Almost) Optimal (Top Down (Recursive) Merge Sort): TC = O(n*log(n)); SC = O(log(n))
    # https://github.com/samyak1409/python-lab-assignments/blob/main/10/a.py
    # https://leetcode.com/problems/sort-list/solution/#approach-1-top-down-merge-sort
    # https://leetcode.com/problems/sort-list/discuss

    # Follow up: Can you sort the linked list in O(n*log(n)) time and O(1) memory (i.e. constant space)?
    # 2.2) Optimal (Bottom Up (Iterative) Merge Sort): TC = O(n*log(n)); SC = O(1)
    # https://leetcode.com/problems/sort-list/solution/#approach-2-bottom-up-merge-sort
    # https://leetcode.com/problems/sort-list/discuss

    # Note:
    # "In an actual interview, I am not sure if you'd get extra points for coding the bottoms-up solution.
    # Both bottoms-up and top-down are O(n*log(n)) and the latter's use of O(log(n)) space should not be an issue in
    # practice. Even 1 trillion nodes is only 40 stack frames(1024 is pow(2,10) so 1 trillion is pow(2,40).
    # Paraphrasing `Cracking The Coding Interview`, every recursive problem can be made into an iterative one,
    # but it can be tricky."
    # -https://leetcode.com/problems/sort-list/solution/880670
