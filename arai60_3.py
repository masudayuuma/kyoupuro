# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
            
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow is fast:
                return True
                
        return False
        

#Linked List Cycle II
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                break
        else:
            return None

        fast = head
        cnt = 0
        while fast != slow:
            fast = fast.next
            slow = slow.next

        return fast

