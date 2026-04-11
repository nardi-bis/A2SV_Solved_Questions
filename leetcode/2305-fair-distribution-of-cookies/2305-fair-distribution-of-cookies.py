class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        ans = float('inf')
        boys = [0] * k

        def back(i):
            nonlocal ans
            if i == n:
                ans = min(ans, max(boys))
                return

            for j in range(k):
                if boys[j] + cookies[i] >= ans:
                    continue
                boys[j] += cookies[i]
                back(i+1)
                boys[j] -= cookies[i]

        back(0)
        return ans