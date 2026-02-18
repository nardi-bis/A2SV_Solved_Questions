class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        #using bubble sort
        for i in range(len(names)):
            for k in range(len(heights)-i-1):
                if heights[k]<heights[k+1]:
                    heights[k],heights[k+1]=heights[k+1],heights[k]
                    names[k],names[k+1]=names[k+1],names[k]
        return names
        
        