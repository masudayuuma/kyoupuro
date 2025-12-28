# A11 - Binary Search 1
#めぐる式
# N, X = map(int, input().split())
# A = list(map(int, input().split()))

# ng = -1
# ok = N
# while ok - ng > 1:
#     mid = (ok + ng) // 2
#     if X <= A[mid]:
#         ok = mid
#     else:
#         ng = mid

# print(ok+1)

#普通
# N, X = map(int, input().split())
# A = list(map(int, input().split()))

# left = 0
# right = N-1
# flag = False
# while left <= right:
#     mid = (left+right)//2
#     if A[mid] > X:
#         right = mid-1
#         continue
#     if A[mid] < X:
#         left = mid+1
#         continue

#     flag = True
#     break

# if flag == True:
#     print(mid+1)
# else:
#     print(-1)    

# ライブラリ使用
# from bisect import bisect_right, bisect_left
# N, X = map(int, input().split())
# A = list(map(int, input().split()))

# print(bisect_left(A, X)+1)

# A12 - Printer
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

# right = 10**9
# left = 1

# while left < right:
#     mid = (left+right)//2
#     num = 0
    
#     for i in A:
#         num += mid//i
#     # print(mid, num)
#     if num >= K:
#         right = mid
#     if num < K:
#         left = mid+1
    
# print(right)


# A13 - Close Pair
# 配列のスライスはTLEなる
# from bisect import bisect_left
# N, K =map(int, input().split())
# A = list(map(int, input().split()))

# ans = 0
# for i in range(N-1):
#     target = A[i]+K
    
#     num = bisect_left(A, target+1)
#     # print(num)
#     ans += max(0, num-(i+1))
    
# print(ans)

# A14 - Four Boxes
# set版
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))
# B_list = list(map(int, input().split()))
# C_list = list(map(int, input().split()))
# D_list = list(map(int, input().split()))

# A_B_list = []
# C_D_list = []
# for i in range(N):
#     for j in range(N):
#         A_B_list.append(A_list[i]+B_list[j])
#         C_D_list.append(C_list[i]+D_list[j])
# C_D_list = set(C_D_list)

# for i in range(N**2):
#     if K-A_B_list[i] in C_D_list:
#         print('Yes')
#         exit()

# print('No')

# 2分探索
# from bisect import bisect_left
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))
# B_list = list(map(int, input().split()))
# C_list = list(map(int, input().split()))
# D_list = list(map(int, input().split()))

# A_B_list = []
# C_D_list = []
# for i in range(N):
#     for j in range(N):
#         A_B_list.append(A_list[i]+B_list[j])
#         C_D_list.append(C_list[i]+D_list[j])
# C_D_list.sort()

# for A_B_num in A_B_list:
#     n = bisect_left(C_D_list, K-A_B_num)
#     if n < len(C_D_list) and C_D_list[n] == K -A_B_num:
#         print('Yes')
#         exit()

# print('No')


# A15 - Compression
# from bisect import bisect_left
# N = int(input())
# A = list(map(int, input().split()))

# set_sort_A = sorted(list(set(A)))
# after_A = []
# for a in range(N):
#     ans = bisect_left(set_sort_A, A[a])
#     after_A.append(ans+1)

# print(*after_A)

# A16 - Dungeon 1（※初版第 1 刷の B22 も同じ問題です）
# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# minitu_dp = [0]*N
# minitu_dp[0] = 0
# minitu_dp[1] = A[0]


# for i in range(2, N):
#     min_minitu = min(minitu_dp[i-2]+B[i-2], minitu_dp[i-1]+A[i-1])
#     minitu_dp[i] = min_minitu
#     # print(min_minitu)

# print(minitu_dp[-1])

# A17 - Dungeon 2
# INF = 10**8
# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# minitu_dp = [[INF, -1] for _ in range(N)]
# minitu_dp[0] = [0, -1]
# minitu_dp[1] = [A[0], 0]

# for i in range(2, N):
#     min_cost_i = -1
#     min_cost = min(minitu_dp[i-2][0]+B[i-2], minitu_dp[i-1][0]+A[i-1])
#     if min_cost == minitu_dp[i-2][0]+B[i-2]:
#         min_cost_i = i-2
#     else:
#         min_cost_i = i-1

#     minitu_dp[i] = [min_cost, min_cost_i]
#     # print(minitu_dp[i])

# path = []
# j = N-1
# while j != -1:
#     path.append(j+1)
#     j = minitu_dp[j][1]

# path.reverse()
# print(len(path))
# print(*path)


# A18 - Subset Sum
# N, S = map(int, input().split())
# A = list(map(int, input().split()))
# # A.sort()
# cnt_S_dp = [False for _ in range(S+1)]
# cnt_S_dp[0] =True

# for i in range(N):
#     # print(cnt_S_dp)
#     for j in range(S, A[i]-1, -1):
#         if cnt_S_dp[j-A[i]] == True:
#             cnt_S_dp[j] = True

# # print(cnt_S_dp)
# if cnt_S_dp[-1] == True:
#     print('Yes')
# else:
#     print('No')

# A19 - Knapsack 1
# N, W = map(int, input().split())
# napzac = []
# for i in range(N):
#     w, v = map(int, input().split())
#     napzac.append((w, v))

# dp = [[0]*(W+1) for _ in range(N+1)]

# for i in range(1, N+1):
#     w, v = napzac[i-1]
#     for j in range(W+1):
#         dp[i][j] = dp[i-1][j]
#         if 0 <= j-w <= W:
#             # print(dp[i][j])
#             dp[i][j] = max(dp[i][j], dp[i-1][j-w]+v)
#         # print(dp[i][j])

# print(dp[-1][-1])

# A20 - LCS
# N = input()
# T = input()
# n, t = len(N), len(T)
# dp = [[0]*(t+1) for _ in range(n+1)]

# for i in range(1, n+1):
#     for j in range(1, t+1):
#         max_cnt = max(dp[i-1][j], dp[i][j-1])
#         if N[i-1] == T[j-1]:
#             max_cnt = max(max_cnt, dp[i-1][j-1]+1)
#         dp[i][j] = max_cnt
#             # print(max_cnt)
        
        
# print(dp[-1][-1])


# A21 - Block Game
#区間DP
# N = int(input())
# P = [None]*(N+1)
# A = [None]*(N+1)

# for i in range(1, N+1):
#     P[i], A[i] = map(int, input().split())

# dp = [[None]*(N+1) for i in range(N+1)]
# dp[1][N] = 0
# for LEN in reversed(range(0, N-1)):
#     for l in range(1, N-LEN+1):
#         r = l+LEN

#         score1 = 0
#         if l>= 2 and l <= P[l-1] and P[l-1] <= r:
#             score1 = A[l-1]

#         score2 = 0
#         if r <=N-1 and l <= P[r+1] and P[r+1]<= r:
#             score2 = A[r+1]

#         if l == 1:
#             dp[l][r] = dp[l][r+1] + score2
#         elif r==N:
#             dp[l][r] = dp[l-1][r] + score1
#         else:
#             dp[l][r] = max(dp[l-1][r] + score1, dp[l][r+1]+score2)

# ans = 0
# for i in range(1, N+1):
#     ans = max(ans, dp[i][i])
# print(ans)


# A22 - Sugoroku
#到達していないマスを考慮
# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# INF = -10**8
# max_score_dp = [INF]*(N+1)
# max_score_dp[1] = 0

# for i in range(N-1):
#     if max_score_dp[i+1] == INF:
#         continue
#     max_score_dp[A[i]] = max(100+max_score_dp[i+1], max_score_dp[A[i]])
#     max_score_dp[B[i]] = max(150+max_score_dp[i+1], max_score_dp[B[i]])

# print(max_score_dp[N])

# # A23 - All Free
# N, M = map(int, input().split())

# coupons = []
# for i in range(M):
#     A = list(map(int, input().split()))
#     mask = 0
#     for j in range(N):
#         if A[j] == 1:
#             mask |= (1 << j)
#     coupons.append(mask)

# INF = float('inf')
# dp = [[INF] * (1 << N) for _ in range(M+1)]

# dp[0][0] = 0
# for i in range(1, M+1):
#     coupons_mask = coupons[i-1]

#     for mask in range(1 << N):
#         dp[i][mask] = dp[i-1][mask]

#         for prev_mask in range(1 << N):
#             if (prev_mask | coupons_mask) == mask:
#                 if dp[i-1][prev_mask] != mask:
#                     if dp[i-1][prev_mask] != INF:
#                         dp[i][mask] = min(dp[i][mask], dp[i-1][prev_mask]+1)

# all_items = (1 << N)-1
# ans = dp[M][all_items]

# if ans == INF:
#     print(-1)
# else:
#     print(ans)

# A24 - LIS
#without dp
# from bisect import bisect_right, bisect_left
# N = int(input())
# A = list(map(int, input().split()))

# L = [float('inf')]*N

# for i in range(N):
#     index = bisect_left(L, A[i])
#     L[index] = A[i]
    
# ans = bisect_left(L, float('inf'))
# print(ans)

#use dp
#復元とかも考えるならこっちらしい
# import bisect
# N = int(input())
# A = list(map(int, input().split()))

# LEN = 0
# L = []
# dp = [None]*N

# for i in range(N):
#     pos = bisect.bisect_left(L, A[i])
#     dp[i] = pos

#     if dp[i] >= LEN:
#         L.append(A[i])
#         LEN += 1
#     else:
#         L[dp[i]] = A[i]

# print(LEN)


# A25 - Number of Routes
# H, W = map(int, input().split())
# C = [input() for _ in range(H)]

# dp = [[0]*(W+1) for _ in range(H+1)]
# dp[1][1] = 1
# for i in range(1, H+1):
#     for j in range(1, W+1):
#         if C[i-1][j-1] == '#':
#             continue
#         dp[i][j] += dp[i-1][j] + dp[i][j-1]
#         # print(dp[i][j])

# print(dp[-1][-1])

# A57 - Doubling
# ダブリング
# N, Q = map(int, input().split())
# A = list(map(int, input().split()))
# queries = [ list(map(int, input().split())) for i in range(Q)]

# LEVELS = 31

# dp = [[None] * N for i in range(LEVELS)]
# for i in range(N):
#     dp[0][i] = A[i]-1

# for d in range(1, LEVELS):
#     for i in range(N):
#         dp[d][i] = dp[d-1][dp[d-1][i]]

# for X, Y in queries:
#     current_place = X-1
#     for d in range(29, -1, -1):
#         if ((Y >> d) & 1) == 1:
#             current_place = dp[d][current_place]
#     print(current_place+1)

# B57 - Calculator
# N, K = map(int, input().split())

# dp = [[0]*300009 for _ in range(30)]

# for i in range(N+1):
#     dp[0][i] = i - sum(map(int, str(i)))

# for d in range(29):
#     for i in range(N+1):
#         dp[d+1][i] = dp[d][dp[d][i]]

# for num in range(1, N+1):
#     for d in range(30):
#         if K & (1 << d):
#             num = dp[d][num]
#     print(num)