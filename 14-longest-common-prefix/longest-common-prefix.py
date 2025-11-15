class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for strng in strs[1:]:
                if i == len(strng) or strng[i]!= strs[0][i]:
                    return res
            res += strs[0][i]
        return res