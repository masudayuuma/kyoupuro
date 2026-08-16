# A - Nine or Nein
# A, B = map(int, input().split())

# tashi = A+B
# hiki = A-B
# kake = A*B
# wari = A//B if A%B == 0 else 0

# for ans in (tashi, hiki, kake, wari):
#     if ans == 9:
#         print('Nine')
#         exit()

# print('Nein')

# B - Survey Tabulation
# from collections import Counter
# N = int(input())
# ans = []
# for i in range(N):
#     s = input().lower()
#     ans.append(s)

# ans_cnt = Counter(ans)

# max_cnt = 0

# for key, val in ans_cnt.items():
#     max_cnt = max(max_cnt, val)

# print(max_cnt)


# C - Cookies and Greedy Takahashi
# from sortedcontainers import SortedList
# N = int(input())
# INF = float('inf')
# A = list(map(int, input().split()))
# A.append(0)
# A.sort()
# now = A.index(0)
# # print(A)
# left = now-1 if now > 0 else -INF
# right = now+1 if now < N else INF
# cnt = 0

# while left != -INF or right != INF:
#     print(now, left, right)
#     if left == -INF:
#         cnt += abs(A[now]-A[right])
#         now = right
#         right = now+1 if now < N-1 else INF
#         print(cnt, A[now], right) 
#         continue
#     elif right == INF:
#         cnt += abs(A[now]-A[left])
#         now = left
#         left = now-1 if now > 0 else -INF
#         print(cnt, A[now], left)    
#         continue    


#     if abs(A[now]-A[left]) > abs(A[now]-A[right]):
#         cnt += abs(A[now]-A[right])
#         now = right
#         right = now+1 if now < N-1 else INF
#         print(cnt, A[now], right)
#     else:
#         cnt += abs(A[now]-A[left])
#         now = left
#         left = now-1 if now > 0 else -INF
#         print(cnt, A[now], left)

# print(cnt)


# N = int(input())
# INF = float('inf')

# A = list(map(int, input().split()))
# A.append(0)
# A.sort()

# now = A.index(0)

# left = now - 1 if now > 0 else -INF
# right = now + 1 if now < N else INF

# cnt = 0

# while left != -INF or right != INF:

#     if left == -INF:
#         cnt += abs(A[now] - A[right])
#         now = right
#         right = now + 1 if now < N else INF
#         continue

#     elif right == INF:
#         cnt += abs(A[now] - A[left])
#         now = left
#         left = now - 1 if now > 0 else -INF
#         continue

#     if abs(A[now] - A[left]) > abs(A[now] - A[right]):
#         cnt += abs(A[now] - A[right])
#         now = right
#         right = now + 1 if now < N else INF
#     else:
#         # 同距離なら座標の小さい左側
#         cnt += abs(A[now] - A[left])
#         now = left
#         left = now - 1 if now > 0 else -INF

# print(cnt)

# D - Chargers
# import heapq
# Q, V = map(int, input().split())

# heap = []

# for i in range(Q):
#     query = list(map(int, input().split()))

#     if query[0] == 1:
#         t, w = query[1], query[2]
#         heapq.heappush(heap, -(w-t))
#     else:
#         t = query[1]
#         if not heap:
#             print(-1)
#             continue
#         ans = -heapq.heappop(heap)+t
#         ans = V if ans > V else ans
#         print(ans)


# E - Sum of Square of Sum
# MOD = 998244353
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

# fact = [1]*(N+1)

# for i in range(1, N+1):
#     fact[i]= fact[i-1]*i % MOD

# inv_fact = [1]*(N+1)
# inv_fact[N] = pow(fact[N], MOD - 2, MOD)

# for i in range(N, 0, -1):
#     inv_fact[i - 1] = inv_fact[i] * i % MOD

# def comb(n, r):
#     if r < 0 or r > n:
#         return 0

#     return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

# sumA = sum(A) % MOD
# sumSq = sum(a * a for a in A) % MOD
# ans = comb(N-1, K-1) * sumSq % MOD

# pair = (sumA * sumA - sumSq)

# ans += comb(N - 2, K - 2) * pair
# ans %= MOD

# print(ans)

