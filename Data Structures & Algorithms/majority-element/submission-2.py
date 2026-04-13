class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        n=len(nums)
        for num in nums:
            freq[num]=freq.get(num,0)+1
            if freq[num]>n//2:
                return num
        # count=Counter(nums)
        # max_=max(count,key=count.get)
        # return max_


        # res,count=0,0
        # for i in nums:
        #     if count==0:
        #         res=i
        #     count +=(1 if i== res else -1)
        # return res        


        
# from collections import Counter

# nums = [5, 7, 5, 7, 7, 9, 5, 7]

# count = Counter(nums)

# max_key = max(count, key=count.get)

# print(max_key)# answer=7
# print(count[max_key])  #answer=4      