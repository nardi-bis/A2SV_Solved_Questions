class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        curr = []

        def back(i):
            if i == n:
                return len(curr) >= 3

            for j in range(i+1, n+1):
                a = num[i:j]

                if a[0] == '0' and len(a) > 1:
                    break

                val = int(a)

                if len(curr) >= 2:
                    if val < curr[-1] + curr[-2]:
                        continue
                    if val > curr[-1] + curr[-2]:
                        break

                curr.append(val)
                if back(j):
                    return True
                curr.pop()
                    
            return False

        return back(0)
