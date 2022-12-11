"""
https://leetcode.com/problems/delete-greatest-value-in-each-row
"""


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        
        ans = 0
        
        while grid and grid[0]:
            
            max2 = 0
            for row in grid:
                max1 = 0
                for val in row:
                    max1 = max(max1, val)
                row.remove(max1)
                max2 = max(max2, max1)
            
            ans += max2
        
        return ans
