"""
https://leetcode.com/problems/palindrome-linked-list
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def is_palindrome(head: ListNode | None) -> bool:
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
    # https://leetcode.com/problems/palindrome-linked-list/solutions/4908031/interview-approach-4-approach-list-stack-recursion-two-pointer-approach
    # https://leetcode.com/problems/palindrome-linked-list/solutions/181453/java-5-lines-method-2ms-o-n-recursive-easy-to-understand
    # NOTE: This algorithm is not optimal (in terms of space due to recursion stack) but:
    # i) Recursion gives us an elegant way to iterate through the nodes in reverse. For example, following algorithm
    # will print out the values of the nodes in reverse. Given a node, the algorithm checks if it is null. If it is
    # null, nothing happens. Otherwise, all nodes after it are processed, and then the value for the current node is
    # printed.
    '''
    def print_values_in_reverse(head: ListNode | None) -> None:
        if head:
            print_values_in_reverse(head.next)  # recurse in
            print(head.val)  # prints values while recursing out
    '''
    # Remarks: It's basically just using stack implicitly, we can do the same thing in 2 more ways:
    # -> either use stack explicitly
    # -> or reverse the LL, print the values, and reverse the LL back.
    # ii) The downside of `2) Optimal (Reverse Half LL)` approach is that in a concurrent environment (multiple threads
    # and processes accessing the same data), access to the Linked List by other threads or processes would have to be
    # locked while this function is running, because the Linked List is temporarily broken. This is a limitation of many
    # in-place algorithms though. Current approach doesn't have this downside.

    # So now coming back to the algo:
    # We'd just recurse all the way in to the last node, and then while recursing out, we'd get the nodes in reverse,
    # and we can easily have the forward LL traversal, so we can compare them.

    # 1.1) Having `node_l` (forward traversal node) as return value, `is_palin` bool as global var:
    """
    # Recursive Function:
    def recurse(node_r: ListNode | None) -> ListNode | None:
        if node_r:  # if not reached None
            node_l = recurse(node_r=node_r.next)  # recurse in, and store the result
            # Only if `node_l` is not None but a node (which means that LL is palin till now), compare the values,
            # if same, return next node in forward traversal (to compare with the next node in backward traversal):
            if node_l and node_l.val == node_r.val:
                return node_l.next
            # Else, update the bool, and return None (so that we do not compare the vals above next):
            else:
                is_palin[0] = False
                return None
        return head  # if reached None node, just return the head node (to compare with the tail node)

    is_palin = [True]  # list for mutability
    recurse(node_r=head)
    return is_palin[0]
    """

    # 1.2) Better: Having `node_l` (forward traversal node) as global var, `is_palin` bool as return value:
    """
    # Recursive Function:
    def recurse(node_r: ListNode | None) -> bool:
        if node_r:  # if not reached None
            is_palin_so_far = recurse(node_r=node_r.next)  # recurse in, and store the result
            # Only if LL is palin so far, compare the values:
            if is_palin_so_far and node_l[0].val == node_r.val:
                node_l[0] = node_l[0].next  # if vals are same, update forward traversal node
                return True
            else:
                return False
        return True  # if reached None node, return True (to start comparison)

    node_l = [head]  # list for mutability
    return recurse(node_r=head)
    """

    # 1.2.1) [Pythonic] Using generator function (iterator) instead of global var makes it a bit effortless:
    """
    # Generator Function:
    def iterate(node: ListNode | None):
        # Yield the nodes one by one:
        while node:
            yield node
            node = node.next

    # Recursive Function:
    def recurse(node_r: ListNode | None) -> bool:
        if node_r:  # if not reached None
            is_palin_so_far = recurse(node_r=node_r.next)  # recurse in, and store the result
            # Only if LL is palin so far, compare the values and return bool:
            return is_palin_so_far and iterator.__next__().val == node_r.val
            # (`iterator.__next__().val`: OTG gets the next node in forward traversal)
        return True  # if reached None node, return True (to start comparison)

    iterator = iterate(node=head)  # init our iterator
    return recurse(node_r=head)
    """

    # Follow up: Could you do it in O(n) time and O(1) space?

    # 2) Optimal (Reverse Half LL Iteratively): TC = O(n); SC = O(1)
    # https://leetcode.com/problems/palindrome-linked-list/solutions/64500/11-lines-12-with-restore-o-n-time-o-1-space

    # Step 1: Traverse 1st half (using slow & fast ptrs to know where the 1st half ends) and reverse the ptr direction:
    slow = fast = head
    prev = None
    while fast and fast.next:  # O(n//2)
        fast = fast.next.next  # +2
        # https://github.com/samyak1409/DSA/blob/main/SDE%20Sheet/02%29%20Linked%20List/025%29%20Reverse%20Linked%20List.py:
        slow.next, slow, prev = prev, slow.next, slow  # change ptr direction, ++, ++
    # After this, `1 -> 2 -> 2 -> 1 -> None` will convert into `None <- 1 <- 2 & 2 -> 1 -> None`,
    # and `prev` will be pointing to start of left LL and `slow` to start of right LL.

    # Step 2: Compare values while traversing 1st & 2nd half, and reverse back the ptr direction of 1st half
    # (in order to reset the input LL back to original):
    node_l, prev = prev, slow  # init, ++
    node_r = slow if not fast else slow.next  # init; skipping the mid node if len(LL) == odd, illustrated below:
    # None <- 1 <- 2  &  3 -> 2 -> 1 -> None          None <- 1 <- 2  &  3 -> 2 -> 1 -> None
    #              ↑     ↑                      =>                 ↑     ↑    ↑
    #         node_l     prev & node_r                        node_l   prev   node_r
    is_palin = True
    while node_r:  # or `while node_l:` (len is same); O(n//2)
        if is_palin and node_l.val != node_r.val:  # (check for palin only if palin till here)
            is_palin = False
        # https://github.com/samyak1409/DSA/blob/main/SDE%20Sheet/02%29%20Linked%20List/025%29%20Reverse%20Linked%20List.py:
        node_l.next, node_l, prev = prev, node_l.next, node_l  # change ptr direction, ++, ++
        node_r = node_r.next  # ++

    return is_palin


# Similar Questions:
# https://leetcode.com/problems/palindrome-number
# https://leetcode.com/problems/valid-palindrome
# https://leetcode.com/problems/reverse-linked-list
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list
