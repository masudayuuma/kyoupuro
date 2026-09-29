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

# C - Range Search Query
# Q = int(input())
# S = list(input())
# T = list(input())
# N = len(S)
# M = len(T)

# flag = [0]*(N+1)

# for i in range(N):
#     ok = True
#     for j in range(M):
#         if i+j >= N:
#             ok = False
#             break
#         if S[i+j] != T[j]:
#             ok = False
#             break

#     if ok:
#         flag[i+1] = 1

# # print(flag)

# for i in range(N):
#     flag[i+1] += flag[i]

# # print(flag)

# for i in range(Q):
#     l, r = map(int, input().split())

#     if r-M+1 < l:
#         print('No')
#         continue

#     if flag[r-M+1]-flag[l-1] > 0:
#         print('Yes')
#         continue

#     print('No')


# D - Masking Tape
# N, Q = map(int, input().split())

# all_paste_at = -1
# now = "a"
# wall = [False]*N
# colors = ['a']*N
# deleat_at = [-1]*N
# for i in range(Q):
#     q, val = input().split()
#     q = int(q)

#     if q == 1:
#         val = int(val)-1

#         if wall[val] == True:
#             deleat_at[val] = i
#             wall[val] = False
#         else:
#             wall[val] = True
#             if all_paste_at > deleat_at[val]:
#                 colors[val] = now
#     else:
#         all_paste_at = i
#         now = val

# for i in range(N):
#     if wall[i] == True or deleat_at[i] > all_paste_at:
#         continue

#     colors[i] = now


# print("".join(colors))

# E - Wheel Distance
# from collections import defaultdict
# import heapq
# N, Q = map(int, input().split())

# A = list(map(int, input().split()))
# B = list(map(int, input().split()))


# prefix = [0]

# for _ in range(2):
#     for i in range(N):
#         prefix.append(prefix[-1]+A[i])

# graph = defaultdict(list)

# for i in range(N):
#     graph[i+1].append(((i+1) % N+1, A[i]))
#     graph[(i+1) % N+1].append((i+1, A[i]))
#     graph[i+1].append((N+1, B[i]))
#     graph[N+1].append((i+1, B[i]))


# ans = {}
# heap = [(0, N+1)]
# now_c = 0
# while heap:
#     cost, target = heapq.heappop(heap)

#     if target in ans:
#         continue
#     ans[target] = cost

#     for nt, nc in graph[target]:
#         if nt in ans:
#             continue
#         heapq.heappush(heap, (cost+nc, nt))

# # print(ans, prefix)

# for i in range(Q):
#     s, t = map(int, input().split())

#     minans = float('inf') if s == N+1 or t == N+1 else min(prefix[t-1]-prefix[s-1], prefix[s+N-1]-prefix[t-1])
#     minans = min(ans[s]+ans[t], minans)

#     print(minans)

# D - Pawn Line
import heapq
T = int(input())

for _ in range(T):
    ans = 0
    N = int(input())
    R = list(map(int, input().split()))
    minr = min(R)
    heap = []
    visited = set()
    for i, r in enumerate(R):
        heapq.heappush(heap, (r, i))

    while heap:
        # print(heap)
        val, index = heapq.heappop(heap)
        visited.add(index)

        if index -1 >= 0 and index-1 not in visited:
            heapq.heappush(heap, (min(val+1, R[index-1]), index-1))
            c = max(R[index-1]-(val+1), 0)
            ans += c
            visited.add(index-1)
        if index+1 < N and index+1 not in visited:
            c = max(R[index+1]-(val+1), 0)
            ans += c
            heapq.heappush(heap, (min(val+1, R[index+1]), index+1))
            visited.add(index+1)

    print(ans)