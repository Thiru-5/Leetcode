class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def quick(arr):
            if len(arr) <= 1:
                return arr
            a = arr[len(arr) // 2]
            l = [i for i in arr if i < a]
            m = [i for i in arr if i == a]
            r = [i for i in arr if i > a]
            return quick(l) + m + quick(r)
        
        a = quick(nums)
        for i in range(len(nums)):
            nums[i] = a[i]
