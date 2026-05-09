class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}

        for s in strs:
            freq = [0] * 26
            
            for c in s:
                c_ind = ord(c) - ord('a')
                freq[c_ind] += 1
            
            key = tuple(freq)

            if key not in anagrams:
                anagrams[key] = []
            
            anagrams[key].append(s)

        return list(anagrams.values())