class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr1, arr2):
            merged = []
            i, j = 0, 0
            while i < len(arr1) or j < len(arr2):
                if j == len(arr2) or (i < len(arr1) and arr1[i] < arr2[j]):
                    merged.append(arr1[i])
                    i += 1
                else:
                    merged.append(arr2[j])
                    j += 1
            return merged 

        def msort(arr):
            if len(arr) == 1:
                return arr
            mid = len(arr) // 2

            left = msort(arr[:mid])
            right = msort(arr[mid:])
            return merge(left, right)
        return msort(nums)


            
            

        