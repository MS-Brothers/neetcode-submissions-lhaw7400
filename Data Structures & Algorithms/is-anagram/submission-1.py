class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s)==sorted(t)
        # return Counter(s)==Counter(t)


        #Using Map

        # if len(s) != len(t):
        #     return False

        # countS,countT={},{}
        # for i in range(len(s)):
        #     countS[s[i]]=1+countS.get(s[i],0) # making dictionary
        #     countT[t[i]]=1+countT.get(t[i],0)

        # for  i in countS:
        #     if countS[i]!= countT.get(i,0):
        #         return False
        # return True  

        dictS={}
        for i in s:
            if i in dictS:
                dictS[i]+=1
            else:
                dictS[i]=1
        dictT={}
        for i in t:
            if i in dictT:
                dictT[i]+=1
            else:
                dictT[i]=1
        return dictS == dictT                


