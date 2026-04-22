class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if nums == []:
            return 0
        else:
            longest = 0
            longest_inner = 1
            nums_set = set(nums)
            iter = [i for i in range(min(nums_set), max(nums_set) + 1) if i in nums_set]
            l = len(nums_set)
            for i in range(l):
                    if longest < longest_inner:
                        longest = longest_inner
                    if i+1<l and iter[i+1] == iter[i] + 1:
                        longest_inner+=1
                    else:
                        longest_inner = 1

            return longest