class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        
        if nums == []:
            return 0
        
        length = 0
        index = []
        # compute the index array size
        min_nums = min(nums)
        index_size = max(nums) + 1
        if min_nums < 0:
            index_size += min(nums)*-1
        else:
            min_nums = 0 
        
        index = [0 for _ in range(index_size)]
        
        for e in nums:
            index[e-min_nums] = 1

        max_length = 0
        for e in index:
            if e == 0:
                if length > max_length:
                    max_length = length
                length = 0
            else:
                length +=1

        if length > max_length:
            max_length = length
        return max_length