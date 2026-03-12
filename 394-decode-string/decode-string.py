class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = "" 
        current_num = 0 
        for ch in s:
            if ch.isdigit():
                current_num = current_num * 10 + int(ch)
            elif ch == '[': 
                stack.append((current_string, current_num))
                current_num = 0
                current_string =""

            elif ch == ']':
                item = stack.pop()
                last_string = item[0]
                num = item[1]
                current_string = last_string + num * current_string
                # [a2[c]] c = current_string, 2 = num, a = last_string

            else:
                current_string += ch
        return current_string

