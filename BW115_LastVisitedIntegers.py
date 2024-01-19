class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        curr=0
        val,ans=[],[]
        for i in words:
            if i=="prev":
                curr+=1
                if curr>len(val):
                    ans.append(-1)
                else:
                    ans.append(val[curr-1])
                
            else:
                val.insert(0,int(i))
                curr=0
        return ans
                
