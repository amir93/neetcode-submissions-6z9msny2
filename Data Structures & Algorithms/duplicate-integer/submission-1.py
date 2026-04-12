class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        elements = {}
        for e in nums:
            if e in elements:
                return True
            else:
                elements[e] = 1
        return False
