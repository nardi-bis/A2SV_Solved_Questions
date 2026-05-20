class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        n = len(text1)
        m = len(text2)

        def dp(i, j):
            if i >= n:
                return 0
            if j >= m:
                return 0
            #take
            if (i,j) not in memo:
                take = 0
                for nj in range(j, m):
                    if text1[i] == text2[nj]:
                        take = 1 + dp(i + 1, nj + 1)
                        break
                no_take = dp(i +1 ,j)
                memo[(i,j)] = max(take, no_take)
            return memo[(i, j)]
        return dp(0, 0)

        