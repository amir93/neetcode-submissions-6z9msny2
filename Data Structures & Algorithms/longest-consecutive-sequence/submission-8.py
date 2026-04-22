class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if nums == []:
            return 0
        else:
            nums_dict = {e:0 for e in set(nums)}
            longest = 0
            longest_inner = 0
            for i in range(min(set(nums)), max(set(nums)) + 3):
                if longest < longest_inner:
                        longest = longest_inner

                if i in nums_dict:
                    longest_inner+=1
                else:
                    longest_inner = 0    
        return longest