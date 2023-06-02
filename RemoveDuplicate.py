# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
nums: list[int]    
list[6] = {1,3,2,1,4,9}
for i in range(len(nums)):
  for j in range(len(nums)-1):
   if(nums[i]==nums[j]):
     nums[j]= nums[j]+1 
   j+=1
for i in range(len(nums)):
 print(nums[i])
