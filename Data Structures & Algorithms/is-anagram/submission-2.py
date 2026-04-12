class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t:
            return True
        return sorted(s) == sorted(t)
         