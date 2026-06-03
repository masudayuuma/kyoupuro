# Sort Colors
'''
input nums list[int]
output res list[int]
just sort but don't use sort method

assumptions:
inputlenght 1 <= nums.lenght <= 300
nums[i]lenght <= nums[i] <= 2

time complexity O(n)
space complexity O(n)
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = []
        white = []
        blue = []

        for n in nums:
            if n == 0:
                red.append(0)
            elif n == 1:
                white.append(1)
            else:
                blue.append(2)
            
        nums = red+white+blue

# Majority Element II
import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        goal = math.ceil(n/3)

        nums.sort()
        target = float('inf')
        cnt = 0
        res = []
        for n in nums:
            if n != target:
                if cnt >= goal:
                    res.apppend(target)
                target = n
                cnt = 0
            cnt += 1

        if cnt >= goal:
            res.append(target)

        return res
            
# Subarray Sum Equals K
"""
input nums : list[int], k : int
output res : int

"""
from collections import Counter
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cursum = 0
        prefix = defaultdict(int)
        prefix[0] = 1
        ans = 0

        for n in nums:
            cursum += n

            need = cursum-k
            ans += prefix[need]
            prefix[cursum] += 1

# Reverse String
"""
input s: list[str]
output s (None)
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        l = 0
        r = len(n)-1
        half = (l+r)//2
        for i in range(harf):
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

# Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        nxt = []
        for c in s:
            if c.isalnum():
                nxt.append(c.lower())

        if nxt == nxt[::-1]:
            return True
        else:
            return False

# Valid Palindrome II
"""

"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        l = 0
        r = n-1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue
            else:
                break

        if abs(l-r) <= 1:
            return True
        r1 = r-1
        l1 = l
        r2 = r
        l2 = l+1
        flag = True

        while l1 < r1:
            if s[l1] == s[r1]:
                l1 += 1
                r1 -= 1
                continue
            else:
                flag = False
                break
        
        if abs(l1-r1) <= 1 and flag:
            return True
            
        while l2 < r2:
            if s[l2] == s[r2]:
                l2 += 1
                r2 -= 1
                continue
            else:
                return False
            
        if abs(l2-r2) <= 1:
            return True
        
# 
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pal(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left = 0
        right = len(s)-1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return is_pal(left+1, right) or is_pal(left, right-1)
        return True
    
# Merge Sorted Array
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        k = m+n-1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

# Remove Duplicates From Sorted Array
"""
input : 
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        n = len(nums)
        l = 0
        r = 1
        a = []

        while r < len(nums):
            if nums[l-k] == nums[r-k]:
                nums.remove(nums[l-k])
                l = r
                r += 1
                k += 1
                continue
            else:
                l += 1
                r += 1

        k = n-k
        return k

# Remove Duplicates From Sorted Array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        write = 1

        for read in (1, len(nums)):
            if nums[read] != nums[read-1]:
                nums[write] = nums[read]
                write += 1

        return write
    
# 3Sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            r = len(nums)-1
            l = i+1

            while r > l:
                if nums[i]+nums[l]+nums[r] == 0:
                    out.append([nums[i],nums[l],nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    continue
                if nums[i]+nums[l]+nums[r] > 0:
                    r -=1
                elif nums[i]+nums[l]+nums[r] < 0:
                    l +=1
        return out
                    

# 4Sum
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] ==nums[j-1]:
                    continue
                l = j+1
                r = len(nums)-1

                while r > l:
                    if nums[i]+nums[j]+nums[r]+nums[l] == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l +=1
                        while r >= l > j+1 and nums[l] == nums[l-1]:
                            l += 1
                        continue
                    elif nums[i]+nums[j]+nums[r]+nums[l] > target:
                        r -= 1
                    else:
                        l += 1
        return res

# Baseball Game
"""
input : operations list[int]
output : res int
[1, 2, 2]

time complexity O(n)
space complextiy O(n)
"""

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for n in operations:
            if n == '+':
                res.append(res[-1]+res[-2])
            elif n == 'C':
                res.pop()
            elif n == 'D':
                res.append(res[-1]*2)
            else:
                res.append(int(n))

        return sum(res)

# Asteroid Collision
"""
input : asteroids list[int]
output : list[int]

[2, -1]
"""
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []

        def explode(a):
            while res and abs(res[-1]) < abs(a) and res[-1] > 0 and a < 0:
                res.pop()
            if res and abs(res[-1]) == abs(a) and res[-1]*a < 0:
                res.pop()
                return
            if res and abs(res[-1]) > abs(a) and res[-1]*a < 0:
                return
            
            res.append(a)

        for a in asteroids:
            if not res:
                res.append(a)
            elif res[-1] < 0 and a < 0:
                res.append(a)
            elif res[-1] > 0 and a > 0:
                res.append(a)
            elif res[-1] < 0 and a > 0:
                res.append(a)
            else:
                explode(a)

        return res

# Search Insert Position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = -1
        r = len(nums)

        while r-1 > l:
            mid = (l+r)//2

            if nums[mid] > target:
                r = mid
            else:
                l = mid

        return l if nums[l] == target else l+1

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        l = 1
        r = n
        mid = 0

        while r >= l:
            mid = (l+r)//2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                r = mid-1
            else:
                l = mid+1

        return mid
    
# Sqrt(x)
#  ok - ng > 1
class Solution:
    def mySqrt(self, x: int) -> int:
        ok = 0
        ng = x

        while ok < ng:
            mid = (ok+ng)//2

            if mid*mid > x:
                ng = mid
            else:
                ok = mid
        return ok if abs(ok-x) < abs(ng-x) else ng
    
# Capacity to Ship Packages Within D Days
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #bottom max(weights)
        # maxmam sum(weights)
        ng = max(weights)-1
        ok = sum(weights)+1

        while ok-ng > 1:
            mid = (ok+ng)//2
            daystack = []
            total = 0
            for w in weights:
                if total+w > mid:
                    daystack.append(total)
                    total = 0
                total += w
            if total > 0:
                daystack.append(total)
            
            if len(daystack) > days:
                ng = mid
            else:
                ok = mid

        return ok

        return False

# Contains Duplicate II
"""
input nums: int, k: int
output res: bool

"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        for r in range(len(nums)):
            l = r-k
            if l > 0:
                window.remove(nums[l-1])

            if nums[r] in window:
                return True
            else:
                window.add(nums[r])
        return False
    
# Longest Repeating Character Replacement
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_cnt = 0
        l = 0
        ans = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0)+1
            max_cnt = max(max_cnt, count[s[r]])

            while r-l+1 -max_cnt > k:
                count[s[l]] -= 1
                l += 1
            
            ans = max(ans, r-l+1)

        return ans

# Minimum Size Subarray Sum
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        ans = float('inf')
        l = 0
        r = 0

        for r in range(len(nums)):
            total += nums[r]

            while total-nums[l] >= target:
                total -= nums[l]
                l += 1

            if total >= target:
                ans = min(ans, r-l+1)

        return ans if ans != float('inf') else 0

# Find K Closest Elements
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = 0

        for r in range(len(arr)):
            if r-l+1 > k:
                if abs(nums[l]-x) > abs(nums[r]-x):
                    l += 1
                else:
                    return nums[l:r]
                
        return nums[l:r+1]

# Path with Minimum Effort
"""
input : heights list[list[int]]
output : res int

grid[][]
visited = set()
heap = heapq()
"""
import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        visited = set()
        heap = [(0, 0, 0)] #differentcost, i, j
        diff = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while heap:
            cost, i, j = heapq.heappop(heap)
            if (i, j) in visited:
                continue
            if i == len(heights)-1 and j == len(heights[0])-1:
                return cost
            
            visited.add((i, j))
            for dy, dx in diff:
                y = dy+i
                x = dx+j
                if 0 <= y < len(heights) and 0 <= x < len(heights[0]) and (y, x) not in visited:
                    heapq.heappush(heap, (max(cost, (abs(heights[y][x]-heights[i][j]))), y, x))

            
# Find Critical and Pseudo Critical Edges in Minimum Spanning Tree
class UniouFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0]*n
        self.count = n

    def find(self, x: int):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a: int, b: int) -> bool:
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False

        self.parent[root_b] = root_a
        
        if self.rank[root_a] < self.rank[root_b]:
            self.rank[root_a] += 1

        self.count -= 1
        return True
    
class Solution:
    def findCriticalAndPseudoCriticalEdges(
        self,
        n: int,
        edges: List[List[int]]
    ) -> List[List[int]]:
        
        indexed_edges = []
        for i, (u, v, w) in enumerate(edges):
            indexed_edges.append([u, v, w, i])

        indexed_edges.sort(key=lambda x:x[2])

        def kruskal(skip_index: int = -1, force_edge=None) -> int:
            uf = UniouFind(n)
            total_weight = 0

            if force_edge is not None:
                u, v, w, original_index = force_edge
                if uf.union(u, v):
                    total_weight += w

            for u, v, w, original_index in indexed_edges:
                if original_index == skip_index:
                    continue

                if uf.union(u, v):
                    total_weight += w

            if uf.count != 1:
                return float('inf')
            
            return total_weight
        
        base_weight = kruskal()
        critical = []
        pseudo_critical = []

        for edge in indexed_edges:
            u, v, w, original_index = edge

            weight_without_edge = kruskal(skip_index=original_index)

            if weight_without_edge > base_weight:
                critical.append(original_index)
                continue

            weight_without_edge = kruskal(force_edge=edge)

            if weight_without_edge == base_weight:
                pseudo_critical.append(original_index)

        return [critical, pseudo_critical]
    
# Build a Matrix With Conditions
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        graph_row = {c: set() for _ in range(1, k+1)}
        indegree_row = {c: 0 for _ in range(1, k+1)}

        graph_col = {c: set() for _ in range(1, k+1)}
        indegree_col = {c: 0 for _ in range(1, k+1)}

        for above, below in rowConditions:
            graph_row[above].add(below)
            indegree_row[below ] += 1


        for left, right in colConditions:
            graph_col[left] .add(below)
            indegree_col[right] += 1

        implement_row = []
        for ind in indegree_row:
            if indegree_row[ind] == 0:
                implement_row.append(ind)

        
# Sum of All Subsets XOR Total
"""
input : nums list[int]
output : res : int

assumptions
1 <= nums.lenght <= 12
1 <= nums[i] <= 20


time complexity O(2^n)
space complexty O(n) <= nは同時に存在するdfsの数

"""
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def dfs(i, total):
            nonlocal res
            if i >= len(nums):
                return

            total ^= nums[i]
            res += total
            dfs(i+1, total)
            total ^= nums[i]
            dfs(i+1, total)
        dfs(0, 0)
        return res


# Combinations
"""
input : n: int, k: int
output : list[list[str]]

assumptions
1 <= k <= n <= 20

time, space
O(n^2)
O(n)

"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        res = []
        def dfs(i):
            if i >= n+1:
                if len(ans) == k:
                    res.append(ans.copy())
                return

            dfs(i+1)
            ans.append(i)
            dfs(i+1)
            ans.pop()
        dfs(1)
        return res
    

# Permutations II
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        ans = []
        visited = [False]*(len(nums))
        def dfs(c):
            if c >= len(nums):
                res.append(ans.copy())

            for i in range(len(nums)):
                if visited[i] == True:
                    continue
                visited[i] = True
                ans.append(nums[i])
                dfs(c+1)
                visited[i] = False
                ans.pop()

        dfs(0)
        return res

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        path = []
        used = [False]*len(nums)

        def dfs():
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue

                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                used[i] = True
                path.append(nums[i])

                dfs()

                path.pop()
                used[i] = False

        dfs()
        return res

# Matchsticks to Square
"""
input : matchsticks : list[int]
output : res : bool

assumptions

backtracking
variables
difinition
"""
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_length = sum(matchsticks)
        if total_length % 4 != 0:
            return False

        length = total_length // 4
        sides = [0] * 4
        matchsticks.sort(reverse=True)

        def dfs(i):
            if i == len(matchsticks):
                return True

            for side in range(4):
                if sides[side] + matchsticks[i] <= length:
                    sides[side] += matchsticks[i]
                    if dfs(i + 1):
                        return True
                    sides[side] -= matchsticks[i]

                if sides[side] == 0:
                    break

            return False

        return dfs(0)

# Partition to K Equal Sum Subsets
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        target = 0
        visited = [False]*len(nums)
        if total % k != 0:
            return False
        else:
            target = total // k
        backet = [0]*k

        def dfs(i):
            if i >= len(nums):
                for i in range(k-1):
                    if backet[i] != backet[i+1]:
                        return False
                return True

            visited[i] = True
            flag = False
            for j in k:
                backet[j] += nums[i]
                flag = dfs(i+1)
                if flag == True:
                    return True
                else:
                    backet[j] -= nums[i]
            visited[i] = False
            return flag

        return dfs(0)

# N-Queens II
class Solution:
    def totalNQueens(self, n: int) -> int:
        plus = set()
        minus = set()
        col = set()
        tmp = []
        ans = 0
        def dfs(i):
            nonlocal ans
            if i >= n:
                ans += 1
                return

            for j in range(n):
                if j in col or i+j in plus or i-j in minus:
                    continue

                col.add(j)
                plus.add(i+j)
                minus.add(i-j)
                dfs(i+1)
                col.remove(j)
                plus.remove(i+j)
                minus.remove(i-j)

        dfs(0)
        return ans
    
# Word Break II
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        output = []
        res = []

        def dfs(i):
            if i >= len(s):
                res.append(" ".join(output))
                return
            
            for word in wordDict:
                if len(word)+i <= len(s) and s[i:i+len(word)] == word:
                    output.append(word)
                    dfs(i+len(word))
                    output.pop()

        dfs(0)
        return res


# Island Perimeter
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        res = 0
        diff = ((1, 0), (-1, 0), (0, 1), (0, -1))


        def dfs(i, j):
            nonlocal res
            if grid[i][j] == 0:
                return

            tmp = 4
            for dy, dx in diff:
                y = dy+i
                x = dx+j
                if 0 <= y < len(grid) and 0 <= x < len(grid[0]) and grid[y][x] == 1:
                    tmp -= 1
                    if (y, x) in visited:
                        continue
                    visited.add((y, x))
                    dfs(y, x)
            res += tmp

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in visited:
                    continue
                visited.add((i, j))
                dfs(i, j)

        return res
    
# Verifying An Alien Dictionary
from typing import Lists
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        def dfs(i):
            if i >= len(words):
                return True
            if len(words[i-1]) > len(words[i]) and words[i-1].startswith(words[i]):
                return False
            
            for c1, c2 in zip(words[i-1], words[i]):
                if c1 == c2:
                    continue

                if order.find(c1) < order.find(c2):
                    return dfs(i+1)
                else:
                    return False
            return dfs(i+1)
        
        return dfs(1)

# Find the Town Judge
from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        ans = defaultdict(list)
        for i, j in trust:
            ans[j].append(i)

        if len(ans) == 1:
            return ans.keys()[0]
        else:
            return -1

# Open The Lock
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)

        if "0000" in dead:
            return -1
        
        queue = deque()
        queue.append(("0000", 0))

        visited = set()
        visited.add("0000")

        while queue:
            state, steps = queue.popleft()
            if state == target:
                return steps
            
            for i in range(4):
                digit = int(state[i])

                for move in (-1, 1):
                    new_digit = (digit+move)%10
                    new_state = state[:i]+str(new_digit)+state[i+1:]
                    if new_state in dead:
                        continue
                    if new_state in visited:
                        continue
                    visited.add(new_state)
                    queue.append((new_state, steps+1))

        return -1
    
# Course Schedule IV
"""

"""
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        ans = []

        for i, j in prerequisites:
            graph[i].append(j)

        visited = set()
        needed = defaultdict(set)

        def dfs(i):
            if i in visited:
                return needed[i]
            for j in graph[i]:
                needed[i].add(j)
                needed[i] |= dfs(j)
            visited.add(i)
            return needed[i]

        for i in range(numCourses):
            dfs(i)

        for i, j in queries:
            if j in needed[i]:
                ans.append(True)
            else:
                ans.append(False)
        return ans

# Redundant Connection
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [x for x in range(len(edges))]
        def find(a):
            if parent[a] != a:
                return find(parent[a])
            else:
                return a

        def unionfind(a, b):
            a_parent = find(a)
            b_parent = find(b)
            if a_parent == b_parent:
                return True
            
            parent[b_parent] = a_parent
            return False

        flag = False
        for i, j in edges:
            flag = unionfind(i-1, j-1)
            if flag == True:
                return [i, j]
        return [-1, -1]
    
# Accounts Merge
from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        e2n = defaultdict(list)
        n2e = defaultdict(list)
        output = []

        for account in account[1:]:
            e2n[account] = account[0]

        for email, name in e2n.items():
            n2e[name].append(email)

        for name, email in n2e.items():
            output.append([name]+email)

# N-th Tribonacci Number
"""
input: n:int
output: res: int

0 <= n <= 37
numans = {}
nums
for i in range(len(n)):
    numsans[i] = nums[i-3]+numsi-2
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}

        memo[0] = 0
        memo[1] = 1
        memo[2] = 1

        for i in range(3, n+1):
            memo[i] = memo[i-3]+memo[i-2]+memo[i-1]

        return memo[n]
    
# Combination Sum IV
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(target+1)
        dp[0] = 1

        for i in range(1, target+1):
            for n in nums:
                if i-n >= 0:
                    dp[i] += dp[i-n]

        return dp[target]
    
# Perfect Squares
class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        x = 1
        while x*x <= n:
            squares.append(x*x)
            x += 1

        for i in range(1, n+1):
            for s in squares:
                if s > i:
                    break
                if i-s >= 0:
                    dp[i] = min(dp[i], dp[i-s]+1)
        return dp[n]

# Integer Break
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1

        for num in range(1, n+1):
            for i in range(2, n+1):
                if i-num >= 1:
                    dp[i] = max(dp[i-num]*num, dp[i], (i-num)*num)

        return dp[-1]
    
# Stone Game III
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0]*(n+1)
        for i in range(n-1, -1, -1):
            val = 0
            best = float('-inf')

            for k in range(3):
                

                if i+k >= n:
                    break

                val += stoneValue[i+k]

                best = max(best, val-dp[i+k+1])
            dp[i] = best

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
        
# Unique Paths II
"""
input: obstacleGrid : list[list[int]]
output: res: int

[]
[]

000.  111
000 ->123 
010   103
time O(n*m) space O(n*m)
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*(m+1) for _ in range(n+1)]
        dp[1][1] = 1

        for i in range(1, n+1):
            for j in range(1, m+1):
                dp[i][j] += dp[i-1][j]+dp[i][j-1]

                if obstacleGrid[i-1][j-1] == 1:
                    dp[i][j] = 0

        return dp[-1][-1]
    
# Minimum Path Sum
"""
input : grid: list[list[int]]
output : res : int

assumptions
[]

120.  133
542 ->675
113.  788 res=8
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[float('inf')]*(m) for _ in range(n)]
        dp[0][0] = grid[0][0]
        for i in range(1, n):
            dp[i][0] = dp[i-1][0]+grid[i][0]
        for j in range(1, m):
            dp[0][j] = dp[0][j-1]+grid[0][j]

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = min(dp[i][j-1], dp[i-1][j])+grid[i][j]

        return dp[-1][-1]
    
# Last Stone Weight II
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = set()
        dp.add(0)

        target = sum(stones)//2

        for stone in stones:
            new = dp.copy()

            for n in dp:
                if n+stone <= target:
                    new.add(n+stone)
                
            dp = new

        return sum(stones) - max(dp)*2
    
# Interleaving String
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True
        if len(s3) != len(s2)+len(s1):
            return False

        for i in range(1, n+1):
            dp[0][i] |= dp[0][i-1] and s3[i-1] == s1[i-1]
        for i in range(1, m+1):
            dp[i][0] |= dp[i-1][0] and s3[i-1] == s2[i-1]

        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] |= dp[i-1][j] and s3[i+j-1] == s2[i-1]
                dp[i][j] |= dp[i][j-1] and s3[i+j-1] == s1[j-1]
        
        return dp[-1][-1]


# Stone Game
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0]*n for _ in range(n)]

        for i in range(n):
            dp[i][i] = piles[i]

        for length in range(2, n+1):
            for l in range(n-length+1):
                r = l+length-1
                dp[l][r] = max(piles[r]-dp[l][r-1], piles[l]-dp[l+1][r])

        return dp[0][-1] > 0
    
# Stone Game II
from functools import lru_cache
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix = [0]*(n+1)
        for i in range(n-1, -1, -1):
            suffix[i] = suffix[i+1]+piles[i]

        @lru_cache(None)
        def dp(M, i): #M, index

            if 2*M+i >= n:
                return suffix[i]
            best = 0
            for x in range(1, 2*M+1):
                other = dp(max(x, M), i+x)
                me = suffix[i]-other
                best = max(best, me)

            return best

        return dp(1, 0)
         
# Lemonade Change
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        twelve = 0

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five > 0:
                    five -= 1
                    ten += 1
                else:
                    return False
            else:
                if five > 0 and ten > 0:
                    five -= 1
                    ten -= 1
                    twelve += 1
                elif five > 1:
                    five -= 3
                    twelve += 1
                else:
                    return False

        return True
    

# Maximum Sum Circular Subarray
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        numsdouble = nums+nums
        maxans = float('-inf')
        curr = 0
        l = 0
        for r in range(len(numsdouble)):
            curr += nums[r]
            maxans = max(maxans, curr)
            if curr < 0 and l+len(nums) <= r:
                l = r+1
                curr = 0
        return maxans
    
# Longest Turbulent Subarray
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        flag = True
        curr = 1
        maxans = 1
        for i in range(1, len(arr)):
            if flag and arr[i-1] < arr[i]:
                flag = False
                curr += 1
            elif not flag and arr[i-1] > arr[i]:
                flag = True
                curr += 1
            else:
                flag = True
                curr = 1
            maxans = max(maxans, curr)

        flag = True
        curr = 1
        for i in range(1, len(arr)):
            if flag and arr[i-1] > arr[i]:
                flag = False
                curr += 1
            elif not flag and arr[i-1] < arr[i]:
                flag = True
                curr += 1
            else:
                flag = True
                curr = 1
            maxans = max(maxans, curr)

        return maxans


# Jump Game II
from collections import deque
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxlenght = 0
        ans = 0
        l = 0
        r = 0
        
        while r < n-1:
            ans += 1

            for j in range(l, r+1):
                maxlenght = max(maxlenght, j+nums[j])
            
            if maxlenght >= len(nums)-1:
                return ans
            else:
                l = r+1
                r = maxlenght

        return ans

# Binary Tree Inorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)


        dfs(root)
        return ans
    
# Binary Tree Preorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(root):
            if not root:
                return

            ans.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ans

# Binary Tree Postorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(root):
            if not root:
                return

            dfs(root.left)
            dfs(root.right)
            ans.append(root.val)

        dfs(root)
        return ans
    

# Insert into a Binary Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def dfs(root):
            nonlocal val
            if not root:
                return

            if val < root.val:
                dfs(root.left) if root.left else root.left = TreeNode(val)
            else:
                dfs(root.right) if root.right else root.right = TreeNode(val)

        dfs(root)
        return root
    
# Delete Node in a BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        def dfs(root):
            if not root:
                return
            
            if root.val == key:
                if root.right:
                    nxt = root.right
                    while nxt and nxt.left:
                        nxt = nxt.left
                    nxt.left = root.left
                    root = root.right
                else:
                    root = root.left
                return
            else:
                dfs(root.left)
                dfs(root.right)

        dfs(root)
        return root

# First Missing Positive
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        max_num = max(nums)
        heapq.heapify(nums)
        curr_min = 0

        while nums:
            t = heapq.heappop(nums)
            if t < 1:
                continue
            if curr_min+1 < t:
                return curr_min+1
            else:
                curr_min = curr_min+1

        return max_num+1


# Longest Palindromic Substring
"""
input: s: str
output res: str

assemtpitons
1 <= s.length <= 1000

ababd
bab


"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range((n))]
        ans_l, ans_r = 0, 0

        for lenght in range(1,n+1):
            for l in range(n-lenght+1):
                r = l+lenght-1

                if lenght <= 2:
                    if s[l] == s[r]:
                        dp[l][r] = True
                else:
                    if s[l] == s[r] and dp[l+1][r-1]:
                        dp[l][r] = True

                if ans_r-ans_l+1 < r-l+1 and dp[l][r]:
                    ans_r = r
                    ans_l = l

        return s[ans_l:ans_r+1]
    

# Stone Game III
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0]*(n+1)
        dp
        for i in range(n-1, -1, -1):
            best = float('-inf')
            total = 0
            for k in range(3):
                if i+k >=n:
                    break
                total += stoneValue[i+k]
                if total -dp[i+k+1] > best:
                    best = total-dp[i+k+1]
            dp[i] = best
        
        if dp[0] > 0:
            return 'Alice'
        elif dp[0] < 0:
            return 'Bob'
        else:
            return 'Tie'
            

# Last Stone Weight II
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        half = sum(stones)//2
        dp = [False]*(half+1)
        dp[0] = True

        for s in stones:
            for i in range(half+1):
                if dp[i] == True and i+s <= half:
                    dp[i+s] = True

        return dp[-1]
    
# Stone Game
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0]*(n) for _ in range(n)]
        for i in range(n):
            pass
        for lenght in range(2, n+1):
            for l in range(n-lenght+1):
                r = l+lenght-1

                if piles[r] - dp[l][r-1] > piles[l] - dp[l+1][r]:
                    dp[l][r] = piles[r] - dp[l][r-1]
                else:
                    dp[l][r] = piles[l] - dp[l+1][r]

        return True if dp[0][n-1] > 0 else False
    

# Burst Balloons
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1]+nums+[1]
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]

        for lenght in range(2, n+1):
            for l in range(n-lenght):
                r = l+lenght #0+2

                for k in range(l+1, r):
                    dp[l][r] = max(dp[l][r], dp[l][k]+nums[l]*nums[k]*nums[r]+dp[k][r])

        return dp[0][n-1]
    
# Accounts Merge
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        email_to_name = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a, b):
            root_a = find(a)
            root_b = find(b)
            if root_a != root_b:
                parent[root_b] = root_a

        for account in accounts:
            name = account[0]
            first_email =account[1]

            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name
                union(first_email, email)

        groups = defaultdict(list)

        for email in parent:
            root = find(email)
            groups[root].append(email)

        ans = []
        for root, emails in groups.items():
            name = email_to_name[root]
            ans.append([name]+sorted(emails))

        return ans


# Evaluate Division
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1/value))

        def dfs(cur, target, visited, product):
            if cur == target:
                return product
            
            visited.add(cur)

            for nei, weight in graph[cur]:
                if nei in visited:
                    continue

                result = dfs(nei, target, visited, product*weight)
                if result != -1.0:
                    return result
            return -1.0
        
        ans = []

        for start, end in queries:
            if start not in graph or end not in graph:
                ans.append(-1.0)
            else:
                ans.append(dfs(start, end, set(), 1.0))

        return ans


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        graph = defaultdict(list)
        degree = [0]*n

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

            degree[a] += 1
            degree[b] += 1

        queue = deque()

        for node in range(n):
            if degree[node] == 1:
                queue.append(node)

        remaining = 0

        while remaining > 2:
            leaf_count = len(queue)
            remaining -= leaf_count

            for _ in range(leaf_count):
                leaf = queue.popleft()

                for nei in graph[leaf]:
                    degree[nei] -= 1

                    if degree[nei] == 1:
                        queue.append(nei)

        return list(queue)


# Burst Balloons
"""
dp

[]
"""
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1]+nums[1]
        n = len(nums)

        dp = [[0]*n for _ in range(n)]

        for lenght in range(1, n+1):
            for l in range(n-lenght):
                r = l+lenght

                for k in range(l+1, r):
                    coins = dp[l][k] + nums[l]*nums[k]*nums[r]+ dp[k][r]
                    dp[l][r] = max(dp[l][r], coins)

        return dp[0][n-1]
    
def decode_string(s: str) -> str:
    stack = []
    current_stiring = ""
    current_number = 0

    for ch in s:
        if ch.isdigit():
            current_number = current_number*10+int(ch)
        elif ch =="[":
            stack.append((current_stiring, current_number))
            current_stiring = ""
            current_number = 0
        elif ch == "]":
            prev_string, repeat_count = stack.pop()
            current_stiring = prev_string+current_stiring*repeat_count
        else:
            current_stiring += ch

    return current_stiring

def click(board: List[List[int]], r: int, c:int) -> List[List[int]]:
    rows = len(board)
    cols = len(board[0])

    result = [[-1 for _ in range(cols)] for _ in range(rows)]

    if board[r][c] == 9:
        result[r][c] = 9
        return result
    
    if board[r][c] != 0:
        result[r][c] = board[r][c]
        return result
    
    if board[r][c] != 0:
        result[r][c] = board[r][c]
        return result
    
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    queue = deque()
    queue.append((r, c))
    result[r][c] = 0

    while queue:
        cur_r, cur_c = queuq.popleft()

        if board[cur_r][cur_c] != 0:
            continue

        for dr, dc in directions:
            nr = cur_r+dr
            nc = cur_c+dc

            if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                continue

            if result[nr][nc] != -1:
                continue

            if board[nr][nc] == 9:
                continue

            result[nr][nc] = board[nr][nc]

            if board[nr][nc] == 0:
                queue.append((nr, nc))
    return result


# Implement Stack Using Queues
"""
[1, 2, 3]
[2, 1, ]

"""
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()


    def push(self, x: int) -> None:
        self.q2 = self.q1.copy()
        self.q1.clear()
        self.q1.append(x)
        self.q1.extend(self.q2)
        self.q2.clear()

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return True if len(self.q1) == 0 else False        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


# Implement Stack Using Queues
"""
[1, 2, 3]

"""
class MyStack:

    def __init__(self):
        self.q1 = deque()

    def push(self, x: int) -> None:
        self.q1.reverse()
        self.q1.append(x)
        self.q1.reverse()

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return True if len(self.q1) == 0 else False        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# Implement Queue using Stacks
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if self.stack2:
            return self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

    def peek(self) -> int:
        if self.stack2:
            return self.stack2[-1]
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2[-1]
        
    def empty(self) -> bool:
        if not self.stack2 and not self.stack1:
            return True
        else:
            return False


# Online Stock Span
class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        consective = 1
        while self.stack and self.stack[-1][0] <= price:
            consective += self.stack[-1][1]
            self.stack.pop()
        self.stack.append(price, consective)
        return self.stack[-1][1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


# Simplify Path
class Solution:
    def simplifyPath(self, path: str) -> str:
        pathlist = path.split('/')
        res = []

        for s in pathlist:
            if res and s == '..':
                res.pop()
            elif  s != '.' or s != '..':
                res.append(s)

        return '/' + '/'.join(res)

# Decode String
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        currnum = 0
        currstr = ""

        for c in s:
            if c.isdecimal:
                currnum = currnum*10+int(c)
            elif c == '[':
                stack.append([currstr, currnum])
                currnum = 0
                currstr = ""
            elif c == ']':
                prevstr, prevcnt = stack.pop()
                currstr = prevstr+prevcnt*currstr
            else:
                currstr += c

        return currstr 


# Maximum Frequency Stack
class FreqStack:

    def __init__(self):
        self.freq_cnt = defaultdict(int)
        self.heap = []

        self.index = -1
        

    def push(self, val: int) -> None:
        self.freq_cnt[val] += 1
        heapq.heappush(self.heap, [-self.freq_cnt[val], self.index, val])
        self.index -= 1

    def pop(self) -> int:
        freq, i, value = heapq.heappop(self.heap)
        self.freq_cnt[value] -= 1
        return value
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()


# Maximum Frequency Stack
class FreqStack:

    def __init__(self):
        self.freq_cnt = defaultdict(int)
        self.freq_group = defaultdict(list)
        self.maxfreq = 0
        

    def push(self, val: int) -> None:
        self.freq_cnt[val] += 1
        self.maxfreq = max(self.maxfreq,  self.freq_cnt[val])
        self.freq_group[self.freq_cnt[val]].append(val)

    def pop(self) -> int:
        target = self.freq_group[self.maxfreq].pop()
        self.freq_cnt[target] -= 1
        if not self.freq_group[self.maxfreq]:
            del self.freq_group[self.maxfreq]
            self.maxfreq -= 1
        return target
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

