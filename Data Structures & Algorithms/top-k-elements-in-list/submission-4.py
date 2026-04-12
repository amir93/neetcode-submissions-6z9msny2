class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        input_len = len(nums)
        counted_elements = {}
        frequency_elements = [[] for _ in range(input_len)]
        # compute the dict with the frequency
        for n in nums:
            counted_elements[n] = 1 + counted_elements.get(n, 0) 
        
        for i, j in counted_elements.items():
            frequency_elements[j-1].append(i)
                
        
        res = []
        j = 0 # counter for the result array
         # the counter for the frequency_elements
        for m in range(input_len, 0, -1):
            print(m)
            e = frequency_elements[m-1]
            for val in e:
                res.append(val)
                j+=1
                if j==k:
                    return res
                