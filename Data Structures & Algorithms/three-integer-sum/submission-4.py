class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()

        result: list[int] = []

        for i, num in enumerate(nums):

            if i > 0 and num == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum = num + nums[left] + nums[right]

                if sum == 0:
                    result.append([num, nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                    
                elif sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1

            
        return result

sol = Solution()
print(sol.threeSum([0,0,0]))