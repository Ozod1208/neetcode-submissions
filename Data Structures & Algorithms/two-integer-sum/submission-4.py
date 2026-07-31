class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
      prev_map: dict[int, int] = {}

      for idx, num in nums:
        diff = target - num
        if diff in prev_map:
          return [prev_map[diff], idx]
        prev_map[num] = idx
      
      return []