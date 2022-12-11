"""
https://leetcode.com/problems/maximum-number-of-points-from-grid-queries
"""


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:

        def r(q, i, j):
            
            if i >= m or j >= n or q <= grid[i][j] or (i, j) in visited:
                return  # stop recurse
            
            ans[0] += 1
            visited.add((i, j))
            r(q, i-1, j), r(q, i+1, j), r(q, i, j-1), r(q, i, j+1)  # recurse in; up, down, left, right
            
        
        m, n = len(grid), len(grid[0])
        start = [0, 0]
        
        for query in queries:
            
            ans, visited = [0], set()
            
            r(query, *start)
            
            yield ans[0]
