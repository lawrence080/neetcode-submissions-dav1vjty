class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        def quick_sort(arr):
            if len(arr) <= 1: return arr
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return quick_sort(left) + middle + quick_sort(right)

        arr1 = quick_sort(nums)

        for i in range(1,len(arr1)):
            if arr1[i] == arr1[i-1]:
                return True
        return False
        