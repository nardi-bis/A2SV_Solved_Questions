class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        parent = list(range(max(nums) + 1))
        rank   = [0] * (max(nums) + 1)
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
        def prime_factors(n):
            factors = []
            d = 2
            while d * d <= n:      
                if n % d == 0:
                    factors.append(d)
                    while n % d == 0:
                        n //= d    
                d += 1
            if n > 1:               
                factors.append(n)
            return factors

        for num in nums:
            for factor in prime_factors(num):
                union(num, factor)  
        roots = []
        for num in nums:
            roots.append(find(num))
        root_counts = Counter(roots)
        return max(root_counts.values())                                  

   