class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}

        for num in nums:
            freq[num]=freq.get(num,0) +1
        #{
        # 1:2
        # 2:4
        # 3:3
        # }  

        #Buckets banan hai bhai
        buckets=[[] for _ in range(len(nums)+1)]
        #Ise buckets banata hai len=6 hai to
        # [
        # [],
        # [],
        # [],
        # [],
        # [],
        # [],
        # []
        # ] 

        for num,count in freq.items():
            #freq.items return karta hai 
            # (1,3)
            # (2,2)
            # (3,1)
            # first iteration num=1 count=3

            buckets[count].append(num)
            # buckets[3].append(1)
            # [
            #     [],   
            #     [],
            #     [],
            #     [1], so 1 is added not 3 here frequency and index is 3
            #     [],
            #     [],
            #     []
            # ]

        result=[]
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                result.append(num)  

                if len(result)==k:
                    return result  
