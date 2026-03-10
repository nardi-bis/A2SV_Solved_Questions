class Solution:
    def simplifyPath(self, path: str) -> str:
        # split using "/"
        # ust add it to a stack the name and when.. remove the one in the top
        # then get the values form the stack by join"/" then return / + answer
        # path=path.split('/')
        # stack =[]
        # for fir in path:
        #     if fir =="..":
        #         if stack:
        #             stack.pop()
        #     elif fir != '' and fir != '':

        path = path.split('/')
        stack = []
        for x in path:
            if x =="..":
                if stack:
                    stack.pop()
            elif x !="." and x != "":
                stack.append(x)
        return '/'+'/'.join(stack)