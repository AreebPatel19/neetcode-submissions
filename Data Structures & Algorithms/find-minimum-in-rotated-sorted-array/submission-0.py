class Solution:
    def findMin(self, nums: List[int]) -> int:
        small=nums[0]
        for i in nums:
            if i <= small:
                small =i
        return small
