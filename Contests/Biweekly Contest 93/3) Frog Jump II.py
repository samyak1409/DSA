"""
https://leetcode.com/problems/frog-jump-ii
"""


class Solution:
    def maxJump(self, stones: List[int]) -> int:
        
        if len(stones) == 2:
            return stones[1] - stones[0]
        
        ans = 0

        for i in range(len(stones)-2):

            ans = max(ans, stones[i+2]-stones[i])

        return ans
