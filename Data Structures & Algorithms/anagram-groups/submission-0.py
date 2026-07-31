class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        frequency = [0] * 26
        words_map: dict[tuple, list[str]] = {}
        
        for strr in strs:
            for w in strr:
                frequency[ord(w) - ord('a')] += 1
            
            tup = tuple(frequency)

            if tup not in words_map:
              words_map[tup] = []

            words_map[tup].append(strr)
            frequency = [0] * 26
        
        return list(words_map.values())