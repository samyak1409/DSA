"""
https://leetcode.com/problems/design-task-manager
"""


from heapq import heapify, heappush, heappop


class TaskManager:

    def __init__(self, tasks: list[list[int]]):  # TC = O(n); SC = O(n) {n: no. of tasks}
        # Hashmap to quickly lookup/edit/remove tasks: O(n); O(n)
        self.hm = {t: [p, u] for u, t, p in tasks}
        # Heap (Priority Queue) for fast retrieval of top priority task: O(n); O(n)
        self.heap = [(-p, -t) for u, t, p in tasks]  # negating the vals in order to get max heap behaviour from `heapq`
        # which is min heap by default
        # Heapify in the end which impressively takes just O(n) time: O(n); O(1)
        heapify(self.heap)

    def add(self, user_id: int, task_id: int, priority: int) -> None:  # TC = O(log(n)); SC = O(1)
        # Add in `hm` and `heap`:
        self.hm[task_id] = [priority, user_id]  # O(1); O(1)
        heappush(self.heap, (-priority, -task_id))  # O(log(n)); O(1)

    def edit(self, task_id: int, new_priority: int) -> None:  # TC = O(log(n)); SC = O(1)
        # Just edit in `hm`, and (as we can't edit the priority directly in the heap), we'd need to remove the curr, and
        # then add the new one, but we won't remove but just add for now (reason in `rmv` method):
        self.hm[task_id][0] = new_priority  # O(1); O(1)
        heappush(self.heap, (-new_priority, -task_id))  # O(log(n)); O(1)

    def rmv(self, task_id: int) -> None:  # TC = O(1); SC = O(1)
        # Remove from `hm`: O(1); O(1)
        self.hm.pop(task_id)
        # [IMP] Removing from `heap` would take O(?), so it'd not be optimal to do it here, faster way would be when
        # `execTop` is called, before returning the top task, we'd check if the top task is there in `hm` or not, if not
        # that means the task was removed, and so we'd not return and pop the next top value until we found a task
        # that's present in the `hm`.

    def execTop(self) -> int:  # TC = O(m*log(n)); SC = O(1) {m: no. of invalid tasks in heap}
        while True:
            try:
                # Get the top priority, task_id: O(log(n)); O(1)
                p, t = map(abs, heappop(self.heap))
            except IndexError:
                # If heap is empty: "If no tasks are available, return -1.":
                return -1
            # Only if the top task is there in the `hm`, implies that task was not removed in `rmv` method:
            if t in self.hm and p == self.hm[t][0]:
                # So return the associated user_id:
                return self.hm.pop(t)[1]
            # Else, continue with the loop.


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
