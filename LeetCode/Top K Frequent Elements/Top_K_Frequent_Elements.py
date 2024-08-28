# https://leetcode.com/problems/top-k-frequent-elements/
class Solution:
    def topKFrequent(self, nums, k):
        if len(nums) == k:
            return nums

        freq_nums = dict() # key: number, value: frequency

        for num in nums:
            if num not in freq_nums:
                freq_nums[num] = 1
            else:
                freq_nums[num] = freq_nums[num] + 1
        
        frequences = list(set(freq_nums.values()))
        frequences.sort(reverse=True)
        
        freq = dict() # key: frequency, value: list of numbers
        for key, value in freq_nums.items():
            if value in freq:
                freq[value].append(key)
            else:
                freq[value] = [key]

        resullt = []
        for f in frequences:
            if len(resullt) < k:
                resullt.extend(freq[f])
            else:
                break
        return resullt[:k]
    
Solution = Solution()

nums = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6]
k = 10
print(Solution.topKFrequent(nums, k))