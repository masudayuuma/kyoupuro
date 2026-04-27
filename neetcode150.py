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
# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         stack = []
#         ans = [0]*len(temperatures)

#         for i, t in enumerate(temperatures):
#             while len(stack) > 0 and stack[-1][1] < t:
#                 index, tmp = stack.pop()
#                 ans[index] = i-index
#             stack.append((i, t))

#         return ans

# Car Fleet
# class Solution:
#     def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
#         sort_list = []
#         for p, s in zip(position, speed):
#             sort_list.append((p, s))

#         sort_list = sorted(sort_list)

#         offset = 0
#         fleets = len(position)

#         while len(sort_list) > 0:

#             p, s = sort_list.pop()
#             cnt = (target-p)/s
#             if cnt > offset:
#                 offset = cnt
#             else:
#                 fleets -= 1
#                 continue
#         return fleets
            
# 
# Car Fleet
# class Solution:
#     def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
#         pair = [[p, s] for p, s in zip(position, speed)]

#         stack = []

#         for p, s in sorted(pair)[::-1]:
#             stack.append((target-p)/s)
#             if len(stack)>= 2 and stack[-1] <= stack[-2]:
#                 stack.pop()

#         return len(stack)
    
# Binary Search
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         ok, ng = -1, len(nums)

#         while ng - ok > 1:
#             mid = (ok + ng) // 2
#             if nums[mid] < target:
#                 ok = mid
#             else:
#                 ng = mid

#         return ng if ng < len(nums) and nums[ng] == target else -1


# Search a 2D Matrix
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
#         for numlist in matrix:
#             ok = len(numlist)-1
#             ng = -1
#             while ok - ng < 1:
#                 mid = (ok+ng)//2
#                 if numlist[mid] < target:
#                     ng = mid
#                 else:
#                     ok = mid
#             if numlist[ok] == target:
#                 return True
            
#         return False

# Koko Eating Bananas
# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         ok, ng = 1000000000, -1

#         while ok - ng > 1:
#             mid = (ok+ng)//2
#             hour = 0
#             for p in piles:
#                 cnt = p//mid
#                 if cnt == 0:
#                     cnt = 1
#                 hour += cnt
#             if h >= hour:
#                 ok = mid
#             else:
#                 ng = mid

#         return ok

# Find Minimum in Rotated Sorted Array
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1

        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid

        return nums[left]
    
# Search in Rotated Sorted Array
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:  # 左がソート済み
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # 右がソート済み
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

# Reverse Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            if not head:
                return None
            
            newHead = head
            if head.next:
                newHead = self.reverseList(head.next)
                head.next.next = head
            head.next = None

            return newHead
    

# Merge Two Sorted Linked Lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list2 and not list1:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
            head.next = self.mergeTwoLists(list1, list2)

        else:
            head = list2
            list2 = list2.next
            head.next = self.mergeTwoLists(list1, list2)

        return head

# Linked List Cycle Detection
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return None
        
        seen = set()

        while head and head.next:
            if head in seen:
                return True
            seen.add(head)
            head = head.next

        return False
    
# Last Stone Weight
import heapq

class Solution:
    def lastStoneWeight(self, stones):
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = -heapq.heappop(stones)
            stone2 = -heapq.heappop(stones)

            if stone1 != stone2:
                heapq.heappush(stones, -(stone1 - stone2))

        return -stones[0] if stones else 0
    

    
# K Closest Points to Origin
# import heapq
# import math
# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         distance_heapq = []
#         heapq.heapify(distance_heapq)
#         ans = []
#         for x, y in points:
#             distance = math.sqrt(x**2+y**2)
#             heapq.heappush(distance_heapq, (distance, x, y))

#         for i in range(k):
#             tmp = heapq.heappop(distance_heapq)
#             ans.append([tmp[1], tmp[2]])
#         return ans

# Kth Largest Element in an Array
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         import heapq
#         optimized_nums = []
#         for i in nums:
#             optimized_nums.append(-i)

#         heapq.heapify(optimized_nums)
#         ans = 0
#         for i in range(k):
#             ans = heapq.heappop(optimized_nums)

#         return -ans

# Task Scheduler
# import collections
# import heapq

# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) -> int:
#         count = collections.Counter(tasks)
#         maxHeap = [-cnt for cnt in count.values()]
#         heapq.heapify(maxHeap)

#         time = 0
#         q = collections.deque()

#         while maxHeap or q:
#             time += 1

#             if not maxHeap:
#                 time = q[0][1]
#             else:
#                 cnt = 1+ heapq.heappop(maxHeap)
#                 if cnt:
#                     q.append([cnt, time+n])
#             if q and q[0][1] == time:
#                 heapq.heappush(maxHeap, q.popleft()[0])
#         return time

# Subsets
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
        
#         res = []
#         subset = []
#         def dfs(i):
#             if i > len(nums):
#                 res.append(subset.copy())
#                 return
#             subset.append(nums[i])
#             dfs(i+1)
#             subset.pop()
#             dfs(i+1)
#         dfs(0)
#         return res

# Combination Sum
import sys
sys.setrecursionlimit(100000000)
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(index):
            if sum(subset) > target:
                return
            if sum(subset) == target:
                res.append(subset[:])
                return
            if index >= len(nums):
                return

            subset.append(index)
            dfs(subset)
            subset.pop()

            dfs(index+1)


        dfs(0)
        return res

# Combination Sum II
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()

        def dfs(index):
            total = sum(subset)

            if total == target:
                res.append(subset[:])
                return
            if total > target:
                return
            if index >= len(candidates):
                return

            # 今の値を使う
            subset.append(candidates[index])
            dfs(index + 1)
            subset.pop()

            # 同じ値を飛ばして次へ
            next_index = index + 1
            while next_index < len(candidates) and candidates[next_index] == candidates[index]:
                next_index += 1
            dfs(next_index)

        dfs(0)
        return res
    
# Permutations
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         subset = []

#         def dfs(length):
#             if length == len(nums):
#                 res.append(subset.copy())
#                 return

#             for i in nums:
#                 if i in subset:
#                     continue
#                 subset.append(i)
#                 dfs(length+1)
#                 subset.pop()

#         dfs(0)
#         return res

# class Solution:
#     def permulte(self, nums:List[int]) -> List(List[int]):
#         res = []
#         path = []
#         used = [False] * len(nums)

#         def dfs():
#             if len(path) == len(nums):
#                 res.append(path[:])
#                 return
            
#             for i in range(len(nums)):
#                 if used[i]:
#                     continue

#                 used[i] = True
#                 path.append(nums[i])

#                 dfs()

#                 path.pop()
#                 used[i] = False

#         dfs()
#         return res

# class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(length):
            if length == len(nums):
                res.append(subset.copy())
                return

            for i in nums:
                if i in subset:
                    continue
                subset.append(i)
                dfs(length+1)
                subset.pop()

        dfs(0)
        return res
    
# class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(length):
            if length == len(nums):
                res.append(subset.copy())
                return

            for i in nums:
                if i in subset:
                    continue
                subset.append(i)
                dfs(length+1)
                subset.pop()

        dfs(0)
        return res
    
# Subsets II
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(lenght):
            if lenght == len(nums):
                res.append(subset[:])
                return
            
            dfs(lenght+1)
            subset.append(nums[lenght])
            dfs(lenght+1)
            subset.pop()

        dfs(0)
        return res
    

# Subsets II
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def backtrack(i, subset):
            if i == len(nums):
                res.add(tuple(subset))
                return
            
            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()
            backtrack(i+1, subset)

        nums.sort()
        backtrack(0, [])
        return [list(s) for s in res]
    
# Generate Parentheses
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         res = []
#         substr = ''

#         def dfs(cnt, open_cnt):
#             if cnt == n:
#                 res.append(subset)

#             substr + '('
#             dfs(cnt+1)

# Number of Islands
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:

#         grid_flag = [[False for _ in range(len(grid[0]))] for _ in range(len(grid)) ]
#         cnt = 0
#         search_point = ((0, 1), (0, -1), (1, 0), (-1, 0))


#         def search_island(i, j):
#             for dy, dx in search_point:
#                 t_x = dx+j
#                 t_y = dy+i
#                 if not 0 <= t_x < len(grid[0]) or not 0 <= t_y < len(grid):
#                     continue


#                 if grid[t_y][t_x] == '1' and grid_flag[t_y][t_x] == False:
#                     grid_flag[t_y][t_x] = True
#                     search_island(t_y, t_x)

        
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid_flag[i][j] == True or grid[i][j] == '0':
#                     continue
#                 grid_flag[i][j] = True
#                 search_island(i, j)
#                 cnt += 1

#         return cnt

# Max Area of Island
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_cnt = 0
        direction = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def island_search(i, j):
            count = 0
            for dy, dx in direction:
                y = i+dy
                x = j+dx
                if not 0 <= x < len(grid[0]) or not 0 <= y < len(grid):
                    continue

                if grid[y][x] == 1:
                    count += 1
                    grid[y][x] = 0
                    count += island_search(y, x)
            return count

        for i in range(len(grid)):

            for j in range(len(grid[0])):

                if grid[i][j] == 1:
                    grid[i][j] = 0
                    cnt = 1
                    cnt += island_search(i, j)

                    max_cnt = max(max_cnt, cnt)

        return max_cnt
    

# Clone Graph
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        pass

# Islands and Treasure
# from collections import deque
# class Solution:
#     def islandsAndTreasure(self, grid):
#         row, col = len(grid), len(grid[0])
#         diff = ((1, 0), (-1, 0), (0, 1), (0, -1))
#         calc_grid = [row[:] for row in grid]
#         queue = deque()

#         for i in range(row):
#             for j in range(col):
#                 if grid[i][j] == 0:
#                     calc_grid[i][j] = 0
#                     queue.append((i, j))
        
#         while queue:
#             i, j = queue.popleft()
#             for dy, dx in diff:
#                 x = dx+j
#                 y = dy+i
#                 if not 0 <= y < len(grid) or not 0 <= x < len(grid[0]) or grid[y][x] == -1:
#                     continue
#                 if grid[y][x] == 2147483647:
#                     grid[y][x] = grid[i][j]+1
#                     queue.append((y, x))

# Rotting Fruit
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        diff = ((1, 0), (-1, 0), (0, 1), (0, -1))
        final = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j, 0))

        while q:
            i, j, time = q.popleft()
            final =max(final, time)
            for dy, dx in diff:
                y = i+dy
                x = j+dx
                
                if not 0 <= y < len(grid) or not 0 <= x < len(grid[0]) or grid[y][x] == 0 or grid[y][x] == 2:
                    continue

                grid[y][x] = 2 
                q.append((y, x, time+1))
        flag = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    flag = True

        return final if not flag else -1
    

# Climbing Stairs
# DP
# class Solution:
#     def climbStairs(self, n: int) -> int:
        
#         if n <= 2:
#             return n
        
#         dp = [0]*(n+1)
#         dp[1], dp[2] = 1, 2
#         for i in range(3, n+1):
#             dp[i] = dp[i-1]+dp[i-2]
#         return dp[n]

# Single Number
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         ans = 0
#         for num in nums:
#             ans = ans^num

#         return ans

# Number of 1 Bits
class Solution:
    def hammingWeight(self, n: int) -> int:
        
        ans = 0

        for i in len(str(n)):
            if 1 << i & 1:
                ans += 2*i

        return ans
    
# Counting Bits
class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0]*(n+1)

        for i in range(n+1):
            cnt = 0
            for j in range(32):
                if i >> j & 1:
                    cnt +=1
            output[i] = cnt

        return output
    
# Reverse Bits

class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0

        for i in range(32):
            if n >> i & 1:
                output += 2**(31-i)
        return output

# Missing Number
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for n in range(len(nums)+1):
            ans ^= n

        for n in nums:
            ans ^= n

        return ans
    
# Sum of Two Integers
class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        res = 0
        mask = 0xFFFFFFFF

        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1
            cur_bit = a_bit ^ b_bit ^ carry
            carry = (a_bit + b_bit + carry) >= 2
            if cur_bit:
                res |= (1 << i)

        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)

        return res
    
# Insert Interval
from collections import deque
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        res = []

        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        while i < n:
            res.append(intervals[i])
            i += 1

        return res

# Merge Intervals
# class Solution:
#     from collections import deque
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
#         n = len(intervals)
#         i = 0
#         res = []

#         while i < n:
#             t_s, t_e = intervals[i]
#             if i+1 <n and t_e < intervals[i+1][0]:
#                 res.append([t_s, t_e])
#                 continue

#             if i+1 < n and t_e >= intervals[i+1][0]:
#                 while i+1 < n and t_e >= intervals[i+1][0]:
#                     t_e = max(t_e, intervals[i+1][1])
#                     i += 1
#                 res.append([t_s, t_e])
#                 continue
            
#             res.append([t_s, t_e])
            
#         return res

# Non-overlapping Intervals
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        def dfs(i, prev):
            if i == len(intervals):
                return 0
            res = dfs(i+1, prev)
            if prev == -1 or intervals[prev][1] <= intervals[i][0]:
                res = max(res, 1+dfs(i+1, i))
        return len(intervals) - dfs(0, -1)
    
# Meeting Rooms
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort()
        t_s, t_e = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)-1):
            next_s, next_e = intervals[i+1][0], intervals[i+1][1]

            if t_e >= next_e:
                return False

            t_s, t_e = intervals[i][0], intervals[i][1]

        return True

# Meeting Rooms II
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# class Solution:
#     def minMeetingRooms(self, intervals: List[Interval]) -> int:
#         intervals.sort(key=lambda x: x.start)
#         min_heap = []

#         for interval in intervals:
#             if min_heap and min_heap[0] <= interval.start:
#                 heapq.heappop(min_heap)
#             heapq.heappush(min_heap, interval.end)

#         return len(min_heap)

# Climbing Stairs
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        dp= [0]*(n+1)
        dp[1] = 1 
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]
    
# Min Cost Climbing Stairs
# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         if len(cost) <= 2:
#             return min(cost)
#         n = len(cost)
#         dp = [0]*(n)
#         dp[0] = cost[0]
#         dp[1] = cost[1]

#         for i in range(2, n):
#             dp[i] = min(dp[i-1], dp[i-2])+cost[i]

#         return min(dp[-1], dp[-2])

# House Robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        n = len(nums)
        dp = [0]*n

        dp[0] = nums[0]
        # これmax(dp[0], dp[1])にしたらi-2まで考慮でも通る
        dp[1] = nums[1]
        dp[2] = max(nums[0]+nums[2], nums[1])

        for i in range(3, len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1], dp[i-3]+nums[i])


        return dp[-1]
    
# House Robber II
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if len(nums) <= 2:
#             return max(nums)
        
#         n = len(nums)
#         dp = [0]*n

#         dp[0] = 0
#         dp[1] = max(nums[1])
#         dp[2] = max(nums[1:3])
#         first_dp = [0]*(n-1)
#         first_dp[0] = nums[0]
#         first_dp[1] = max(nums[:2])
        
#         for i in range(2, n-1):
#             first_dp[i] = max(dp[i-1], dp[i-2]+nums[i])

#         for i in range(3, n):
#             dp[i] = max(dp[i-1], dp[i-2]+nums[i])

#         return max(dp[-1], first_dp[-1])

# Longest Palindromic Substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIndex, resLen = 0, 0
        n = len(s)

        dp = [[False]*n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True

                    if resLen < j-i+1:
                        resIndex = i
                        resLen = j-i+1

        return s[resIndex: resIndex+resLen]

# Palindromic Substrings
class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        res = 0
        dp = [[True]*n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j-i <= 2 or dp[i-1][j-1] > 0):
                    dp[i][j] += True
                    res += 1

        return res
    
# Decode Ways
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        dp = [0] * (n+1)

        dp[0] =1

        dp[1] =1

        for i in range(2, n+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]

            two = int(s[i-2:i])
            if 10 <= two <= 26:
                dp[i] += dp[i-2]

        return dp[n]
    
# Coin Change
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         if amount == 0:
#             return 0

#         coins.sort()
#         INF = 10**9
#         n = len(coins)
#         dp = [[INF]*(amount+1) for _ in range(n+1)]

#         for i in range(n+1):
#             dp[i][0] = 0

#         for i in range(n+1):
#             for j in range(1, amount+1):
#                 dp[i][j] = dp[i-1][j]
#                 if j >= coins[i-1]:
#                     dp[i][j] = min(dp[i][j], dp[i][j-coins[i-1]]+1)

#         return dp[-1][-1] if dp[-1][-1] != INF else -1


# Invert Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    
# Maximum Depth of Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return None

        left_cnt = 1
        right_cnt = 1

        if self.maxDepth(root.left):
            cnt += self.maxDepth(root.left) 

        if self.maxDepth(root.right):
            cnt += self.maxDepth(root.right)

        return max(left_cnt, right_cnt)
    
# Diameter of Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            ans = max(ans, left+right)
            return 1+max(left, right)
        
        dfs(root)
        return ans
    
# Balanced Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def dfs(node):
            if not node: return 0
            length_r = dfs(node.right)
            length_l = dfs(node.left)
            if abs(length_r - length_r) > 1:
                return -1

            return max(length_l, length_r)+1

        ans = True if dfs(root) >= 0 else False
        return ans
    
# Same Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p and not q) or (not p and q):
            return False
        if not p and not q:
            return True
        
        if p.val == q.val:
            result = self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            result = False

        return result

# Subtree of Another Tree 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or
               self.isSubtree(root.right, subRoot))

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and
                   self.sameTree(root.right, subRoot.right))
        return False


# Maximum Product Subarray
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = nums[0]
        cur_min = nums[0]
        ans =[0]

        for i in range(1, len(nums)):
            x = nums[i]
            tmp_max = max(x, cur_max*x, cur_min*x)
            tmp_min = min(x, cur_max*x, cur_min*x)

            cur_max = tmp_max
            cur_min = tmp_min

            ans = max(ans, cur_max)

        return ans
    
# Word Break
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if (i+len(w)) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]
    
# Longest Increasing Subsequence
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

# Partition Equal Subset Sum
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) %2 != 0:
            return False
        
        def dnf(i, target):
            if i >= len(nums):
                return target == 0
            if target < 0:
                return False
            
            return dnf(i+1, target) or dnf(i+1, target-nums[i])
        
        return dnf(0, sum(nums)//2)
    
# Partition Equal Subset Sum
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)
        dp = [[False] * (target + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if nums[i - 1] <= j:
                    dp[i][j] = (dp[i - 1][j] or
                                dp[i - 1][j - nums[i - 1]])
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][target]
    
# Unique Paths
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*(n) for _ in range(m)]
        for i in range(n):
            dp[0][i] = 1
        for i in range(m):
            dp[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] += dp[i-1][j]+dp[i][j]

        return dp[-1][-1]

# Longest Common Subsequence
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0]*(m+1) for _ in range(n+1)]


        for i in range(1,n+1):
            for j in range(1, m+1):
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)

        return dp[-1][-1]
    
# Contains Duplicate
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numset = set()

        for i in nums:
            if i in numset:
                return True
            
            numset.add(i)

        return False
    
# Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s =sorted(s)
        t = sorted(t)

        for i in len(s):
            if s[i] != t[i]:
                return False
            
        return True
    
# Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsdict = {}

        for i, val in enumerate(nums):
            if target-val in numsdict:
                return [numsdict[target-val], i]
            
            numsdict[val] = i 

# Group Anagramss
class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        strsdict = defaultdict(list)
        ans = []

        for string in strs:
            str_sorted = str(sorted(string))
            strsdict[str_sorted].append(string)

        for str_list in strsdict.values():
            ans.append(str_list)

        return ans
    
# Top K Frequent Elements
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict

        numsdict = defaultdict(int)
        ans = []

        for num in nums:
            numsdict[num] += 1

        cnt = 0
        for num in sorted(numsdict, key=numsdict.get, reverse=True):
            if cnt >= k:
                return ans
            
            ans.append(num)
            cnt += 1

        return ans
    
#bucket
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]

        for num, freq in count.items():
            bucket[freq].append(num)

        res = []
        for i in range(len(bucket)-1, -1, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
                
# Encode and Decode Strings


# Products of Array Except Self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_products = [1]*n
        right_products = [1]*n
        sum =[0]*n

        for i in range(n-2, -1, -1):
            right_products[i] *= nums[i+1]*right_products[i+1]

        for i in range(1, n):
            left_products[i] *= nums[i-1]*left_products[i-1]

        for i in range(n):
            sum[i] = left_products[i]*right_products[i]

        return sum
    
# Valid Sudoku
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        pass

# Longest Consecutive Sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []: return 0
        numsset = set(nums)
        res = 1

        for n in numsset:
            if not n-1 in numsset:
                cnt = 1
                while n+1 in numsset:
                    cnt += 1
                    n += 1
                res = max(cnt, res)

        return res  

# Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = ''

        for i in s:
            if i.isalnum:
                chars += i.lower()

        for i in range(len(chars)//2):
            if chars[i] != chars[-1-i]:
                return False
            
        return True
    
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l < r:
            while  l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[l]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l+1, r+1
        return True
    
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))
    
    
# Two Integer Sum II
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while l < r:
            if target == numbers[l]+numbers[r]:
                return [l+1, r+1]

            if target > numbers[l]+numbers[r]:
                l += 1
            elif target < numbers[l]+numbers[r]:
                r -= 1

        return [-1, -1]
    
# 3Sum
# two pointerで動かすところはどっちか端で

# Container With Most Water
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1:
        ans = 0
        while l < r:
            ans = max(min(l, r)*(r-l), ans)
            if heights[r] <= heights[l]:
                r -= 1

            if heights[l] < heights[r]:
                l +=1

        return ans

# Trapping Rain Water
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l, r = 0, len(height)-1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])

# Min Stack
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

# Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        maxprofit = 0

        for price in prices:
            if not stack:
                stack.append(price)
                continue

            if stack[-1] > price:
                stack.append(price)
            else:
                maxprofit = max(maxprofit, price-stack[-1])

        return maxprofit
    
# Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_set = set()
        ans = 0

        for i in range(s):
            if s[i] in s_set:
                s_set.remove(s[i])
            s_set.add(s[i])
            ans = max(ans, len(s_set))

        return ans

# slide window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res
    
# Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        if s == "[]": return True
        
    
        stack = []
        s_dict = {')':'(', '}': '{', ']':'['}

        for i in range(len(s)):
            if stack and s[i] in s_dict and s_dict[s[i]] == stack[-1]:
                stack.pop()
                continue
            else:
                stack.append(s[i])

        return True if stack == [] else False
    
# Evaluate Reverse Polish Notation
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        pass

# Daily Temperatures
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*(len(temperatures))

        for i in range(len(temperatures), -1, -1):
            if stack:
                while stack[-1][0] < temperatures[i]:
                    stack.pop()
                    continue
                if stack:
                    j, temperature = stack[-1]
                    ans[i] = j-i+1
                stack.append((i, temperatures[i]))
            else:
                stack.append((i, temperatures[i]))

        return ans
    
# Car Fleet
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        car_stack = []
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars = sorted(cars)

        for i in range(len(position)-1, -1, -1):
            cnt = (target-cars[i][0])/cars[i][1]

            if car_stack and cnt <= car_stack[-1]:
                continue
            else:
                car_stack.append(cnt)

        return len(car_stack)

# Largest Rectangle In Histogram
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []

        leftMost = [-1]*n

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftMost[i] = stack[-1]
            stack.append(i)

        stack = []
        rightMost = [n]*n
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightMost[i] = stack[-1]
            stack.append(i)

        maxArea = 0
        for i in range(n):
            leftMost[i] += 1
            rightMost[i] -= 1
            maxArea = max(maxArea, heights[i]*(rightMost[i]-leftMost[i]+1))
        return maxArea

# Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid-1
            else:
                l = mid+1
        return -1
# めぐるしき
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = -1, len(nums)

        while r-l > 1:
            mid = (l+r)//2

            if nums[mid] >= target:
                r = mid
            else:
                l = mid
        
        return r if r < len(nums) and nums[r] == target else -1

# Search a 2D Matrix
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(len(matrix)):
            l, r = -1, len(matrix[0])

            while r-l > 1:
                mid = (l+r)//2

                if matrix[i][mid] >= target:
                    r = mid
                else:
                    l = mid
                if target == matrix[i][mid]:
                    return True
        return False
    
# Koko Eating Bananas
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 0, max(piles)

        while r-l > 1:
            mid = (l+r)//2
            cnt = 0
            for p in piles:
                # math.cell使えばこれできそう関数で１行に
                if p%mid == 0:
                    cnt += p//mid  
                else:
                    cnt += p//mid+1
                
            if cnt <= h:
                r = mid
            else:
                l = mid

        return r
    
# Find Minimum in Rotated Sorted Array
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while r >= l:
            mid = (l+r)//2

            if nums[r] > nums[mid]:
                r = mid
            else:
                l = mid+1

        return nums[r]
    
# Search in Rotated Sorted Array
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r) // 2

            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid +1
                else:
                    r = mid-1

        return -1


# Time Based Key-Value Store
# use binary search for search-number
from collections import defaultdict
class TimeMap:
    
    def __init__(self):
        self.timedict = defaultdict(list)
        self.datadict = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timedict[key].append(timestamp)
        self.datadict[(key, timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        if self.timedict[key]:
            if self.datadict.get((key, timestamp)):
                return self.datadict[(key, timestamp)]
            else:
                l, r = -1, len(self.timedict[key])

                while r - l > 1:
                    mid = (r+l)//2
                    if self.timedict[key][mid] <= timestamp:
                        l = mid
                    else:
                        r = mid
                time = self.timedict[key][l]
                return self.datadict[(key, time)] if l > -1 else ""
            
            
# Median of Two Sorted Arrays
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pass

# Longest Repeating Character Replacement
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)

        for c in charSet:
            count = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1
                
                while (r -l +1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1

                res = max(res, r -l+1)
        return res
    
# Permutation in String
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count1 = Counter(s1)
        window = Counter()

        l = 0

        for r in range(len(s2)):
            window[s2[r]] += 1

            if r -l +1 > len(s1):
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    del window[s2[l]]
                l += 1

            if window == count1:
                return True
            
        return False
    
# Kth Largest Element in a Stream
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]
        
# Last Stone Weight
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        hp = [-s for s in stones]
        heapq.heapify(hp)

        while len(hp) > 1:
            hp1 = heapq.heappop(hp)
            hp2 = heapq.heappop(hp)

            smashed = abs(hp1-hp2)
            heapq.heappush(hp, -smashed) if smashed != 0 else None

        return 0 if not hp else hp[0]
    
# Maximum Subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            cur = max(nums[i], nums[i]+cur)
            ans = max(cur, ans)

        return ans

# Subsets
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        tmp = []
        def dfs(i):
            if i >= len(nums):
                ans.append(tmp[:])

            dfs(i+1)
            tmp.append(nums[i])
            dfs(i+1)
            tmp.pop()

        
        dfs(0)
        return ans
    
# Combination Sum
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        tmp = []

        def dfs(i):
            if len(nums) == i and sum(tmp) == target:
                ans.append(tmp[:])

            dfs(i+1)
            tmp.append(nums[i])
            dfs(i+1)
            tmp.pop()

        dfs(0)
        return ans
    
# Combination Sum II
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        tmp = []
        candidates.sort()

        def dfs(i):
            if i >= len(candidates) or target <= sum(tmp):
                if target == sum(tmp):
                    ans.append(tmp[:])
                return
            nxt = i+1
            while nxt < len(candidates) and candidates[nxt] == candidates[i]:
                nxt += 1
            tmp.append(candidates[i])
            dfs(i+1)

            tmp.pop()
            dfs(nxt)

        dfs(0)
        return ans
    

# bfsはqueueを使う
# Permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        tmp = []

        def dfs(i):
            if i >= len(nums):
                ans.append(tmp[:])
                return 

            for n in nums:
                if n in tmp:
                    continue
                tmp.append(n)
                dfs(i+1)
                tmp.pop()

        dfs(0)
        return ans

# Subsets II
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        tmp = []
        nums.sort()

        def dfs(i):
            if i >= len(nums):
                res.append(tmp[:])
                return
            nxt = i+1
            while nxt < len(nums) and nums[nxt] == nums[i]:
                nxt += 1

            dfs(i+1)
            tmp.append(nums[i])
            dfs(nxt)
            tmp.pop()

        dfs(0)
        return res
    
# dfs( s+1)はimmutable
# Generate Parentheses
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(open, close, s):
            if open < close:
                return
            if len(s) > n*2 or open > n or close > n:
                return
            if len(s) == n*2:
                ans.append(s[:])
                return
            
            dfs(open+1, close, s+'(')
            dfs(open, close+1, s+')')

        dfs(0, 0, '')
        return ans

    
# Word Search
# visitedで訪問済みマス管理
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        diff = ((1, 0), (-1, 0), (0, 1), (0, -1))
        visited = set()
        def dfs(i, j, index):
            if index >= len(word):
                return True

            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or not board[i][j] == word[index] or (i, j) in visited:
                return False
            
            for dy, dx in diff:
                flag = dfs(i+dy, j+dx, index+1)
                if flag == True:
                    return True
            visited.remove((i, j))
                
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):

                f = dfs(i, j, 0)
                if f == True:
                    return True
        return False
        
# Palindrome Partitioning
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        tmp = []

        def is_palindrome(text):
            return text == text[::-1]
        
        def dfs(start):
            if start == len(s):
                ans.append(tmp[:])
                return
            
            for end in range(start+1, len(s)+1):
                part = s[start:end]

                if is_palindrome(part):
                    tmp.append(part)
                    dfs(end)
                    tmp.pop()

        dfs(0)
        return ans
    
# Letter Combinations of a Phone Number
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits = list(digits)
        ans = []
        tmp = []
        digits_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        def dfs(i):
            if i >= len(digits):
                ans.append("".join(tmp[:]))
                return
            
            for d in digits_dict[digits[i]]:
                tmp.append(d)
                dfs(i+1)
                tmp.pop()

        dfs(0)
        return ans

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [["."] * n for _ in range(n)]

        cols = set()
        diag1 = set()  # row - col
        diag2 = set()  # row + col

        def dfs(row):
            if row == n:
                ans.append(["".join(r) for r in board])
                return

            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                board[row][col] = "Q"
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                dfs(row + 1)

                board[row][col] = "."
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        dfs(0)
        return ans

# Number of Islands
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        diff = ((1, 0), (-1, 0), (0, 1), (0, -1))
        cnt = 0

        def dfs(i, j):    
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or (i, j) in visited or grid[i][j] == '0':
                return False
            visited.add((i, j))
            for dy, dx in diff:
                y = i+dy
                x = j+dx
                dfs(y, x)
            return True

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                f = dfs(i, j)
                if f == True:
                    cnt += 1

        return cnt
    
# Max Area of Island
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxisland = 0
        diff = ((1, 0), (-1, 0), (0, 1,), (0, -1))
        def dfs(i, j):
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[0] or grid[i][j] == 0):
                return 0
            cnt = 1
            for dy, dx in diff:
                y = dy+i
                x = dx+j
                cnt += dfs(y, x)

            return cnt
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans = dfs(i, j)
                maxisland = max(maxisland, ans)

        return maxisland
    
# Clone Graph
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        old_to_new = {}

        def dfs(n):
            if n in old_to_new:
                return old_to_new[n]
            copy = Node(n.val)
            old_to_new[n] = copy

            for nei in n.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node)
    
# Islands and Treasure
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        q = deque()
        visited = set()
        diff = ((1, 0), (-1, 0), (0, 1,), (0, -1))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j, 0))
                    visited.add((i, j))

        while q:
            i, j, cnt = q.popleft()
            for dy, dx in diff:
                y = dy+i
                x = dx+j
                if 0 <= y < len(grid) and 0 <= x < len(grid[0]) and (y, x) not in visited and not grid[y][x] == -1:
                    q.append((y, x, cnt+1))
                    grid[y][x] = cnt+1
                    visited.add((y, x))

# Rotting Fruit
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        diff = ((1, 0), (-1, 0), (0, 1), (0, -1))

        anscnt = 0
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append(i, j, 0)

        while q:
            i, j, cnt = q.pop()
            anscnt = max(anscnt, cnt)

            for dy, dx in diff:
                y = dy+i
                x = dx+j
                if not 0 <= y < len(grid) or not 0 <= x < len(grid[0]) or not grid[y][x] == 1:
                    continue
                
                q.append((i, j, cnt+1))
                grid[i][j] = 2
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == 1:
                    return -1
                
        return anscnt
                
# Pacific Atlantic Water Flow
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        diff = ((1, 0), (-1, 0), (0, 1), (0, -1))
        pacificset = set()
        atlanticset = set()

        def dfs(i, j, seaname):
            if not 0 <= i < len(heights) or not 0 <= j < len(heights[0]):
                return
            if (seaname == 'pacific' and (i, j) in pacificset) or (seaname == 'atlantic' and (i, j) in atlanticset):
                return
            elif seaname == 'pacific':
                pacificset.add((i, j))
            elif seaname == 'atlantic':
                atlanticset.add((i, j))

            for dy, dx in diff:
                y = dy+i
                x = dx+j
                if (not 0 <= i < len(heights) or not 0 <= j < len(heights[0])) and heights[y][x] >= heights[i][j]:
                    dfs(y, x, seaname)


        for i in range(len(heights)):
            dfs(i, 0, 'pacific')
            dfs(i, len(heights[0])-1, 'atlantic')

        for j in range(len(heights[0])):
            dfs(0, j, 'pacific')
            dfs(len(heights)-1, j, 'atlantic')

        ans = pacificset & atlanticset

        ans = [ a for a in ans]

        return ans
    
# Surrounded Regions
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        diff = ((1, 0), (-1, 0), (0, 1), (0, -1))
        visited = set()
        targetisland = set()

        def dfs(i, j):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != 'O' or (i, j) in visited:
                return True
            
            visited.add((i, j))
            targetisland.add((i, j))

            surrounded = not (
                i == 0 or i == len(board) - 1 or
                j == 0 or j == len(board[0]) - 1
            )

            for dy, dx in diff:
                y = dy + i
                x = dx + j
                flag = dfs(y, x)
                if flag == False:
                    surrounded = False

            return surrounded

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i, j) not in visited:
                    f = dfs(i, j)
                    if f == True:
                        for y, x in targetisland:
                            board[y][x] = 'X'
                    targetisland.clear()


# Course Schedule
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}

        for a, b in prerequisites:
            graph[b].append(a)

        visiting = set()
        visited = set()

        def dfs(node):
            if node in visiting:
                return False
            
            if node in visited:
                return True
            
            visiting.add(node)

            for nei in graph[node]:
                if not dfs(nei):
                    return False
                
            visiting.remove(node)
            visited.add(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
            
        return True
    
# Course Schedule II
# トポロジカルソート　これ重要らしい
# Iの拡張
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}

        for a, b in prerequisites:
            graph[b].append(a)

        visiting = set()
        visited = set()
        res = []

        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True
            
            visiting.add(node)

            for nei in graph[node]:
                if not dfs(nei):
                    return False
            visiting.remove(node)
            visited.add(node)
            res.append(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
            
        return res[::-1]

# BFS / indegree
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        res = []

        while q:
            node = q.popleft()
            res.append(node)

            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if len(res) == numCourses:
            return res
        else:
            return []
        
# Graph Valid Tree
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        pass

# Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        minp = 1000000
        for p in prices:
            if p < minp:
                minp = p

            maxprofit = max(maxprofit, p-minp)

        return maxprofit
    
# Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlenght = 0
        charset = set()
        deli = 0

        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[deli])
                deli += 1

            charset.add(s[r])
            maxlenght = max(maxlenght, len(charset))

        return maxlenght

# Longest Repeating Character Replacement
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charset = set(list(s))
        maxlenght = 0

        for c in charset:
            i = 0
            l = 0
            others = 0
            while i < len(s):
                if c != s[i]:
                    others += 1
                
                while others > k:
                    if s[l] != c:
                        others -= 1
                    l += 1

                maxlenght = max(maxlenght, i-l+1)
                i += 1
        return maxlenght
    
# Permutation in String
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1counter = Counter(s1)
        window = Counter()

        l = 0
        for r in range(len(s2)):
            window[s2[r]] += 1
            while s1counter[s2[r]] < window[s2[r]]:
                window[s2[l]] -= 1
                l += 1

            if s1counter == window:
                return True
            
        return False
    
# Minimum Window Substring
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = Counter()
        l = 0

        def contains():
            for c in need:
                if window[c] < need[c]:
                    return False
            return True
        
        ans = ''

        for r in range(len(s)):
            window[s[r]] += 1

            while contains():
                cur = s[l:r+1]
                if ans == '' or len(cur) < len(ans):
                    ans = cur

                window[s[l]] -= 1
                l += 1
        return ans
    
# Sliding Window Maximum
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r+1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output
    
# Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = -1, len(nums)

        while r - l > 1:
            mid = (r+l)//2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid

        return r if nums[r] == target else -1
    
# Search a 2D Matrix
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ng, ok = -1, len(matrix[0])

        for i in range(len(matrix)):
            while ok - ng > 1:
                mid = (ng+ok)//2

                if matrix[i][mid] >= target:
                    ok = mid
                else:
                    ng = mid
            if matrix[i][ok] == target:
                return True
            
        return False

# Koko Eating Bananas
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ng, ok = -1, max(piles)
        import math

        while ok-ng > 1:
            mid = (ok+ng)//2

            cnt = 0
            for p in piles:
                cnt += math.ceil(p/mid)

            if mid >= cnt:
                ok = mid
            else:
                ng = mid

        return ok
    
# Find Minimum in Rotated Sorted Array
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while r > l:
            mid = (r+l)//2

            if nums[mid] > nums[r]:
                l = mid
            else:
                r = mid-1

        return nums[r]

# Search in Rotated Sorted Array
# index系は r>=lでやる, 値を見つけたい時はこれ
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while r >= l:
            mid = (r+l)//2
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid+1
                else:
                    r = mid-1

        return -1

# Time Based Key-Value Store
class TimeMap:
    from collections import defaultdict

    def __init__(self):
        self.timedict = defaultdict(list)
        self.timeworddict = defaultdict(str)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timedict[key].append(timestamp)
        self.timeworddict[(key, timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        l, r = -1, len(self.timedict[key])

        while r-l > 1:
            mid = (r+l)//2
            if self.timedict[key][mid] <= timestamp:
                l = mid
            else:
                r = mid
        if l == -1:
            return ''

        return self.timeworddict[(key, self.timedict[key][l])]


# Median of Two Sorted Arrays
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def get_kth(a, b, k):
            i = 0
            j = 0

            while True:
                if i == len(a):
                    return b[j+k-1]
                if j == len(b):
                    return a[i+k-1]
                if k == 1:
                    return min(a[i], b[j])
                
                half = k//2

                new_i = min(i+half, len(a))-1
                new_j = min(j+half, len(b))-1
                if a[new_i] <= b[new_j]:
                    k -= new_i-i+1
                    i = new_i+1
                else:
                    k -= new_j-j+1
                    j = new_j+1

        total = len(nums1)+len(nums2)
        left = (total+1)//2
        right = (total+2)//2
        return (get_kth(nums1, nums2, left)+get_kth(nums1, nums2, right))/2

# Single Number
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        for n in nums:
            ans ^= n

        return ans
    
# Number of 1 Bits
class Solution:
    def hammingWeight(self, n: int) -> int:
        
        ans = 0

        for i in range(32):
            if n >> i & 1:
                ans += 1

        return ans
    
# Counting Bits
class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0]*(n+1)

        for i in range(1, n+1):
            for mask in range(32):
                if i >> mask & 1:
                    output[i] += 1

        return output
    
# Reverse Bits
class Solution:
    def reverseBits(self, n: int) -> int:
        
        ans = 0

        for i in range(32):
            if n >> i & 1:
                ans += 2**(32-i-1)

        return ans
    
# Missing Number
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            ans ^= n

        for n in range(1, len(nums)+1):
            ans ^= n

        return ans
    
class Solution:
    def getSum(self, a: int, b: int) -> int:
        ans = 0
        carry = 0

        for i in range(32):
            af = 1 if (a >> i) & 1 else 0
            bf = 1 if (b >> i) & 1 else 0

            bit = af ^ bf ^ carry
            carry = 1 if (af & bf) or (af & carry) or (bf & carry) else 0

            ans += 2 ** i if bit == 1 else 0

        # 32bit符号付き整数に変換
        if ans >= 2 ** 31:
            ans -= 2 ** 32

        return ans
    
# Reverse Integer
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x:
            digit = x % 10
            x //= 10

            # オーバーフローチェック
            if res > (2**31 - 1) // 10:
                return 0
            if res == (2**31 - 1) // 10 and digit > 7:
                return 0

            res = res * 10 + digit

        return sign * res
    
# Graph Valid Tree
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node, parent):
            visited.add(node)

            for nei in graph[node]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                if not dfs(nei, node):
                    return False
            return True
        
        if not dfs(0, -1):
            return False
        return len(visited) == n
    
# Number of Connected Components in an Undirected Graph
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graphdict = defaultdict(list)
        graph = [False]*n

        for a, b in edges:
            graphdict[a].append(b)
            graphdict[b].append(a)


        def dfs(i):
            if i >= n or graph[i] == True:
                return
            
            graph[i] = True
            for a in graphdict[i]:
                dfs(a)


        for i in range(n):
            if graph[i] == True:
                continue
            else:
                dfs(i)
                cnt += 1

        return cnt

# Redundant Connection
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return False
            
            parent[rootB] = rootA
            return True
        
        for a, b in edges:
            if not union(a, b):
                return [a, b]

# Word Ladder
from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        q = deque([(beginWord, 1)])
        visited = set([beginWord])

        while q:
            word, dist = q.popleft()

            if word == endWord:
                return dist

            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    nxt = word[:i] + ch + word[i+1:]

                    if nxt in wordSet and nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, dist + 1))

        return 0

# Climbing Stairs
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1]+dp[i-2]

        return dp[-1]
    
# Min Cost Climbing Stairs
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]*(len(cost)+1)

        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])

        return dp[-1]

# House Robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*len(nums)

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])

        return dp[-1]
        
# House Robber II
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        if n == 3:
            return max(nums[0]+nums[2], nums[1])
        dp1 = [0]*(len(nums))
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])
        dp2 = [0]*(len(nums))
        dp2[1] = nums[1]
        dp2[2] = nums[2]


        for i in range(2, len(nums)-1):
            dp1[i] = max(dp1[i-1], dp1[i-2]+nums[i])

        for i in range(3, len(nums)):
            dp2[i] = max(dp2[i-1], dp2[i-2]+nums[i])

        return max(dp1[-1], dp2[-1])

# Longest Palindromic Substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [1]*len(s)

        for c in range(len(s)):
            now1 = 1
            now2 = 0
            l = c-1
            r = c+1
            while l <= 0 and r < len(s) and s[l] == s[r]:
                now1 += now1+2
                l -= 1
                r += 1

            l = c
            r = c+1
            while l <= 0 and r < len(s) and s[l] == s[r]:
                now2 += now2+2
                l -= 1
                r += 1

            dp[c] = max(now1, now2)

