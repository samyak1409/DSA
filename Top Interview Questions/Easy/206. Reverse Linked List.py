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

        # 1) Iterative Method 1 (by changing the values): TC = O(n) = SC

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

        # 2) Iterative Method 2 (by changing the direction of the pointers): TC = O(n); SC = O(1)

        """
        prev = None  # at first (as the end of the linked list is 'None')

        while head:  # iterating till the end of the linked list (till head is not 'None')

            n = head.next  # saving ref to the next of cur node
            head.next = prev  # changing the pointer direction from next to prev node (reversing)
            
            prev = head  # updating the prev node
            head = n  # moving the head node to the next

        return prev  # returning prev, that would be the last node but as the direction of pointers are changed, prev basically now is head!
        """

        # 3) Recursive (same method as above):

        return self._reverse(cur=head)

    def _reverse(self, cur, prev=None):

        if not cur:  # base condition
            return prev

        n = cur.next  # saving ref to the next of cur node
        cur.next = prev  # changing the pointer direction from next to prev node (reversing)

        return self._reverse(cur=n, prev=cur)
