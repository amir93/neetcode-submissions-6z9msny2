class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        d = {}
        first = nums[0]
        d[0] = first
        rest = target - first
        
        for i in range(1, n):
            if nums[i] == rest:
                return [0, i]
            d[nums[i]] = i
        
        for i in range(1, n):
            rest = target - nums[i]
            index = d.get(rest)
            if index and index != i:
                return [i, index]
