#二分探索
# def binary_search(list, item):
#     low = 0                        # lowとhighを使ってリストの検索部分を追跡
#     high = len(list) - 1
#     while low <= high:             # 1つの要素に絞り込まれるまでの間は...
#         mid = (low + high) // 2
#         guess = list[mid]          # 真ん中の要素を調べる
#         if guess == item:          # アイテムを検出
#             return mid
#         if guess > item:           # 推測した数字が大きすぎた
#             high = mid - 1
#         else:                      # 推測した数字が小さすぎた
#             low = mid + 1
#     return None                    # アイテムが存在しない
# my_list = [1, 3, 5, 7, 9]          # テストしてみる

# print (binary_search(my_list, 3))    # 結果は1：リストは0始まりなので、
#                                    # 2つ目のスロットのインデックスは1
# print (binary_search(my_list, -1))   # 結果はNone:Pyhonにおいて「nil」を意味し、
                                   # アイテムが検出されなかったことを示す

#めぐる式二分探索法


#DFS 深さ優先探索(easy)
# import sys
# sys.setrecursionlimit(10000)

# N, M = map(int, input().split())
# road = [[] for _ in range(N+1)]

# for i in range(M):
#     A, B = map(int, input().split())
#     road[A].append(B)

# def dfs(s):
#     if goal[s]: return
#     goal[s] = True
#     for r in road[s]: dfs(r)

# ans = 0
# for i in range(1, N+1):
#     goal = [False]* (N+1)
#     dfs(i)
#     ans += sum(goal)

# print(ans)

#DFS（テンプレ）
# import sys
# sys.setrecursionlimit(10000)

# def dfs(G, v, seen):
#     seen[v] = True

#     for nxt in G[v]:
#         if seen[nxt]:
#             continue
#         dfs(G, nxt, seen)

# N, M = map(int, input().split())
# G =[[] for _ in range(N)]
# for _ in range(M):
#     a, b = map(int, input().split())
#     G[a].append(b)
#     G[b].append(a)

# seen = [False] * N
# dfs(G, 0, seen)

#(DFS)例題 4-1. s から t へ辿り着けるか
# import sys
# sys.setrecursionlimit(10*6)
# input = sys.stdin.readline

# N, M, s, t = map(int, input().split())
# G = [[] for _ in range(N)]
# for _ in range(M):
#     a, b = map(int, input().split())
#     G[a].append(b)

# seen = [False]*N

# def dfs(v):
#     seen[v] = True
#     for nxt in G[v]:
#         if not seen[nxt]:
#             dfs(nxt)

# dfs(s)
# print("Yes" if seen[t] else "No")

#グリッドの場合
# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# H, W = map(int, input().split())
# field = [input().rstrip() for _ in range(H)]
# seen = [[False]*W for _ in range(H)]
# dx = (1, 0, -1, 0)
# dy = (0, 1, 0, -1)

# for i in range(H):
#     for j in range(W):
#         if field[i][j] == 's':
#             sh, sw = i, j
#         if field[i][j] == 'g':
#             gh, gw = i, j



# def dfs(h, w):
#     seen[h][w] =True
#     for dir in range(4):
#         if ( h+dy[dir] < 0 or h+dy[dir] >= H or w+dx[dir] < 0 or w+dx[dir] >= W): 
#             continue
#         if field[h+dy[dir]][w+dx[dir]] == "#":
#             continue
#         if (seen[h+dy[dir]][w+dx[dir]]):
#             continue
#         dfs(h+dy[dir], w+dx[dir])

# dfs(sh, sw)
# print("Yes" if seen[gh][gw] else "No")

#4‑2. 無向グラフの連結成分個数
# N, M = map(int, input().split())
# G = [[] for _ in range(N)]
# for _ in range(M):
#     a, b = map(int, input().split())
#     G[a].append(b)
#     G[b].append(a)

# seen = [False] * N
# def dfs(v):
#     seen[v] = True
#     for nxt in G[v]:
#         if not seen[v]:
#             dfs(nxt)

# cnt = 0
# for v in range(N):
#     if not seen[v]:
#         dfs(v)
#         cnt += 1
# print(cnt)


#4‑3. 二部グラフ判定（彩色 DFS）
# N, M = map(int, input().split())
# G = [[] for _ in range(N)]
# for _ in range(M):
#     a,b = map(int, input().split())
#     G[a].append(b)
#     G[b].append(a)

# color = [None] * N

# def dfs(v, c):
#     color[v] = c
#     for nxt in G[v]:
#         if color[nxt] is None:
#             if not dfs(nxt, c^1):
#                 return False
#             elif color[nxt] == c:
#                 return False
#         return True

# is_bipartite = True
# for v in range(N):
#     if color[v] is None:
#         if not dfs(v, 0):
#             is_bipartite = False
#             break

# print("Yes" if is_bipartite else "No")


#1. 問題 1：最大和問題（足し算 DP）
# import sys
# input = sys.stdin.readline

# n = int(input())
# a = list(map(int, input().split()))

# dp = [0]*(n+1)
# for i in range(n):
#     dp[i+1] = max(dp[i]+a[i], dp[i])

# print(dp[n])

#2. 0/1 ナップサック（重さ制限付き最大価値）
# import sys
# input = sys.stdin.readline

# n, W = map(int, input().split())
# values = []
# weights = []

# for _ in range(n):
#     v, w = map(int, input().split())
#     values.append(v)
#     weights.append(w)

# dp = [[0]*(W+1) for _ in range(n+1)]

# for i in range(n):
#     for w in range(W):
#         dp[i+1][w] = max(dp[i+1][w], dp[i][w])
#         if w >= weights[i]:
#             dp[i+1][w] = max(dp[i][w-weights[i]]+ values[i], dp[i+1][w])

# print(dp[n][W])

#bit全探索
# A = [3, 5, 8, 10]
# n = len(A)
# best = 0

# for mask in range(1<<n): #0~15
#     total = 0
#     for i in range(n):
#         if mask & (1 << i): #2^i
#             total += A[i]

#C - Switches
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# bulb = []
# for _ in range(M):
#     v = list(map(int, input().split()))
#     k, *swiches = v
#     bulb.append([s-1 for s in swiches])
# p = list(map(int,( input().split)))

# ans = 0
# for mask in range(1<<N):
#     ok = True
#     for i in range(M):
#         cnt =0
#         for s in bulb[i]:
#             if mask & (1 << s):
#                 cnt += 1
#         if cnt % 2 != p[i]:
#             ok = False
#             break
#     if ok:
#         ans += 1

# print(ans)


# heapq 優先度付きキュー（priority queue）とは、優先度にしたがって、優先度の高いものから順番に取り出すことができるものだ。
#最小値、最大値を素早く取り出すことができる 値の挿入順は気にしなくても良い。Olog(N)でできる
# import heapq
# numbers = [3, 5, 1, 6, 2, 4]
# heapq.heapify(numbers)
# print(numbers)

# print(heapq.heappop(numbers))
# print(heapq.heappop(numbers))

# print(numbers)

#例題1: ABC137 D - Summer Vacation いわゆる貪欲法
# import heapq
# n, m = map(int, input().split())
# jobs = [[] for _ in range(m+1)]

# for _ in range(n):
#     a, b = map(int, input().split())

#     if a <= m:
#         jobs[a].append(b)

# heap = []
# heapq.heapify(heap)
# total = 0

# for day in range(1, m+1):
#     for i in jobs[day]:
#         heapq.heappush(heap, -i)

#     if len(heap) > 0:
#         total += abs(heapq.heappop(heap))

# print(total)

#ABC141 D - Powerful Discount Tickets
# import heapq

# n, m = map(int, input().split())
# alist = list(map(lambda x: int(x)*(-1), input().split()))

# heapq.heapify(alist)

# for _ in range(m):
#     temp = heapq.heappop(alist)*(-1)//2
#     heapq.heappush(alist, temp*(-1))

# print(sum(map(lambda x: -x, alist)))


#ABC212 D - Querying Multiset
# import heapq
# q = int(input())
# sack = []
# heapq.heapify(sack)
# total = 0

# for i in range(q):
#     query = list(map(int, input().split()))
#     if query[0] == 1:
#         heapq.heappush(sack, query[1]-total)
#     elif query[0] == 2:
#         total += query[1]
#     else:
#         ans = heapq.heappop(sack)
#         print(ans + total)


#ランレングス圧縮
#ランレングス圧縮とは連続したデータを(値,連続する個数)として圧縮する可逆的データ圧縮アルゴリズム
#https://qiita.com/DaikiSuyama/items/07e237b7372e7c7b3432
from itertools import groupby
iterable = [1, 1, 2, 2, 2, 4, 4, 4, 5]
[[key,len(list(group))] for key,group in groupby(iterable)]
#[[1, 2], [2, 3], [4, 3], [5, 1]]


#座標圧縮
# https://qiita.com/mm-saito-1204/items/7ee43bc83c9bc766535b
# 目的：MLE(メモリ上限超過)を防ぐこと
# 配列がでかい時に有効

def zahyouassyuku(before_list):
    set_sort = sorted(list(set(before_list)))
    rank = {x:i+1 for i,x in enumerate(set_sort)}
    after_list = []
    for tmp in before_list:
        after_list.append(rank[tmp])
    return after_list

# C - Reorder Cards (座標圧縮の問題)
# H, W, N = map(int, input().split())
# A_list = []
# B_list = []

# for i in range(N):
#     a, b = map(int, input().split())
#     A_list.append(a)
#     B_list.append(b)

# A_set_sort = sorted(list(set(A_list)))
# B_set_sort = sorted(list(set(B_list)))
# A_rank = {x:i+1 for i,x in enumerate(A_set_sort)}
# B_rank = {x:i+1 for i,x in enumerate(B_set_sort)}

# A_after_list = []
# B_after_list = []
# for A_tmp, B_tmp in zip(A_list, B_list):
#     A_after_list.append(A_rank[A_tmp])
#     B_after_list.append(B_rank[B_tmp])
#     print(f'{A_rank[A_tmp]} {B_rank[B_tmp]}')


# C - 座圧
# N = int(input())
# A = list()
# for i in range(N):
#     a = int(input())
#     A.append(a)


# sort_set_A = sorted(list(set(A)))
# A_rank = {x:i for i,x in enumerate(sort_set_A)}
# after_A = []

# for a in A:
#     print(A_rank[a])

# C - ID 書き方勉強なるで
# from collections import defaultdict
# N, M = map(int, input().split())

# P_dict = defaultdict(list)
# before_ans = []

# for i in range(M):
#     p, y = map(int, input().split())
#     P_dict[p].append(y)
#     before_ans.append((p, y))

# rank_dict = {}
# for p in P_dict:
#     sorted_years = sorted(P_dict[p])
#     rank_dict[p] = {year: idx+1 for idx, year in enumerate(sorted_years)}

# for p,y in before_ans:
#     compressed_id = str(rank_dict[p][y]).zfill(6)
#     print(f"{p:06d}{compressed_id}")



# bit全探索
# https://qiita.com/mm-saito-1204/items/3feabbed2ba7bc9d06bd
# bit全探索の注意点
# bit全探索は先ほどの通り、2^N通りの全探索です。
# Nが30を超えるあたりで、AtCoderでTLEになってしまう20億を超えてしまいます。
# (実際は、他の処理でもループが発生するので、Nが20を超えたあたりからは事前に計算量を考えましょう。)

# TLEしそうな時は以下を検討します。
# 他のアルゴリズムを利用する
# (動的計画法(DP)や累積和など)
# ソートや重複排除など、データを工夫して減らしてからbit全探索する
# (数字の種類だけでいいなら0~9で10種類、2^10通りでいける等)
#example みかん
# N = int(input())
# X = list(map(int, input().split()))

# ans = 0
# for bit_num in range(1 << 20):
#     eat_grain = 0
#     eat_orange = 0

#     for i in range(20):
#         if bit_num & (1 << i):
#             eat_grain += X[i]
#             eat_orange += 1

#     if eat_orange != N:
#         continue

#     if eat_grain % 10 == 0:
#         ans += 1

# print(ans)

# B - 価格の合計
# n, X = map(int, input().split())

# A = list(map(int, input().split()))
# ans = 0
# for i in range(n):
#     if X & (1 << i):
#         ans += A[i]

# print(ans)

# C - Switches
# N, M = map(int, input().split())

# bulbs = []
# for i in range(M):
#     line = list(map(int, input().split()))
#     k = line[0]
#     switches = line[1:]
#     bulbs.append([s-1 for s in switches])

# p = list(map(int, input().split()))

# ans = 0

# for mask in range(1 << N):
#     ok = True
#     for i in range(M):
#         count = 0
#         for switch_idx in bulbs[i]:
#             if mask & (1 << switch_idx):
#                 count += 1

#         if count % 2 != p[i]:
#             ok = False
#             break

#     if ok:
#         ans += 1

# print(ans)

# C - HonestOrUnkind2
# N = int(input())
# say = []
# for n in range(N):
#     a = int(input())
#     for _ in range(a):
#         x, y = map(int, input().split())
#         say.append((x-1, y, n))
# ans = 0

# for mask in range(1 << N):
#     flag = True
#     for x, y, a in say:
#         if not mask & (1 << a):
#             continue
#         # 2ritomo honest
#         if y == 1 and mask & (1 << x) and mask & (1 << a):
#             continue
#         # syougennsyaga honest
#         elif y == 0 and not mask & (1 << x) and mask & (1 << a):
#             continue
#         else:
#             flag = False
#     if flag == True:
#         num_honest = bin(mask).count('1')
#         ans = max(num_honest, ans)

# print(ans)


# 順列全探索
# import itertools
# arr = [0, 1, 2]
# print(list(itertools.permutations(arr)))

# C - Average Length
# import itertools, math

# N = int(input())

# points = []
# for _ in range(N):
#     xy = list(map(int, input().split()))
#     points.append(xy)

# num = list(range(N))

# ptn = list(itertools.permutations(num))

# sum_dist = 0

# for p in ptn:
#     for i in range(len(p)-1):
#         a = p[i]
#         b = p[i+1]
#         x1 = points[a][0]
#         y1 = points[a][1]
#         x2 = points[b][0]
#         y2 = points[b][1]
#         sum_dist += math.sqrt((x1-x2)**2 + (y1-y2)**2)

# print(sum_dist/len(ptn))


# AtCoder Beginner Contest 150 C - Count Order
# from itertools import permutations

# N = int(input())
# P = list(map(int, input().split()))
# Q = list(map(int, input().split()))

# S = 0
# G = 0
# num = list(range(1, N+1))
# ptn = list(permutations(num))
# # print(num)
# # print(ptn)

# for index, perm in enumerate(ptn):
#     if P == list(perm):
#         S = index
#     if Q == list(perm):
#         G = index

# print(abs(S-G))


# C - One-stroke Path
# from itertools import permutations
# N, M = map(int, input().split())

# path_set = set()

# for i in range(M):
#     a, b = map(int, input().split())
#     path_set.add((a-1, b-1))

# num = list(range(N))
# ptn = list(permutations(num))
# cnt = 0
# for perm in ptn:
#     if perm[0] != 0:
#         continue
#     flag = True
#     for i in range(len(perm)-1):
#         if (perm[i], perm[i+1]) in path_set or (perm[i+1],perm[i]) in path_set:
#             continue
#         else:
#             flag = False
#             break

#     if flag == True:
#         cnt += 1

# print(cnt)

#区間DP
# 区間DPは「型ゲー」
# 分割型
# 区間をどこかで分割して「左 + 右 + コスト」で最小化／最大化。

# for length in range(2, n+1):
#     for l in range(0, n-length+1):
#         r = l+length-1
#         dp[l][r] = min(dp[l][k] + dp[k+1][r] + cost(l,r,k) for k in range(l,r))


# 例：連鎖行列積、石の合体、凸包DPなど。

# ペアリング型
# 左端を誰かと組ませて区間を縮めるタイプ。

# for length in range(2, n+1):
#     for l in range(0, n-length+1):
#         r = l+length-1
#         dp[l][r] = max(
#             dp[l+1][r],
#             max(dp[l+1][k-1] + score(l,k) + dp[k+1][r] for k in range(l+1,r+1))
#         )


# 例：最長括弧列、ゲーム系（区間取り合い）、部分列スコア最適化。

# → 区間DPは基本的にこのどっちかに収まる。