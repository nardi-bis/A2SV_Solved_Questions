class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        n = len(cost)
        if n < 3:
            return sum(cost)
        cost.sort(reverse = True)
        i = 2
        ans = 0
        while i < n:
            ans += cost[i]
            i += 3
        return sum(cost) - ans



        