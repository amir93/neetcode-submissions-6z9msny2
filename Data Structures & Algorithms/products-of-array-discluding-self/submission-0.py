class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_cum = 1
        product = [1 for e in nums]

        for i, e in enumerate(nums):
            product[i] *= product_cum
            product_cum *= e

        product_cum = 1
        for i in range(len(nums)-1, -1, -1):
            product[i] *= product_cum
            product_cum *= nums[i]
        
        return product
