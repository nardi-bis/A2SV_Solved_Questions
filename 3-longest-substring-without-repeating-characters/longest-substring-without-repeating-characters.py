class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # left = 0
        # seen = {}
        # max_ = 0
        
        # for right, curr in enumerate(s): # index,value
        #     if curr in seen:
        #         left = max(left, seen[curr] + 1)
        #     max_ = max(max_, right - left + 1)
        #     seen[curr] = right

        # return max_
        window=set()
        l=0
        m=0
        for i in range(len(s)):
            while s[i] in window:
                window.remove(s[l])
                l+=1
            window.add(s[i])
            m=max(m,i-l+1)
        return m

