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

#Max Area of Island
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def mark_as_visited(row, col):
            nonlocal menseki
            if not (0 <= row < m and 0 <= col < n):
                return
            if grid[row][col] == 0:
                return
            menseki += 1
            grid[row][col] = 0
            dirs = [(1,0), (-1, 0), (0, 1), (0,-1)]
            for dr, dc in dirs:
                mark_as_visited(row+dr, col+dc)
            return menseki
 
        m, n = len(grid), len(grid[0])
        max_of_islands = 0
        menseki = 0
        for row in range(m):
            for col in range(n):
                
                if grid[row][col] == 1:
                    menseki = 0
                    max_of_islands = max(max_of_islands, mark_as_visited(row, col))
        return max_of_islands
    
# class Solution:
#     def maxAreaOfIsland(self, grid):
#         seen = set()
#         def area(r,c):
#             if not (0 <= r < len(grid) and 0 <= c < len(grid[0])) and (r, c) not in seen and grid[r][c]:
#                 return 0
#             seen.add((r,c))
#             return (1+area(r+1, c)+ area(r-1, c)+ area(r, c-1))
        
#         return max(area(r, c)
#                    for r in range(len(grid))
#                    for c in )

# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         def mark_as_visited(row, col):
#             if not (0 <= row < m and 0 <= col < n):
#                 return 0
#             if grid[row][col] == 0:
#                 return 0
#             grid[row][col] = 0
#             #dirs = [(1,0), (-1,0), (0,1), (0,-1)]
#             return (1 + mark_as_visited(row+1, col) + mark_as_visited(row-1, col) +
#                     mark_as_visited(row, col-1) + mark_as_visited(row, col+1))
        
#         m, n = len(grid), len(grid[0])
#         max_of_islands = 0
#         for row in range(m):
#             for col in range(n):
#                 if grid[row][col] == 1:
#                     max_of_islands = max(max_of_islands, mark_as_visited(row, col))

#         return max_of_islands

#Number of Connected Components in an Undirected Graph
#有料

#Word Ladder
# from collections import defaultdict
# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         pattern_to_words = defaultdict(list)

#         def make_patterns(word):
#             patterns = []
#             for i in range(len(word)):
#                 patterns.append(f"{word[:i]}*{word[i+1:]}")
#             return patterns
        
#         for word in wordList:
#             patterns = make_patterns(word)
#             for pattern in patterns:
#                 pattern_to_words[pattern].append(word)

#         words = [beginWord]
#         seen = set(word)
#         num_of_words = 1
#         while words:
#             num_of_words += 1
#             next_words = []
#             for word in words:
#                 patterns = make_patterns(word)
#                 for pattern in patterns:
#                     for next_word in pattern_to_words[pattern]:
#                         if next_word == endWord:
#                             return num_of_words
#                         if next_word in seen:
#                             continue
#                         seen.add(next_word)
#                         next_words.append(next_word)
#             words = next_words
#         return 0

#Maximum Depth of Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from collections import deque
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         leftDepth = self.maxDepth(root.left)
#         rightDepth = self.maxDepth(root.right)
#         return max(leftDepth, rightDepth)+1

# class Solution:
#     def maxDepth(self, root):
#         if not root:
#             return 0
#         nodes = [root]
#         depth = 0
#         while nodes:
#             newNodes = []
#             depth += 1
#             for node in nodes:
#                 if node.left:
#                     newNodes.append(node.left)
#                 if node.right:
#                     newNodes.append(node.right)
#             nodes = newNodes
#         return depth
    


# class Solution:
#     def maxDepth(self, root):
#         if not root:
#             return 0
        
#         depth = 0
#         q = deque()
#         q.append(root)
#         while q:
#             depth += 1
#             for _ in range(len(q)):
#                 node = q.popleft()
#                 if node.right:
#                     q.append(node.right)
#                 if node.left:
#                     q.append(node.left)
#         return depth

    
#Minimum Depth of Binary Tree
# class Solution:
#     def minDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         leftDepth = self.minDepth(root.left)
#         rightDepth = self.minDepth(root.right)
#         if leftDepth and rightDepth:
#             return min(leftDepth, rightDepth)+1
#         elif leftDepth and not rightDepth:
#             return leftDepth +1
#         elif rightDepth and not leftDepth:
#             return rightDepth+1
#         else:
#             return 1

# class Solution:
#     def minDepth(self, root):
#         if not root:
#             return 0
        
#         nodes = []
#         nodes.append(root)
#         depth = 0
#         while nodes:
#             depth += 1
#             next_nodes = []
#             for node in nodes:
#                 if node.left in None and node.right is None:
#                     return depth
#                 if node.left:
#                     next_nodes.append(node.left)
#                 if node.right:
#                     next_nodes.append(node.right)
#             nodes = next_nodes
        
#Merge Two Binary Trees
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
#         if root1 is None: return root2
#         if root2 is None: return root1

#         root = TreeNode(root1.val + root2.val)
#         root.left = self.mergeTrees(root1.left, root2.left)
#         root.right = self.mergeTrees(root1.right, root2.right)

#         return root

#Convert Sorted Array to Binary Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
#             if not nums:
#                 return None
            
#             mid = len(nums) // 2
#             root = TreeNode(nums[mid])
#             root.left = self.sortedArrayToBST(nums[:mid])
#             root.right = self.sortedArrayToBST(nums[mid+1:])

#             return root
    
#Path Sum
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         if not root:
#             return False

#         if not root.right and not root.left:
#             return targetSum - root.val == 0

#         targetSum -= root.val
#         return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)          


#Binary Tree Level Order Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from collections import deque
# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []
#         q = deque([root])
#         ans = []
#         while True:
#             new_q = deque()
#             tmp_ans = []
#             while q:
#                 node = q.popleft()
#                 tmp_ans.append(node.val)
#                 if node.left: new_q.append(node.left)
#                 if node.right: new_q.append(node.right)
            
#             ans.append(tmp_ans)
#             if not new_q:
#                 return ans
#             q = new_q


# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []
        
#         ans = []
#         queue = deque([root])
#         while queue:
#             currentLevelNodes = []
#             for _ in range(len(queue)):
#                 node = queue.popleft()
#                 currentLevelNodes.append(node.val)
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#             ans.append(currentLevelNodes)
#         return ans

#Binary Tree Zigzag Level Order Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from collections import deque
# class Solution:
#     def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []
        
#         result = []
#         queue =deque([root])
#         is_left_to_right = True

#         while queue:
#             level_size = len(queue)
#             current_level = [0]*level_size

#             for i in range(level_size):
#                 node = queue.popleft()
#                 index = i if is_left_to_right else level_size -1 -i
#                 current_level[index] = node.val

#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)

#             result.append(current_level)
#             is_left_to_right = not is_left_to_right

#         return result

#Binary Tree Zigzag Level Order Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from collections import deque
# class Solution:
#     def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []
        
#         ans = []
#         q = deque([root])
#         flag = True
#         while q:
#             current_level_n = len(q)
#             current_level_q = [0]*current_level_n
#             for i in range(current_level_n):
#                 i = i if flag else current_level_n -i -1 
#                 current_q = q.popleft()
#                 current_level_q[i] = current_q.val
#                 if current_q.left:
#                     q.append(current_q.left)
#                 if current_q.right:
#                     q.append(current_q.right)

#             flag = not flag
#             ans.append(current_level_q)
        
#         return ans


#Validate Binary Search Tree
