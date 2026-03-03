class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        pre = [0] * (n+1)
        for left,right,k in shifts:
            if k == 0:
                pre[left]-=1
                pre[right+1]+=1
            else:
                pre[left]+=1
                pre[right+1]-=1
        #Example 1= 0,1,1,-2
        res=list(s)
        new=0
        for i in range(n):
            new +=pre[i]
            # new will add example 1  one by one 
            shift=new%26
            res[i]=chr((ord(res[i])-ord('a')+shift)%26+ord('a'))
        return "".join(res)
        

            

        