class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        current = 0
        for k in s:
            if k == '(':
                stack.append(current)
                current = 0
            else:
                current += stack.pop() + max(current, 1)
        return current

        