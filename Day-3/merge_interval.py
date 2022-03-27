class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x:x[0])
        
        s = intervals[0][0]
        e = intervals[0][1]
        i=1
        ans = []
        while i < len(intervals):
            if e >= intervals[i][0]:
                e = max(e,intervals[i][1])
            else:
                ans.append([s,e])
                s = intervals[i][0]
                e = intervals[i][1]
            
            i += 1
        
        ans.append([s,e])
        
        return ans
            
        