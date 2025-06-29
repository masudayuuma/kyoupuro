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
    

