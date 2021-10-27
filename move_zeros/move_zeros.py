nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]

class Solution:
    def moveZeros(self, nums):
        nums.sort(key = int('0').__eq__) # why use __eq__:(https://www.pythontutorial.net/python-oop/python-__eq__/)

Solution().moveZeros(nums) 
print(nums)
