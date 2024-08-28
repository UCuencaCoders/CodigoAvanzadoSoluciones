class Solution:
    def threeSum(self, nums):
        l = 0
        r = len(nums) - 1
        nums = sorted(nums)
        size = len(nums)
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r =  size - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    a = sorted([nums[i], nums[l], nums[r]])
                    if a not in res:
                        res.append(a)
                    l += 1
                    r -= 1
        return res
            
                
 # nums = [-4, -1, -1, 0, 1, 2]  
nums = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
Solution = Solution()
print(Solution.threeSum(nums))