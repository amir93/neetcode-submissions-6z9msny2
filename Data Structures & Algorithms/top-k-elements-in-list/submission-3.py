class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        input_len = len(nums)
        counted_elements = {}
        frequency_elements = [None] * (input_len + 1)
        # compute the dict with the frequency
        for n in nums:
            if n in counted_elements:
                counted_elements[n] +=1
            else:
                counted_elements[n] = 1
        
        for i, j in counted_elements.items():
            if frequency_elements[j] is None:
                frequency_elements[j] = [i]
            else:
                frequency_elements[j].append(i)
        
        res = []
        j = 0 # counter for the result array
        i = input_len # the counter for the frequency_elements

        while i >= 1 and j < k:
            e = frequency_elements[i]
            if e is not None:
                for val in e:
                    res.append(val)
                    j+=1
            i -= 1
        return res