"""
https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def pair_sum(head: Optional[ListNode]) -> int:
    """"""

    # This problem is just a little variation of `034 Palindrome Linked List.py` and thus all the approaches from it
    # applies here too.
    # (https://github.com/samyak1409/DSA/blob/main/02%29%20Linked%20List/034%29%20Palindrome%20Linked%20List.py)
    # Just writing the Optimal one here.
    # IMP: `The NUMBER OF NODES IN THE LIST IS AN EVEN INTEGER in the range [2, 105].`

    # 1) Optimal (Reverse Half LL): TC = O(n); SC = O(1)

    # Step 1: Traverse 1st half and reverse the pointer direction: O(n/2)
    node = node2x = head
    prev = None
    while node2x:
        node2x = node2x.next.next  # +2
        # https://github.com/samyak1409/DSA/blob/main/02%29%20Linked%20List/025%29%20Reverse%20Linked%20List.py:
        node.next, node, prev = prev, node.next, node  # change pointer direction, ++, ++
    # After this, `5 -> 4 -> 2 -> 1 -> None` will convert into `None <- 5 <- 4 & 2 -> 1 -> None`,
    # and `prev` will be pointing to start of left LL and `node` to start of right LL.

    # Step 2: Compare the values while traversing the 1st and the 2nd half, and reverse the pointer direction back of
    #         the 1st half (in order to reset the input LL back to original): O(n/2)
    node_l, prev, node_r = prev, node, node  # init, ++, init; result: None <- 5 <- 4  &  2 -> 1 -> None
    #                                                                               ↑     ↑
    max_sum = 2  # `1 <= Node.val <= 10^5`                                     node_l     prev & node_r
    while node_r:  # or `while node_l:` (len is same so doesn't matter)
        max_sum = max(max_sum, node_l.val+node_r.val)
        # https://github.com/samyak1409/DSA/blob/main/02%29%20Linked%20List/025%29%20Reverse%20Linked%20List.py:
        node_l.next, node_l, prev = prev, node_l.next, node_l  # change pointer direction, ++, ++
        node_r = node_r.next  # ++

    return max_sum
