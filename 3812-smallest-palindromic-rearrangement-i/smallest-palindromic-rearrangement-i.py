class Solution:
    def smallestPalindrome(self, s: str) -> str:
        half = ""
        mid = ""
        C = Counter(s)
        for k,v in sorted (C.items()):
            half += k *(v//2)
            if v % 2 != 0:
                mid = k
        return half + mid +half[::-1]

        