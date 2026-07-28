import math
class Solution:
    def findMin(self, nums: List[int]) -> int:
        L=0
        R=len(nums)-1
        i=0
        small=nums[0]
        while L <= R :
            mid = (L + R) // 2
            print(mid)
            if nums[mid] > nums[R]:
                L=mid+1
            elif nums[mid] > nums[L]:
                R=mid-1
            else:
                L+=1
                R-=1
                if nums[mid] < small:
                    small = nums[mid]
        return small
            