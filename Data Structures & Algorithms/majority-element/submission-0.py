class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=Counter(nums)
        max_=max(count,key=count.get)
        return max_
        
        