"""
https://leetcode.com/problems/implement-router
"""


from collections import deque, defaultdict
from bisect import bisect_left, bisect_right


class Router:

    # 1) Optimal (Queue, HashSet, HashMap): TC = O(n*log2(n)); SC = O(n)

    def __init__(self, ml: int):  # TC = O(1); SC = O(1)
        # Store packets in FIFO:
        self.q = deque(maxlen=ml)
        # Hashset to check in a packet is already there in O(1):
        self.hs = set()
        # `destination: queue of packets` mapping for `getCount` method:
        self.hm = defaultdict(deque)
        # ("Note that queries for `addPacket` will be made in increasing order of `timestamp`.")

    def addPacket(self, s: int, d: int, t: int) -> bool:  # TC = O(1); SC = O(1)
        # Return False if the packet `(s, d, t)` is duplicate:
        if (tup:=(s, d, t)) in self.hs:
            return False
        # If the memory is full, remove the oldest packet:
        if len(self.hs) == self.q.maxlen:
            """
            # No need to remove from queue, because when we'd add, since the queue size if limited, oldest would
            # automatically be popped.
            # Remove from hs and hm:
            self.hs.remove(self.q[0]), self.hm[self.q[0][1]].popleft()
            """
            # Or we can just use `forwardPacket`:
            self.forwardPacket()
        # Now, add the packet:
        self.q.append(tup), self.hs.add(tup), self.hm[d].append(t)
        return True

    def forwardPacket(self) -> list[int]:  # TC = O(1); SC = O(1)
        try:
            # Remove the packet from storage:
            tup = self.q.popleft()
        except IndexError:
            # If there are no packets to forward, return an empty array:
            return []
        else:
            # Remove from hs and hm:
            self.hs.remove(tup), self.hm[tup[1]].popleft()
            return tup

    def getCount(self, d: int, st: int, et: int) -> int:  # TC = O(log2(n)); SC = O(1)
        # Binary search to count the number of packets in the given range:
        return bisect_right(a=self.hm[d], x=et) - bisect_left(a=self.hm[d], x=st)


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source, destination, timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination, startTime, endTime)
