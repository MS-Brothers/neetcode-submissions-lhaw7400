class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans=[]
        count=0

        for i in nums:
            if i in ans:
                return True
            else:
                ans.append(i)

        return False            
        