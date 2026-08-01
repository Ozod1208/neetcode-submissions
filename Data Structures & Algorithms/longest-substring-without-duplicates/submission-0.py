class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            # Yangi harfni ramkaga qo'shamiz
            char_set.add(s[right])
            # Rekordni tekshiramiz (right - left + 1 -> joriy ramka eni)
            max_len = max(max_len, right - left + 1)
        return max_len