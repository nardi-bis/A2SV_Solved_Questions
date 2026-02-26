class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # last occurence of each character=last
        last={}

        for i in range(len(s)):    #{ a:2,b:3,c:5}
            last[s[i]]=i

        left=0
        right=0
        res=[]
        for i in range(len(s)):
            ch=s[i]
            if ch in last:
                right=max(right,last[ch])
                
            if i==right:
                res.append(i-left+1)
                left=i+1
        return res

        
        