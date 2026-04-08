class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return "".join(sorted(s)) == "".join(sorted(t))
        # return set(s) == set(t) and len(s) == len(t)
        