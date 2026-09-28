class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        cnt = len(nums)
        ans = []
        
        for i in range(cnt * 2):
            if i < cnt:
                ans.append(nums[i])
            else:
                ans.append(nums[i - cnt])        
        return ans