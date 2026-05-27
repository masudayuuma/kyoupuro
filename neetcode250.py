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
    
