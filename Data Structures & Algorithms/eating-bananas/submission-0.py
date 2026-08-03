import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = right

        while left <= right:
            mid = (left + right) // 2
            
            # mid tezlikda barcha bananlarni yeyish uchun ketadigan jami soat:
            total_hours = sum(math.ceil(p / mid) for p in piles)
            
            if total_hours <= h:
                # mid tezlik yetarli bo'ldi! Lekin bizga eng kichik k kerak, 
                # shuning uchun javobni saqlab, yanada kichikroq tezlikni izlaymiz.
                ans = mid
                right = mid - 1
            else:
                # mid tezlik juda sekin (soat h dan oshib ketdi), tezlikni oshiramiz
                left = mid + 1

        return ans