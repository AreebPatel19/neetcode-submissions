class Solution:
    def findMin(self, nums: List[int]) -> int:
        small=nums[0]
        for i in range(0,len(nums)-1):
            j = nums[i]
            j+=1
            if j == nums[i+1]:
                i+=1
            else:
                if nums[i+1] < small:
                    small = nums[i+1]
        return small
