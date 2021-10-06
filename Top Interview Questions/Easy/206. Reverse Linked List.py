"""
https://leetcode.com/problems/reverse-linked-list/
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Iterative Method 1 (by changing values): TC = SC = O(n)

        """
        copy = head
        vals = []
        while copy:
            vals.append(copy.val)  # saving values
            copy = copy.next

        copy = head
        for v in vals[::-1]:  # reverse traversing
            copy.val = v  # altering them
            copy = copy.next

        return head
        """

        # Iterative Method 2 (by changing pointers): TC = O(n); SC = O(1)

        """
        prev = None  # at first

        while head:  # iterating till the end of the linked list

            copy = head  # copy
            head = head.next  # moving head to next
            copy.next = prev  # changing the pointer of the copied head node to point to prev node instead of next (basically reversing)
            prev = copy  # updating prev

        return prev  # returning prev, that would be the last node but as the direction of pointers are changed, good will take place 😉
        """

        # Recursive (same method as above!):

        return self._reverse(head)

    def _reverse(self, node, prev=None):
        if not node:  # base condition
            return prev

        copy = node
        node = node.next
        copy.next = prev
        return self._reverse(node, prev=copy)
