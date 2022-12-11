"""
https://leetcode.com/problems/maximum-star-sum-of-a-graph
"""


class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:

        from heapq import heappop, heappush
        
        star_sum = {node: [] for node in range(len(vals))}  # node: its star sum
        for i, j in edges:
            if len(star_sum[i]) <= k and vals[j] > 0:
                heappush(star_sum[i], vals[j])  # O(log(n))
                if len(star_sum[i]) == k+1:
                    heappop(star_sum[i])  # O(log(n))
            if len(star_sum[j]) <= k and vals[i] > 0:
                heappush(star_sum[j], vals[i])  # O(log(n))
                if len(star_sum[j]) == k+1:
                    heappop(star_sum[j])  # O(log(n))
        
        ans = float('-inf')
        for node, star_sum in star_sum.items():
            ans = max(ans, sum(star_sum)+vals[node])
        return ans
