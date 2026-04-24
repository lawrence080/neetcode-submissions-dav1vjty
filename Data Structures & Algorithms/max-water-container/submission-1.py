class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                height = min(heights[i],heights[j])
                if (j-i)*height > maxarea:
                    maxarea = (j-i)*height
        return maxarea