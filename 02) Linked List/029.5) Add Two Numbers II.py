"""
https://leetcode.com/problems/add-two-numbers-ii
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """"""

    # 0.1) Brute-force (Copy Values to List (Stack to be precise)): TC = O(n); SC = O(n)
    # https://leetcode.com/problems/add-two-numbers-ii/discuss/92623/Easy-O(n)-Java-Solution-using-Stack

    # 0.2) Brute-force (Only limited to Python) (Convert the Long Number to Int): TC = O(n); SC = O(1)
    # Do you realised that why are we not converting the number represented in the LL format to int and directly doing
    # `+`? (and why the number is being represented in the LL format at the first place?)
    # Because the integer is very long here, `The number of nodes in each linked list is in the range [1, 100].`,
    # that means the maximum possible number is 10**100 - 1 {len(str(10**100 - 1)) == 100}.
    # So, it can't be represented with `int` datatypes, because it's general limit is 2**64, even if we use `long` or
    # `long_long`, then also we can't represent 10e100.
    # But wait, Python doesn't have limit on ints! So we can do this!
    # https://leetcode.com/problems/add-two-numbers-ii/discuss/92627/There-is-no-maximum-of-INT-in-python-so.....

    # 1) Better (`025 Reverse Linked List.py` + `029 Add Two Numbers.py`): TC = O(n); SC = O(1)
    # https://github.com/samyak1409/DSA/blob/main/02%29%20Linked%20List/025%29%20Reverse%20Linked%20List.py
    # + https://github.com/samyak1409/DSA/blob/main/02%29%20Linked%20List/029%29%20Add%20Two%20Numbers.py
    # Algo:
    # -> Reverse both input LLs.
    # -> Traverse & Add the node values, for every add, create a new node and assign the add to it.
    # -> While creating new nodes only, assign the next pointers in opposite direction.
    # -> In the end, Reverse both input LLs back.
    # -> Return the last node got from traversal (of step 2).

    # Follow up: Could you solve it without reversing the input lists?
    # 2) Optimal (Handle Carry/ies In Different/Dedicated Traversal): TC = O(n); SC = O(1)
    # Good Question 👌; I myself came up with this approach 😁
    # https://leetcode.com/problems/add-two-numbers-ii/discuss/687339/Java-O(N)-solution-with-follow-up-question-no-recursion-no-stacks
    # https://leetcode.com/problems/add-two-numbers-ii/discuss/92624/C%2B%2B-O(1)-extra-space-except-for-output.-Reverse-output-instead.-Is-this-cheating

    # Helper Function:
    def get_len(head: ListNode) -> int:
        length = 1  # len will be at least one as per the Q. constraint
        while head := head.next:
            length += 1
        return length

    # Calc. Lengths:
    m, n = get_len(head=l1), get_len(head=l2)

    # Make the resultant LL in reverse order (with unhandled carry/ies if any):
    node = None
    # Values from the longest LL till it's not = shorter LL:
    if m > n:
        for _ in range(m-n):
            node = ListNode(val=l1.val, next_=node)
            l1 = l1.next  # ++
    elif m < n:
        for _ in range(n-m):
            node = ListNode(val=l2.val, next_=node)
            l2 = l2.next  # ++
    # Values from both LL:
    for _ in range(min(m, n)):
        node = ListNode(val=l1.val+l2.val, next_=node)
        l1, l2 = l1.next, l2.next  # ++

    # Fix Carry/ies if any and re-reverse the LL:
    carry = 0
    prev = None
    while node:
        carry, node.val = divmod(node.val+carry, 10)  # x//y, x%y
        node.next, node, prev = prev, node.next, node  # reverse ptr direction, node++, prev++
    if carry:  # carry increase the len of num (carry from MSB) e.g. 99 + 01 = 100
        prev = ListNode(val=carry, next_=prev)

    return prev
