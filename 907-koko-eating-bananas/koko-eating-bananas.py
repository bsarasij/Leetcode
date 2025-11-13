class Solution:
    def kWorks(self, k: int, piles: List[int], h: int) -> bool:
        hrs = 0
        for banana in piles:
            hrs += ceil(banana/k)
        return True if hrs <= h else False

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        while lo < hi:
            k = (lo + hi)//2
            if self.kWorks(k, piles, h):
                hi = k
            else:
                lo = k + 1
        return lo