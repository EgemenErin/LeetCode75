class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        tonto = 0

        def production(tonto):
            product = 1

            for i in range(len(nums)):
                if nums[i] != nums[tonto]:
                    product *= nums[i]
            ans.append(product)
        while tonto < len(nums):
            production(tonto)
            tonto += 1

        return ans
