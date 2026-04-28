class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binary_search(arr, target):
            low = 0
            high = len(arr) - 1

            while low <= high:
                # Calculate middle index (integer division)
                mid = (low + high) // 2
                
                # Check if target is at mid
                if arr[mid] == target:
                    return mid
                
                # If target is greater, ignore left half
                elif arr[mid] < target:
                    low = mid + 1
                    
                # If target is smaller, ignore right half
                else:
                    high = mid - 1
                    
            # Target not present
            return -1 

        numbers = sorted(numbers)
        for i in range(len(numbers)):
            sub = target - numbers[i]
            res = binary_search(numbers, sub)

            if binary_search(numbers, sub) != -1:
                return [i+1,res+1]
        return -1

