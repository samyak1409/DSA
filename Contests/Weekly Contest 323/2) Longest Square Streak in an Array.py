"""
https://leetcode.com/problems/longest-square-streak-in-an-array
"""


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        
        ans = 0
        
        nums = sorted(set(nums))  # set to remove duplicates, otherwise those will interfere
        # print(nums)  #debugging
        
        hm = {}
        for num in nums:
            hm[num] = hm_ = hm.get(sqrt:=num**.5, 0) + 1
            ans = max(ans, hm_)
            try:
                del hm[sqrt]
            except:
                pass
        # print(hm)  #debugging
        
        return ans if ans > 1 else -1
