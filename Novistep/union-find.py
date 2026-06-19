# A - Disjoint Set Union
# from atcoder.dsu import DSU
# N, Q = map(int, input().split())

# unionfind = DSU(N)

# for i in range(Q):
#     t, u, v = map(int, input().split())

#     if t == 0:
#         unionfind.merge(u, v)
#     else:
#         if unionfind.leader(u) == unionfind.leader(v):
#             print(1)
#         else:
#             print(0)

# A66 - Connect Query
# from atcoder.dsu import DSU
# N, Q = map(int, input().split())

# unionfind = DSU(N+1)

# for _ in range(Q):
#     q, a, b = map(int, input().split())

#     if q == 1:
#         unionfind.merge(a, b)
#     else:
#         if unionfind.same(a, b):
#             print('Yes')
#         else:
#             print('No')

# C - Count Connected Components
