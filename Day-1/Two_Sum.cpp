class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
     
       
        
        unordered_map<int,int> m;
        vector<int> res;
        for(int i=0;i<nums.size();i++){
            
            if(m.count(nums[i])==0)
                m[nums[i]] = i;
            
            if(m.count(target-nums[i])!=0 && (m[target-nums[i]]!=i))
                {
                    res.push_back(i);
                    res.push_back(m[target-nums[i]]);
                    break;
                }         
        }
                    return res;
    }
};