class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        res, curr = [], []
        def back(i):
            if len(curr) == n:
                res.append("".join(curr[:]))
                return 

            for ch in ['a', 'b', 'c']:
                if not curr or curr[-1] != ch:
                    curr.append(ch)
                    back(i+1)
                    curr.pop()

        back(0)
        
        if k > len(res):
            return ""
        return sorted(res)[k-1]