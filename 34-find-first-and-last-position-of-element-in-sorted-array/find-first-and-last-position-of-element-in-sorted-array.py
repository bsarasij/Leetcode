class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        early_occur = -1
        late_occur = -1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target:
                early_occur = mid
                r = mid - 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        if early_occur == -1:
            return [-1, -1]

        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target:
                late_occur = mid
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return [early_occur, late_occur]