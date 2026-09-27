# # A - Traffic Light
# c = input()

# if c =='B':
#     print('Y')
# elif c == 'Y':
#     print('R')
# else:
#     print('B')


# B - Standing Outliers
# from collections import defaultdict
# N, D = map(int, input().split())

# P = list(map(int, input().split()))

# p2i = defaultdict(int)
# for i, val in enumerate(P):
#     p2i[val] = i+1

# P.sort()
# ans = []
# for i, val in enumerate(P):
#     if i > 0 and P[i-1]+D > P[i]:
#         continue

#     if i < N-1 and P[i+1]-D < P[i]:
#         continue


#     ans.append(p2i[val])

# print(len(ans))
# print(*sorted(ans))

# C - Range Search Query
# from collections import defaultdict
# Q = int(input())
# S = list(input())
# T = list(input())

# anslist = [float('inf')]*len(S)

# for i in range(len(S)):
#     ok = True
#     for j in range(len(T)):
#         if i+j >= len(S):
#             ok = False
#             break
#         if S[i+j] != T[j]:
#             ok = False
#             break

#     if ok:
#         anslist[i] = min(anslist[i], i+j)
# # print(anslist)
# min_r = float('inf')
# for i in range(len(S)-1, -1, -1):
#     min_r = min(anslist[i], min_r)
#     anslist[i] = min_r

# # print(anslist)
# for i in range(Q):
#     l, r = map(int, input().split())
#     l -= 1
#     r -= 1

#     if anslist[l] > r:
#         print('No')
#     else:
#         print('Yes')

# D - Masking Tape
# N, Q = map(int, input().split())

# now = 'a'
# last = -1

# covered = [False] * N
# color = ['a'] * N
# removed_at = [-1] * N

# for t in range(Q):
#     q, val = input().split()

#     if q == '1':
#         i = int(val) - 1

#         if covered[i]:
#             covered[i] = False
#             removed_at[i] = t
#         else:
#             if last > removed_at[i]:
#                 color[i] = now

#             covered[i] = True
#     else:
#         now = val
#         last = t

# ans = []
# for i in range(N):
#     if covered[i] or removed_at[i] >= last:
#         ans.append(color[i])
#     else:
#         ans.append(now)

# print(''.join(ans))

# E - Wheel Distance
# import heapq

# N, Q = map(int, input().split())

# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# prefix = [0]

# for _ in range(2):
#     for i in range(N):
#         prefix.append(prefix[-1] + A[i])

# graph = [[] for _ in range(N+2)]

# for i in range(1, N+1):
#     nxt = i % N+1

#     graph[i].append((nxt, A[i-1]))
#     graph[nxt].append((i, A[i-1]))

#     graph[i].append((N+1, B[i-1]))
#     graph[N+1].append((i, B[i-1]))


# dist = [float('inf')] * (N+2)
# dist[N+1] = 0

# heap = [(0, N+1)]

# while heap:
#     cost, now = heapq.heappop(heap)

#     if cost > dist[now]:
#         continue

#     for nxt, weight in graph[now]:
#         nxt_cost = cost + weight

#         if nxt_cost < dist[nxt]:
#             dist[nxt] = nxt_cost
#             heapq.heappush(heap, (nxt_cost, nxt))

# for i in range(Q):
#     s, t = map(int, input().split())

#     minans = dist[s] + dist[t]

#     if t != N + 1:
#         minans = min(
#             minans,
#             prefix[t-1] - prefix[s-1],
#             prefix[s-1+N] - prefix[t-1]
#         )

#     print(minans)

# 