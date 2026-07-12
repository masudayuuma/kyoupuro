# A - Compromise
# N = int(input())
# X = list(map(int, input().split()))

# if all(x < 0 for x in X):
#     print('Yes')
# else:
#     print('No')

# B - Representative Balls
# from collections import defaultdict
# N, M = map(int, input().split())
# color = defaultdict(list)

# for i in range(N):
#     c, s = map(int, input().split())
#     color[c].append(s)

# ans = []
# for i in range(1, M+1):
#     if len(color[i]) == 0:
#         ans.append(-1)
#     else:
#         ans.append(max(color[i]))

# print(*ans)

# C - Count Close Pairs
# import sys

# N = int(input())
# r = 0 
# ans = 0

# for i in range(1, N + 1):
#     if r < i:
#         r = i
#     while r < N:
#         print(f"? {i} {r + 1}")
#         sys.stdout.flush()
#         res = input()
#         if res == "Yes":
#             r += 1
#         else:
#             break
#     ans += r - i 

# print(f"! {ans}")
# sys.stdout.flush()

# D - Placing Rooks
# N, M = map(int, input().split())

# timestamps = []
# for i in range(M):
#     r, c = map(int, input().split())

#     timestamps.append((r, c))

# timestamps.reverse()

# col = set()
# row = set()
# ans = 0
# for r, c in timestamps:
#     if not c in col and not r in row:
#         ans += 1
#     col.add(c)
#     row.add(r)

# print(ans)

# E - Range Flipimport
# N, K = map(int, input().split())
# A = [0]*N
# B = [0]*N
# for i in range(N):
#     A[i], B[i] = map(int, input().split())

# INF = float('-inf')
# dp0 = [0]*(K+1)
# dp1 = [INF]*(K+1)

# for i in range(N):
#     a = A[i]
#     b = B[i]
#     ndp0 = [0]*(K+1)
#     ndp1 = [INF]*(K+1)
#     for k in range(K+1):
#         ndp0[k] = max(dp0[k], dp1[k]) + a
#         best = dp1[k]
#         if k > 0 and dp0[k-1] > best:
#             best = dp0[k-1]
#         if best != INF:
#             ndp1[k] = best + b
#     dp0 = ndp0
#     dp1 = ndp1

# ans = max(max(dp0), max(dp1))
# print(ans)

# C - Count Close Pairs
# N = int(input())
# r = 2
# total = 0
# for l in range(1, N):
#     if r <= l: r = l+1
#     while r < N+1:
#         print(f"? {l} {r}", flush=True)
#         res = input()
#         if res == 'Yes':
#             r += 1
#         else:
#             break

#     total += r-1-l

# print(f"! {total}")

# E - Range Flip
# N, K = map(int, input().split())

# k2 = K*2+1

# dp = [0]*k2

# for i in range(N):
#     a, b = map(int, input().split())

#     for j in range(k2):
#         dp[j] += a if j % 2 == 0 else b
    
#     for j in range(k2-1):
#         if dp[j] > dp[j+1]:
#             dp[j+1] = dp[j]

# print(dp[k2-1])

# E - Range Flip
# N, K = map(int, input().split())

# A = []
# B = []

# for i in range(N):
#     a, b = map(int, input().split())
#     A.append(a)
#     B.append(b)

# dp_a = [0]*(K+1)
# dp_b = [float('-inf')]*(K+1)

# for i in range(N):
#     a = A[i]
#     b = B[i]
#     nxt_a = [0]*(K+1)
#     nxt_b = [float('-inf')]*(K+1)

#     for k in range(K+1):
#         nxt_a[k] = max(dp_a[k], dp_b[k])+a

#         best = dp_b[k]
#         if k > 0 and dp_a[k-1] > best:
#             best = dp_a[k-1]
#         if best != float('-inf'):
#             nxt_b[k] = best+b
#     dp_a = nxt_a.copy()
#     dp_b = nxt_b.copy()

# print(max(dp_a[-1], dp_b[-1]))

# F - Many Mod Calculation
# import heapq
# T = int(input())

# for _ in range(T):
#     N, X = map(int, input().split())
#     A = list(map(int, input().split()))

#     heap = [(-(X+1), 1)]

#     for a in A:
#         num = 0
#         while heap and -heap[0][0] > a:
#             negw, c = heapq.heappop(heap)
#             w = -negw
#             num += (w//a)*c
#             heapq.heappush(heap, (-(w%a), c))
#         heapq.heappush(heap, (-a, num))

#     ans = -1
#     while heap:
#         negw, c = heapq.heappop(heap)
#         w =  -negw
#         if w == 0:
#             continue
#         ans += c
#     print(ans)