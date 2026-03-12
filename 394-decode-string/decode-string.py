class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = "" # to store the sting 
        current_num = 0 # to store the current number
        for ch in s:
            if ch.isdigit():
                current_num = current_num * 10 + int(ch)
            elif ch == '[': 
                stack.append((current_string, current_num))
                current_num = 0
                current_string =""

            elif ch == ']':
                last_string, num = stack.pop()
                current_string = last_string + num * current_string

            else:
                current_string += ch
        return current_string

