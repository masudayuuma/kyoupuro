# S = list(input())
# ans = []
# for a in S:
#     if a == 'A':
#         ans.append('A')
#     else:
#         ans.append('.')

# print("".join(ans))

# B - Break a Stick
# N = int(input())
# L = list(map(int, input().split()))
# ans = float('inf')
# for i in range(N-1):
#     ans = min(abs(sum(L[:i+1])-sum(L[i+1:])), ans)

# print(ans)


# C - On a Diet
# print(216519459+804733999+297250023)
# N, M, K = map(int, input().split())
# A = list(map(int, input().split()))
# days = [0]*N

# now_k = 0
# final_exam = -1
# for i in range(N):
#     if i-M >= 0:
#         final_exam += 1
#         now_k -= days[final_exam]
#     # print(now_k, i)
#     if now_k + A[i] <= K:
#         days[i] = A[i]
#         now_k += A[i]
#         print('Yes')
#     else:
#         print('No')

# D - Bomber Mad
# from collections import deque
# H, W, K = map(int, input().split())

# grid = [list(input()) for _ in range(H)]

# row_baku = set()
# col_baku = set()

# for i in range(H):
#     for j in range(W):
#         if grid[i][j] == '#':
#             row_baku.add(i)
#             col_baku.add(j)


# ans_grid = [[float('inf')]*W for _ in range(H)]
# q = deque()
# for i in range(H):
#     for j in range(W):
#         if grid[i][j] != '#' and i not in row_baku and j not in col_baku:
#             q.append((i, j))
#             ans_grid[i][j] = 0

# diff = ((1, 0), (-1, 0), (0, -1), (0, 1))



# while q:
#     i, j = q.popleft()
#     # print(i, j)
#     # print('a')
#     for dy, dx in diff:
#         y = dy+i
#         x = dx+j
#         # print(y, x)

#         if not 0 <= y < H or not 0 <= x < W or grid[y][x] == '#' or ans_grid[y][x] != float('inf'):
#             continue
#         # print('a')

#         ans_grid[y][x] = ans_grid[i][j]+1
#         q.append((y, x))

# ans = 0
# for i in range(H):
#     for j in range(W):
#         if ans_grid[i][j] <= K:
#             ans += 1

# print(ans)

# E - Odd Cycle
import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    graph = defaultdict(list)
    visited = set()

    for i in range(M):
        a, b = map(int, input().split())

        graph[a].append(b)
        graph[b].append(a)

    now = dict()
    ok = False
    ans = []
    cycle_s = -1
    def dfs(i, depth):
        global ok, cycle_s
        
        now[i] = depth
        visited.add(i)
        for ni in graph[i]:
            if ok:
                break
            if ni not in visited:
                dfs(ni, depth+1)
            elif ni in now and (depth+now[ni]) % 2 == 0:
                cycle_s = ni
                ok = True
                break
        if ok:
            ans.append(i)
        del now[i]


    for i in range(1, N+1):
        if i not in visited:
            dfs(i, 1)
            
            if ok:
                ans.reverse()
                idx = ans.index(cycle_s)
                ans = ans[idx:]
                print(len(ans))
                print(*ans)
                break

    if not ok:
        print(-1)
                

# c
# N, M, K = map(int, input().split())
# A = list(map(int, input().split()))
# s = 0

# for i in range(N):
#     if i >= M:
#         s -= A[i-M]
#     if s+A[i] <= K:
#         s += A[i]
#         print('Yes')
#     else:
#         A[i] = 0
#         print('No')

# d
# from collections import deque

# h, w, k = map((int, input().split()))
# s = [input() for _ in range(h)]

# r = [0]*h
# c = [0]*w
# for i in range(h):
#     for j in range(w):
#         if s[i][j] == "#":
#             r[i] = 1
#             c[i] = 1

# d = [[-1]*w for _ in range(h)]
# q = deque()

# for i in range(h):
#     for j in range(w):
#         if r[i] == c[j] == 0:
#             d[i][j] = 0
#             q.append((i, j))

# ans = 0
# while q:
#     i, j = q.popleft()
#     if d[i][j] <= k:
#         ans += 1

#     for ni, nj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
#         if 0 <= ni < h and 0 <= nj < w:
#             if s[ni][nj] == '.' and d[ni][nj] ==-1:
#                 d[ni][nj] == '.' and d[ni][nj] == -1:
#                 d[ni][nj] == d[i][j]+1
#                 q.append((ni, nj))

# print(ans)

