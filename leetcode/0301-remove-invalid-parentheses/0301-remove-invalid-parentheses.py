class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        res = set([""])
        mx_ln = 0
        stack= []
        cnt = 0
        def recur(idx):
            nonlocal cnt,mx_ln, res
        
            if idx >= len(s):
                if cnt == 0:
                    if len(stack) > mx_ln:
                        mx_ln = len(stack)
                        res = set()
                    if len(stack) == mx_ln:
                        res.add("".join(stack))
                return 

            if len(s) - idx  + len(stack) < mx_ln:
                return

            if s[idx] != ")" or cnt > 0:
                cnt += s[idx] == "("
                cnt -= s[idx] == ")"
                stack.append(s[idx])
                recur(idx+1)
                stack.pop()
                cnt -= s[idx] == "("
                cnt += s[idx] == ")"
            if s[idx] == "(" or s[idx] == ")":
                recur(idx+1)

        recur(0)
        return list(res)
        