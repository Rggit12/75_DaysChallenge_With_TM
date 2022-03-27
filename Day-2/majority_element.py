class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele=nums[0]
        fre=1
    
        for i in range(1,len(nums)):
            
            if ele == nums[i]:
                fre+=1
            elif i <= len(nums)-1 and  fre != 0:
                fre-=1
            elif i<= len(nums)-1 and fre == 0:
                ele = nums[i+1]
            if(fre == 0):
                ele = nums[i+1]
        
        fre = 0    
        for i in range(len(nums)):
            
            if ele == nums[i]:
                fre+=1
    
        if fre > 0:
            return ele
        
        return 0