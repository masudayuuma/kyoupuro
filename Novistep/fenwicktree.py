# A59 - RSQ (Range Sum Queries)
# N, Q = map(int, input().split())

# from atcoder.fenwicktree import FenwickTree

# fw = FenwickTree(N)
# A = [0]*(N)

# for i in range(Q):
#     q, a, b = map(int, input().split())
    
#     if q == 1:
#         diff = b - A[a-1]
#         fw.add(a-1, diff)
#         A[a-1] = b
#     else:
#         print(fw.sum(a-1, b-1))

# B - Fenwick Tree
# from atcoder.fenwicktree import FenwickTree

# N, Q = map(int, input().split())

# A = list(map(int, input().split()))
# fw = FenwickTree(N)
# for i, a in enumerate(A): fw.add(i, a)

# for i in range(Q):
#     q, a, b = map(int, input().split())

#     if q == 0:
#         fw.add(a, b)
#     else:
#         print(fw.sum(a, b))

# J - 数列の反転
# from atcoder.fenwicktree import FenwickTree

# N, Q = map(int, input().split())

# fw = FenwickTree(N + 1)

# for _ in range(Q):
#     t, k = map(int, input().split())

#     if t == 1:
#         if k <= N:
#             card = N - k + 1
#         else:
#             card = k - N

#         cnt = fw.sum(card, N + 1)

#         if cnt % 2 == 0:
#             print(k)
#         else:
#             print(2 * N - k + 1)

#     else:
#         fw.add(k, 1)

# F - Range Xor Query
# from atcoder.segtree import SegTree

# N, Q = map(int, input().split())

# A = list(map(int, input().split()))

# seg = SegTree(lambda a, b: a^b, 0, A)

# for _ in range(Q):
#     t, x, y = map(int, input().split())

#     if t == 1:
#         x -= 1
#         seg.set(x, seg.get(x)^y)
#     else:
#         x -= 1
#         print(seg.prod(x, y))

#
# from atcoder.segtree import SegTree
# N, Q = map(int, input().split())

# A = list(map(int, input().split()))

# seg = SegTree(lambda a, b: a^b, 0, A)

# for _ in range(Q):
#     t, x, y = map(int, input().split())

#     if t == 1:
#         x -= 1
#         seg.set(x, seg.get(x)^y)
#     else:
#         x -= 1
#         print(seg.prod(x, y))

# B - Fenwick Tree
from atcoder.segtree import SegTree
# N, Q = map(int, input().split())

# A = list(map(int, input().split()))
# seg = SegTree(lambda a, b: a+b, 0, A)
# for _ in range(Q):
#     q, x, y = map(int, input().split())

#     if q == 0:
#         seg.set(x, seg.get(x)+y)
#     else:
#         print(seg.prod(x, y))

# Range Minimum Query (RMQ)　セグ木
# from atcoder.segtree import SegTree
# n, q = map(int, input().split())
# A = [2147483647]*(n)

# seg = SegTree(min, 2147483647, A)

# for i in range(q):
#     com, x, y = map(int, input().split())

#     if com == 0:
#         seg.set(x, y)
#     else:
#         print(seg.prod(x, y+1))

# Range Sum Query セグ木
# from atcoder.segtree import SegTree
# n, q = map(int, input().split())
# A = [0]*n

# seg = SegTree(lambda a, b: a+b, 0, A)

# for _ in range(q):
#     com, x, y = map(int, input().split())

#     x -= 1

#     if com == 0:
#         seg.set(x, seg.get(x)+y)
#     else:
#         print(seg.prod(x, y))

# B59 - Number of Inversions
# from atcoder.fenwicktree import FenwickTree
# N = int(input())

# A = list(map(int, input().split()))
# fw = FenwickTree(N)
# ans = 0
# for x in A:
#     x -= 1

#     ans += fw.sum(x, N)
#     fw.add(x, 1)

# print(ans)

# E - A > B substring
# from atcoder.fenwicktree import FenwickTree

# N = int(input())
# S = input()

# P = [0]

# cur = 0
# for ch in S:
#     if ch == "A":
#         cur += 1
#     elif ch == 'B':
#         cur -= 1
#     P.append(cur)

# vals = sorted(set(P))
# comp = {v: i for i, v in enumerate(vals)}

# fw = FenwickTree(len(vals))

# ans = 0

# for p in P:
#     idx = comp[p]

#     ans += fw.sum(0, idx)
#     fw.add(idx, 1)
# print(ans)

# F - Starry Landscape Photo
from atcoder.fenwicktree import FenwickTree
N = int(input())
B = list(map(int, input().split()))


pos = [0]*(N+1)

for i, b in enumerate(B):
    pos[b] = i

fw = FenwickTree(N+1)

ans = 0

for i in range(1, len(pos)):
    left = fw.sum(0, pos[i])
    right = fw.sum(pos[i], N+1)

    ans += (left+1)*(right+1)
    fw.add(pos[i], 1)

print(ans)


# F - Insert
