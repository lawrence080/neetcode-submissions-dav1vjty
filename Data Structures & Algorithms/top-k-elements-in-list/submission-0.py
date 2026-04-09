class Solution:
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in nums:
            if i not in seen:
                seen[i] = 1
            else:
                seen[i] += 1
        return heapq.nlargest(k,seen,key = seen.get)