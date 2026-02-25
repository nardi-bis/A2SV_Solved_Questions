class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        
        for i in range(len(citations)):
            h = len(citations) - i
            if citations[i] >= h:
                return h
        
        return 0