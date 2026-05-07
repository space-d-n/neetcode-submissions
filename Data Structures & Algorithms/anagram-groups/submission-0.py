class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}

        for s in strs:
            ss = "".join(sorted(s))
            if ss not in anagrams:
                anagrams[ss] = []
            anagrams[ss].append(s)

        return list(anagrams.values())