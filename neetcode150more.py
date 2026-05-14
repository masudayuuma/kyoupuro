# Subsets
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        tmp = []
        
        def dfs(i):
            if i >= len(nums):
                ans.append(tmp[:])
                return

            dfs(i+1)
            tmp.append(nums[i])
            dfs(i+1)
            tmp.pop()
        
        dfs(0)
        return ans
    
# Combination Sum
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        tmp = []
        def dfs(i):
            if i >= len(nums) or target <= sum(tmp):
                if target == sum(tmp):
                    ans.append(tmp[:])
                return
            
            tmp.append(nums[i])
            dfs(i)
            tmp.pop()
            dfs(i+1)
        
        dfs(0)
        return ans
    
# Combination Sum II
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        tmp = []

        def dfs(i):
            if i >= len(candidates) or sum(tmp) >= target:
                if target == sum(tmp):
                    ans.append(tmp[:])
                return
            tmp.append(candidates[i])
            dfs(i+1)
            tmp.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            dfs(i+1)
            
            
        dfs(0)
        return ans

# Permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        tmp = []
        ans = []
        def dfs(i):
            if i >= len(nums):
                ans.append(tmp[:])

            for j in range(len(nums)):
                if nums[j] in tmp:
                    continue
                tmp.append(nums[j])
                dfs(i+1)
                tmp.pop()
        dfs(0)
        return ans
    
# Subsets II
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        tmp = []
        def dfs(i):
            if i >= len(nums):
                ans.append(tmp[:])
                return
            
            tmp.append(nums[i])
            dfs(i+1)
            tmp.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1)
        dfs(0)
        return ans

# Generate Parentheses
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        tmp = []
        def dfs(opencnt, i):
            if i > n or opencnt > n:
                return
            if i == n and opencnt == 0:
                ans.append(''.join(tmp[:]))
                return

            tmp.append('(')
            dfs(opencnt+1, i+1)
            tmp.pop()

            if opencnt > 0:
                tmp.append(')')
                dfs(opencnt-1, i)
                tmp.pop()
        
        dfs(0, 0)
        return ans
    
# Word Search
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        diff = ((1, 0), (-1, 0), (0, 1), (0, -1))
        visited = [[False]*len(board[0]) for _ in range(len(board))]

        def dfs(i, j, mozi):
            if len(mozi) > len(word):
                return False
            if mozi == word:
                return True
            f = False
            for dy, dx in diff:
                x = dx+j
                y = dy+i
                if not 0 <= y < len(board) or not 0 <= x < len(board[0]) or visited[y][x]:
                    continue
                visited[y][x] = True
                f |= dfs(y, x, mozi+board[y][x])
                visited[y][x] = False

            return f


        for i in range(len(board)):
            for j in range(len(board[0])):
                visited[i][j] = True
                f = dfs(i, j, board[i][j])
                visited[i][j] = False

                if f == True:
                    return True
                
        return False

# Palindrome Partitioning
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        tmp = []
        def dfs(start):
            if start >= len(s):
                ans.append(tmp[:])
                return

            for end in range(start+1, len(s)+1):
                if s[start:end] == s[start:end][::-1]:
                    tmp.append(s[start:end])
                    dfs(end)
                    tmp.pop()                    
        
        dfs(0)
        return ans
    
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        digits_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        ans = []
        tmp = []

        def dfs(i):
            if i >= len(digits):
                ans.append(''.join(tmp))
                return

            for n in digits_dict[digits[i]]:
                tmp.append(n)
                dfs(i+1)
                tmp.pop()

        dfs(0)
        return ans
    
# N-Queens
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        tmp = []
        grid = [['.']*n for _ in range(n)]

        plus = set()
        minus = set()
        col = set()

        def dfs(i):
            if i >= n:
                tmp = [''.join(r) for r in grid]
                ans.append(tmp)
                return

            for j in range(n):
                if i+j in plus or i-j in minus or j in col:
                    continue
                plus.add(i+j)
                minus.add(i-j)
                col.add(j)
                grid[i][j] = 'Q'
                dfs(i+1)
                grid[i][j] = '.'
                plus.remove(i+j)
                minus.remove(i-j)
                col.remove(j)
            
        dfs(0)
        return ans

# Reverse Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = prev

        return cur

# Reverse Linked List
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        new = head

        if head and head.next:
            new = self.reverseList(head.next)
            head.next.next = head
            head.next = None

        return new
    
# Merge Two Sorted Linked Lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 and not list2:
            return None
        if not list2:
            return list1
        if not list1:
            return list2
        if list1.val <= list2.val:
            ans = list1
            list1.next = self.mergeTwoLists(list1.next, list2)
        else:
            ans = list2
            list2.next = self.mergeTwoLists(list1, list2.next)

        return ans
    
# Linked List Cycle Detection
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast  == slow:
                return True

        return False
    
# Reorder Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        