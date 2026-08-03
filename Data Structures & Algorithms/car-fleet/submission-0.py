class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # 1. Mashinalarni pozitsiya bo'yicha kamayish tartibida saralaymiz (reverse=True)
        # zip() yordamida position va speed massivlarini juftlaymiz
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        current_fleet_time = 0
        
        # 2. Har bir mashinaning manzilga yetish vaqtini tekshiramiz
        for pos, spd in cars:
            time = (target - pos) / spd
            
            # Agar bu mashinaning vaqti oldingi karvon vaqtidan ko'p bo'lsa,
            # u yetib ololmaydi -> Yangi karvon hosil bo'ladi
            if time > current_fleet_time:
                fleets += 1
                current_fleet_time = time
                
        return fleets


# Ishlatib ko'rish uchun misol:
sol = Solution()
print(sol.carFleet(10, [4, 1, 0, 7], [2, 2, 1, 1]))  # Chiqish: 3