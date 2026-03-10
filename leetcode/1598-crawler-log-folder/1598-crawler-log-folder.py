class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for d in logs:
            if d == "../":
                ans = max(0, ans-1)
            elif d !="./":
                ans += 1
        return ans



        