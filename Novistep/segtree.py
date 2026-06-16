# F - Range Xor Query
# from atcoder.segtree import SegTree

# N, Q = map(int, input().split())

# A = list(map(int, input().split()))
# sg = SegTree(lambda a, b: a^b, 0, A)

# for _ in range(Q):
#     t, x, y = map(int, input().split())

#     if t == 1:
#         x -= 1
#         sg.set(x, sg.get(x)^y)
#     else:
#         x -= 1
#         print(sg.prod(x, y))

# A58 - RMQ (Range Maximum Queries) 
# from atcoder.segtree import SegTree
# N, Q = map(int, input().split())
# A = [0]*N
# sg = SegTree(max, 0, A)
# for _ in range(Q):
#     q, a, b = map(int, input().split())

#     if q == 1:
#         a -= 1
#         sg.set(a, b)
#     else:
#         a -= 1
#         print(sg.prod(a, b-1))

# G - 一点更新・区間最小値
from atcoder.segtree import SegTree
N, Q = map(int, input().split())

A = list(map(int, input().split()))

sg = SegTree(min, float('inf'), A)

for _ in range(Q):
    t, x, y = map(int, input().split())

    if t == 1:
        sg.set(x, y)
    else:
        print(sg.prod(x, y))

# D - Flat Subsequence
