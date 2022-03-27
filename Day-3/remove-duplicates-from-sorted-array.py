class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        i=0
        j=0
        if nums == []:
            return 0
        while i<len(nums)-1:
            
            if nums[i] == nums[i+1]:
                i += 1
            else:
                nums[i],nums[j] = nums[j],nums[i];
                j += 1
                i += 1
                
        nums[i],nums[j] = nums[j],nums[i]
        
        return j+1