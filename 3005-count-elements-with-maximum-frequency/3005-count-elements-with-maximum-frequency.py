class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        maxfreq = 0
        freq_maxfreq = 0
        freqtable = {}
        for num in nums:
            freqtable[num] = freqtable.get(num, 0) + 1
            maxfreq = max(maxfreq, freqtable[num])
            
        for num in freqtable:
            if freqtable[num]==maxfreq:
                freq_maxfreq += 1
        return freq_maxfreq*maxfreq