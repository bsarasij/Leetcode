class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i, ch in enumerate(s):
            last[ch] = i
        
        results = []
        curr_end = last[s[0]]
        curr_start = 0 
        
        for i, ch in enumerate(s):
            curr_end = max(curr_end, last[ch])
            if i == curr_end:
                results.append(curr_end - curr_start + 1)
                curr_start = i + 1
                
        return results
