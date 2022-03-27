class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [1,1]
        ans = [[1]]
        for i in range(1,numRows):
            t = []
            ans.append(res)
            t.append(res[0])
            for j in range(len(res)-1):
                
                t.append(res[j]+res[j+1])
                
            t.append(res[-1])
            res = t
            
        return ans