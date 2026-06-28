# A - Decisive Battle
# from collections import Counter
# S = input()
# s_cnt = Counter(S)

# if s_cnt['E'] > s_cnt['W']:
#     print('East')
# else:
#     print('West')

# B - Crop
# H, W = map(int, input().split())

# grid = [list(input()) for _ in range(H)]

# while grid and grid[0] == ['.'] * len(grid[0]):
#     grid.pop(0)

# while grid and grid[-1] == ['.'] * len(grid[0]):
#     grid.pop()

# while grid and all(row[0] == '.' for row in grid):
#     for row in grid:
#         del row[0]

# while grid and all(row[-1] == '.' for row in grid):
#     for row in grid:
#         del row[-1]

# for i in range(len(grid)):
#     print(''.join(grid[i]))

# C - Plumage Palette
# from collections import defaultdict

# N, M = map(int, input().split())
# m_change = []
# color_cnt = defaultdict(int)
# for i in range(N):
#     a, d, b = map(int, input().split())

#     m_change.append([d, a, b])
#     color_cnt[a] += 1

# result = defaultdict(int)
# first = len(color_cnt)

# m_change.sort()

# for d, a, b in m_change:
#     color_cnt[a] -= 1
#     if color_cnt[a] == 0:
#         del color_cnt[a]
#     color_cnt[b] += 1

#     result[d] = len(color_cnt)

# for m in range(1, M+1):
#     if result[m] == 0:
#         print(first)
#     else:
#         print(result[m])
#         first = result[m]

#C - Plumage PaletteはN+Mの計算量でいける。Mのfor文中で合計してN回しか動かしてないので
# from collections import defaultdict

# N, M = map(int, input().split())

# cnt = defaultdict(int)
# change = [[] for _ in range(M+1)]
# kind = 0

# for _ in range(N):
#     a, d, b = map(int, input().split())

#     if cnt[a] == 0:
#         kind += 1
#     cnt[a] += 1
#     change[d].append((a, b))

# for day in range(1, M+1):
#     for a, b in change[day]:
#         cnt[a] -= 1
#         if cnt[a] == 0:
#             kind -= 1

#         if cnt[b] == 0:
#             kind += 1
#         cnt[b] += 1
#     print(kind)


# D - Celester
# T = int(input())

# for _ in range(T):
#     N = int(input())
#     S = input()
#     X = list(map(int, input().split()))
#     Y = list(map(int, input().split()))

#     dp_S = 0 if S[0] == 'S' else -X[0]
#     dp_R = 0 if S[0] == 'R' else -X[0]

#     for i in range(1, N):
#         cost_S = 0 if S[i] == 'S' else -X[i]
#         cost_R = 0 if S[i] == 'R' else -X[i]

#         newS = max(dp_S + cost_S, dp_R + Y[i - 1] + cost_S)

#         newR = max(dp_S + cost_R, dp_R + cost_R)
#         dp_S, dp_R = newS, newR

#     print(max(dp_S, dp_R))

# B - Crop
# H, W = map(int, input().split())

# C = [input() for _ in range(H)]

# u, d = H, -1
# l, r = W, -1

# for i in range(H):
#     for j in range(W):
#         if C[i][j] == "#":
#             u, d = min(u, i), max(d, i)
#             l, r = min(j, l), max(r, j)

# for i in range(u, d+1):
#     print(C[i][l:r+1])

# 45度回転
# def rotate(a): return ["".join(r) for r in zip(*a[::-1])]

# H, W = map(int, input().split())
# C = [input() for _ in range(H)]

# for _ in range(4):
#     while not "#" in C[0]:
#         C = C[1:]
#     C = rotate(C)

# print(*C, sep = "\n")

# E - Fill-Rect Query
# H, W, Q = map(int, input().split())

# grid = [[0]*W for _ in range(H)]
# index_c = ['A']
# for i in range(Q):
#     r, c, x = input().split()
#     r = int(r)
#     c = int(c)
#     r -= 1
#     c -= 1
#     grid[r][c] = i+1
#     index_c.append(x)


# for i in range(H-1, -1, -1):
#     for j in range(W-1, -1, -1):
#         if i != 0: grid[i-1][j] = max(grid[i][j], grid[i-1][j])
#         if j != 0: grid[i][j-1] = max(grid[i][j], grid[i][j-1])

# for i in range(H):
#     print(''.join(index_c[grid[i][j]] for j in range(W) ))

# E - Fill-Rect Query
# from atcoder.lazysegtree import LazySegTree

# def op(a, b):
#     return max(a, b)

# def e():
#     return 0

# def mapping(f, x):
#     return max(f, x)

# def composition(f, x):
#     return max(f, x)

# def id_():
#     return 0

# H, W, Q = map(int, input().split())

# queries_by_R = [[] for _ in range(H)]

# index_c = ['A']

# for k in range(1, Q+1):
#     R, C, X = input().split()

#     R = int(R)-1
#     C = int(C)

#     queries_by_R[R].append((C, k))
#     index_c.append(X)

# seg = LazySegTree(op, e(), mapping, composition, id_(), [0]*W)

# ans = ['']*H

# for i in range(H-1, -1, -1):
#     for C, k in queries_by_R[i]:
#         seg.apply(0, C, k)

#     row = []

#     for j in range(W):
#         query_index = seg.get(j)
#         row.append(index_c[query_index])

#     ans[i] = ''.join(row)

# print('\n'.join(ans))

# D - Celester
# T = int(input())

# for i in range(T):
#     n = int(input())
#     s = input()
#     X = list(map(int, input().split()))
#     Y = list(map(int, input().split()))
#     Y = [0]+Y

#     dp = [[0]*2 for _ in range(n+1)]
#     dp[0][1] = float('-inf')

#     for i in range(1, n+1):
#         if s[i-1] == 'R': dp[i][0] = -X[i-1]
#         if s[i-1] == 'S': dp[i][1] = -X[i-1]

#         dp[i][0] = max(dp[i-1][0], dp[i-1][1]+Y[i-1])+dp[i][0]
#         dp[i][1] = max(dp[i-1][0], dp[i-1][1])+dp[i][1]
    
#     print(max(dp[-1]))


        
