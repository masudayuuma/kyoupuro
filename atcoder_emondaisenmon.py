# E - Alternating Costs
# T = int(input())

# for i in range(T):
#     a, b, x, y = map(int, input().split())
#     cost = 0
#     x = abs(x)
#     y = abs(y)
#     diff = min(x, y)
#     cost += diff*min(a, b)*2
#     x -= diff
#     y -= diff

#     cnt = 0
#     min_cost_A = min(a, b*3)
#     min_cost_B = min(b, a*3)

#     if x > 0:
#         x_2 = x //2
#         if x % 2 == 1:
#             cost += min_cost_A*(x_2+1)+min_cost_B*x_2
#         else:
#             cost += min_cost_A*x_2+min_cost_B*x_2
#     else:
#         y_2 = y // 2
#         if y % 2 == 1:
#             cost += min_cost_A*y_2+min_cost_B*(y_2+1)
#         else:
#             cost += min_cost_A*y_2+min_cost_B*y_2

#     print(cost)

# E - E-liter
# from atcoder.fenwicktree import FenwickTree
# N, Q = map(int, input().split())

# col_timestamp = [0]*N
# row_timestamp = [-1]*N

# fw_col = FenwickTree(Q+1)
# fw_row = FenwickTree(Q+1)

# ans = 0
# for time in range(Q):
#     q, i = map(int, input().split())
#     i -= 1
#     if q == 1:
#         now_stamp = row_timestamp[i] if row_timestamp[i] > -1 else 0
#         time += 1
#         if row_timestamp[i] == -1:
#             row_timestamp[i] = time
#             ans += N
#         else:
#             fw_row.add(row_timestamp[i], -1)
#             row_timestamp[i] = time
#             ans += fw_col.sum(now_stamp, time)
#         fw_row.add(time, 1)
#         print(ans)
#     else:
#         time += 1
#         if col_timestamp[i] != 0:
#             fw_col.add(col_timestamp[i], -1)
#         now_stamp = col_timestamp[i]
#         ans -= fw_row.sum(now_stamp, time)
#         fw_col.add(time, 1)
#         col_timestamp[i] = time
#         print(ans)

# J - 数列の反転
# from atcoder.fenwicktree import FenwickTree
# N, Q = map(int, input().split())
# fw = FenwickTree(N+2)
# for i in range(Q):
#     t, k = map(int, input().split())

#     if t == 1:
#         pos = k
#         if pos <= N:
#             d = N-pos+1
#         else:
#             d = pos-N
#         flag = fw.sum(0, d+1)%2
#         if flag == 0:
#             print(pos)
#         else:
#             print(2*N+1-pos)
            
#     else:
#         fw.add(1, 1)
#         fw.add(k+1, -1)

# E - E-liter
# from atcoder.fenwicktree import FenwickTree
# N, Q = map(int, input().split())

# row_time = [-1]*N
# col_time = [0]*N

# fw_col = FenwickTree(Q+1)
# fw_row = FenwickTree(Q+1)
# ans = 0
# for i in range(Q):
#     q, n = map(int, input().split())

#     if q == 1:
#         if row_time[n-1] == -1:
#             ans += N
#             row_time[n-1] = i
#             fw_row.add(i, 1)
#         else:
#             ans += fw_col.sum(row_time[n-1], i)
#             fw_row.add(row_time[n-1], -1)
#             row_time[n-1] = i
#             fw_row.add(i, 1)
#     else:
#         ans -= fw_row.sum(col_time[n-1], i)
#         if col_time[n-1] > 0: fw_col.add (col_time[n-1], -1)
#         col_time[n-1] = i
#         fw_col.add(i, 1)

#     print(ans)

# E - Roads and Gates
# from collections import defaultdict
# import heapq
# N, M, Y = map(int, input().split())

# graph = defaultdict(list)

# for i in range(M):
#     u, v, t = map(int, input().split())
#     graph[u-1].append((v-1, t))
#     graph[v-1].append((u-1, t))

# X = list(map(int, input().split()))

# s_g = N
# s_o = N+1
# for i in range(N):
#     graph[i].append((s_g, X[i]))
#     graph[s_o].append((i, X[i]))
# graph[s_g].append((s_o, Y))

# heap = [(0, 0)] # cost, index
# dist = [float('inf')] * (N+2)
# dist[0] = 0

# while heap:
#     cost, index = heapq.heappop(heap)
#     if cost != dist[index]:
#         continue

#     for nxt, nxt_cost in graph[index]:
#         if dist[nxt] > cost+nxt_cost:
#             heapq.heappush(heap, (cost+nxt_cost, nxt))
#             dist[nxt] = cost+nxt_cost

# print(*dist[1:N])

# J - 数列の反転
# from atcoder.fenwicktree import FenwickTree
# N, Q = map(int, input().split())

# fw = FenwickTree(N+1)

# for i in range(Q):
#     t, k = map(int, input().split())

#     if t == 1:
#         target = N-k+1 if N >= k else k-N
#         flag = fw.sum(target, N+1)%2
#         if flag == 1:
#             if k > N:
#                 print(k-target*2+1)
#             else:
#                 print(k+target*2-1)
#         else:
#             print(k)
#     else:
#         fw.add(k, 1)

# E - A > B substring
# from atcoder.fenwicktree import FenwickTree
# N = int(input())

# S = list(input())
# prefix = [0]
# now = 0
# for c in S:
#     if c == 'A':
#        now += 1
#        prefix.append(now)
#     elif c == 'B':
#         now -= 1
#         prefix.append(now)
#     else:
#         prefix.append(now) 


# sort_s = sorted(list(set(prefix)))

# fw = FenwickTree(len(sort_s)+1)

# cmp_s = {v: i for i, v in enumerate(sort_s)}
# ans = 0
# for i in range(N+1):
#     fw.add(cmp_s[prefix[i]], 1)

#     ans += fw.sum(0, cmp_s[prefix[i]])

# print(ans)


# E - Roads and Gates
