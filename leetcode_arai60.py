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

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast =head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else: return None

        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next

        return slow
