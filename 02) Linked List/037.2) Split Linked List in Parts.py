"""
https://leetcode.com/problems/split-linked-list-in-parts
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def split_list_to_parts(head: Optional[ListNode], k: int) -> list[Optional[ListNode]]:
    """"""

    # 1) Optimal (Get Len of LL; Calc. Len of Parts; Do Partitions): TC = O(n); SC = O(k)
    # Better than:
    # https://leetcode.com/problems/split-linked-list-in-parts/solution
    # https://leetcode.com/problems/split-linked-list-in-parts/discuss

    # Get length of LL:
    node = head
    n = 0
    while node:  # TC = O(n)
        n += 1
        node = node.next  # ++

    # Calc. length of parts to be:
    each, remained = divmod(n, k)  # n//k, n%k

    # Do partitions:
    parts = []  # SC = O(k)
    for _ in range(k):  # TC = O(k * n/k) = O(n)
        n_ = each + bool(remained)  # len of partition
        # print(n_)  #debugging

        parts.append(head)
        for _ in range(n_-1):  # go to the last node of this LL part; TC = O(n/k)
            head = head.next  # ++
        if n_:  # or `if head`
            head.next, head = None, head.next  # break (partition) LL, ++

        if remained:  # update "extra-nodes" count
            remained -= 1

    return parts
