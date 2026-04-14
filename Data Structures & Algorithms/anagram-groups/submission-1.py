class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res=defaultdict(list)
        for i in strs:
            key="".join(sorted(i))
            res[key].append(i)
        return list(res.values())    
        
        # res=defaultdict(list)

        # for s in strs:
        #     count=[0]*26

        #     for c in s:
        #         count[ord(c)-ord("a")]+=1

        #     res[tuple(count)].append(s)

        # return list(res.values())

