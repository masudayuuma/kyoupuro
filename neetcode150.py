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
                
# 3Sum

