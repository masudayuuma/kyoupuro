#Linked List Cycle
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        head_1 = head
        head_2 = head

        while head_1.next and head_2.next.next:
            head_1 = head_1.next
            head_2 = head_2.next.next

            if head_1 == head_2:
                return True
            
#Linked List Cycle II
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        point
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                break
        else:
            return None
        
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next

        return fast
    
#Remove Duplicates from Sorted List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        p_1 = head.next
        p_2 = head

        while p_1:
            if head.val == p_1.val:
                p_1 = p_1.next
                head.next = None
                continue
            else:
                head.next = p_1
                head = head.next
                p_1 = p_1.next            

        return p_2
    
# Remove Duplicates from Sorted List II
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0, head)
        prev = dummy
        current = head

        while current:
            is_duplicate = False

            while current.next and current.val == current.next.val:
                is_duplicate = True

                current = current.next

            if is_duplicate:
                prev.next = current.next
            else:
                prev = prev.next

            current = current.next

        return dummy.next

#Add Two Numbers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        ans = dummy
        carry = 0

        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            carry = total // 10
            total %= 10

            ans.next = ListNode(total)
            ans = ans.next

        return dummy.next