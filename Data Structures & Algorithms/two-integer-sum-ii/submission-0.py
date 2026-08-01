class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
          have = numbers[left] + numbers[right]

          if have == target:
            return [numbers[left], numbers[right]]
          
          if have < target:
            left += 1
          elif have > target:
            right -= 1
        return []

sol = Solution()
print(sol.twoSum([1,2,3,4], 3))