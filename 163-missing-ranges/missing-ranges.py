class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower,upper]]
        l = r = lower
        n_prev = lower - 1 
        result = []
        for n in nums:    
            l = n_prev + 1
            r = n - 1
            if r >= l: 
                result.append([l , r])
            
            n_prev = n
        if nums[-1] < upper :
            result.append([nums[-1] + 1 , upper])
        return result