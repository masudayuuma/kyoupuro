# A - Happy Birthday! 4
# X, Y, Z = map(int, input().split())

# for i in range(X, 10000):
#     if i == Y*Z:
#         print('Yes')
#         exit()
    
#     Y += 1

# print('No')
    

# B - Nearest Taller
# N = int(input())
# A = list(map(int, input().split()))
# max_val = (-1, -1)
# for i, val in enumerate(A):
#     for j in range(i-1, -1, -1):
#         if A[j] > val:
#             print(j+1)
#             break
#     else:
#         print(-1)

# C - 1122 Substring 2
# from collections import deque

# S = input()
# int_S = int(S)
# que = deque()
# total = 0
# for i in range(len(S)-1):
#     if int(S[i])+1 == int(S[i+1]):
#         que.append((i, i+1))

# while que:
#     l, r = que.popleft()
#     total += 1
#     target_l = S[l]
#     target_r = S[r]
#     while True:
#         l -= 1
#         r += 1
#         if l >= 0 and r < len(S) and int(S[l])+1 == int(S[r]) and target_l == S[l] and target_r == S[r]:
#             total += 1
#         else:
#             break

# print(total)

# ランレングス圧縮使用バージョン
# from itertools import groupby
# s = input()
# a = [(v, len(list(x))) for v, x in groupby(s)]

# ans = 0
# for i in range(len(a)-1):
#     if int(a[i][0]) +1 == int(a[i + 1][0]):
#         ans += min(a[i][1], a[i+1][1])
# print(ans)

# D - 183183
# from collections import defaultdict

# N, M = map(int, input().split())
# A = list(map(int, input().split()))

# max_L = 10
# pow = [1] * (max_L + 1)
# for L in range(1, max_L + 1):
#     pow[L] = (pow[L - 1] * 10) % M

# cnt = [defaultdict(int) for _ in range(max_L + 1)]

# for a in A:
#     for L in range(1, max_L + 1):
#         r = (a * pow[L]) % M
#         cnt[L][r] += 1

# ans = 0
# for a in A:
#     L = len(str(a))
#     target = (-a) % M
#     ans += cnt[L][target]

# print(ans)

# 解説動画の実装
# from collections import defaultdict
# n, m = map(int, input().split())
# a = list(map(int, input().split()))

# groups = [[] for _ in range(11)]
# for v in a:
#     lenght = len(str(v))
#     groups[lenght].append(v)

# ans = 0
# ten = 1

# for b in range(11):
#     cnt = defaultdict(int)
#     for v in groups[b]:
#         cnt[v % m] += 1

#     for ai in a:
#         r = (-ten * ai )% m
#         ans += cnt[r]

#     ten = (ten*10)% m

# print(ans)

# E - Max Matrix 2
# from collections import defaultdict

# T = int(input())

# for _ in range(T):
#     N, M = map(int, input().split())
#     X = list(map(int, input().split()))
#     Y = list(map(int, input().split()))
#     total = N * M

#     row_of = [-1] * (total + 1)
#     col_of = [-1] * (total + 1)

#     ok = True

#     for i, v in enumerate(X):
#         if not (1 <= v <= total):
#             ok = False
#             break
#         if row_of[v] != -1:
#             ok = False
#             break
#         row_of[v] = i

#     if not ok:
#         print("No")
#         continue

#     for j, v in enumerate(Y):
#         if not (1 <= v <= total):
#             ok = False
#             break
#         if col_of[v] != -1:
#             ok = False
#             break
#         col_of[v] = j

#     if not ok:
#         print("No")
#         continue

#     buckets = [[] for _ in range(total+1)]
#     for i in range(N):
#         xi = X[i]
#         for j in range(M):
#             cap = xi if xi < Y[j] else Y[j]
#             buckets[cap].append(i * M + j)

#     A = [[0] * M for _ in range(N)]

#     global_cells = set()
#     row_cells = [set() for _ in range(N)]
#     col_cells = [set() for _ in range(M)]

#     for v in range(total, 0, -1):
#         for cid in buckets[v]:
#             i = cid // M
#             j = cid % M
#             global_cells.add(cid)
#             row_cells[i].add(cid)
#             col_cells[j].add(cid)

#         r = row_of[v]
#         c = col_of[v]

#         if r != -1 and c != -1:
#             cid = r * M + c
#             if A[r][c] != 0:
#                 ok = False
#                 break
#             A[r][c] = v
#             if cid in global_cells:
#                 global_cells.remove(cid)
#             row_cells[r].discard(cid)
#             col_cells[c].discard(cid)

#         elif r != -1:
#             if not row_cells[r]:
#                 ok = False
#                 break
#             cid = next(iter(row_cells[r]))
#             row_cells[r].remove(cid)
#             global_cells.discard(cid)
#             ci = cid % M
#             col_cells[ci].discard(cid)
#             i = cid // M
#             j = cid % M
#             A[i][j] = v

#         elif c != -1:
#             if not col_cells[c]:
#                 ok = False
#                 break
#             cid = next(iter(col_cells[c]))
#             col_cells[c].remove(cid)
#             global_cells.discard(cid)
#             ri = cid // M
#             row_cells[ri].discard(cid)
#             i = cid // M
#             j = cid % M
#             A[i][j] = v

#         else:
#             if not global_cells:
#                 ok = False
#                 break
#             cid = next(iter(global_cells))
#             global_cells.remove(cid)
#             ri = cid // M
#             ci = cid % M
#             row_cells[ri].discard(cid)
#             col_cells[ci].discard(cid)
#             A[ri][ci] = v

#     if not ok:
#         print("No")
#         continue

#     print("Yes")
#     for i in range(N):
#         print(*A[i])

# 解説動画
import sys

def solve() -> None:
    it = iter(map(int, sys.stdin.read().split()))
    T = next(it)
    out_lines = []

    for _ in range(T):
        N = next(it)
        M = next(it)
        X = [next(it) for _ in range(N)]
        Y = [next(it) for _ in range(M)]

        # 同じ配列内で値が被っていたら不可能
        if len(set(X)) < N or len(set(Y)) < M:
            out_lines.append("No")
            continue

        # 元の行・列インデックスを記録
        rid = {v: i for i, v in enumerate(X)}
        cid = {v: j for j, v in enumerate(Y)}

        # 最大値順に並べ替えた配列
        x = sorted(X, reverse=True)
        y = sorted(Y, reverse=True)

        # 並べ替え後の座標系で作る行列
        a = [[0] * M for _ in range(N)]

        xi = 0  # 有効な行の数
        yi = 0  # 有効な列の数
        cand = []  # まだ空いている候補マス (i, j)
        ok = True

        max_val = N * M
        # 大きい数から順に置いていく
        for v in range(max_val, 0, -1):
            # この値 v を最大値に持つ行があれば、その行を有効化
            if xi < N and x[xi] == v:
                # すでに有効な列との交点をすべて候補に追加
                for j in range(yi):
                    cand.append((xi, j))
                xi += 1

            # この値 v を最大値に持つ列があれば、その列を有効化
            if yi < M and y[yi] == v:
                # すでに有効な行との交点をすべて候補に追加
                for i in range(xi):
                    cand.append((i, yi))
                yi += 1

            # 置けるマスがなければ不可能
            if not cand:
                ok = False
                break

            # 候補から 1 マス選んで v を置く
            i, j = cand.pop()
            a[i][j] = v

        if not ok:
            out_lines.append("No")
            continue

        # 並べ替え前の元の行・列順に戻す
        ans = [[0] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                orig_i = rid[x[i]]
                orig_j = cid[y[j]]
                ans[orig_i][orig_j] = a[i][j]

        out_lines.append("Yes")
        for row in ans:
            out_lines.append(" ".join(map(str, row)))

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    solve()
