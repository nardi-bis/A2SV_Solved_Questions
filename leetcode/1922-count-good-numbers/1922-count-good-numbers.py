class Solution:
    def countGoodNumbers(self, n: int) -> int:
        ans = 1
        val = n//2
        mod = 10 ** 9 + 7
        if n % 2 == 0:
            ans *= pow(5,val,mod)
            ans *= pow(4, val, mod)
        else:
            ans *= pow(4, val, mod)
            vall = n - val
            ans *= pow(5,vall,mod)
        return ans % (10 ** 9 + 7)
