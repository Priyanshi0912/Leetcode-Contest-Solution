class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        ans=[]
        ans.append(words[0])
        curr=groups[0]
        for index in range(1,n):
            if curr!=groups[index]:
                ans.append(words[index])
                curr=groups[index]
        return ans
