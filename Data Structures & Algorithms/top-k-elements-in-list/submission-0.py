class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted_elements = {}
        for n in nums:
            if n in counted_elements:
                counted_elements[n] +=1
            else:
                counted_elements[n] = 1

        counted_elements = dict(sorted(counted_elements.items(), key=lambda x:x[1], reverse=True))
        res = []
        it = iter(counted_elements.keys())
        for i in range(k):
            res.append(next(it, None))
        return res