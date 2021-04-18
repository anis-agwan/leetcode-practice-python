# 180ms and 15.6mb
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]] += 1
            else:
                dict[nums[i]] = 1
                
        for key,value in dict.items():
            if value > (len(nums)/2):
                maxInt = key
        
        return maxInt


# 156ms and 15.6mb
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        maxInt = 0
        for i in counts:
            if counts[i] > len(nums)/2:
                maxInt = i
        
        return maxInt

# 160ms and 15.5mb
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]


# 160ms and 15.5mb
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = nums[0], 0
        for num in nums:
            if num == candidate:
                count += 1
            elif count == 0:
                candidate, count = num, 1
            else:
                count -= 1
        return candidate