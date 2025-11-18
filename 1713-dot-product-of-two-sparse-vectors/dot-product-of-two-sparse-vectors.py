class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums_map = {}
        for idx, num in enumerate(nums):
            if num != 0:
                self.nums_map[idx] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        sum = 0
        for idx in self.nums_map:
            if idx in vec.nums_map:
                sum += self.nums_map[idx]*vec.nums_map[idx]
        return sum

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)