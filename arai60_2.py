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
    
#Valid Parentheses
from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()

        for i in range(len(s)):

            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                q.append(s[i])
                continue
            
            if not q:
                return False
            if s[i] == ")":
                a=  q.pop()
                if a == "(":
                    continue
                else:
                    return False
            if s[i] == "]":
                a = q.pop()
                if a == "[":
                    continue
                else:
                    return False
            if s[i] == "}":
                a = q.pop()
                if a == "{":
                    continue
                else:
                    return False
        return len(q) == 0

class Solution:
    def isValid(self, s:str) -> bool:
        stack = []
        mapping = {"}":"{", "]":"[", ")":"("}

        for char in s:
            if char in mapping.values:
                stack.append(char)
            elif char in mapping.keys():
                if not stack or mapping[char] != stack.pop():
                    return False
            
        return not stack

#Reverse Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        q = deque()

        while head:
            q.append(head.val)
            head = head.next
        
        dummy = ListNode()
        prev = dummy
        while q:
            new_head = ListNode(q.pop())

            prev.next = new_head
            prev = prev.next

        return dummy.next
    
class Solution:
    def reverseList(self, head):
        node = None

        while head:
            temp = head.next
            head.next = node
            node = head
            head = temp

        return node
    

#Kth Largest Element in a Stream
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

#Top K Frequent Elements
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        heap = []
        for i in range(len(nums)):
            d[nums[i]] -= 1

        for key, val in d.items():
            heapq.heappush(heap, (val, key))

        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans

#Find K Pairs with Smallest Sums
# これやとTLEになりますのでご注意
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if len(heap) < k:
                    heapq.heappush(heap, [-(nums1[i]+nums2[j]), nums1[i],nums2[j]])
                elif -heap[0][0] > nums1[i]+nums2[j]:
                    heapq.heapreplace(heap, [-(nums1[i]+nums2[j]), nums1[i], nums2[j]])
        result = []
        for i in heap:
            result.append(i[1], i[2])

        return result
    
#Find K Pairs with Smallest Sums
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        
        h = []
        visited = set()
        result = []

        heapq.heappush(h, (nums1[0]+nums2[0], 0, 0))
        visited.add((0, 0))

        while h and len(result) < k:
            s, i, j = heapq.heappop(h)
            result.append([nums1[i], nums2[j]])

            if j + 1< len(nums2) and (i, j+1) not in visited:
                visited.add((i, j+1))
                heapq.heappush(h, (nums1[i]+nums2[j+1], i, j+1))

            if i+1 <len(nums1) and (i+1, j) not in visited:
                visited.add((i+1, j))
                heapq.heappush(h, (nums1[i+1] + nums2[j], i+1,j))

        return result
    
