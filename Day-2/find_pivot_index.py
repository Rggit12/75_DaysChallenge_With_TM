class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        res = [0]*len(nums)
        res[0]= nums[0]
        
        for i in range(len(nums)):
            res[i] = res[i-1] + nums[i]
            
        
        for i in range(len(nums)):
            
            if i==0:
                if res[-1]-res[i] == 0:
                    return i
            
            elif i == len(nums)-1:
                if (res[i-1]) == 0:
                    return i
            
            elif res[i-1] == (res[-1] - res[i]):
                return i
        
        return -1