class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
       for i in range(len(nums)):
         for j in range(i+1,len(nums)-1):
            if (nums[i] == nums[j]):
                 del nums[j]
            
         return len(nums) , nums