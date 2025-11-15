class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = - inf
        second_max = - inf
        idx = 0
        for i in range(len(nums)):
            if nums[i] >= max_num:
                second_max = max_num
                max_num = nums[i]
                idx = i
            elif nums[i] >= second_max:
                second_max = nums[i]
            print(f"max = {max_num}  second = {second_max} idx = {idx}")
        return idx if max_num >= 2*second_max else -1