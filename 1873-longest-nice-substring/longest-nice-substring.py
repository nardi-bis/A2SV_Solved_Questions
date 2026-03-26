class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        sets = set(s)
        for index, value in enumerate(s):
            if value.swapcase() not in s:
                left = self.longestNiceSubstring(s[:index])
                right = self.longestNiceSubstring(s[index+1:])
                if len(left) >= len(right):
                    return left
                else:
                    return right
        return s