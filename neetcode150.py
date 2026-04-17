#1
# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         ans = set()
#         flag = False
#         for i in nums:
#             if i in ans:
#                 flag = True
#                 break
#             else:
#                 ans.add(i)
#         return flag

# Valid Anagram
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         from collections import Counter
#         s_dict = Counter(s)
#         t_dict = Counter(t)
#         if s_dict == t_dict:
#             return True
#         else:
#             return False

# Two Sum
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 if nums[i]+nums[j] == target:
#                     return [i, j]

# Group Anagrams
# from collections import defaultdict
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         ans = defaultdict(list)

#         for s in strs:
#             char_list = "".join(sorted(s))
#             ans[char_list].append(s)

#         final = []
#         for a in ans.values():
#             final.append(a)

#         return final

# # Top K Frequent Elements
# from collections import defaultdict
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         ans = defaultdict(int)

#         for num in nums:
#             ans[num] += 1

#         ans_list = sorted(ans.keys(), key=ans.get, reverse=True)
#         return ans_list[:k]

# Encode and Decode Strings
# from typing import List

# class Solution:

#     def encode(self, strs: List[str]) -> str:
#         out = []
#         for s in strs:
#             out.append(str(len(s))+"#"+s)
#         return "".join(out)

#     def decode(self, s: str) -> List[str]:
#         res = []
#         i = 0
#         while i < len(s):
#             j = i
#             while s[j] != '#':
#                 j += 1
#             length = int(s[i:j])
#             word = s[j+1 : j+1 + length]
#             res.append(word)
#             i = j+1+length
#         return res

# if __name__ == "__main__":
#     codec = Solution()
#     strs = ["neet", "code", "love", "you"]
#     encoded_string = codec.encode(strs)
#     strs2 = codec.decode(encoded_string)

# Products of Array Except Self
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         left_ans = [0]*len(nums)
#         right_ans = [0]*len(nums)
#         left_tmp = 1
#         for i in range(len(nums)):
#             left_ans[i] += left_tmp
#             left_tmp *= nums[i]
#         right_tmp = 1
#         for i in range(len(nums)-1, -1, -1):
#             right_ans[i] += right_tmp
#             right_tmp *= nums[i]
#         ans = [0]*len(nums)
#         for i in range(len(nums)):
#             ans[i] = right_ans[i] * left_ans[i]

#         return ans

# Valid Sudoku
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         for row in range(9):
#             seen = set()
#             for col in range(9):
#                 if board[row][col] == '.':
#                     continue
#                 if board[row][col] in seen:
#                     return False
#                 seen.add(board[row][col])

#         for col in range(9):
#             seen = set()
#             for row in range(9):
#                 if board[row][col] == '.':
#                         continue
#                 if board[row][col] in seen:
#                     return False
#                 seen.add(board[row][col])

#         for square in range(9):
#             seen = set()
#             for i in range(3):      
#                 for j in range(3):
#                     row = (square//3)*3+i
#                     col = (square%3)*3+j
#                     if board[row][col] == '.':
#                         continue
#                     if board[row][col] in seen:
#                         return False
#                     seen.add(board[row][col])
#         return True
    
    # [[0, 1, 2],
    #  [0, 1, 2],
    #  []]

# Longest Consecutive Sequence
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if nums == []:
#             return 0 

#         nums = sorted(list((set(nums))))
#         right, left = 1, 0
#         count = 1
#         max_count = 1
        
#         while right < len(nums):
#             if nums[right] == nums[left]+1:
#                 count += 1
#                 left += 1
#             else:
#                 left = right
#                 count = 1
#             right += 1
#             max_count = max(max_count, count)
                
#         return max_count
            
# Valid Palindrome
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         string = ""
#         for c in s:
#             if c.isalnum():
#                 string += c.lower()

#         i = 0
#         while i < len(string)//2:
#             if string[i] == string[-i-1]:
#                 i += 1
#                 continue
#             else:
#                 return False
#         return True

# Two Integer Sum II
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         for i in range(len(numbers)-1):
#             for j in range(i+1, len(numbers)):
#                 if numbers[i]+numbers[j] == target:
#                     return [i, j]
                
# 正解
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         right = len(numbers)-1
#         left = 0

#         while left < right:
#             if numbers[left]+numbers[right] > target:
#                 right -= 1
#                 continue

#             if numbers[left]+numbers[right] < target:
#                 left += 1
#                 continue

#             if numbers[left]+numbers[right] == target:
#                 return [left+1, right+1]
            

# 3Sum
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         from collections import defaultdict
#         nums = sorted(nums)
#         numsdict = defaultdict(int)
#         ans = set()
#         for n in nums:
#             numsdict[n] += 1

#         l, r = 0, len(nums)-1
#         while l < r:
#             if nums[l] > nums[l]+nums[r]:
#                 l += 1
#             if nums[r] < nums[l]+nums[r]:
#                 r += 1
#             numsdict[nums[l]] -= 1
#             numsdict[nums[r]] -= 1
#             if numsdict[-(nums[l]+nums[r])] > 0:
#                 tmp = [nums[l], nums[r], -(nums[l]+nums[r])]
#                 ans.add(tuple(sorted(tmp)))
#             numsdict[nums[l]] += 1
#             numsdict[nums[r]] += 1
            
        
#         return ans


# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         nums.sort()

#         for i, a in enumerate(nums):
#             if i > 0 and a == nums[i-1]:
#                 continue

#             l, r = i+1, len(nums)-1
#             while l < r:
#                 threeSum = a + nums[l] + nums[r]
#                 if threeSum > 0:
#                     r -= 1
#                 elif threeSum < 0:
#                     l += 1
#                 else:
#                     res.append([a, nums[l], nums[r]])
#                     l += 1
#                     r -= 1
#                     while nums[l] == nums[l-1] and l < r:
#                         l += 1
#         return res

# Container With Most Water
# class Solution:
#     def maxArea(self, heights: List[int]) -> int:
        
#         max_area = 0
#         for left in range(len(heights)-1):
#             right =len(heights)-1
#             saiteki = heights[left]*(right-left)
#             if max_area >= saiteki:
#                 continue
#             while left < right:
#                 if heights[left] <= heights[right]:
#                     max_area = max(max_area, (right-left)*heights[left])
#                     break
#                 else:
#                     max_area = max(max_area, min(heights[left], heights[right])*(right-left))
#                     right -= 1
#         return max_area
                
# Trapping Rain Water
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         left = 0
#         right = 0
#         cnt = 0
        
#         while right < len(height)-1:
#             right += 1
#             if height[right] < 1:
#                 continue
#             wall = min(height[left], height[right])
#             tmp_cnt = 0
#             while left < right:
#                 left += 1
#                 calc = wall - height[left]
#                 if calc > 0:
#                     tmp_cnt += calc
                
#             cnt += tmp_cnt
#         return cnt


# Best Time to Buy and Sell Stock
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         minby = 10000
#         for i in prices:
#             if minby > i:
#                 minby = i
#                 continue
#             else:
#                 ans = max(ans, i-minby)

#         return ans
            
# Longest Substring Without Repeating Characters
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         c_set = set()
#         ans = 0
#         del_index = 0
#         for c in s:
#             while c in c_set:
#                 c_set.remove(s[del_index])
#                 del_index += 1
#             c_set.add(c)
#             ans = max(len(c_set), ans)

#         return ans

# Longest Repeating Character Replacement
# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         from collections import defaultdict
#         scnt = defaultdict(int)
#         l = 0
#         r = 1
#         while l < r:
#             while r < len(s):
#                 scnt[s[r]] += 1
#                 if r-l+1 -scnt[s[l]] > k:
#                     continue
#                 else:
#                     break

#             ans
                
            
            
# Valid Parentheses
# class Solution:
#     def isValid(self, s: str) -> bool:
#         c_dict = { '(': ')', '[':']', '{':'}'}
#         stack = []

#         for c in s:
#             if c in c_dict:
#                 stack.append(c)
#             else:
#                 if stack == []:
#                     return False
#                 target = stack.pop()
#                 if not (target in c_dict and c_dict[target] ==c):
#                     return False
#         return True if stack == [] else False

# Evaluate Reverse Polish Notation
# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         stack = []

#         for t in tokens:

#             if t ==  "+":
#                 t_1 = stack.pop()
#                 t_2 = stack.pop() 
#                 ans = t_1 + t_2
#                 stack.append(ans)
#                 continue
#             if t ==  "-":
#                 t_1 = stack.pop()
#                 t_2 = stack.pop() 
#                 ans = t_1 - t_2
#                 stack.append(ans)
#                 continue
#             if t ==  "*":
#                 t_1 = stack.pop()
#                 t_2 = stack.pop() 
#                 ans = t_1 + t_2
#                 stack.append(ans)
#                 continue
#             if t ==  "/":
#                 t_1 = stack.pop()
#                 t_2 = stack.pop() 
#                 ans = t_1 / t_2
#                 stack.append(ans)
#                 continue
#             else:
#                 stack.append(int(t))
        
#         return stack[0]

# Daily Temperatures
