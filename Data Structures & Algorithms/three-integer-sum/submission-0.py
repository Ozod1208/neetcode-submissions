class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()

        result: list[int] = []

        for i, num in enumerate(nums):

            if num == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum = num + nums[left] + nums[right]

                if sum == 0:
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
        return result