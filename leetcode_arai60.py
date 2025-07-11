#Linked List Cycle　これでも行けるが最適ではないらしい
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         visited_nodes = set()
#         current_node = head
#         while current_node:
#             if current_node in visited_nodes:
#                 return True
#             visited_nodes.add(current_node)
#             current_node = current_node.next
#         return False

#Linked List Cycle II これでも行けるが最適ではないらしい
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         visited_nodes = set()
#         current_node = head
#         while current_node:
#             if current_node in visited_nodes:
#                 return current_node
#             visited_nodes.add(current_node)
#             current_node = current_node.next
#         return None
    
#Linked List Cycle
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         fast = head
#         slow = head
#         while fast and fast.next:
#             fast = fast.next.next
#             slow = slow.next

#             if fast == slow:
#                 return True
#         return False

#Linked List Cycle II
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         slow = head
#         fast =head

#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next

#             if slow == fast:
#                 break
#         else: return None

#         fast = head
#         while fast != slow:
#             fast = fast.next
#             slow = slow.next

#         return slow


#Remove Duplicates from Sorted List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         res = head

#         while head and head.next:
#             if head.val == head.next.val:
#                 head.next = head.next.next
#             else:
#                 head = head.next

#         return res

#Remove Duplicates from Sorted List II
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

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
    
     
#Add Two Numbers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode()
#         res = dummy 

#         total = carry = 0

#         while l1 or l2 or carry:
#             total = carry
            
#             if l1:
#                 total += l1.val
#                 l1 = l1.next
#             if l2:
#                 total += l2.val
#                 l2 = l2.next

#             num = total % 10
#             carry = total // 10

#             dummy.next = ListNode(num)
#             dummy = dummy.next
#         return res.next
    

#Valid Parentheses
# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         mapping = {")":"(", "}":"{", "]": "["}

#         for char in s:
#             if char in mapping.values():
#                 stack.append(char)
#             elif char in mapping.keys():
#                 if not stack or mapping[char] != stack.pop():
#                     return False
                
#         return not stack
    
#Reverse Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         node = None
#         while head:
#             temp = head.next
#             head.next = node
#             node = head
#             head = temp

#         return node

#Kth Largest Element in a Stream
# import heapq
# class KthLargest(object):
#     def __init__(self, k, nums):
#         self.k = k
#         self.heap = []
#         for num in nums:
#             self.add(num)

#     def add(self, val):
#         if len(self.heap) < self.k:
#             heapq.heappush(self.heap, val)
#         elif val > self.heap[0]:
#             heapq.heapreplace(self.heap, val)
#         return self.heap[0]

#Top K Frequent Elements
# import heapq
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         counter = {}
#         heap = []

#         for n in nums:
#             counter[n] = 1+counter.get(n, 0)

#         for key, val in counter.items():
#             heapq.heappush(heap, (-val, key))

#         res = []
#         while len(res) < k:
#             res.append(heapq.heappop(heap)[1])
        
#         return res

#Find K Pairs with Smallest Sums
# import heapq

# class Solution(object):
#     def kSmallestPairs(self, nums1, nums2, k):
#         if not nums1 or not nums2:
#             return []
        
#         h = []
#         visited = set()
#         result = []

#         heapq.heappush(h, (nums1[0]+nums2[0], 0, 0))
#         visited.add((0,0))

#         while h and len(result) < k:
#             s, i, j = heapq.heappop(h)
#             result.append([nums1[i], nums2[j]])

#             if j + 1 < len(nums2) and (i, j+1) not in visited:
#                 visited.add((i, j+1))
#                 heapq.heappush(h, (nums1[i] + nums2[j+1], i, j+1))

#             if i+1 < len(nums1) and (i + 1, j) not in visited:
#                 visited.add((i+1, j))
#                 heapq.heappush(h, (nums1[i+1]+nums2[j], i+1, j))

#         return result


# class Sotuliton:
#     def kSmallestPairs(self, nums1, nums2, k):
#         from heapq import heappush, heappop
#         m = len(nums1)
#         n = len(nums2)

#         ans = []
#         visited = set()

#         miniHeap = [(nums1[0]+ nums2[0], (0, 0))]
#         visited.add((0, 0))
#         count = 0

#         while k > 0 and miniHeap:
#             val, (i, j) = heappop(miniHeap)
#             ans.append([nums1[i], nums2[j]])

#             if i+1 < m and (i+1, j) not in visited:
#                 heappush(miniHeap, (nums1[i+1]+nums2[j], (i+1, j)))
#                 visited((i+1, j))
            
#             if j +1 < n and (i, j+1) not in visited:
#                 heappush(miniHeap, (nums1[i]+nums2[j+1], (i, j+1)))
#                 visited.add((i, j+1))
#             k = k-1

#         return ans

#Two Sum
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hashmap = {}
#         for i in range(len(nums)):
#             hashmap[nums[i]] = i
#         for i in range(len(nums)):
#             complement = target - nums[i]
#             if complement in hashmap and hashmap[complement] != i:
#                 return [i, hashmap[complement]]
#         return []

#Group Anagrams
# from collections import defaultdict

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         groups = defaultdict(list)
#         for str in strs:
#             groups[tuple(sorted(str))].append(str)
#         return list(groups.values())


#Intersection of Two Arrays
# class Solution(object):
#     def intersection(self, num1, num2):
#         num1.sort()
#         num2.sort()

#         N = len(num1)
#         M = len(num2)
#         p1 = 0
#         p2 = 0

#         intersection = set()

#         while p1 < N and p2 < M:
#             if num1[p1] == num2[p2]:
#                 intersection.add(num1[p1])
#                 p1 += 1
#                 p2 += 1
#             elif num1[p1] < num2[p2]:
#                 p1 += 1
#             else:
#                 p2 += 1

#         result = []
#         for x in intersection:
#             result.append(x)

#         return result


# class Solution(object):
#     def intersection(self, num1, num2):
#         num1 = set(num1)
#         num2 = set(num2)
#         ans = list()

#         for n1 in num1:
#             if n1 in num2:
#                 ans.append(n1)

#         return list(ans)
        
#Unique Email Addresses
#自作　きもい
# class Solution:
#     def numUniqueEmails(self, emails: List[str]) -> int:
#         unq = set()
#         for email in emails:
#             length = len(email)
#             i = 0
#             localflag = True
#             address = ""
#             while i < length:
#                 if email[i] == '@':
#                     localflag =False
#                     address += email[i]
#                     i += 1
#                 elif localflag:
#                     if email[i] == "+":
#                         while not email[i+1] == '@':
#                             i += 1
#                         i += 1
#                     elif email[i] == ".":
#                         i += 1
#                     else:
#                         address += email[i]
#                         i += 1
#                 elif not localflag:
#                     address += email[i]
#                     i += 1
#             unq.add(address)
#         return len(unq)

# class Solution:
#     def numUniqueEmails(self, emails: List[str]) -> int:
#         unique_emails = set()

#         def canonicalize(before):
#             after = []
#             is_domain_part =False
#             ignore_rest_local_part = False
#             for c in before:
#                 if is_domain_part:
#                     after.append(c)
#                     continue
#                 if c== "@":
#                     after.append(c)
#                     is_domain_part =True
#                     ignore_rest_local_part = False
#                     continue
#                 if c == "." or ignore_rest_local_part:
#                     continue
#                 if c == "+":
#                     ignore_rest_local_part = True
#                     continue
#                 after.append(c)
#             return "".join(after)
        
#         for email in emails:
#             unique_emails.add(canonicalize(email))
#         return len(unique_emails)

#First Unique Character in a String
# from collections import defaultdict

# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         s_dict = defaultdict(int)
#         for c in s:
#             s_dict[c] += 1

#         for i, c in enumerate(s):
#             if s_dict[c] == 1:
#                 return i
        
#         return -1

#Subarray Sum Equals K
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         sub_num = {0:1}
#         total = count = 0

#         for n in nums:
#             total += n

#             if total - k in sub_num:
#                 count += sub_num[total-k]

#             sub_num[total] = 1 + sub_num.get(total, 0)

#         return count

#Number of Islands 
#DFS
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         def mark_as_visited(row: int, col: int) -> None:
#             if not (0 <= row < m and 0 <= col < n):
#                 return
#             if grid[row][col] == '0':
#                 return
#             grid[row][col] = "0"
#             dirs = [(1,0), (-1, 0), (0, 1), (0,-1)]
#             for dr, dc in dirs:
#                 mark_as_visited(row+dr, col+dc)

#         m, n = len(grid), len(grid[0])
#         num_of_islands = 0
#         for row in range(m):
#             for col in range(n):
#                 if grid[row][col] == "1":
#                     num_of_islands += 1
#                     mark_as_visited(row, col)
#         return num_of_islands

#BFS
# from collections import deque
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         islands = 0
#         visited = set()
#         rows, cols = len(grid), len(grid[0])

#         def bfs(r, c):
#             q = deque()
#             visited.add((r, c))
#             q.append((r, c))
            
#             while q:
#                 row, col = q.popleft()
#                 directions = [[1, 0], [-1, 0], [0,1], [0,-1]]

#                 for dr, dc in directions:
#                     r,c = row+dr, col+dc
#                     if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1" and [r, c] not in visited:
#                         q.append((r, c))
#                         visited.app((r, c))



#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == "1" and (r, c) not in visited:
#                     islands += 1
#                     bfs(r, c)

#         return islands
