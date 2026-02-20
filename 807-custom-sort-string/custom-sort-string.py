class Solution:
    def customSortString(self, order: str, s: str) -> str:
   
        s_count = Counter(s)
        res = []

        # Add characters in the order specified
        for char in order:
            if char in s_count:
                res.append(char * s_count[char])
                del s_count[char]
        # Add remaining characters that were not in order
        for char, count in s_count.items():
            res.append(char * count)

        return "".join(res)