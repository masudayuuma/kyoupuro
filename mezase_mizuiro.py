#https://qiita.com/e869120/items/eb50fdaece12be418faa

#1　ITP1_7_B - How Many Ways?　基本問題です。
# count_list = []
# while True:
#     n, x = map(int, input().split())
#     count = 0
#     if n == 0:
#         for i in range(len(count_list)):
#             print(count_list[i])
#         exit()
#     for i in range(1, n-1):
#         for j in range(i+1, n):
#             for k in range(j+1, n+1):
#                 if i+j+k == x:
#                     count += 1
#     count_list.append(count) 

#2　AtCoder Beginner Contest 106 B - 105
# N = int(input())

# total = 0
# for i in range(1, N+1):
#     count = 0
#     if i%2 == 1:
#         for j in range(1, N+1):
#             if i%j == 0:
#                 count += 1
#         if count == 8:
#             total += 1

# print(total)


#4 C - カラオケ
# N, M = map(int, input().split())
# A = [ list(map(int, input().split())) for _ in range(N)]

# total_scores = 0
# for s in range(M-1):
#     for r in range(s, M):
#         cnt = 0
#         for k in range(N):
#             cnt += max(A[k][s], A[k][r])
#         total_scores = max(total_scores, cnt)

# print(total_scores)

#5　AtCoder Beginner Contest 095 C - Half and Half
# A, B, C, X, Y = map(int, input().split())

# min_hulf_pizza = 0

# price = 0
# if (A+B)/2 < C:
#     print(A*X+B*Y)
# else:
#     if X == Y:
#         print(X*C*2)
#     elif X > Y and A < 2*C:
#         diff = X-Y
#         print(Y*2*C + A*diff)
#     elif Y > X and B < 2*C:
#         diff = Y-X
#         print(X*2*C + B*diff)
#     else:
#         max_hurf_pizza = max(X, Y)
#         print(C*max_hurf_pizza*2)


#8　Square869120Contest #6 B - AtCoder Markets　全探索すると無数に通り数があるように見えますが、ひとつ工夫すると現実的な通り数で全列挙できる問題です。

#10　ALDS_5_A - 総当たり　基本問題です。
# import sys
# input = sys.stdin.readline

# n = int(input())
# A = list(map(int, input().split()))
# q = int(input())
# M = list(map(int, input().split()))
#TLEしちゃう
# for m in(M):
#     found = False
#     for mask in range(1<<n):
#         if found == True:
#             break
#         cnt = 0
#         for i in range(n):
#             if mask & (1<<i):
#                 cnt += A[i]
#         if cnt == m:
#             print("yes")
#             found = True
#             break
#     if not found:
#         print("no")
#これだといけた
# possible_sums = set()
# for mask in range(1 << n):
#     cnt = 0
#     for i in range(n):
#         if mask & (1 << i):
#             cnt += A[i]
#         possible_sums.add(cnt)

# for m in M:
#     if m in possible_sums:
#         print("yes")
#     else:
#         print("no")

#11　AtCoder Beginner Contest 128 C - Switches
# N, M = map(int, input().split())
# S = []
# # K = []
# for _ in range(M):
#     k, *swhiches = map(int, input().split())
#     # K.append(k)
#     S.append([s-1 for s in swhiches])

# P = list(map(int, input().split()))

# ans = 0
# for mask in range(1 << N):
#     ok = True
#     for i in range(M):
#         cnt = 0
#         for s in S[i]:
#             if mask & (1 << s):
#                 cnt += 1

#         if cnt % 2 != P[i]:
#             ok = False
#             break

#     if ok == True:
#         ans += 1

# print(ans)
    
#12　AtCoder Beginner Contest 002 D - 派閥






#15　AtCoder Beginner Contest 145 C - Average Length
# import itertools, math, sys
# input = sys.stdin.readline

# N = int(input())
# x_y = [list(map(int, input().split())) for _ in range(N)]

# dist = [[0.0]*N for _ in range(N)]
# for i in range(N):
#     xi, yi = x_y[i]
#     for j in range(i+1, N):
#         xj, yj = x_y[j]
#         d = math.hypot(xi-xj, yi-yj)
#         dist[i][j] = dist[j][i] = d

# total = 0.0
# for perm in itertools.permutations(range(N)):
#     path = 0.0
#     for a, b in zip(perm, perm[1:]):
#         path += dist[a][b]
#     total += path

# avg = total/math.factorial(N)
# print(avg)


#18 ALDS_4_B - 二分探索　基本問題です。map でも解けますが二分探索で解いてみてください。
# import sys
# input = sys.stdin.readline

# def question(m, num):
#     return S[m] >= num

# def binarySarch(num):
#     global cnt
#     ng = -1
#     ok = n
#     while(ok - ng > 1):
#         m = (ng+ok)//2
#         if (question(m, num)): 
#             ok = m
#         else:
#             ng = m
#     if S[ok] == num:
#         cnt += 1
        
# n = int(input())
# S = list(map(int, input().split()))
# q = int(input())
# T = list(map(int, input().split()))
# cnt = 0
# for t in T:
#     binarySarch(t)

# print(cnt)


#19　JOI 2009 本選 2 - ピザ　できた
# import sys
# input = sys.stdin.readline

# L = int(input())
# n = int(input())
# q = int(input())
# S = [0]
# T = []
# for _ in range(n-1):
#     s = int(input())
#     S.append(s)

# for _ in range(q):
#     t = int(input())
#     T.append(t)

# S.append(L)
# S.sort()

# cnt = 0
# for i in T:
#     ok = n
#     ng = 0
#     while ok - ng > 1:
#         m = (ok+ng)//2
#         if S[m] >= i:
#             ok = m
#         else:
#             ng = m
        
#     cnt += min(S[ok]-i, i-S[ng])

# print(cnt)

#20　AtCoder Beginner Contest 077 C - Snuke Festival　面白いです。
# import sys, bisect
# input = sys.stdin.readline

# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# C = list(map(int, input().split()))

# A.sort()
# B.sort()
# C.sort()
# total = 0
# for b in B:
#     A_cnt = bisect.bisect_left(A, b)
#     C_cnt = len(C) - bisect.bisect_right(C, b)
#     total += A_cnt * C_cnt

# print(total)

#21　AtCoder Beginner Contest 023 D - 射撃王　教育的に良いです。
# import sys
# input = sys.stdin.readline 
# N = int(input())
# H = []
# S = []
# for _ in range(N):
#     h, s = map(int, input().split())
#     H.append(h)
#     S.append(s)

# ok = 10**18
# ng = 0

# while ok - ng > 1:
#     mid = (ok + ng) // 2
#     flag = True
#     t = [0] * N
#     for i in range(N):
#         if (mid < H[i]):
#             flag = False
#         else:
#             t[i] = (mid - H[i]) // S[i]

#     t.sort()
#     for i in range(N):
#         if (t[i] < i):
#             flag = False

#     if flag:
#         ok = mid
#     else:
#         ng = mid

# print(ok)

#22
#23


#24　ALDS_11_B - 深さ優先探索　基本問題です。
# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# N = int(input())
# G = [[] for _ in range(N+1)]

# for _ in range(N):
#     data = list(map(int, input().split()))
#     u, k, *vs = data
#     G[u] = vs

# time = 0
# d = [0] * (N+1)
# f = [0] * (N+1)
# visited = [False] * (N+1)

# def dfs(v):
#     global time
#     if visited[v]:
#         return
    
#     visited[v] = True
#     time += 1
#     d[v] = time

#     for vv in G[v]:
#         dfs(vv)

#     time += 1
#     f[v] = time


# for v in range(1, N+1):
#     if not visited[v]:
#         dfs(v)
    
# for v in range(1, N+1):
#     print(v, d[v], f[v])


#25　AOJ 1160 - 島はいくつある？　グラフの連結成分数は、深さ優先探索で計算できます。
# import sys
# sys.setrecursionlimit(10**6)

# island_count = []
# while True:
#     island_nums = 0
#     W, H = map(int, input().split())
#     if W==0 and H==0:
#         break
    
#     C = [list(map(int, input().split())) for _ in range(H)]
    
#     seen = [[False]*W for _ in range(H)]
    
#     def dfs(h, w):
#         seen[h][w] = True
#         for i in (-1, 0, 1):
#             for j in (-1, 0, 1):
#                 if h+i >= H or w+j >= W or h+i<0 or w+j <0:
#                     continue
#                 if C[h+i][w+j] == 1 and seen[h+i][w+j] == False:
#                     dfs(h+i, w+j)
#         C[h][w] = 0


#     for i in range(H):
#         for j in range(W):
#             if C[i][j] == 1:
#                 dfs(i, j)
#                 island_nums += 1
#     island_count.append(island_nums)

# for i in island_count:
#     print(i)


#26　AtCoder Beginner Contest 138 D - Ki　木構造の問題の多くは、深さ優先探索を使います。 これだとTLEしちゃう
# import sys
# sys.setrecursionlimit(10**7)

# input =sys.stdin.readline

# N, Q = map(int, input().split())
# connection = [[] for _ in range(N+1)]

# for i in range(N-1):
#     a, b = map(int, input().split())
#     connection[b].append(a)
#     connection[a].append(b)


# n_point = [0 for _ in range(N+1)]
# visited = [False for _ in range(N+1)]
# n_cnt = [0] * (N+1)


# for _ in range(Q):
#     p, x = map(int, input().split())
#     n_point[p] += x 


# def dfs(p, x):
#     if visited[p]:
#         return

#     visited[p] = True
    
#     if n_point[p]:
#         point = n_point[p] + x
#     else:
#         point = x

#     n_cnt[p] += point

#     for c in connection[p]:
#         if visited[c]:
#             continue

#         dfs(c, point)   

# dfs(1, 0)

# print(" ".join(map(str, n_cnt[1:])))

#27　JOI 2009 予選 4 - 薄氷渡り　深さ優先探索は、木構造だけではありません、ということを教えてくれる問題です。再帰関数を使って解けます。
# import sys
# sys.setrecursionlimit(10**7)
# input = sys.stdin.readline

# m = int(input())
# n = int(input())
# ice_square = [list(map(int, input().split())) for _ in range(n)]

# dist = ((0,1), (0,-1), (1,0), (-1,0))
# max_depth = 0
# now_depth = 0

# def dfs(i, j, depth):
#     global now_depth
#     depth += 1
#     ice_square[i][j] = 0
#     for dy, dx in dist:
#         ny = i + dy
#         nx = j + dx
#         if 0 <= nx < m and 0 <= ny < n and ice_square[ny][nx]:
#             dfs(ny, nx, depth)
#     ice_square[i][j] = 1
#     now_depth = max(now_depth, depth)

# for i in range(n):
#     for j in range(m):
#         if ice_square[i][j]:
#             now_depth = 0
#             dfs(i, j, 0)
#             max_depth = max(max_depth, now_depth)

# print(max_depth)


#28　ALDS_11_C - 幅優先探索　基本問題です。
# from collections import deque
# import sys
# input = sys.stdin.readline
# inf = 10**10

# n = int(input())
# network = [[] for _ in range(n+1)]
# length_list = [inf for _ in range(n+1)]
# visited_list = [0 for _ in range(n+1)]

# for _ in range(n):
#     inputs = list(map(int, input().split()))
#     u, k = inputs[:2]
#     v = inputs[2:]
#     network[u] += v

# que = deque()

# que.append(1)
# length_list[1] = 0

# while que:
#     node = que.popleft()
#     visited_list[node] = 1

#     for i in network[node]:
#         if visited_list[i]:
#             continue

#         que.append(i)
#         visited_list[i] = 1

#         if length_list[i] > length_list[node]+1:
#             length_list[i] = length_list[node]+1

# for i in range(1, n+1):
#     if length_list[i] == inf:
#         print(i, -1)
#     else:
#         print(i, length_list[i])

#29　AtCoder Beginner Contest 007 C - 幅優先探索　重み無しグラフの最短経路問題は、幅優先探索で解けます。
# from collections import deque
# import sys
# input = sys.stdin.readline
# inf = 10**10

# R, C = map(int, input().split())
# Sy, Sx = map(int, input().split())
# Gy, Gx = map(int, input().split())

# C_list = list(input() for _ in range(R))

# Sy -= 1
# Sx -= 1
# Gy -= 1
# Gx -= 1

# visited = [[False] * C  for _ in range(R)]
# length = [[inf] * C for _ in range(R)]

# que = deque()
# now = [Sy, Sx]
# que.append(now)
# visited[Sy][Sx] = 1
# length[Sy][Sx] = 0

# while que:
#     y,x = que.popleft()

#     for dy, dx in ((-1,0), (1,0), (0,1), (0,-1)):
#         ny = dy+y
#         nx = dx+x

#         if visited[ny][nx] or C_list[ny][nx] == '#':
#             continue

#         visited[ny][nx] = True
#         que.append([ny, nx])

#         if length[ny][nx] > length[y][x] +1:
#             length[ny][nx] = length[y][x] +1

# print(length[Gy][Gx])

# 30　JOI 2011 予選 5 - チーズ
# 31　JOI 2012 予選 5 - イルミネーション　少し実装が重いですが、頑張れば解けます。
# 32　AOJ 1166 - 迷図と命ず　実装が少し重いです。
# 33　AtCoder Beginner Contest 088 D - Grid Repainting　これが解ければ、幅優先探索に慣れたと思って良いです。


#34　ALDS_10_A - フィボナッチ数　超基本。「DP とは何か」を感じることができます。
# num = int(input())

# dp = [0]*(50)
# dp[0] = 1
# dp[1] = 1

# if num == 0 or num == 1:
#     print(1)
#     exit()

# for n in range(2, num+1):
#     dp[n] = dp[n-1] + dp[n-2]

# print(dp[num])


#35　DPL_1_B - 0,1ナップザック問題　基本問題です。（基本的なナップザック）
# N, W = map(int, input().split())
# value = []
# weight = []

# for _ in range(N):
#     v, w = map(int, input().split())
#     value.append(v)
#     weight.append(w)

# dp = [[0]*(W+1) for _ in range(N+1)]

# for i in range(1, N+1):
#     for j in range(1, W+1):
#         dp[i][j] = max(dp[i][j-1], dp[i-1][j])
#         if j >= weight[i-1]:
#             dp[i][j] = max(dp[i][j], dp[i-1][j-weight[i-1]]+value[i-1])

# print(dp[N][W])

#36　DPL_1_C - ナップザック問題　基本問題です。
# N, W = map(int, input().split())
# dp = [0] * (W+1)
# for i in range(N):
#     v, w = map(int, input().split())
#     for j in range(w, W+1):
#         dp[j] = max(dp[j-w] + v, dp[j])
# print(dp[W])

#37　DPL_1_A - コイン問題　基本問題です。
# import sys 
# input = sys.stdin.readline

# N, M = map(int, input().split())
# C = list(map(int, input().split()))
# dp = [10000000] * (N+1)
# dp[0] = 0
# for i in range(1, M+1):
#     if N >= C[i-1]:    
#         for j in range(C[i-1], N+1):
#             dp[j] = min(dp[j-C[i-1]] + 1, dp[j])

# print(dp[N])

#38　ALDS_10_C - 最長共通部分列　基本問題です。模範解答ではあったけどTLEしたので文字列の小さいほうを外ループにすると通った
# import 
# input = sys.stdin.readline

# q = int(input())
# ans_list = []

# for _ in range(q):
#     x = input().strip()
#     y = input().strip()
#     dp = [[0]*(len(x)+1) for _ in range(len(y)+1)]
    
#     for i in range(1, len(y)+1):
#         for j in range(1, len(x)+1):
#             dp[i][j] = max(dp[i-1][j], dp[i][j-1])
#             if y[i-1] == x[j-1]:
#                 dp[i][j] = max(dp[i-1][j-1]+1, dp[i-1][j], dp[i][j-1])

#     ans_list.append(dp[len(y)][len(x)])

# for ans in ans_list:
#     print(ans)


#39　JOI 2011 予選 4 - 1 年生 DPmuzuinatteomota
# N = int(input())
# X = list(map(int, input().split()))

# DP = [[0]*N for _ in range(21)]
# DP[X[0]][0] = 1

# for n in range(1, N-1):
#     for sum in range(21):
#         plus = sum + X[n]
#         minus = sum - X[n]
#         if 0 <= plus <= 20:
#             DP[plus][n] += DP[sum][n-1]
#         if 0 <= minus <= 20:
#             DP[minus][n] += DP[sum][n-1]

# print(DP[X[N-1]][N-2])


#40　JOI 2012 予選 4 - パスタ
#dp[][][0]は前日とは違うものを食べた時、dp[][][1]は前日と同じものを食べるとき
# N, K = map(int, input().split())
# fixed_days = {}

# for _ in range(K):
#     day, pasta = map(int, input().split())
#     fixed_days[day] = pasta -1

# dp = [[[0] * 2 for _ in range(3)] for _ in range(N+1)]

# if 1 in fixed_days:
#     pasta = fixed_days[1]
#     dp[1][pasta][0] = 1
# else:
#     for pasta in range(3):
#         dp[1][pasta][0] = 1

# for day in range(2, N+1):
#     for today_pasta in range(3):
#         for yestaday_pasta in range(3):
#             if today_pasta != yestaday_pasta:
#                 dp[day][today_pasta][0] += dp[day-1][yestaday_pasta][0]
#                 dp[day][today_pasta][0] += dp[day-1][yestaday_pasta][1]
#             else:
#                 dp[day][today_pasta][1] += dp[day-1][yestaday_pasta][0]

#         else:
#             dp[day][today_pasta][0] %= 10000
#             dp[day][today_pasta][1] %= 10000

#     if day in fixed_days:
#         pasta = fixed_days[day]
#         for p in range(3):
#             if p != pasta:
#                 dp[day][p][0] = 0
#                 dp[day][p][1] = 0

# total = 0
# for pasta in range(3):
#     total += dp[N][pasta][0]
#     total += dp[N][pasta][1]

# print(total % 10000)

#41　JOI 2013 予選 4 - 暑い日々
# INF = 10**9
# d, n = map(int, input().split())
# t = [int(input()) for i in range(d)]
# a = [0] *n
# b = [0]*n
# c = [0]*n
# for i in range(n):
#     a[i], b[i], c[i] = map(int, input().split())
# dp = [[0] *n for i in range(d)]

# #初期設定
# for i in range(n):
#     if not (a[i] <= t[0] <= b[i]):
#         dp[0][i] = -INF

# #DP
# for i in range(1, d):
#     for j in range(n):
#         if not (a[j] <= t[i] <= b[j]):
#             dp[i][j] = -INF
#         else:
#             for k in range(n):
#                 dp[i][j] = max(dp[i][j], dp[i-1][k] + abs(c[k] - c[j]))
# print(max(dp[d-1]))

#42　JOI 2015 予選 4 - シルクロード
# n, m = map(int, input().split())
# INF = 10**9

# kyori = [0]*(n)
# for i in range(n):
#     k = int(input())
#     kyori[i] = k

# tenki = [0]*(m)
# for i in range(m):
#     t = int(input())
#     tenki[i] = t

# dp = [[INF]*(n+1) for _ in range(m+1)]
# dp[0][0] = 0

# for kigenn in range(1, m+1):
#     dp[kigenn][0] = 0
#     for tosi in range(1, n+1):
#         dp[kigenn][tosi] = min(dp[kigenn-1][tosi], dp[kigenn-1][tosi-1]+ tenki[kigenn-1]*kyori[tosi-1])

# print(dp[-1][-1])

#43　パ研杯2019 D - パ研軍旗
# N = int(input())
# S = list(input() for _ in range(5))

# dp = [[10000]*N for _ in range(3)]

# R_1 = 0
# B_1 = 0
# W_1 = 0

# for i in range(5):
#     if S[i][0] == "R":
#         R_1 += 1
#     if S[i][0] == "B":
#         B_1 += 1
#     if S[i][0] == "W":
#         W_1 += 1

# dp[0][0] = 5 -R_1
# dp[1][0] = 5-B_1
# dp[2][0] = 5-W_1

# for i in range(1, N):
#     for j in range(3):
#         R_n = 0
#         B_n = 0
#         W_n = 0
#         for k in range(5):
#             if S[k][i] == "R":
#                 R_n += 1
#             if S[k][i] == "B":
#                 B_n += 1
#             if S[k][i] == "W":
#                 W_n += 1
#         if j == 0:
#             dp[j][i] = 5-R_n + min(dp[j-1][i-1], dp[j-2][i-1])
#         if j == 1:
#             dp[j][i] = 5-B_n + min(dp[j-1][i-1], dp[j-2][i-1])
#         if j == 2:
#             dp[j][i] = 5-W_n + min(dp[j-1][i-1], dp[j-2][i-1])

# print(min(dp[0][-1], dp[1][-1], dp[2][-1])) 