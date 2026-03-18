class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        hasm = {}
        total = 0
        for a in answers:
            if a in hasm:
                hasm[a] -= 1
                if hasm[a] < 0:
                    hasm[a] = a
                    total += a+1
            else:
                hasm[a] = a
                total += a+1
        return total


        