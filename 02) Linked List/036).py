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
