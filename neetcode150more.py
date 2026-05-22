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
# Invert Binary Tree   
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        tmp = TreeNode(root.val)

        tmp.left = self.invertTree(root.right) if root.right else None
        tmp.right = self.invertTree(root.left) if root.left else None

        return tmp
    
# Maximum Depth of Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        cnt = 0

        def dfs(root, c):
            nonlocal cnt
            if not root:
                cnt = max(cnt, c)
                return

            dfs(root.right, c+1)
            dfs(root.left, c+1)

        dfs(root, cnt)
        return cnt

# # Diameter of Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxpath = 0
        
        def dfs(root):
            nonlocal maxpath
            if not root:
                return 0
            
            left = dfs(root.right) 
            right = dfs(root.left)
            maxpath = max(maxpath, right+left)

            return max(left, right)+1
        dfs(root)
        return maxpath 

# Balanced Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        f = False
        
        def dfs(root):
            nonlocal f
            if not root:
                return 0
            
            left = dfs(root.right)
            right = dfs(root.left)
            if abs(left-right) >= 2:
                f |= True

            return max(left, right)+1
            

        dfs(root)
        f = not f
        return f
    
# Same Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        f = True

        def dfs(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if q.val != p.val:
                return False
            
            fact = (dfs(q.left, p.left) and dfs(q.right, p.right)) or (dfs(q.right, p.left) and dfs(q.right, p.right))
            return fact

        return dfs(p, q)
    
# Subtree of Another Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sametree(root, sub):
            if not root and not sub:
                return True
            if not root or not sub or root.val != sub.val:
                return False
            return sametree(root.right, sub.right) and sametree(root.left, sub.left)
        
        def dfs(root, sub):
            if not root and not sub:
                return True
            if not root or not sub:
                return False
            
            flag = False
            if root.val == sub.val:
                flag |= sametree(root.right, sub.right) and sametree(root.left, sub.left)
                
            flag |= dfs(root.right, sub) or dfs(root.left, sub)
            return flag

        return dfs(root, subRoot)

# Implement Trie (Prefix Tree)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        root = self.root
        for c in word:
            if c not in root.children:
                root.children[c] = TrieNode()
            root = root.children[c]

        root.end = True

    def search(self, word: str) -> bool:
        root = self.root
        for c in word:
            if c not in root.children:
                return False
            root = root.children[c]
        return root.end

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for c in prefix:
            if c not in root.children:
                return False
            
            root = root.children[c]
        return True
        
# Design Add and Search Word Data Structure
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        root = self.root
        for c in word:
            if c not in root.children:
                root.children[c] = TrieNode()
            root = root.children[c]
        root.end = True

    def search(self, word: str) -> bool:
        root = self.root

        def dfs(root, i):
            flag = False
            if i == len(word):
                return root.end

            if word[i] in root.children:
                flag |= dfs(root.children[word[i]], i+1)
            if word[i] == '.':
                for c in root.children:
                    flag |= dfs(root.children[c], i+1)
            return flag

        return dfs(root, 0)

# Word Search II
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class Solution:
    def __init__(self):
        self.root = TrieNode()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for word in words:
            root = self.root
            for c in word:
                if c not in root.children:
                    root.children[c] = TrieNode()
                root = root.children[c]
            root.end = True

        out = []
        visited = set()
        diff = ((1, 0), (-1, 0), (0, 1), (0, -1))
        ans = []

        def search(root, i, j):
            if root.end == True:
                out.append(''.join(ans))

            for dy, dx in diff:
                y = dy+i
                x = dx+j
                if not 0 <= y < len(board) or not 0 <= x < len(board[0]) or (y, x) in visited:
                    continue
                if board[y][x] in root.children:
                    ans.append(board[y][x])
                    visited.add((y, x))
                    search(root.children[board[y][x]], y, x)
                    ans.pop()
                    visited.remove((y, x))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in self.root.children:
                    root = self.root
                    visited.add((i, j))
                    ans.append(board[i][j])
                    search(root.children[board[i][j]], i, j)
                    ans.pop()
                    visited.remove((i, j))

        return out
    
# Reorder Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        fast = slow.next
        slow.next = None
        prev = None
        while fast:
            nxt = fast.next
            fast.next = prev
            prev = fast
            fast = nxt
        fast = prev

        dummy = head
        while fast:
            nxt = head.next
            head.next = fast
            fast = fast.next
            head.next.next = nxt
            head = nxt

# Remove Nth Node From End of List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        cnt = 0
        late = dummy
        while head:
            head = head.next
            cnt += 1
            if cnt > n:
                late = late.next

        late.next = late.next.next
        return dummy.next
                
# Copy Linked List with Random Pointer
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        old2new = {}
        root = head

        while head:
            old2new[head] = Node(head.val)
            head = head.next
        head = root
        while head:
            old2new[head].next = old2new[head.next] if head.next else None
            old2new[head].random = old2new[head.random] if head.random else None
            head = head.next

        return old2new[root]

# Add Two Numbers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        root = ListNode()
        out = root


        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1+v2+carry
            digit = total%10
            carry = total//10
            out.next = ListNode(digit)
            out = out.next
            l2 = l2.next if l2 else None
            l1 = l1.next if l1 else None
        if carry:
            out.next = ListNode(carry)

        return root.next
    
# Find the Duplicate Number
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]

            if slow == fast:
                return slow

# LRU Cache
class Node:
    def __init__(self, key: int =0, val: int =0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev = self.right.prev
        nxt = self.right
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)

            del self.cache[lru.key]

# Sort an Array
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        import heapq
        heapq.heapify(nums)

        out = []
        while heapq:
            out.append(heapq.heappop(nums))

        return out

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curmin = 10000000
        profit = 0

        for n in prices:
            if curmin >= n:
                curmin = n
                continue
            else:
                profit += n - curmin
                curmin = n
        
        return profit
    

# Merge Strings Alternately
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l2 = 0
        l1 = 0
        out = ""
        while l1 < len(word1) or l2 < len(word2):
            t1 = word1[l1] if l1 < len(word1) else ""
            t2 = word2[l2] if l2 < len(word2) else ""

            out += t1+t2
            l1 += 1
            l2 += 1

        return out
    

# Lowest Common Ancestor in Binary Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ans = root
        def dfs(root):
            if not root:
                return
            nonlocal ans
            if (p.val <= root.val and root.val <= q.val) or (p.val >= root.val and root.val >= q.val):
                ans = root
                return
            
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ans
    
# Binary Tree Level Order Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        maxlevel = 0
        out = []

        def dfs(root, cnt):
            if not root:
                return
            
            if len(out) <= cnt:
                out.append([root.val])
            else:
                out[cnt].append(root.val)
            dfs(root.left, cnt+1)
            dfs(root.right, cnt+1)
            

        dfs(root, 0)
        return out
    
    
# Binary Tree Right Side View
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        
        def dfs(root, cnt):
            if not root:
                return
            
            if len(out) <= cnt:
                out.append(root.val)

            dfs(root.right, cnt+1)
            dfs(root.left, cnt+1)

        dfs(root, 0)
        return out
    
# Count Good Nodes in Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        out = []
        
        def dfs(root, mcnt):
            if not root:
                return
            if mcnt <= root.val:
                out.append(root.val)
            mcnt = max(mcnt, root.val)
            dfs(root.right, mcnt)
            dfs(root.left, mcnt)

        dfs(root, -1000)
        return len(out)
    
# Valid Binary Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, maxval, minval):
            if not root:
                return True
            if not minval < root.val < maxval:
                return False
            
            f1 = dfs(root.right, maxval, minval=root.val)
            f2 = dfs(root.left, maxval=root.val, minval=minval)

            return f1 and f2
        
        return dfs(root, 10000, -10000)
        
# Kth Smallest Integer in BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        out = -1
        def dfs(root, cnt):
            nonlocal out
            if not root:
                return cnt
            
            cnt = dfs(root.left, cnt)
            cnt += 1
            if cnt == k:
                out = root.val
            cnt = dfs(root.right, cnt)
            return cnt

        dfs(root, 0)
        return out
    
# Construct Binary Tree from Preorder and Inorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preolderで最初の位置を決めれる
        # 
        id_dict = {num: i for i, num in enumerate(inorder)}
        self.id = 0

        def dfs(l, r):
            if l > r:
                return None
            
            root_v = preorder[self.id]
            self.id += 1
            mid = id_dict[root_v]
            root = TreeNode(root_v)
            root.left = dfs(l, mid-1)
            root.right = dfs(mid+1, r)
            return root

        return dfs(0, len(preorder)-1)

# Binary Tree Maximum Path Sum     
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        out = -10000
        
        def dfs(root):
            nonlocal out
            if not root:
                return 0

            maxnum = root.val
            l = dfs(root.left)
            r = dfs(root.right)
            res = max(maxnum, maxnum+l, maxnum+r)
            maxnum = max(maxnum, maxnum+l, maxnum+r, maxnum+l+r)
            out = max(out, maxnum)
            return res

        dfs(root)
        return out
    
# Serialize and Deserialize Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        vals = []
        def dfs(root):
            if not root:
                vals.append('N')
                return 
            
            vals.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)        
        return ','.join(vals)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(',')
        self.i = 0
        def dfs():
            if vals[self.i] == 'N':
                return None
            
            head = TreeNode(int(vals[self.i]))
            self.i += 1
            head.left = dfs()
            self.i += 1
            head.right = dfs()
            return head

        return dfs()
    
# Kth Largest Element in a Stream
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
          self.heap = nums
          heapq.heapify(self.heap)
          if len(self.heap) > k:
              heapq.heappop(self.heap)
          self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]

# Last Stone Weight
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stonelist = [-s for s in stones]
        heapq.heapify(stonelist)

        while len(stonelist) > 1:
            t1 = heapq.heappop(stonelist)
            t2 = heapq.heappop(stonelist)
            if abs(t1-t2) != 0:
                heapq.heappush(stonelist, -abs(t1-t2)) 

        return 0 if not stonelist else -stonelist[0]
    
# K Closest Points to Origin
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = 100000

        pointlist = [[x**2+y**2, x, y] for x, y in points]
        heapq.heapify(pointlist)
        out = []
        for i in range(k):
            diff, x, y = heapq.heappop(pointlist)
            out.append((x, y))

        return out
    
# Kth Largest Element in an Array
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)

        for i in range(k):
            out = heapq.heappop(nums)


        return -out
    
# Task Scheduler
from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)

        heap = [-v for v in cnt.values()]
        heapq.heapify(heap)

        q = deque()
        time = 0

        while heap or q:
            time += 1
            if heap:
                c = heap.heappop(heap)+1

                if c < 0:
                    q.append((c, time+n))
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])

        return time
    
from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        self.followMap[userId].add(userId)

        for followee in self.followMap[userId]:
            if self.tweetMap[followee]:
                idx = len(self.tweetMap[followee]) - 1
                time, tweetId = self.tweetMap[followee][idx]

                heapq.heappush(heap, (time, tweetId, followee, idx - 1))

        while heap and len(res) < 10:
            time, tweetId, followee, idx = heapq.heappop(heap)

            res.append(tweetId)

            if idx >= 0:
                time, tweetId = self.tweetMap[followee][idx]

                heapq.heappush(heap, (time, tweetId, followee, idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

# Number of Islands
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        diff = ((1, 0), (-1, 0), (0, -1), (0, 1))
        ans = 0
        def dfs(i, j):
            if (i, j) in visited or grid[i][j] == '0':
                return 0
            visited.add((i, j))
            for dy, dx in diff:
                y = dy+i
                x = dx+j

                if not 0 <= y < len(grid) or not 0 <= x < len(grid[0]) or grid[y][x] != '1' or (y, x) in visited:
                    continue
                dfs(y, x)
            return 1
            
            

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans += dfs(i, j)
        return ans
    
# Max Area of Island
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0
        diff = ((1, 0), (-1, 0), (0, -1), (0, 1))

        def dfs(i, j):
            if grid[i][j] == 0:
                return 0
            cnt = 1
            grid[i][j] = 0
            for dy, dx in diff:
                y = dy+i
                x = dx+j
                if not 0 <= y < len(grid) or not 0 <= x < len(grid[0]):
                    continue
                cnt += dfs(y, x)
            return cnt
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cnt = dfs(i, j)
                maxarea = max(maxarea, cnt)

        return maxarea
            
# Clone Graph
# Definition for a Node.
# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copynode = Node(1)

        nodedict = {}

        def dfs(node):
            if not node:
                return None
            if node in nodedict:
                return nodedict[node]
            
            nodedict[node] = Node(node.val)
            for nei in node.neighbors:
                nodedict[node].neighbors.append(dfs(nei))
            return nodedict[node]

        return dfs(node)

# Islands and Treasure
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j, 0))
        diff = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while q:
            i, j, k = q.popleft()
            for dy, dx in diff:
                y = dy+i
                x = dx+j
                if 0 <= y < len(grid) and 0 <= x < len(grid[0]) and grid[y][x] == 2147483647:
                    grid[y][x] = k+1
                    q.append((y, x, k+1))

# # Islands and Treasure
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j, 0))
        diff = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while q:
            i, j, k = q.popleft()
            for dy, dx in diff:
                y = dy+i
                x = dx+j
                if 0 <= y < len(grid) and 0 <= x < len(grid[0]) and grid[y][x] == 2147483647:
                    grid[y][x] = k+1
                    q.append((y, x, k+1))

# Rotting Fruit
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        diff = ((1, 0), (-1, 0), (0, -1), (0, 1))
        q = deque()
        maxcnt = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j, 0))

        while q:
            i, j, k = q.popleft()
            maxcnt = max(maxcnt, k)

            for dx, dy in diff:
                y = dy+i
                x = dx+j
                if 0 <= y < len(grid) and 0 <= x < len(grid[0]) and grid[y][x] == 1:
                    grid[y][x] = 2
                    q.append((y, x, k+1))


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return maxcnt

# Pacific Atlantic Water Flow
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        from_atlantic_root = deque()
        from_pacific_root = deque()
        visitedpath_atlantic = [[False]*(len(heights[0])) for _ in range(len(heights))]
        visitedpath_pacific = [[False]*(len(heights[0])) for _ in range(len(heights))]

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j == 0:
                    from_pacific_root.append((i, j))
                    visitedpath_pacific[i][j] = True
                if i == len(heights)-1 or j == len(heights[0])-1:
                    from_atlantic_root.append((i, j))
                    visitedpath_atlantic[i][j] = True

        ansset1 = set()
        diff = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while from_atlantic_root:
            i, j = from_atlantic_root.pop()
            if i == 0 or j == 0:
                ansset1.add((i, j))
            
            for dy, dx in diff:
                y = dy+i
                x = dx+j
                if 0 <= y < len(heights) and 0 <= x < len(heights[0]) and heights[y][x] >= heights[i][j] and visitedpath_atlantic[y][x] == False:
                    visitedpath_atlantic[y][x] = True
                    from_atlantic_root.append((y, x))
        ansset2 = set()
        while from_pacific_root:
            i, j = from_pacific_root.pop()
            if i == len(heights)-1 or j == len(heights[0])-1:
                ansset2.add((i, j))
            
            for dy, dx in diff:
                y = dy+i
                x = dx+j
                if 0 <= y < len(heights) and 0 <= x < len(heights[0]) and heights[y][x] >= heights[i][j] and visitedpath_pacific[y][x] == False:
                    visitedpath_pacific[y][x] = True
                    from_pacific_root.append((y, x))
        ans = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if visitedpath_atlantic[i][j] and visitedpath_pacific[i][j]:
                    ans.append([i, j])

        return ans

# Surrounded Regions
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        diff = ((1, 0), (-1, 0), (0, 1), (0, -1))
        visited = set()
        tmpchanges = set()

        def dfs(i, j):
            if not 0 < i < len(board)-1 or not 0 < j < len(board[0])-1:
                return True
            tmpchanges.add((i, j))
            f = False
            for dy, dx in diff:
                y = dy+i
                x = dx+j
                if not 0 <= y < len(board) or not 0 <= x < len(board[0]) or board[y][x] == 'X' or (y, x) in visited:
                    continue
                visited.add((y, x))
                f |= dfs(y, x)
            return f

        for i in range(1, len(board)):
            for j in range(1, len(board[0])):
                if (i, j) in visited or board[i][j] == 'X':
                    continue
                visited.add((i, j))
                f = dfs(i, j)
                if f == False:
                    for y, x in tmpchanges:
                        board[y][x] = 'X'
                tmpchanges.clear()

# Course Schedule
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisitesdict = defaultdict(list)

        for i, j in prerequisites:
            prerequisitesdict[i].append(j)

        need = set()

        def dfs(i):
            if i in need:
                return False
            f = True
            need.add(i)
            for want in prerequisitesdict[i]:
                f = dfs(want)
                if f == False:
                    return False
            need.remove(i)
            return f
        
        for i, j in prerequisites:
            f = dfs(i)
            need.clear()
            if f == False:
                return False
            
        return True

from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for course, pre in prerequisites:
            graph[course].append(pre)

        visiting = set()
        visited = set()

        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            
            visiting.add(course)

            for pre in graph[course]:
                if dfs(pre) == False:
                    return False
                
            visiting.remove(course)
            visited.add(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
            
        return True
    
# Course Schedule II
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        visited = set()
        visiting = set()
        res = []

        for i, j in prerequisites:
            graph[i].append(j)

        def dfs(i):
            if i in visiting:
                return False
            if i in visited:
                return True
            visiting.add(i)
            for pre in graph[i]:
                if dfs(pre) == False:
                    return False
            visiting.remove(i)
            visited.add(i)
            res.append(i)
            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return []
            
        return res

# Graph Valid Tree
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        visiting = set()

        graph = defaultdict(list)

        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        def dfs(i, preb=None):
            if i in visiting:
                return False
            
            visiting.add(i)
            for pre in graph[i]:
                if pre == preb:
                    continue
                if dfs(pre, i) == False:
                    return False
            visiting.remove(i)
            visited.add(i)
            return True
        

        dfs(0)
        if len(visited) == n:
            return True
        else:
            return False

# Number of Connected Components in an Undirected Graph
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graphdict = defaultdict(list)

        for i, j in edges:
            graphdict[i].append(j)
            graphdict[j].append(i)

        graph = [False]*n
        cnt = 0

        def dfs(i):
            if graph[i] == True:
                return
            graph[i] = True
            for j in graphdict[i]:
                dfs(j)

        for i in range(n):
            if graph[i] == False:
                dfs(i)
                cnt += 1

        return cnt
    
# Redundant Connection
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        parent = [i for i in range(len(edges))]

        def find(x):
            while x != parent[x]:
                x = parent[parent[x]]
            return x

        def unionfind(i, j):
            a = find(i)
            b = find(j)
            if a == b:
                return True
            parent[b] = a
            return False

        for i, j in edges:
            if unionfind(i-1, j-1) == True:
                return [i, j]


# Word Ladder
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set()

        graph = defaultdict(list)

        wordList.append(beginWord)

        for word1 in wordList:
            for word2 in wordList:
                if word1 == word2:
                    continue
                if len(word1) != len(word2):
                    continue
                cnt = 0
                for w1, w2 in zip(word1, word2):
                    if w1 == w2:
                        continue
                    else:
                        cnt += 1
                if cnt < 2:
                    graph[word1].append(word2)
                    graph[word2].append(word1)
        
        q = deque()
        q.append((beginWord, 1))
        visited.add(beginWord)
        while q:
            word, c = q.popleft()

            if word in graph[endWord]:
                return c+1
            for nxt in graph[word]:
                if nxt in visited:
                    continue
                visited.add(nxt)
                q.append((nxt, c+1))

        return 0

# Network Delay Time
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        
        for i, target, cost in times:
            graph[i].append((cost, target))

        heap = [(0, k)]
        dist = {}
        
        while heap:
            cost, target = heapq.heappop(heap)

            if target in dist:
                continue
            
            dist[target] = cost
            for time, nxt in graph[target]:
                heapq.heappush(heap, (time+cost, nxt))


        if len(dist) == n:
            return max(dist.values())
        else:
            return -1

# Network Delay Time
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, t in times:
            graph[u].append([t, v])

        heap = [(0, k)]
        dist = {}

        while heap:
            t, v = heapq.heappop(heap)
            if v in dist:
                continue
            dist[v] = t
            for nxtime, nxt in graph[v]:
                if nxt in dist:
                    continue

                heapq.heappush(heap, (t+nxtime, nxt))

        if len(dist) != n:
            return -1

        return max(dist.values())


# Reconstruct Flight Path
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = defaultdict(list)
        final = []

        for i, j in tickets:
            graph[i].append(j)

        for i in graph:
            heapq.heapify(graph[i])

        used = set()
        def dfs(target):
            nonlocal final
            if len(out) == len(tickets):
                final = out.copy()
                return
            if final or not graph[target]:
                return
            for _ in range(len(graph[target])):
                nxt = heapq.heappop(graph[target])
                out.append(nxt)
                dfs(nxt)
                if final:
                    return
                out.pop()
                heapq.heappush(graph[target], nxt)
        out = []

        dfs('JFK')
        return ['JFK'] + final
    
# 
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for i, j in tickets:
            heapq.heappush(graph[i], j)

        out = []
        def dfs(i):
            while graph[i]:
                dfs(heapq.heappop(graph[i]))

            out.append(i)

        dfs('JFK')
        return out[::-1]
    
# Min Cost to Connect Points
# prim法
# 今ある木から、一番安く新ノードを追加
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # cost, index
        heap = [(0, 0)]
        dist = {}
        while heap:
            cost, index = heapq.heappop(heap)
            if index in dist:
                continue
            dist[index] = cost

            y1, x1 = points[index]
            for i in len(points):
                if i in dict:
                    continue
                y2, x2 = points[i]

                heapq.heappush(heap, (abs(y2-y1)+abs(x2-x1)+cost, i))

        return max(dist.values())

# Kruskal 法
# cycle 判定には：Union Find
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        edges = []

        # 全辺生成
        for i in range(n):
            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]

                dist = abs(x1 - x2) + abs(y1 - y2)

                edges.append((dist, i, j))

        # 重み順 sort
        edges.sort()

        parent = [i for i in range(n)]
        rank = [1] * n

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra = find(a)
            rb = find(b)

            if ra == rb:
                return False

            if rank[ra] >= rank[rb]:
                parent[rb] = ra
                rank[ra] += rank[rb]
            else:
                parent[ra] = rb
                rank[rb] += rank[ra]

            return True

        ans = 0
        used = 0

        for dist, i, j in edges:
            if union(i, j):
                ans += dist
                used += 1

                if used == n - 1:
                    break

        return ans
    
# Swim in Rising Water
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # time, i, j
        heap = [(grid[0][0], 0, 0)]
        diff = ((1, 0), (-1, 0), (0, -1), (0, 1))
        visited = set()

        while heap:
            time, i, j = heapq.heappop(heap)

            if (i, j) in visited:
                continue
            if i == len(grid)-1 and j == len(grid[0])-1:
                return time
            visited.add((i, j))
            for dy, dx in diff:
                y = dy+i
                x = dx+j
                if 0 <= y < len(grid) and 0 <= x < len(grid[0]) and (y, x) not in visited:
                    heapq.heappush(heap, (max(time, grid[y][x]), y, x))

        return -1
    
# Alien Dictionary
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c: set() for word in words for c in word}
        indegree = {c: 0 for c in graph}

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]

            if len(w1) > len(w2) and w1.startswith(w2):
                return ''
            
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        indegree[c2] += 1
                    break

        q = deque()

        for c in indegree:
            if indegree[c] == 0:
                q.append(c)

        res = []

        while q:
            c = q.popleft()
            res.append(c)

            for nei in graph[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if len(res) != len(graph):
            return ""
        
        return "".join(res)
    
# Cheapest Flights Within K Stops
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for i, to, cost in flights:
            graph[i].append((cost, to))
        
        heap = [(0, src, k)]
        dist = {}

        while heap:
            cost, target, k = heapq.heappop(heap)
            if target == dst:
                dist[target] = cost
                return

            if target in dist or k <= 0:
                continue

            dist[target] = cost

            for nxtcst, nxt in graph[target]:
                if nxt not in dist:
                    heapq.heappush(heap, (cost+nxtcst, nxt, k-1))

        return dist[dst] if dist[dst] else -1

# Cheapest Flights Within K Stops
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')]*n
        prices[src] = 0

        for _ in range(k+1):
            tmp = prices.copy()

            for frm, to, cost in flights:
                if prices[frm] == float('inf'):
                    continue

                tmp[to] = min(tmp[to], prices[frm]+cost)

            prices = tmp

        return -1 if prices[dst] == float('inf') else prices[dst]
    
# Insert Interval
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        out = []
        heapq.heapify(intervals)
        heapq.heappush(intervals, newInterval)

        while intervals:
            i, j = heapq.heappop(intervals)

            if out and out[1] >= i:
                out[-1][1] = max(j, out[-1][1])

        return out
    
# Insert Interval
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0

        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        res.append(newInterval)

        while i < n:
            res.append(intervals[i])
            i += 1

        return res
        
# Merge Intervals
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        res = []
        intervals.sort()
        i = 0
        while i < n:
            if res and res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])
            i += 1

        return res 
    
# Non-overlapping Intervals
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = []
        ans = 0
        intervals = sorted(intervals, key=lambda x: x[1])

        for i, j in intervals:
            if res and res[-1][1] > i:
                ans += 1
                continue
            else:
                res.append([i, j])

        return ans
    
# Meeting Rooms
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        res = []
        intervals.sort(key=lambda x: x.start)
        n = len(intervals)

        for i in range(n):
            s = intervals[i].start
            e = intervals[i].end
            if res and res[-1][1] > s:
                return False
            else:
                res.append([s, e])

        return True
    
# Meeting Rooms II
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key= lambda x : x.start)

        heap = []

        for interval in intervals:
            if heap and heap[0] <= interval.start:
                heapq.heappop(heap)
            heapq.heappush(heap, interval.end)

        return len(heap)
    
# Minimum Interval to Include Each Query
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        intervals.sort()

        sorted_queries = sorted((q, i) for i, q in enumerate(queries))

        res = [-1]*len(queries)

        heap = []

        j = 0

        for q, idx in sorted_queries:
            while j < len(intervals) and intervals[j][0] <= q:
                left, right = intervals[j]
                lenght = right-left+1
                heapq.heappush(heap, (lenght, right))

                j +=1

            while heap and heap[0][1] < q:
                heap.heappop(heap)

            if heap:
                res[idx] = heap[0][0]

        return res

# Maximum Subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxans = 0
        ans = 0
        l = 0
        for r in range(len(nums)):            
            if ans < 0:
                ans = 0
                l = r
            ans += nums[r]
            maxans = max(maxans, ans)

        return maxans if maxans != 0 else max(nums)
    
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = nums[0]
        ans = nums[0]

        for r in range(len(nums)):
            cur = max(cur+nums[r], nums[r])
            ans = max(cur, ans)

        return ans
    
# Jump Game
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxjump_i = 0

        for i in range(len(nums)):
            if maxjump_i < i:
                return False

            maxjump_i = max(nums[i]+i, maxjump_i)

        return True

# Jump Game II
# if there are maxjump, tmp_max_jump = maxjump
class Solution:
    def jump(self, nums: List[int]) -> int:
        l = 0
        r = 0
        ans = 0

        while r < len(nums)-1:
            ans += 1
            maxlenght = 0
            for i in range(l, r+1):
                maxlenght = max(maxlenght, nums[i]+i)
                
            if maxlenght >= len(nums):
                return ans
            
            l = r+1
            r = maxlenght

        return ans
    
# Gas Station
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        tank = 0
        start = 0

        for i in range(len(gas)):
            diff = gas[i]-cost[i]

            total += diff
            tank += diff

            if tank < 0:
                tank = 0
                start = i+1
        
        if total < 0:
            return -1
        return start

# Hand of Straights
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        handcnt = Counter(hand)

        for x in sorted(handcnt):
            if not handcnt[x]:
                continue
            need = handcnt[x]

            for i in range(x, x+groupSize):
                if handcnt[i] >= need:
                    handcnt[i] -= need
                else:
                    return False
        return True

# Merge Triplets to Form Target
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ans = [0, 0, 0]

        for i, j, k in triplets:
            if i <= target[0] and  j <= target[1] and k <= target[2]:
                ans[0] = max(ans[0], i)
                ans[1] = max(ans[1], j)
                ans[2] = max(ans[2], k)

        return True if ans == target else False
    
# Partition Labels
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        strcnt = Counter(s)
        res = []
        r = 0
        wait_num = set()
        tmp = []
        while r < len(s):
            strcnt[s[r]] -= 1
            wait_num.add(s[r])
            tmp.append(s[r])
            if strcnt[s[r]] == 0:
                del strcnt[s[r]]
                wait_num.remove(s[r])
            if len(wait_num) == 0:
                res.append(len(tmp))
                tmp  = []
            r += 1
        return res
    
# Valid Parenthesis String
class Solution:
    def checkValidString(self, s: str) -> bool:
        minopen = 0
        maxopen = 0

        for i in s:
            if i == '(':
                minopen += 1
                maxopen += 1
            elif i == ')':
                minopen -= 1
                maxopen -= 1
            else:
                minopen -= 1
                maxopen += 1
            
            if maxopen < 0:
                return False

            minopen = max(minopen, 0)

        return True if minopen == 0 else False

# Climbing Stairs
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1]+dp[i-2]

        return dp[-1]
    
# Min Cost Climbing Stairs
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [float('inf')] * (len(cost)+1)

        dp[0] = 0
        dp[1] = 0

        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])

        return dp[-1]

# House Robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        dp = [0]*(len(nums))

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])

        return dp[-1]
    
# House Robber II
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 3:
            return max(nums[0], nums[1], nums[2])

        dp1 = [0]*len(nums)
        dp2 = [0] *len(nums)
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])
        dp2[1] = nums[1]
        dp2[2] = max(nums[1], nums[2])

        for i in range(2, len(nums)-1):
            dp1[i] = max(nums[i]+dp1[i-2], dp1[i-1])
        
        for i in range(3, len(nums)):
            dp2[i] = max(nums[i]+dp2[i-2], dp2[i-1])

        return max(dp1[-2], dp2[-1])
    
# Longest Palindromic Substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxans = ''
        for i in range(len(s)):
            r = i
            l = i
            while l >= 0 and r < len(s) and s[r] == s[l]:
                if len(maxans) < len(s[l:r+1]):
                    maxans = s[l:r+1]
                r += 1
                l -= 1

            while l >= 0 and r < len(s) and s[r] == s[l]:
                if len(maxans) < len(s[l:r+1]):
                    maxans = s[l:r+1]
                r += 1
                l -= 1

        return maxans
    
# Longest Palindromic Substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]

        ans_l = 0
        ans_r = 0

        for lenght in range(1, n+1):
            for l in range(n-lenght+1):
                r = l+lenght-1

                if lenght == 1:
                    dp[l][r] = True
                elif lenght == 2 and s[r] == s[l]:
                    dp[l][r] = True
                else:
                    dp[l][r] = s[r]==s[l] and dp[l+1][r-1]

                if lenght > ans_r-ans_l+1 and dp[l][r] == True:
                    ans_l = l
                    ans_r = r

        return s[ans_l:ans_r+1]
    
# Palindromic Substrings
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        ans = 0

        for lenght in range(n):
            for l in range(n-lenght+1):
                r = l+lenght-1

                if lenght == 1:
                    dp[l][r] = True
                elif lenght == 2:
                    dp[l][r] = s[l]==s[r]
                else:
                    dp[l][r] = dp[l+1][r-1] and s[r] == s[l]

                if dp[l][r] == True:
                    ans += 1

        return ans

# Decode Ways
class Solution:
    def numDecodings(self, s: str) -> int:
        # 123 -> 3
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        dp = [0]*(len(s)+1)
        dp[1] = 1
        dp[0] = 1

        for i in range(2, len(s)+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
        
            if '10' <= s[i-2:i] <= "26":
                dp[i] += dp[i-2]

            if dp[i] == 0:
                return 0
        
        return dp[-1]
    
# Coin Change
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0

        
        for c in coins:
            for i in range(1, amount+1):
                if i-c >= 0:
                    dp[i] = min(dp[i-c]+1, dp[i])

        return dp[-1] if dp[-1] != float('inf') else -1
    
# Maximum Product Subarray
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxans = 1
        minans = 1
        res = -float('inf')

        for n in nums:
            nowmax = maxans
            nowmin = minans

            if n > 0:
                maxans = max(nowmax*n, n)
                minans = min(nowmin*n, n)
            else:
                maxans = max(nowmin*n, n)
                minans = min(nowmax*n, n)

            res = max(res, maxans, minans)
        return res
    
# Word Break
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)

        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True

        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordset:
                    dp[i] = True
                    break
        return dp[n]

# Longest Increasing Subsequence
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        