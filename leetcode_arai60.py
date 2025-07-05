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

