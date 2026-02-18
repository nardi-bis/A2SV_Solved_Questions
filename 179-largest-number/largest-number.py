class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num=list(map(str,nums))
        num.sort(key=lambda x:x*10, reverse=True)
        result="".join(num)
        if result[0]=="0":
            return "0"
        else:
            return result
        