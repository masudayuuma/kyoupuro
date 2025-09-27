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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        flag = False
        ans = ListNode()
        tmp_ans = ans
        while head :
            if flag == True and head.next and head.next.val == head.val:
                head = head.next
                continue         
            if head.next and head.val == head.next.val:
                flag = True
                head = head.next
                continue

            if not flag:
                tmp_ans.next = head
                tmp_ans = tmp_ans.next
            flag = False
            head = head.next
        tmp_ans.next = None
        return ans.next
            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total = ListNode()
        tmp = total
        carry = 0
        while l1 or l2 or carry:
            val1 = 0
            val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            ans = val1+val2+carry
            carry = ans//10
            num = ans % 10
            tmp.next = ListNode(num)
            tmp = tmp.next
        return total.next
            

from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return
        q = deque()
        dict = {']':'[', ')':'(', '}':'{'}
        for i in range(len(s)):
            target = s[i]
            if target in ('(', '[', '{'):
                q.append(target)
            else:
                if q and q.pop() == dict[target]:
                    continue
                else:
                    return False
        

        return True if not q else False
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        ans = ListNode()
        tmp = None
        while head:
            ans.next = ListNode(head.val)
            ans.next.next = tmp
            tmp = ans.next
            head = head.next

        return ans.next
    
import heapq
class KthLargest:
    def __init__(self, k:int, nums: List[int]):
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
    
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = defaultdict(int)

        for n in nums:
            dict[n] += 1

        ans = []

        for i in dict:
            if len(ans) < k:
                heapq.heappush(ans, (dict[i], i))
                continue
            if ans[0][0] < dict[i]:
                heapq.heapreplace(ans, (dict[i], i))
        final = []
        for i in range(len(ans)):
            final.append(ans[i][1])
            
        final.reverse()
        return final

#Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []
        dict = defaultdict(int)
        n = len(nums)
        for i in range(n):
            if target-nums[i] in dict:
                return [dict[target-nums[i]], i]
            dict[nums[i]] = i

        return []
        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for st in strs:
            s = ''.join(sorted(st))
            dict[s].append(st)
        ans = []
        for i, v in enumerate(dict):
            ans.append(dict[v])
        return ans
    
