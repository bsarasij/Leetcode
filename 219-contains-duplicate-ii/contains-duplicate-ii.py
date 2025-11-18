class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return False
        l = 0
        r = 0
        n = len(nums)
        hash_map = {}
        while r < n:
            if nums[r] in hash_map:
                if abs(r - hash_map[nums[r]]) <= k and r != hash_map[nums[r]]:
                        return True
            
            hash_map[nums[r]] = r
            r += 1
        return False