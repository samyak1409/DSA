"""
https://leetcode.com/problems/maximum-value-of-a-string-in-an-array
"""


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        
        ans = 0
        for s in strs:
            try:
                ans = max(ans, int(s))
            except:
                ans = max(ans, len(s))
        return ans
