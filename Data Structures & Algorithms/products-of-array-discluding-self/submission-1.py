class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        newArr =[]
        for i in nums:
            newArr.append(prefix)
            prefix *= i
    

        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            newArr[i] *= postfix
            postfix *= nums[i]
            
        return newArr