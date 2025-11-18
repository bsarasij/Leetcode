class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        hashmap = {'0':'0', '1':'1', '8':'8', '6':'9', '9':'6'}
   
        l = 0
        r = len(num) - 1
        while l <= r:
            if num[l] not in hashmap or num[r] not in hashmap:
                return False
            if hashmap[num[l]] != num[r] or hashmap[num[r]] != num[l]:
                return False
            l += 1
            r -= 1
        return True
