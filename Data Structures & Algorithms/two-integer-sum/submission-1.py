class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # # 2 Pointer Approach
        # nums.sort()
        # left=0
        # right=len(nums)-1

        # while left<right:
        #     curr_sum=nums[left]+nums[right]

        #     if curr_sum==target:
        #         return [left,right]
        #     elif curr_sum<target:
        #         left +=1
        #     else:
        #         right -=1
        # return []                



        # Uisng HashMap
        prevMap={}

        for i,n in enumerate(nums):
            diff=target-n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n]=i
        return     






