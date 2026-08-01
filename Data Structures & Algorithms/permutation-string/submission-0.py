from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        # 1. s1 dagi harflar chastotasini sanab olamiz
        s1_count = Counter(s1)
        # 2. s2 ning birinchi oyna (n1 o'lchamdagi) chastotasi
        window_count = Counter(s2[:n1])
        # Agar birinchi oynadayoq mos kelsa
        if s1_count == window_count:
            return True

        # 3. Oynani s2 bo'ylab 1 qadamdan o'ngga suramiz
        for i in range(n1, n2):
            # Oynaga yangi kirgan harfni oshiramiz
            new_char = s2[i]
            window_count[new_char] += 1

            # Oynadan chiqib ketgan harfni kamaytiramiz
            left_char = s2[i - n1]
            window_count[left_char] -= 1

            # Agar harf soni 0 bo'lsa, lug'atdan o'chiramiz (tenglikni to'g'ri tekshirish uchun)
            if window_count[left_char] == 0:
                del window_count[left_char]

            # Solishtiramiz
            if s1_count == window_count:
                return True

        return False