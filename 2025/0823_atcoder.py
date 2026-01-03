# A - What month is it?
# X, Y = map(int, input().split())

# ans = (X+Y)%12
# if ans == 0:
#     print(12)
# else:
#     print(ans)

# B - Most Minority
# N, M = map(int, input().split())
# S = []
# ans = [0]*N
# for n in range(N):
#     s = input()
#     S.append(s)

# for m in range(M):
#     ans_X = 0
#     ans_Y = 0
#     for n in range(N):
#         if S[n][m] == '0':
#             ans_X += 1
#         elif S[n][m] == '1':
#             ans_Y += 1
#     if ans_X == 0 or ans_Y == 0:
#         for i in range(N):
#             ans[i] += 1
#         continue

#     if ans_X > ans_Y:
#         for n in range(N):
#             if S[n][m] == '1':
#                 ans[n] += 1
#     elif ans_X < ans_Y:
#         for n in range(N):
#             if S[n][m] == '0':
#                 ans[n] += 1

# max_score = max(ans)
# result = []
# for i in range(N):
#     if ans[i] == max_score:
#         result.append(i + 1) 

# print(*result)

# C - Sum of Min Query
# N, Q = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# min_list = []
# ans = 0
# for i in range(N):
#     n = min(A[i], B[i])
#     min_list.append(n)
#     ans += n

# for i in range(Q):
#     c, x, v = map(str, input().split())
#     x = int(x)-1
#     v = int(v)

#     before_min = min_list[x]

#     if c == 'A':
#         A[x] = v
#         after_min = min(A[x], B[x])
#     else:
#         B[x] = v
#         after_min = min(A[x], B[x])

#     diff = after_min - before_min
#     min_list[x] = after_min
#     ans += diff
#     print(ans)


# D - Toggle Maze
# from collections import deque

# h, w = map(int, input().split())
# a = [input() for _ in range(h)]
# sx, sy, gx, gy = -1, -1, -1, -1
# for i in range(h):
#     for j in range(w):
#         if a[i][j] == 'S':
#             sx, sy =  i, j
#         if a[i][j] =='G':
#             gx, gy = i, j

# INF = 10**9
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# d = [[[INF] * w for _ in range(h)] for _ in range(2)]
# q = deque()
# q.append((0, sx, sy))
# d[0][sx][sy] = 0
# while q:
#     c, x, y = q.popleft()
#     for k in range(4):
#         xx, yy = x+dx[k], y+dy[k]
#         if (
#             not (0 <= xx < h and 0 <= yy < w)
#             or a[xx][yy] == '#'
#             or (c == 0 and a[xx][yy] == 'x')
#             or (c == 1 and a[xx][yy] == 'o')
#         ):
#             continue
#         # XOR
#         cc = c ^ (a[xx][yy] == '?')
#         if d[cc][xx][yy] != INF:
#             continue
#         q.append((cc, xx, yy))
#         d[cc][xx][yy] = d[c][x][y] + 1
# ans = min(d[0][gx][gy], d[1][gx][gy])
# print(-1 if ans == INF else ans)



# E - Reachability Query
# from atcoder.dsu import DSU
# N, Q = map(int, input().split())
# uf = DSU(N)
# is_B = [False]*N
# black_cnt = [0]*N

# for i in range(Q):
#     q = list(map(int, input().split()))
#     if q[0] == 1:
#         u, v = q[1] - 1, q[2] - 1 
#         root_u = uf.leader(u)
#         root_v = uf.leader(v)

#         if root_u != root_v:
#             total_black = black_cnt[root_u] + black_cnt[root_v]
#             uf.merge(u, v)
#             new_root = uf.leader(u)
#             black_cnt[new_root] = total_black
#     elif q[0] == 2:
#         v = q[1]-1
#         root = uf.leader(v)
#         if is_B[v]:
#             is_B[v] = False
#             black_cnt[root] -= 1
#         else:
#             is_B[v] = True
#             black_cnt[root] += 1
#     else:
#         v = q[1] -1
#         root = uf.leader(v)
#         if black_cnt[root] > 0:
#             print('Yes')
#         else:
#             print('No')
    
