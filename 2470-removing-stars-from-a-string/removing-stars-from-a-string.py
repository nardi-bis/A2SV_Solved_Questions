class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for l in s:
            if l == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(l)
        return "".join(stack)

   
  

        