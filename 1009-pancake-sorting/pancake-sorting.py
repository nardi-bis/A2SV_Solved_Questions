class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        r=[]
        n=len(arr)
        for i in range(n,1,-1): #start #stop #step
            max=arr.index(i)
            if max!=i-1:
                if max!=0:
                    r.append(max+1)
                    arr[:max+1] = reversed(arr[:max+1])

                r.append(i)
                arr[:i] = reversed(arr[:i])
        return r



       