"""
https://leetcode.com/problems/palindrome-linked-list
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def is_palindrome(head: Optional[ListNode]) -> bool:
    """"""

    # 0) Brute-force (Save Vals to Array): TC = O(n); SC = O(n)

    """
    # Save:
    vals = [head.val]
    while head := head.next:
        vals.append(head.val)
    # Check:
    for i in range(len(vals)//2):
        if vals[i] != vals[~i]:
            return False
    return True
    """

    # 1) Time-Optimal (Recursion): TC = O(n); SC = O(n) {recursion stack}
    # https://leetcode.com/problems/palindrome-linked-list/solution/#approach-2-recursive-advanced
    # https://leetcode.com/problems/palindrome-linked-list/discuss/181453/Java-or-5-lines-method-or-2ms-or-O(n)-or-recursive-or-easy-to-understand
    # NOTE: This algorithm is not optimal (in terms of space due to recursion stack) but:
    # i) Recursion gives us an elegant way to iterate through the nodes in reverse. For example, following algorithm
    # will print out the values of the nodes in reverse. Given a node, the algorithm checks if it is null. If it is
    # null, nothing happens. Otherwise, all nodes after it are processed, and then the value for the current node is
    # printed.
    """
    def print_values_in_reverse(head: Optional[ListNode]) -> None:
        if head:
            print_values_in_reverse(head.next)  # recurse in
            print(head.val)  # prints values while recurs-ing out
    """
    # Remarks: It's basically just using stack implicitly, if we were to do the same thing, we would have two options:
    # -> either use stack explicitly
    # -> or reverse the LL, print the values, and reverse the LL back.
    # ii) The downside of `2) Optimal (Reverse Half LL)` approach is that in a concurrent environment (multiple threads
    # and processes accessing the same data), access to the Linked List by other threads or processes would have to be
    # locked while this function is running, because the Linked List is temporarily broken. This is a limitation of many
    # in-place algorithms though. Current approach doesn't have this downside.

    def check(back: Optional[ListNode]) -> bool:
        if back:
            palindrome_till_here = check(back=back.next)  # ++; go all the way back (recurse in)
            # following will execute while recurs-ing out:
            if palindrome_till_here:  # only check further if palindrome till here
                front_val = front[0].val
                front[0] = front[0].next  # ++; update for next comparison
                return front_val == back.val
            return False  # already not palindrome so don't check further
        return True  # since LL with no nodes is palindrome

    front = [head]  # global var
    # using list so that it's mutable, and so new local var is not created while updating inside the function
    return check(back=head)
