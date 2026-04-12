class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            rest = target - n
            index = d.get(rest)
            
            if index is not None:
                return [index, i]
            d[n]=i