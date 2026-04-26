class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        size = set()
        maxsize =0
        
        for right in range(len(s)):
            while s[right] in size:
                size.remove(s[left])
                left+=1
            size.add(s[right])
            maxsize = max(maxsize, len(size))
            
        return maxsize