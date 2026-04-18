class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        
        if nums == []:
            return 0
        
        set_nums = set(nums)

        d = {e:1 for e in set_nums}
        longest = 0
        length = 0
        
        min_nums = min(set_nums)
        min_nums = 0 if min_nums > 0 else min_nums
        max_nums = max(set_nums)    

        for i in range(min_nums, max_nums + 2):
            if i in d:
                length +=1
            elif length > longest:
                    longest = length
                    length = 0
            else:    
                length = 0
            
        return longest