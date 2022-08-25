"""
https://leetcode.com/problems/delete-node-in-a-linked-list
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val, next_=None):
        self.val = val
        self.next = next_


def delete_node(node: ListNode) -> None:
    """
    Do not return anything, modify node in-place instead.
    """

    # 1) Optimal (Copy Value): TC = O(1); SC = O(1)
    # https://youtu.be/icnp4FJdZ_c
    # We can't really delete the node, but we can kinda achieve the same effect by instead removing the next node after
    # copying its data into the node that we were asked to delete.

    node.val = node.next.val  # copying value from the next node
    node.next = node.next.next  # freeing the next node
    # Python Garbage Collector (GC) automatically collects the garbage (will deallocate that next node).

    # Let's analyze why this problem isn't a good interview question.
    # The whole point of asking any candidates a linked list problem is to test if the candidates think about edge
    # cases, including:
    # - De-referencing Null Pointer, usually targeting tail pointer
    # - When given Head is None
    # - When there are duplications in the list
    # This question specifically mentioned all the above edge cases and extracted them out for you.
    # Someone who can solve this problem might not even think of all the edge cases, which can backfire on them in real
    # interview settings.

    # What time it is guys? It is Meme Time!!
    # First read:
    # https://leetcode.com/problems/delete-node-in-a-linked-list/discuss/65461/This-question-is-wrong.You-cannot-delete-the-node
    # Then:
    # https://leetcode.com/problems/delete-node-in-a-linked-list/discuss/65461/This-question-is-wrong.You-cannot-delete-the-node/67291


# Similar Question: https://leetcode.com/problems/remove-linked-list-elements
