# #Linked List Cycle
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         head_1 = head
#         head_2 = head

#         while head_1.next and head_2.next.next:
#             head_1 = head_1.next
#             head_2 = head_2.next.next

#             if head_1 == head_2:
#                 return True
            
# #Linked List Cycle II
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         fast = head
#         slow = head

#         point
#         while fast and fast.next:
#             fast = fast.next.next
#             slow = slow.next

#             if fast == slow:
#                 break
#         else:
#             return None
        
#         fast = head
#         while fast != slow:
#             fast = fast.next
#             slow = slow.next

#         return fast
    
# #Remove Duplicates from Sorted List
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head:
#             return None
        
#         p_1 = head.next
#         p_2 = head

#         while p_1:
#             if head.val == p_1.val:
#                 p_1 = p_1.next
#                 head.next = None
#                 continue
#             else:
#                 head.next = p_1
#                 head = head.next
#                 p_1 = p_1.next            

#         return p_2
    
# # Remove Duplicates from Sorted List II
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next:
#             return head
        
#         dummy = ListNode(0, head)
#         prev = dummy
#         current = head

#         while current:
#             is_duplicate = False

#             while current.next and current.val == current.next.val:
#                 is_duplicate = True

#                 current = current.next

#             if is_duplicate:
#                 prev.next = current.next
#             else:
#                 prev = prev.next

#             current = current.next

#         return dummy.next

# #Add Two Numbers
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
#         dummy = ListNode()
#         ans = dummy
#         carry = 0

#         while l1 or l2 or carry:
#             total = carry
#             if l1:
#                 total += l1.val
#                 l1 = l1.next
#             if l2:
#                 total += l2.val
#                 l2 = l2.next

#             carry = total // 10
#             total %= 10

#             ans.next = ListNode(total)
#             ans = ans.next

#         return dummy.next
    
# #Valid Parentheses
# from collections import deque
# class Solution:
#     def isValid(self, s: str) -> bool:
#         q = deque()

#         for i in range(len(s)):

#             if s[i] == "(" or s[i] == "[" or s[i] == "{":
#                 q.append(s[i])
#                 continue
            
#             if not q:
#                 return False
#             if s[i] == ")":
#                 a=  q.pop()
#                 if a == "(":
#                     continue
#                 else:
#                     return False
#             if s[i] == "]":
#                 a = q.pop()
#                 if a == "[":
#                     continue
#                 else:
#                     return False
#             if s[i] == "}":
#                 a = q.pop()
#                 if a == "{":
#                     continue
#                 else:
#                     return False
#         return len(q) == 0

# class Solution:
#     def isValid(self, s:str) -> bool:
#         stack = []
#         mapping = {"}":"{", "]":"[", ")":"("}

#         for char in s:
#             if char in mapping.values:
#                 stack.append(char)
#             elif char in mapping.keys():
#                 if not stack or mapping[char] != stack.pop():
#                     return False
            
#         return not stack

# #Reverse Linked List
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# from collections import deque
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head:
#             return None
#         q = deque()

#         while head:
#             q.append(head.val)
#             head = head.next
        
#         dummy = ListNode()
#         prev = dummy
#         while q:
#             new_head = ListNode(q.pop())

#             prev.next = new_head
#             prev = prev.next

#         return dummy.next
    
# class Solution:
#     def reverseList(self, head):
#         node = None

#         while head:
#             temp = head.next
#             head.next = node
#             node = head
#             head = temp

#         return node
    

# #Kth Largest Element in a Stream
# import heapq
# class KthLargest:

#     def __init__(self, k: int, nums: List[int]):
#         self.k = k
#         self.heap = []
#         for n in nums:
#             self.add(n)

#     def add(self, val: int) -> int:
#         if len(self.heap) < self.k:
#             heapq.heappush(self.heap, val)
#         elif val > self.heap[0]:
#             heapq.heapreplace(self.heap, val)
#         return self.heap[0]

# # Your KthLargest object will be instantiated and called as such:
# # obj = KthLargest(k, nums)
# # param_1 = obj.add(val)

# #Top K Frequent Elements
# from collections import defaultdict
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         d = defaultdict(int)
#         heap = []
#         for i in range(len(nums)):
#             d[nums[i]] -= 1

#         for key, val in d.items():
#             heapq.heappush(heap, (val, key))

#         ans = []
#         for i in range(k):
#             ans.append(heapq.heappop(heap)[1])

#         return ans

# #Find K Pairs with Smallest Sums
# # これやとTLEになりますのでご注意
# class Solution:
#     def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
#         heap = []
#         for i in range(len(nums1)):
#             for j in range(len(nums2)):
#                 if len(heap) < k:
#                     heapq.heappush(heap, [-(nums1[i]+nums2[j]), nums1[i],nums2[j]])
#                 elif -heap[0][0] > nums1[i]+nums2[j]:
#                     heapq.heapreplace(heap, [-(nums1[i]+nums2[j]), nums1[i], nums2[j]])
#         result = []
#         for i in heap:
#             result.append(i[1], i[2])

#         return result
    
# #Find K Pairs with Smallest Sums
# class Solution:
#     def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
#         if not nums1 or not nums2:
#             return []
        
#         h = []
#         visited = set()
#         result = []

#         heapq.heappush(h, (nums1[0]+nums2[0], 0, 0))
#         visited.add((0, 0))

#         while h and len(result) < k:
#             s, i, j = heapq.heappop(h)
#             result.append([nums1[i], nums2[j]])

#             if j + 1< len(nums2) and (i, j+1) not in visited:
#                 visited.add((i, j+1))
#                 heapq.heappush(h, (nums1[i]+nums2[j+1], i, j+1))

#             if i+1 <len(nums1) and (i+1, j) not in visited:
#                 visited.add((i+1, j))
#                 heapq.heappush(h, (nums1[i+1] + nums2[j], i+1,j))

#         return result
    
# #Two Sum
# # class Solution:
# #     def twoSum(self, nums: List[int], target: int) -> List[int]:
# #         l = len(nums)
# #         for i in range(l-1):
# #             for j in range(i, l):
# #                 if nums[i]+nums[j] == target:
# #                     return list[i, j]

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         pair_idx = {}
#         for i, num in  enumerate(nums):
#             if target - num in pair_idx:
#                 return [i, pair_idx[target-num]]
#             pair_idx[num] = i


# #Group Anagrams
# from collections import defaultdict

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         ans = defaultdict(list)

#         for s in strs:
#             key = "".join(sorted(s))
#             ans[key].append(s)
            
#         return list(ans.values())
    

# #Intersection of Two Arrays
# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         if not nums1 or not nums2:
#             return []
        
#         n_1 = defaultdict(False)
#         for n in nums1:
#             n_1[n] = True
#         ans = set()
#         for n in nums2:
#             if n in n_1:
#                 ans.add(n)

#         return list(ans)
    

# #Unique Email Addresses
# class Solution:
#     def numUniqueEmails(self, emails: List[str]) -> int:
#         seen = set()

#         for email in emails:
#             name, domain = email.split('@')
#             local = name.split('+')[0].replace('.', '')
#             email = local+'@'+domain
#             seen.add(email)
#         return len(seen)
    
# #First Unique Character in a String
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         seen = defaultdict(int)

#         for i in s:
#             seen[i] += 1

#         for i, i_s in enumerate(s):
#             if seen[i_s] == 1:
#                 return i
            
#         return -1
    
# class Solution:
#     def firstUniqChar(self, s:str) -> int:
#         freq = {}

#         for c in s:
#             freq[c] = 1+freq.get(c, 0)

#         for i, c in enumerate(s):
#             if freq[c] == 1:
#                 return i
            
#         return -1
    
# #Subarray Sum Equals K
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         sub_num = {0:1}
#         total = count = 0

#         for n in nums:
#             total += n

#             if total - k in sub_num:
#                 count += sub_num[total-k]

#             sub_num[total] = 1+sub_num.get(total, 0)

#         return count
    

# # Number of Islands
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid:
#             return 0
#         ans = 0
#         m, n = len(grid), len(grid[0])
#         def dfs(i, j):
#             grid[i][j] = "0"

#             d = ((1,0), (-1,0), (0, 1), (0, -1))

#             for di, dj in d:
#                 if 0 <= i+di < m and 0 <= j+dj < n and grid[i+di][j+dj] == "1":
#                     dfs(i+di, j+dj)

#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == "1":
#                     dfs(i, j)
#                     ans += 1
#         return ans
    
# # Max Area of Island
# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         if not grid:
#             return 0
#         m, n = len(grid), len(grid[0])
#         ans = 0

#         def cnt_island(i, j, cnt):
#             cnt += 1
#             grid[i][j] = 0
#             d = ((1,0), (-1,0), (0,1), (0,-1))
#             for dy, dx in d:
#                 if 0 <= i+dy < m and 0 <= j+dx < n and grid[i+dy][j+dx] == 1:
#                     cnt = cnt_island(i+dy, j+dx, cnt)
#             return cnt


#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == 1:
#                     num = cnt_island(i, j, 0)
#                     ans = max(ans, num)

#         return ans
    
# # Word Ladder
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        q = deque()
        q.append((beginWord, 1))

        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps
            
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    temp = i[:i] + ch + i[i+1:]
                    if temp in wordSet:
                        wordSet.remove(temp)
                        q.append((temp. steps+1))

        return 0
    