class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        duplicate = set()
        nums.sort()
        
        for i in range(len(nums)):
            target = -nums[i]
            left,right = i+1,len(nums)-1
            
            while left < right:
                val = nums[left] + nums[right]
                
                if val == target and (nums[left],nums[right]) not in duplicate:
                    res.append([nums[i],nums[left],nums[right]])
                    duplicate.add((nums[left],nums[right]))
                    
                if val > target:
                    right -= 1
                else:
                    left+=1
                    
        return res