# Sort Colors
'''
input nums list[int]
output res list[int]
just sort but don't use sort method

assumptions:
inputlenght 1 <= nums.lenght <= 300
nums[i]lenght <= nums[i] <= 2

time complexity O(n)
space complexity O(n)
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = []
        white = []
        blue = []

        for n in nums:
            if n == 0:
                red.append(0)
            elif n == 1:
                white.append(1)
            else:
                blue.append(2)
            
        nums = red+white+blue

# Majority Element II
import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        goal = math.ceil(n/3)

        nums.sort()
        target = float('inf')
        cnt = 0
        res = []
        for n in nums:
            if n != target:
                if cnt >= goal:
                    res.apppend(target)
                target = n
                cnt = 0
            cnt += 1

        if cnt >= goal:
            res.append(target)

        return res
            
# Subarray Sum Equals K
"""
input nums : list[int], k : int
output res : int

"""
from collections import Counter
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cursum = 0
        prefix = defaultdict(int)
        prefix[0] = 1
        ans = 0

        for n in nums:
            cursum += n

            need = cursum-k
            ans += prefix[need]
            prefix[cursum] += 1

# 
