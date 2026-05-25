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

# Reverse String
"""
input s: list[str]
output s (None)
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        l = 0
        r = len(n)-1
        half = (l+r)//2
        for i in range(harf):
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

# Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        nxt = []
        for c in s:
            if c.isalnum():
                nxt.append(c.lower())

        if nxt == nxt[::-1]:
            return True
        else:
            return False

# Valid Palindrome II
"""

"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        l = 0
        r = n-1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue
            else:
                break

        if abs(l-r) <= 1:
            return True
        r1 = r-1
        l1 = l
        r2 = r
        l2 = l+1
        flag = True

        while l1 < r1:
            if s[l1] == s[r1]:
                l1 += 1
                r1 -= 1
                continue
            else:
                flag = False
                break
        
        if abs(l1-r1) <= 1 and flag:
            return True
            
        while l2 < r2:
            if s[l2] == s[r2]:
                l2 += 1
                r2 -= 1
                continue
            else:
                return False
            
        if abs(l2-r2) <= 1:
            return True
        
# 
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pal(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left = 0
        right = len(s)-1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return is_pal(left+1, right) or is_pal(left, right-1)
        return True
    
# Merge Sorted Array
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        k = m+n-1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

# Remove Duplicates From Sorted Array
"""
input : 
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        n = len(nums)
        l = 0
        r = 1
        a = []

        while r < len(nums):
            if nums[l-k] == nums[r-k]:
                nums.remove(nums[l-k])
                l = r
                r += 1
                k += 1
                continue
            else:
                l += 1
                r += 1

        k = n-k
        return k

# Remove Duplicates From Sorted Array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        write = 1

        for read in (1, len(nums)):
            if nums[read] != nums[read-1]:
                nums[write] = nums[read]
                write += 1

        return write
    
# 3Sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            r = len(nums)-1
            l = i+1

            while r > l:
                if nums[i]+nums[l]+nums[r] == 0:
                    out.append([nums[i],nums[l],nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    continue
                if nums[i]+nums[l]+nums[r] > 0:
                    r -=1
                elif nums[i]+nums[l]+nums[r] < 0:
                    l +=1
        return out
                    

# 4Sum
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        