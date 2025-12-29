class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        gap_array = []
        last_end = 0
        for i in range(len(startTime)):
            curr_start = startTime[i]
            gap_array.append(curr_start - last_end)
            last_end = endTime[i]

        gap_array.append(eventTime - endTime[-1])
        print(gap_array)

        curr_pref_sum = sum(gap_array[:k+1])
        max_sum = curr_pref_sum
        if len(gap_array) > k:
            for j in range(k+1, len(gap_array)):
                curr_pref_sum = curr_pref_sum - gap_array[j - (k+1)] + gap_array[j]
                max_sum = max(max_sum, curr_pref_sum)
        return max_sum