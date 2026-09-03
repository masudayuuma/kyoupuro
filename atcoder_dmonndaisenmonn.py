#D - Escape Route
# import sys
# from collections import deque

# input = sys.stdin.readline
# H, W = map(int, input().split())
# S = [list(input().rstrip()) for _ in range(H)]

# # 4 方向
# dr = (1, -1, 0, 0)
# dc = (0, 0, 1, -1)
# arrow = {(1, 0): 'v', (-1, 0): '^', (0, 1): '>', (0, -1): '<'}

# dist  = [[-1]*W for _ in range(H)]
# ans   = [row[:] for row in S]             # 出力用グリッドをコピー
# q = deque()

# # 1. 入口 (E) を BFS キューへ
# for r in range(H):
#     for c in range(W):
#         if S[r][c] == 'E':
#             dist[r][c] = 0
#             q.append((r, c))

# # 2. BFS
# while q:
#     r, c = q.popleft()
#     for k in range(4):
#         nr, nc = r + dr[k], c + dc[k]
#         if not (0 <= nr < H and 0 <= nc < W):
#             continue
#         if S[nr][nc] == '#':
#             continue
#         if dist[nr][nc] != -1:
#             continue
#         # nr,nc はまだ未訪問 -> parent は (r,c)
#         dist[nr][nc] = dist[r][c] + 1
#         ans[nr][nc] = arrow[(-dr[k], -dc[k])]   # 親方向へ向かう矢印
#         q.append((nr, nc))

# # 3. 出力
# for row in ans:
#     print(''.join(row))

#D - Domino Covering XOR
# def solve():
#     # 入力読み込み
#     H, W = map(int, input().split())
#     grid = []
#     for i in range(H):
#         row = list(map(int, input().split()))
#         grid.append(row)
    
#     # 全マスの値を1次元リストに変換
#     values = []
#     for i in range(H):
#         for j in range(W):
#             values.append(grid[i][j])
    
#     total_cells = H * W
#     max_score = 0
    
#     # 全ての可能なドミノ配置を試す
#     # ビットマスクで各マスが使用されているかを管理
#     def backtrack(pos, used_mask, current_xor):
#         nonlocal max_score
        
#         if pos == total_cells:
#             max_score = max(max_score, current_xor)
#             return
        
#         # 現在のマスが既に使用されている場合、次へ
#         if used_mask & (1 << pos):
#             backtrack(pos + 1, used_mask, current_xor)
#             return
        
#         # 1次元位置を2次元座標に変換
#         i, j = pos // W, pos % W
        
#         # オプション1: このマスに何も置かない（マスの値をXORに含める）
#         backtrack(pos + 1, used_mask, current_xor ^ values[pos])
        
#         # オプション2: 右隣とドミノを置く（水平）
#         if j + 1 < W:
#             right_pos = pos + 1
#             if not (used_mask & (1 << right_pos)):
#                 new_mask = used_mask | (1 << pos) | (1 << right_pos)
#                 backtrack(pos + 1, new_mask, current_xor)
        
#         # オプション3: 下隣とドミノを置く（垂直）
#         if i + 1 < H:
#             down_pos = pos + W
#             if not (used_mask & (1 << down_pos)):
#                 new_mask = used_mask | (1 << pos) | (1 << down_pos)
#                 backtrack(pos + 1, new_mask, current_xor)
    
#     backtrack(0, 0, 0)
#     print(max_score)

# solve()

# D - String Rotation
# これなんか上手くいかんかった、ロジックが違う、眠いのでchatgptに直してもらったのが下にある
# T = int(input())

# for i in range(T):
#     n = int(input())
#     s = input()
#     ans = s
#     for j in range(1, n):
#         if s[j-1] < s[j]:
#             continue
#         else:
#             for k in range(j, n):
#                 if s[j] < s[k]:
#                     ans = s[:j]+s[j+1:k]+s[j]+s[k:]
#                     break
#             break
#     print(ans)

# import sys
# input = sys.stdin.readline

# これは通った
# T = int(input())
# for _ in range(T):
#     n = int(input())
#     s = input().strip()

#     ans = s
#     # 最初の降順位置を探す（s[l] > s[l+1]）
#     for j in range(1, n):
#         if s[j-1] <= s[j]:
#             continue
#         l = j - 1  # 移動する文字の位置
#         # k = 最初に s[k] > s[l] となる位置（なければ n）
#         k = j
#         while k < n and s[k] <= s[l]:
#             k += 1
#         # 区間 [l, k-1] を左に1回巡回シフト
#         ans = s[:l] + s[l+1:k] + s[l] + s[k:]
#         break

#     print(ans)

# D - Garbage Removal
# １つでみたら最大N出るが、均し計算量がNなので
# H, W, N = map(int, input().split())
# nums_x = [set() for _ in range(H)]
# nums_y = [set() for _ in range(W)]
# for i in range(N):
#     x, y = map(int, input().split())
#     x -= 1
#     y -= 1
#     nums_x[x].add(y)
#     nums_y[y].add(x)

# Q = int(input())
# for i in range(Q):
#     q, number = input().split(' ')
#     cnt = 0
#     number = int(number)
#     if q == '1':
#         for num in nums_x[number-1]:
#             nums_y[num].discard(number-1)
#             cnt += 1
#         nums_x[number-1].clear()
#     else:
#         for num in nums_y[number-1]:
#             nums_x[num].discard(number-1)
#             cnt += 1
#         nums_y[number-1].clear()
#     print(cnt)

# D - Escape Route
# from collections import deque
# H, W = map(int, input().split())
# S = [ input() for i in range(H)]
# T = [list(row) for row in S]

# queue = deque()
# visited = [[False]*W for _ in range(H)]
# for i in range(H):
#     for j in range(W):
#         if S[i][j] == 'E':
#             queue.append((i, j))


# diff = ((1, 0), (-1, 0), (0, -1), (0, 1))
# while queue:
#     i, j = queue.popleft()
#     for dx, dy in diff:
#         if not 0 <= i+dx < H or not 0 <= j+dy < W or not T[i+dx][j+dy] == '.':
#             continue
#         if dx == 1:
#             T[i+dx][j+dy] = '^'
#         elif dx == -1:
#             T[i+dx][j+dy] = 'v'
#         elif dy == 1:
#             T[i+dx][j+dy] = '<'
#         elif dy == -1:
#             T[i+dx][j+dy] = '>'

#         queue.append((i+dx, j+dy))


# for row in T:
#     print(''.join(row))

# D - Swap to Gather
# from collections import defaultdict
# N = int(input())
# S = input()
# dict_r_l_n = defaultdict(list)
# cnt_l_1 = 0
# cnt_r_1 = 0
# for i in range(len(S)):
#     if S[i] == '0':
#         dict_r_l_n[i].append(cnt_l_1)
#     else:
#         cnt_l_1 += 1

# for i in range(len(S)-1, -1, -1):
#     if S[i] == '0':
#         dict_r_l_n[i].append(cnt_r_1)
#     else:
#         cnt_r_1 += 1

# ans = 0
# for key_i, d in dict_r_l_n.items():
#     target = min(d[0], d[1])
#     ans += target

# print(ans)

# D - Bonfire  / 
# N, R, C = map(int, input().split())

# S = input()

# work_dict = {'N': (1, 0), 'S': (-1, 0), 'E': (0, -1), 'W': (0, 1)}
# cnt = 0
# person_pos = [R, C]
# fire_pos = [0, 0]
# smoke_pos = {(0, 0)}
# ans = []
# for i in range(len(S)):
#     dx, dy = work_dict[S[i]]
#     person_pos[0] += dx
#     person_pos[1] += dy
#     fire_pos[0] += dx
#     fire_pos[1] += dy
#     smoke_pos.add(tuple(fire_pos))
#     if tuple(person_pos) in smoke_pos:
#         ans.append(1)
#     else:
#         ans.append(0)
# print(''.join(map(str, ans)))

# D - Minimum XOR Path
# from collections import defaultdict, deque
# N, M = map(int, input().split())

# path_dict = defaultdict(list)
# ans = float('inf')
# for m in range(M):
#     u, v, w = map(int, input().split())
#     path_dict[u].append((v, w))
#     path_dict[v].append((u, w))

# # total_xor = 0
# # set_n = {1}
# def dft(i:int, total_xor:int, s_n:set):
#     # local_total_xor = total_xor
#     global ans
#     for n, w in path_dict[i]:
#         if n in s_n:
#             continue
#         new_xor = total_xor ^ w
#         s_n.add(n)
#         if n == N:
#             ans = min(ans, new_xor)
#         else:
#             dft(n, new_xor, s_n)
#         new_xor ^= w
#         s_n.remove(n)

# dft(1, 0, {1})

# print(ans)

# D - Pop and Insert
# T = int(input())

# for i in range(T):
#     n = int(input())
#     s = input()
#     ran_length = [[s[0], 1]]

#     for i in range(1, len(s)):
#         if s[i-1] == s[i]:
#             ran_length[-1][1] += 1
#         else:
#             ran_length.append([s[i], 1])

#     max_cnt_0 = (0, '0', 0)
#     max_cnt_1 = (0, '1', 0)
#     for i, lenght_list in enumerate(ran_length):
#         if lenght_list[0] == '0' and max_cnt_0[2] < lenght_list[1]:
#             max_cnt_0 = (i, lenght_list[0], lenght_list[1])
#         if lenght_list[0] == '1' and max_cnt_1[2] < lenght_list[1]:
#             max_cnt_1 = (i, lenght_list[0], lenght_list[1])

#     ans_list_0 = [x for i, x in enumerate(ran_length) if i != max_cnt_0[0]]
#     ans_list_1 = [x for i, x in enumerate(ran_length) if i != max_cnt_1[0]]
#     ans_0_cnt = 0
#     ans_1_cnt = 0
#     for num, cnt in ans_list_0:
#         if num == '1':
#             ans_0_cnt += 1*cnt
#         else:
#             ans_0_cnt += 2*cnt

#     for num, cnt in ans_list_1:
#         if num == '1':
#             ans_1_cnt += 2*cnt
#         else:
#             ans_1_cnt += 1*cnt

#     print(min(ans_1_cnt, ans_0_cnt))

# D - Ulam-Warburton Automaton
# from collections import deque
# H, W = map(int, input().split())

# S = [list(input()) for _ in range(H)]

# queue = deque()
# ans = 0
# for i in range(H):
#     for j in range(W):
#         if S[i][j] == "#":
#             ans += 1
#             queue.append((i, j))

# diff = ((1, 0), (-1, 0), (0, 1), (0, -1))

# while queue:
#     new_queue = deque()
#     nurikae = set()
#     for h, w in queue:
#         for dh, dw in diff:
#             nh, nw = h+dh, w+dw
#             if not 0 <= nh <H or not 0 <= nw <W or S[nh][nw] == '#':
#                 continue
#             # target_pos = S[h][w]
#             cnt = 0
#             for t_dh, t_dw in diff:
#                 t_h = t_dh+nh
#                 t_w = t_dw+nw
#                 if not 0 <= t_h <H or not 0 <= t_w <W:
#                     continue
#                 if S[t_h][t_w] == '#':
#                     cnt += 1
#             if cnt == 1:
#                 nurikae.add((nh, nw))
#                 ans += 1
#                 new_queue.append((nh, nw))
#     for h, w in nurikae:
#         S[h][w] = '#'
#     queue.clear()
#     queue = new_queue

# print(ans)

# from collections import deque
# H, W = map(int, input().split())
# S = [list(input()) for _ in range(H)]

# queue = deque()
# ans = 0
# for i in range(H):
#     for j in range(W):
#         if S[i][j] == "#":
#             ans += 1
#             queue.append((i, j))

# diff = ((1, 0), (-1, 0), (0, 1), (0, -1))

# while queue:
#     to_add = set()
#     seen = set()
#     # いま黒いマスの隣だけを調べて、その手で黒くなる候補を集める
#     for h, w in queue:
#         for dh, dw in diff:
#             nh, nw = h + dh, w + dw
#             if not (0 <= nh < H and 0 <= nw < W):
#                 continue
#             if S[nh][nw] == '#':
#                 continue
#             if (nh, nw) in seen:
#                 continue
#             seen.add((nh, nw))
#             # この手では「もともとの盤面」で黒近傍1かどうかだけを見る
#             cnt = 0
#             for t_dh, t_dw in diff:
#                 th, tw = nh + t_dh, nw + t_dw
#                 if 0 <= th < H and 0 <= tw < W and S[th][tw] == '#':
#                     cnt += 1
#             if cnt == 1:
#                 to_add.add((nh, nw))
#     # 同時更新：この手で黒くなるマスをまとめて反映
#     if not to_add:
#         break
#     for h, w in to_add:
#         S[h][w] = '#'
#     ans += len(to_add)
#     queue = deque(to_add)

# print(ans)

# D - Get Many Stickers
# ちゃうかったやつ
# from collections import defaultdict
# from bisect import bisect_right
# N, M = map(int, input().split())

# a_b = [list(map(int, input().split())) for _ in range(M)]
# seted_b_dict = defaultdict(int)


# for i in range(M):
#     a, b = a_b[i]
#     seted_b_dict[a] = max(seted_b_dict[a], b)

# max_value = 0
# saitekika_b_dict = defaultdict(int)
# saiteki_a_list = []
# for key, value in sorted(seted_b_dict.items()):
#     max_value = max(max_value, value)
#     saitekika_b_dict[key] = max_value
#     saiteki_a_list.append(key)

# # N_i = 1
# cnt = 0
# while bisect_right(saiteki_a_list, N) > 0:
#     idx = bisect_right(saiteki_a_list, N)
#     N = N-saiteki_a_list[idx-1]+saitekika_b_dict[saiteki_a_list[idx-1]]
#     cnt += 1

# print(cnt)

# # D - Get Many Stickers
# N, M = map(int, input().split())
# a_b = [list(map(int, input().split())) for _ in range(M)]

# # (d, a, b) のリストを作成してdでソート
# exchanges = []
# for a, b in a_b:
#     d = a - b
#     exchanges.append((d, a, b))

# exchanges.sort()  # dの昇順でソート

# ans = 0
# for d, a, b in exchanges:
#     if a > N:
#         continue
#     # この交換を何回連続で実行できるか
#     x = (N - a) // d + 1
#     ans += x
#     N -= x * d

# print(ans)

# D - Colorful Bracket Sequence
# from collections import deque
# S = input()

# que = deque()

# backet_dict = {')': '(', ']': '[', '>': '<'}
# for i in range(len(S)):
#     if S[i] in ('(', '[', '<'):
#         que.append(S[i])
#     else:
#         if not que:
#             que.append(S[i])

#         if backet_dict[S[i]] == que[-1]:
#             que.pop()
#         else:
#             que.append(S[i])

# print('Yes' if len(que) == 0 else 'No')

# D - Neighbor Distance
#通らず、複雑すぎるロジック
# from sortedcontainers import SortedList
# N = int(input())
# X = list(map(int, input().split()))

# st = SortedList([[0, X[0]], [X[0], X[0]]])
# ans = X[0]*2
# print(ans)

# for val in X[1:]:
#     index = st.bisect_left([val, 0])
#     if index == len(st):
#         st.add((val, val-st[index-1][0]))
#         target_l = st[index-1]
#         if target_l[1] > val-target_l[0]:
#             ans += val-target_l[0]*2-target_l[1]
#             target_l[1] = val-target_l[0]
#         else:
#             ans +- val-target_l[0]
#     else:
#         st.add((val, min(val-st[index-1][0], st[index][0]-val)))
#         ans += min(val-st[index-1][0], st[index][0]-val)
#         target_l = st[index-1]
#         target_r = st[index+1]
#         if target_l[1] > val-target_l[0]:
#             ans += val-target_l[0]-target_l[1] 
#             target_l[1] = val-target_l[0]
#         if target_r[1] > target_r[1]-val:
#             ans += target_r[0]-val-target_r[1]
#             target_r[1] = val-target_r[0]
#     print(ans)

#ai回答だけど通った
# from sortedcontainers import SortedList

# def nearest(x, st):
#     """座標xの最近傍距離を計算 O(log N)"""
#     idx = st.index(x)
#     res = 2 * 10**9
#     if idx > 0:
#         res = min(res, x - st[idx - 1])
#     if idx < len(st) - 1:
#         res = min(res, st[idx + 1] - x)
#     return res

# N = int(input())
# X = list(map(int, input().split()))

# st = SortedList([0, X[0]])
# ans = X[0] * 2
# print(ans)

# for val in X[1:]:
#     # valを挿入する位置を探す
#     idx = st.bisect_left(val)
    
#     # 影響を受ける点（左隣、右隣）を特定
#     hit = []
#     if idx > 0:
#         hit.append(st[idx - 1])
#     if idx < len(st):
#         hit.append(st[idx])
    
#     # 古い距離を引く
#     for pos in hit:
#         ans -= nearest(pos, st)
    
#     # 新しい点を挿入
#     st.add(val)
#     hit.append(val)
    
#     # 新しい距離を足す
#     for pos in hit:
#         ans += nearest(pos, st)
    
#     print(ans)

# ↑を模写
# from sortedcontainers import SortedList

# def nearest(x, st):
#     idx = st.index(x)
#     res =2* 10**9
#     if idx > 0:
#         res = min(res, x-st[idx-1])
#     if idx < len(st)-1:
#         res < len(st)-1
#         res = min(res, st[idx+1]-x)
#     return res

# N = int(input())
# X = list(map(int, input().split()))

# st = SortedList([0, X[0]])
# ans = X[0]*2
# print(ans)

# for val in X[1:]:
#     idx = st.bisect_left(val)
#     hit = []
#     if idx > 0:
#         hit.append(st[idx-1])
#     if idx < len(st):
#         hit.append(st[idx])

#     for pos in hit:
#         ans -= nearest(pos, st)

#     st.add(val)
#     hit.append(val)

#     for pos in hit:
#         ans += nearest(pos, st)

#     print(ans)

# D - 183184
# from math import isqrt

# T = int(input())
# for _ in range(T):
#     C, D = map(int, input().split())
#     ans = 0
    
#     xmin, xmax = 1, 9
#     cshift = 10
    
#     while xmin <= C + D:
#         l = max(xmin, C + 1)
#         r = min(xmax, C + D)
        
#         if l <= r:
#             vl = C * cshift + l
#             vr = C * cshift + r
#             # 区間 [vl, vr] に含まれる平方数の個数
#             ans += isqrt(vr) - isqrt(vl - 1)
        
#         xmin *= 10
#         xmax = (xmax + 1) * 10 - 1
#         cshift *= 10
    
#     print(ans)

# 模写
# from math import sqrt

# T = int(input())
# for _ in range(T):
#     C, D = map(int, input().split())
#     ans = 0

#     xmin, xmax = 1, 9
#     cshift = 10

#     while xmin <= C+D:
#         l = max(xmin, C+1)
#         r = min(xmax, C+D)

#         if l <= r:
#             vl = C*cshift+l
#             vr = C*cshift+r
#             ans += isqrt(vr)-isqrt(vr-1)

#         xmin *= 10
#         xmax = (xmax+1)*10-1
#         cshift *= 10
#     print(ans)

# D - On AtCoder Conference
# from collections import defaultdict
# from bisect import bisect_left
# N, M, C = map(int, input().split())
# A = list(map(int, input().split()))

# a_dict = defaultdict(int)
# for a in A:
#     a_dict[a] += 1

# positions = sorted(a_dict.keys())


# prefix_list = [0]
# # prefix_list_pos = []
# for i in range(2):
#     for pos in positions:
#         prefix_list.append(prefix_list[-1]+a_dict[pos])
#         # if i == 1:
#         #     prefix_list_pos.append(pos+M)
#         # else:
#         #     prefix_list_pos.append(pos)




# ans = 0
# K = len(positions)
# for i, start_pos in enumerate(positions):
#     idx = i+1
#     target_idx = bisect_left(prefix_list, prefix_list[idx]+C, idx)
#     people_met = prefix_list[target_idx]-prefix_list[idx]
#     if i+1 < K:
#         gap = positions[i+1]-start_pos
#     else:
#         gap = M - start_pos+ positions[0]
#     ans += people_met*gap

# print(ans)

# D - Transmission Mission
# from sortedcontainers import SortedDict
# N, M = map(int, input().split())
# X = sorted(set((list(map(int, input().split())))))

# house_have_range = []
# negihbor_range = list()
# for i in range(1, len(X)):
#     negihbor_range.append(X[i]-X[i-1])

# if M >= len(X):
#     print(0)
#     exit()

# negihbor_range.sort()

# do_num = len(X)-M
# total = sum(negihbor_range[:do_num])

# print(total)

# D - Make Geometric Sequence
#場合分けに対応できずWA
# T = int(input())

# for t in range(T):
#     N = int(input())
#     A = list(map(int, input().split()))

#     A_abs_sorted = sorted(A, key=lambda x: abs(x))
#     set_A = set(A)

#     for i in range(2, len(A_abs_sorted)):
#         if A_abs_sorted[i-1]*A_abs_sorted[1] != A_abs_sorted[i]*A_abs_sorted[0]:
#             print('No')
#             break
#     else:
#         print('Yes')

# T = int(input())

# for i in range(T):
#     n = int(input())
#     a = list(map(int, input().split()))

#     a.sort(key=lambda x: abs(x))

#     ok = True
#     for i in range(n-2):
#         if a[i]*a[i+2] != a[i+1]*a[i+1]:
#             ok = False
#             break
#     if ok:
#         print('Yes')
#         continue
    
#     if abs((a[0])) == abs(a[-1]):
#         pos = sum(1 for x in a if x > 0)
#         neg = n-pos
#         if abs(neg-pos) <= 1:
#             print('Yes')
#             continue

#     print('No')

# D - Goin' to the Zoo
# 下記の回答は間違っている
# bitで1024回回して、その結果をset()に動物入れていけば良さそう。
# from collections import defaultdict
# N, M = map(int, input().split())
# C = list(map(int, input().split()))

# love_animals = set(i+1 for i in range(M))
# zoo_to_animal = defaultdict(set)

# for m in range(M):
#     k, *a = map(int, input().split())
#     for i in a:
#         zoo_to_animal[i-1].add(m+1)

# ans = float('inf')
# for mask in range(1 << N):
#     ans_set = set()
#     total_cost = 0
#     for i in range(N):
#         if (1 << i) & mask:
#             ans_set = ans_set.union(zoo_to_animal[i])
#             total_cost += C[i]
#     if love_animals == ans_set:
#         ans = min(total_cost, ans)

# print(ans*2)

# こっちはあってる
# N, M =map(int, input().split())

# C =list(map(int, input().split()))

# a = []
# for _ in range(M):
#     tmp = list(map(int, input().split()))
#     k, arr = tmp[0], tmp[1:]
#     arr = [z-1 for z in arr]
#     a.append(arr)

# # 3進数表現実装
# p3 = [1]*(N+1)
# for i in range(N):
#     p3[i+1] = p3[i]*3

# INF = float('inf')
# ans = INF

# for s in range(p3[N]):
#     t_i = [0]*N
#     cost = 0

#     for i in range(N):
#         # 3進数表現実装
#         t = (s // p3[i]) %3
#         t_i[i] = t
#         cost += C[i]*t
#     if cost >= ans:
#         continue

#     ok = True
#     for j in range(M):
#         cnt = 0
#         for z in a[j]:
#             cnt += t_i[z]
#         if cnt < 2:
#             ok = False
#             break

#     if ok:
#         ans = cost
# print(ans)

# ３進数表現を[00, 01, 10]でやってる
# n, m = map(int, input().split())
# cost = tuple(map(int, input().split()))
# zoo = [[] for _ in range(m)]
# for animal in range(m):
#     _, *a = map(lambda s_: int(s_) -1, input().split())
#     for j in a:
#         zoo[j].append(animal)

# ones = [sum(1 << 2*j for j in z) for z in zoo]
# two_all = sum(2 << 2*j for j in range(m))

# def add_one(watched, one):
#     return watched+(one & ~watched >> 1)

# def dfs(i, watched, ans):
#     if i == n:
#         return ans if watched == two_all else 10**18
#     ans0 = dfs(i+1, watched, ans)
#     watched = add_one(watched, ones[i])
#     ans1 = dfs(i+1, watched, ans+cost[i])
#     watched = add_one(watched, ones[i])
#     ans2 = dfs(i+1, watched, ans+cost[i]*2)
#     return min(ans0, ans1, ans2)

# print(dfs(0, 0, 0))

# O((4^N)NM)
# N, M = map(int, input().split())
# C = list(map(int, input().split()))
# G = [[] for i in range(N)]
# for i in range(M):
#     v = list(map(int, input().split()))[1:]
#     for e in v:
#         G[e-1].append(i)

# ans = float('inf')
# for S in range(1 << (2*N)):
#     cnt = [0]*M
#     cost = 0
#     for i in range(2*N):
#         if S >> i & 1:
#             for e in G[i//2]:
#                 cnt[e] += 1
#             cost += C[i//2]
#     if min(cost) >= 2:
#         ans = min(ans, cost)
# print(ans)

# D - Robot Customize
# 幸福値順でソート？
# 500^2 = 
# めちゃくちゃDP問題
# これはMLEした1次元の配列に圧縮する必要ある
# N = int(input())
# W = [0 for _ in range(N)]
# H = [0 for _ in range(N)]
# B = [0 for _ in range(N)]

# total = 0
# base_happines = 0
# for i in range(N):
#     W[i], H[i], B[i] = map(int, input().split())
#     total += W[i]
#     base_happines += B[i]


# INF = float('inf')
# head_weigt_max = total//2
# dp = [[-INF for _ in range(head_weigt_max+1)] for _ in range(N+1)]

# dp[0][0] = 0


# for i in range(1, N+1):
#     for j in range(head_weigt_max+1):
#         if dp[i-1][j] == -INF:
#             continue
#         dp[i][j] = max(dp[i-1][j], dp[i][j])
#         hap = dp[i-1][j]
#         if H[i-1]>B[i-1] and j+W[i-1] <= head_weigt_max:
#             dp[i][j+W[i-1]] = max(hap + H[i-1]-B[i-1], dp[i][j])

# print(max(dp[-1])+base_happines)

# 1次元配列で実装_AC
# N = int(input())
# W = [0 for _ in range(N)]
# H = [0 for _ in range(N)]
# B = [0 for _ in range(N)]

# total = 0
# base_happines = 0
# for i in range(N):
#     W[i], H[i], B[i] = map(int, input().split())
#     total += W[i]
#     base_happines += B[i]

# INF = float('inf')
# head_weigt_max = total//2
# # 1次元配列に変更
# dp = [-INF for _ in range(head_weigt_max+1)]

# dp[0] = 0

# for i in range(N):
#     # 後ろから更新することで、同じ配列を使い回せる
#     for j in range(head_weigt_max, -1, -1):
#         if dp[j] == -INF:
#             continue
#         # 頭に付ける
#         if j + W[i] <= head_weigt_max:
#             dp[j + W[i]] = max(dp[j + W[i]], dp[j] + H[i] - B[i])

# print(max(dp) + base_happines)

# D - Doubles
# from collections import Counter
# N = int(input())
# A_counter_list = []
# A_cnt = []
# for i in range(N):
#     k, *a = map(int, input().split())

#     A = Counter(a)
#     A_counter_list.append(A)
#     A_cnt.append(k)
# ans = 0.0
# for i in range(N-1):
#     for j in range(i+1, N):
#         tmp_ans = 0.0
#         mother = A_cnt[i]*A_cnt[j]
#         for num in A_counter_list[i]:
#             if num in A_counter_list[j]:
#                 child = A_counter_list[i][num]*A_counter_list[j][num]
#                 tmp_ans += child/mother
#         ans = max(tmp_ans, ans)

# print(ans)

# # D - The Simple Game
# # dp問題
# # まず、最終から考えてやっていく。
# from collections import defaultdict
# T = int(input())

# for i in range(T):
#     n, m, k = map(int, input().split())
#     s = input()
#     gragh_dict = defaultdict(set)
#     for j in range(m):
#         u, v = map(int, input().split())
#         gragh_dict[u-1].add(v-1)

#     dp = [None]*n
#     for j in range(n-1, -1, -1):
#         if s[j] == 'A':
#             dp[j] = True
#         else:
#             dp[j] = False

#     for x in range(2*k-1, -1, -1):
#         nex = dp[:]
#         flag = (x%2 == 0)
#         # 0index
#         for u in range(n):
#             for v in gragh_dict[u]:
#                 if not nex[v] and not flag:
#                     dp[u] = False
#                     # flag = not flag
#                     break
#                 if nex[v] and flag:
#                     dp[u] = True
#                     # flag = not flag
#                     break
#                 else:
#                     dp[u] = nex[v]
#                     continue
#     print('Alice' if dp[0] else 'Bob')
        
# D - XOR Shortest Walk
# DFSかな
# 下のやつだとDFSが指数関数的に計算量が増えてしまうのでTLE。
# from collections import defaultdict
# N, M = map(int, input().split())

# move_cost = defaultdict(set)
# min_weight = float('inf')
# for i in range(M):
#     a, b, w = map(int, input().split())

#     move_cost[a].add((b, w))


# def walk_xor(base, total_w, visited):
#     global min_weight
#     if base == N:
#         min_weight = min(min_weight, total_w)

#     for nex, w in move_cost[base]:
#         if (nex, w) in visited:
#             continue
#         visited.add((nex, w))
#         now_w = total_w^w
#         walk_xor(nex, now_w, visited)
#         visited.remove((nex, w))

# visited = set()
# walk_xor(1, 0, visited)
# print(min_weight if not min_weight == float('inf') else -1)

# from collections import defaultdict, deque

# N, M = map(int, input().split())

# move_cost = defaultdict(list)
# for _ in range(M):
#     a, b, w = map(int, input().split())
#     move_cost[a].append((b, w))

# MAX_W = 1 << 10
# dp = [[False] * MAX_W for _ in range(N+1)]

# q = deque()
# dp[1][0] = True

# q.append((1, 0))

# while q:
#     v, x = q.popleft()
#     for nex, w in move_cost[v]:
#         nx = x^w
#         if not dp[nex][nx]:
#             dp[nex][nx] = True
#             q.append((nex,nx))

# ans = -1
# for x in range(MAX_W):
#     if dp[N][x]:
#         ans =x
#         break

# print(ans)

# D - Flip to Gather
# T = int(input())

# for i in range(T):
#     n = int(input())
#     s = input()

#     r1 = [0]*(n+1)
#     for i in range(n-1, -1, -1):
#         r1[i] = r1[i+1]
#         if s[i] == '1':
#             r1[i] += 1

#     INF = 10**18
#     ans = INF

#     l0 = 0
#     l01 = 0
#     best = 0

#     for r in range(1, n+1):
#         if s[r-1] == '0':
#             l0 += 1
#             l01 -= 1
#         else:
#             l01 += 1

#         best = min(best, l01)

#         # best = left_1-left_0
#         now = r1[r] + l0 + best
#         ans = min(ans, now)

#     print(ans)

# DPバージョン
# T = int(input())

# for t in range(T):
#     n = int(input())
#     s = input()
#     INF = 10**18
#     dp = [[INF]*(n+1) for _ in range(3)]
#     dp[0][0] = 0

#     for j in range(n):
#         for i in range(3):
#             if dp[i][j] == INF:
#                 continue

#             want = 1 if i == 1 else 0

#             cost = 1 if s[j] != str(want) else 0

#             dp[i][j+1] = min(dp[i][j+1], dp[i][j]+cost)
#             if i < 2:
#                 next_cost = 0 if cost == 1 else 1
#                 dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j]+next_cost)
#     print(min(dp[0][n], dp[1][n], dp[2][n]))

# D - Switch Seats
# from collections import defaultdict

# T = int(input())

# for t in range(T):
#     N = int(input())
#     A = list(map(int, input().split()))
#     ans = 0
#     non_see_val = set()

#     val_dict = defaultdict(set)
#     for i in range(N*2):
#         if (i < N*2-1 and A[i] == A[i+1]) or (i > 0 and A[i] == A[i-1]):
#             non_see_val.add(A[i])
#             continue
#         val_dict[A[i]].add(i)

#     collab_set = set()
#     for i in range(N*2-1):
#         if A[i] in non_see_val or A[i+1] in non_see_val:
#             continue
#         target = tuple(sorted([A[i], A[i+1]]))
#         if not target in collab_set:
#             collab_set.add(target)
#         else:
#             continue

#         pos = sorted(val_dict[A[i]] | val_dict[A[i+1]])
#         if pos[0] + 1 == pos[1] and pos[2] + 1 == pos[3]:
#             ans += 1

#     print(ans)

# D - Squares in Circle
# R = int(input())
# ans = 0
# for x in range(1, R):
#     y = int((R**2-(x+0.5)**2)**(0.5)-0.5)
#     ans += y+1

# print(ans*4+1)

# D - Coming of Age Celebration
# N = int(input())
# A = list(map(int, input().split()))

# s = 0
# r = [0]*N

# for i in range(N):
#     A[i] += s

#     num = min(A[i], N-i-1)
#     A[i] -= num

#     s += 1
#     r[i+num] += 1

#     s -= r[i]
# print(*A)

# D - Repeated Sequence
# N, S = map(int, input().split())
# A = list(map(int, input().split()))

# sum_A = sum(A)
# nxt_s = S
# if nxt_s >= sum_A:
#     nxt_s = S%sum_A

# l, r = 0, 0
# B = A+A
# total = 0
# while l < N:
#     while total < nxt_s and r < N*2:
#         total += B[r]
#         r += 1
#         # print(total, nxt_s)
#     if total == nxt_s:
#         print('Yes')
#         exit()
#     total -= B[l]
#     l += 1

# print('No')

# D - Keep Distance
# N, M = map(int, input().split())

# ans = []

# def dfs(a :list):
#     if len(a) == N:
#         ans.append(a[:])
#         return
    
#     l = 1
#     if len(a) > 0:
#         l = a[-1] + 10

#     a.append(l)

#     while a[-1]+10 * (N-len(a)) <= M:
#         dfs(a)
#         a[-1] += 1

#     a.pop()

# dfs([])

# print(len(ans))
# for a in ans:
#     print(*a)

# D - Count Simple Paths
# H, W, K = map(int, input().split())

# grid = [list(input()) for _ in range(H)]
# ans = 0

# diff = ((-1, 0), (1, 0), (0, -1), (0, 1))
# def dfs(i, j, rest):
#     global ans
#     if rest == 0:
#         ans += 1
#         return
    
#     original = grid[i][j]
#     grid[i][j] = '#' 

#     for dx, dy in diff:
#         tx, ty = i+dx, j+dy
#         if not 0 <= tx < H or not 0 <= ty < W or grid[tx][ty] == '#':
#             continue
#         dfs(tx, ty, rest-1)
    
#     grid[i][j] = original


# for i in range(H):
#     for j in range(W):
#         if grid[i][j] == '.':
#             dfs(i, j, K)

# print(ans)

# D - Forbidden List 2
# from bisect import bisect_left
# N, Q = map(int, input().split())
# A = list(map(int, input().split()))
# A.sort()

# for _ in range(Q):
#     x, y = map(int, input().split())
#     si = bisect_left(A, x)

#     ng = si-1
#     ok = N

#     while ok - ng > 1:
#         mid = (ok+ng)//2
#         total = A[mid]-x+1
#         forbidden = mid-si+1
#         allowed = total - forbidden

#         if allowed >= y:
#             ok = mid
#         else:
#             ng = mid

#     ans = x+(y-1)+(ok-si)
#     print(ans)

# D - Adjacent Distinct String
# from collections import Counter
# import heapq
# T = int(input())

# for q in range(T):
#     s = list(input())
#     s_cnt = Counter(s)
#     s_cnt_list = [(-cnt, val) for val, cnt in s_cnt.items()]
#     heapq.heapify(s_cnt_list)
#     save = None
#     ans = []

#     while s_cnt_list:
#         cnt, val = heapq.heappop(s_cnt_list)

#         cnt += 1
#         ans.append(val)
#         if save:
#             heapq.heappush(s_cnt_list, save)
#             save = None
#         if cnt < 0:
#             save = (cnt, val)

#     if save:
#         print('No')
#     else:
#         print('Yes')
#         print(''.join(ans))


# D - Repeatedly Repainting
# 最初でqueueに入れるタイミングで#がなければ、全部.で出力できる？
# from collections import deque
# H, W = map(int, input().split())
# grid = []
# for i in range(H):
#     s = list(input())

#     grid.append(s)

# flag = [[False]*(W) for _ in range(H)]
# queue = deque()
# for i in range(H):
#     for j in range(W):
#         if grid[i][j] == '#':
#             queue.append((i, j))
        
# if len(queue) == 0 or len(queue) == H*W:
#     for _ in range(H):
#         print('.'*W)
#     exit()

# diff = ((1, 0), (1, -1), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1))
# nxt_q = deque()
# cnt = 0

# while queue:
#     i, j = queue.popleft()
#     for dy, dx in diff:
#         y = dy+i
#         x = dx+j
#         if not 0 <= y < H or not 0 <= x < W or flag[y][x] or grid[y][x] != '.':
#             continue
#         flag[y][x] = True
#         nxt_q.append((y, x))


# while queue or nxt_q:
#     if not queue:
#         queue = nxt_q.copy()
#         nxt_q = deque()
#         cnt += 1

#     i, j = queue.popleft()
#     if cnt % 2 == 1:
#         grid[i][j] = "."
#     else:
#         grid[i][j] = "#"

#     for dy, dx in diff:
#         y = dy+i
#         x = dx+j

#         if not 0 <= y < H or not 0 <= x < W or flag[y][x]:
#             continue
#         flag[y][x] = True
#         nxt_q.append((y, x))

# for i in range(H):
#     print(''.join(grid[i]))

# D - Accomplice
# N, D = map(int, input().split())
# prefix = [0]*(10**6+1)
# ans = 0
# for i in range(N):
#     s, t = map(int, input().split())

#     if s > t-D+1:
#         continue

#     prefix[s] += 1
#     prefix[t-D+1] -= 1

# for i in range(1, len(prefix)):
#     prefix[i] += prefix[i-1]
#     if prefix[i] >= 2:
#         cnt = prefix[i]
#         ans += cnt*(cnt-1)//2

# print(ans)

# D - Count Subgrid Sum = K
# H, W, K = map(int, input().split())
# grid = []
# for _ in range(H):
#     grid.append(list(map(int, input())))

# for i in range(1, H):
#     for j in range(W):
#         grid[i][j] += grid[i-1][j]

# ans = 0
# for h1 in range(H):
#     for h2 in range(h1, H):
        
#         total = 0
#         l = 0
#         c = {}
#         c[0] = 1

#         for w in range(W):
#             h1_c = grid[h1-1][w] if h1-1 >= 0 else 0
#             h2_c = grid[h2][w]
#             total += h2_c-h1_c
#             ans += c[total-K] if total-K in c else 0
#             c[total] = c.get(total, 0) + 1

# print(ans)

# D - Chalkboard Median
# from sortedcontainers import SortedList

# sorted_list = SortedList()
# sorted_list.add(int(input()))

# for i in range(int(input())):
#     a, b = map(int, input().split())

#     sorted_list.add(a)
#     sorted_list.add(b)

#     print(sorted_list[i+1])

# D - Raise Minimum
# import math 
# N, K = map(int, input().split())

# A = list(map(int, input().split()))
# l = min(A)-1
# r = min(A) + K * N + 1
# while r-l > 1:
#     mid = (l+r)//2
#     cnt = 0
#     for i, a in enumerate(A):
#         cnt += (mid - a + i) // (i + 1) if mid > a else 0
#         if cnt > K:
#             break
#     if cnt > K:
#         r = mid
#     else:
#         l = mid

# print(l)

# D - Not Adjacent 2
# S = input()

# c_dict = {'a': 0, 'b': 0, 'c': 0}

# total = 0
# for s in S:
#     ans = 1
#     for c in c_dict:
#         if c == s:
#             continue
#         ans += c_dict[c]
#     ans %= 998244353
#     c_dict[s] += ans
#     total += ans
#     total %= 998244353

# print(total)


# D - Card Pile Query
# import sys
# sys.setrecursionlimit(10**7)
# N, Q = map(int, input().split())
# mount_dict = {i+1: i+1 for i in range(N)}
# not_move = {i+1 for i in range(N)}

# for i in range(Q):
#     c, p = map(int, input().split())

#     mount_dict[c] = p
#     not_move.discard(c)

# cnt = [0]*(N)
# memo_dict = {}

# def dfs(i):
#     if i in memo_dict:
#         return memo_dict[i]
    
#     if i in not_move:
#         memo_dict[i] = mount_dict[i]
#         return i
    
#     memo_dict[i] = dfs(mount_dict[i])
#     return memo_dict[i]


# for i in range(1, N+1):
#     cnt[dfs(i)-1] += 1

# print(*cnt)


# D - (xx)
# T = int(input())

# for _ in range(T):
#     A = list(input())
#     B = list(input())
#     astack = []
#     for i, a in enumerate(A):
#         if a == ')' and len(astack) >= 3 and astack[-1] == 'x' and astack[-2] == 'x' and astack[-3] == '(':
#             astack.pop()
#             astack.pop()
#             astack.pop()
#             astack.append('x')
#             astack.append('x')
#         else:
#             astack.append(a)

#     bstack = []
#     for i, b in enumerate(B):
#         if b == ')' and len(bstack) >= 3 and bstack[-1] == 'x' and bstack[-2] == 'x' and bstack[-3] == '(':
#             bstack.pop()
#             bstack.pop()
#             bstack.pop()
#             bstack.append('x')
#             bstack.append('x')
#         else:
#             bstack.append(b)

#     if bstack == astack:
#         print('Yes')
#     else:
#         print('No')

# 
# D - Go Straight
# D - Go Straight
# import sys
# from collections import deque

# input = sys.stdin.readline

# H, W = map(int, input().split())
# grid = [input().strip() for _ in range(H)]

# sy = sx = gy = gx = -1

# for i in range(H):
#     for j in range(W):
#         if grid[i][j] == 'S':
#             sy, sx = i, j
#         elif grid[i][j] == 'G':
#             gy, gx = i, j

# # 0:U, 1:D, 2:L, 3:R
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
# move_char = "UDLR"

# # 状態番号を作る
# # 状態 = (y, x, d)
# # d は「直前に動いた方向」
# def encode(y, x, d):
#     return (y * W + x) * 4 + d

# # 状態番号から y, x, d に戻す
# def decode(state):
#     d = state % 4
#     pos = state // 4
#     y = pos // W
#     x = pos % W
#     return y, x, d

# total_states = H * W * 4

# # parent[state] の意味
# # -2: まだ訪問していない
# # -1: スタート状態
# # それ以外: 1つ前の状態番号
# parent = [-2] * total_states

# q = deque()

# # Sには「直前の方向」がないので、4方向すべてを初期状態にする
# for d in range(4):
#     st = encode(sy, sx, d)
#     parent[st] = -1
#     q.append(st)

# goal_state = -1

# while q:
#     state = q.popleft()
#     y, x, d = decode(state)

#     if y == gy and x == gx:
#         goal_state = state
#         break

#     cell = grid[y][x]

#     # 今いるマスから、次に進める方向を決める
#     if cell == 'o':
#         # 直進しかできない
#         next_dirs = [d]
#     elif cell == 'x':
#         # 直進以外ならOK
#         next_dirs = []
#         for nd in range(4):
#             if nd != d:
#                 next_dirs.append(nd)
#     else:
#         # '.', 'S', 'G' は自由に動ける
#         next_dirs = [0, 1, 2, 3]

#     for nd in next_dirs:
#         ny = y + dy[nd]
#         nx = x + dx[nd]

#         if not (0 <= ny < H and 0 <= nx < W):
#             continue
#         if grid[ny][nx] == '#':
#             continue

#         next_state = encode(ny, nx, nd)

#         if parent[next_state] != -2:
#             continue

#         parent[next_state] = state
#         q.append(next_state)

# if goal_state == -1:
#     print("No")
# else:
#     ans = []
#     cur = goal_state

#     while parent[cur] != -1:
#         y, x, d = decode(cur)
#         ans.append(move_char[d])
#         cur = parent[cur]

#     ans.reverse()

#     print("Yes")
#     print("".join(ans))

# D - No-Subsequence Substring
# from collections import Counter
# S = list(input())

# T = list(input())

# ans = len(S)*(len(S)+1)//2

# t_cnt = Counter(T)
# s_cnt = Counter()
# l = 0
# prev_l = -1
# for r in range(len(S)):
#     s_cnt[S[r]] += 1

#     if t_cnt > s_cnt:
#         continue

#     while t_cnt < s_cnt:
#         s_cnt[S[l]] -= 1
#         l += 1
    
#     ans -= (l-prev_l)*(len(S)-r)
#     prev_l = l
#     l += 1

# print(ans)

# D - Count Subgrid Sum = K
# H, W, K = map(int, input().split())

# S = [list(map(int, input())) for _ in range(H)]

# for i in range(H):
#     for j in range(1, W):
#         S[i][j] += S[i][j-1]

# ans = 0

# for h1 in range(H):
#     now = [0]*W
#     for h2 in range(h1, H):
#         cnt_dict = {0: 1}
#         for j in range(W):
#             now[j] += S[h2][j]
#             ans += cnt_dict.get(now[j]-K, 0)
#             cnt_dict[now[j]] = cnt_dict.get(now[j], 0) + 1

# print(ans)

# D - No-Subsequence Substring
# S = input()
# T = input()

# N = len(S)
# M = len(T)

# dp = [-1]*(M+1)

# ans = 0

# for i, ch in enumerate(S):
#     dp[0] = i
    
#     for j in range(M-1, -1, -1):
#         if dp[j] != -1 and ch == T[j]:
#             dp[j+1] = max(dp[j+1], dp[j])

#     if dp[M] == -1:
#         ans += i+1
#     else:
#         ans += (i+1)-(dp[M]+1)

# print(ans)

# D - X to Y
# T = int(input())

# for i in range(T):
#     X, Y, K = map(int, input().split())
#     cnt = 0
#     while X != Y:
#         if X > Y:
#             X //= K
#         else:
#             Y //= K

#         cnt += 1

#     print(cnt)

# D - No-Subsequence Substring
# S = list(input())
# T = list(input())

# dp = [-1]*len(T)
# ans = (len(S)*(len(S)+1))//2
# for i in range(len(S)):
#     for j in range(len(T)-1, -1, -1):
#         if T[j] != S[i]:
#             continue
        
#         if j==0:
#             dp[j] = i
#             continue
#         if dp[j-1] != -1:
#             dp[j] = dp[j-1]
            

#     if dp[-1] != -1:
#         ans -= dp[-1]+1

# print(ans)

# D - Concat Power of 2
# N = int(input())

# powers = []
# x = 1

# while x < 10**9:
#     powers.append(str(x))
#     x *= 2

# good = set()

# def dfs(s):
#     if s:
#         good.add(int(s))
#     for p in powers:
#         if len(s) + len(p) <= 9:
#             dfs(s+p)

# dfs("")

# A = sorted(good)
# print(A[N-1])

# D - Minimize Range
# N, K = map(int, input().split())

# A = list(map(int, input().split()))

# wari_A = [a%K for a in A]
# wari_A.sort()

# wari_A = wari_A+ [ a+K for a in wari_A]

# min_wide = float('inf')
# for i in range(N):
#     min_wide = min(min_wide, abs(wari_A[i]-wari_A[i+N-1]))

# print(min_wide)
                   
# D - Make Target 2
# L, R, D, U = map(int, input().split())

# ans = 0

# for k in range(1000001):
#     dx = max(0, min(R, k)-max(L, -k)+1)
#     dy = max(0, min(U, k)-max(D, -k)+1)
#     v = dx*dy
#     if k % 2 ==0:
#         ans += v
#     else:
#         ans -= v

# print(ans)

# L, R, D, U = map(int, input().split())

# ans = 0

# # ① |x| > |y| の場合
# # このとき max(|x|, |y|) = |x|
# # よって x が偶数なら数える
# for x in range(L, R + 1):
#     if x % 2 == 0:
#         low = max(D, -abs(x) + 1)
#         high = min(U, abs(x) - 1)

#         cnt = high - low + 1
#         ans += max(cnt, 0)

# # ② |x| <= |y| の場合
# # このとき max(|x|, |y|) = |y|
# # よって y が偶数なら数える
# for y in range(D, U + 1):
#     if y % 2 == 0:
#         low = max(L, -abs(y))
#         high = min(R, abs(y))

#         cnt = high - low + 1
#         ans += max(cnt, 0)

# print(ans)

# L, R, U, D = map(int, input().split())

# ans = 0

# while L <= R and U <= D:
#     ma = max(abs(L), abs(R), abs(U), abs(D))

#     if abs(L) == ma:
#         if L % 2 == 0:
#             ans += D - U + 1
#         L += 1

#     elif abs(R) == ma:
#         if R % 2 == 0:
#             ans += D - U + 1
#         R -= 1

#     elif abs(U) == ma:
#         if U % 2 == 0:
#             ans += R - L + 1
#         U += 1

#     else:
#         if D % 2 == 0:
#             ans += R - L + 1
#         D -= 1

# print(ans)
    
# D - Integer-duplicated Path
# import sys
# sys.setrecursionlimit(10**7)
# from collections import defaultdict
# N = int(input())

# A = list(map(int, input().split()))
# a_flag = [False]*N
# same_num = [False]*N
# graph = defaultdict(list)

# for i in range(N-1):
#     u, v = map(int, input().split())

#     graph[u-1].append(v-1)
#     graph[v-1].append(u-1)

# now = defaultdict(int)
# def dfs(i, flag):
#     a_flag[i] = True
#     if flag or A[i] in now:
#         same_num[i] = True
#         now[A[i]] += 1
#     else:
#         now[A[i]] += 1

#     for nxt in graph[i]:
#         if a_flag[nxt]:
#             continue
#         dfs(nxt, same_num[i])

#     now[A[i]] -= 1
#     if now[A[i]] == 0:
#         del now[A[i]]
#     a_flag[i] = False

# dfs(0, False)

# for f in same_num:
#     if f:
#         print('Yes')
#     else:
#         print('No')

# D - Take ABC 2
# S = list(input())

# ans = 0
# dp = {'A': 0, 'B': 0, 'C': 0}

# for c in S:
#     for key in dp:
#         if key != c:
#             continue

#         if (key == 'B' and dp['A'] == dp['B']) or (key == 'C' and dp['B'] == dp['C']):
#             continue

#         dp[key] += 1

#         if key == 'C':
#             dp['A'] -= 1
#             dp['B'] -= 1
#             dp['C'] -= 1
#             ans += 1
# print(ans)

# D - Celester
# T = int(input())

# for _ in range(T):
#     N = int(input())

#     S = [0 if s == 'S' else 1 for s in list(input())]
#     X = list(map(int, input().split()))
#     Y = [0]+list(map(int, input().split()))

#     dp = [0, -float('inf')]

#     for i in range(len(S)):
#         prev = dp.copy()
#         dp = [-float('inf'), -float('inf')]
#         for j in range(2):
#             for p_i in range(len(prev)):
#                 cost = 0 if S[i] == j else -X[i]
#                 if p_i == 1 and j == 0:
#                     cost += Y[i]
#                 cost += prev[p_i]
#                 dp[j] = max(dp[j], cost)
#     print(max(dp))

# D - Max Straight
# from collections import defaultdict

# N = int(input())
# A = list(map(int, input().split()))
# cnt_a = defaultdict(int)
# for i in range(len(A)):
#     cnt_a[A[i]] = max(cnt_a[A[i]-1]+1, cnt_a[A[i]]) if cnt_a[A[i]-1] > 0 else 1

# print(max(cnt_a.values()))

# D - Reconstruct Chocolate
# from collections import defaultdict
# H, W, N = map(int, input().split())

# h_dict = defaultdict(set)
# w_dict = defaultdict(set)
# i2hw = []
# for i in range(N):
#     h, w = map(int, input().split())
#     h_dict[h].add((i, w))
#     w_dict[w].add((i, h))
#     i2hw.append((h, w))
# ans = [(0, 0) for _ in range(N)]
# now_H = 0
# now_W = 0
# while w_dict or h_dict:
#     if h_dict[H]:
#         i, w = h_dict[H].pop()
#         if h_dict[H] == []: del h_dict[H]
#         h, w = i2hw[i]
#         w_dict[w].remove((i, h))
#         if not w_dict[w]: del w_dict[w]
#         nxt_W = w+now_W
#         ans[i] = now_H+1, now_W+1
#         now_W = nxt_W
#         W -= w
#     else: 
#         i, h = w_dict[W].pop()
#         if not w_dict[W]: del w_dict[W]
#         h, w = i2hw[i]
#         h_dict[h].remove((i, w))
#         if h_dict[h] == []: del h_dict[h]
#         nxt_H = h+now_H
#         ans[i] = now_H+1, now_W+1
#         now_H = nxt_H
#         H -= h

# for a in ans:
#     print(*a)


# from collections import defaultdict

# H, W, N = map(int, input().split())

# h_dict = defaultdict(set)
# w_dict = defaultdict(set)
# i2hw = []

# for i in range(N):
#     h, w = map(int, input().split())
#     h_dict[h].add((i, w))
#     w_dict[w].add((i, h))
#     i2hw.append((h, w))

# ans = [(0, 0) for _ in range(N)]

# now_H = 0
# now_W = 0

# while h_dict or w_dict:
#     if H in h_dict:
#         i, w = h_dict[H].pop()

#         if not h_dict[H]:
#             del h_dict[H]

#         h, w = i2hw[i]

#         w_dict[w].remove((i, h))
#         if not w_dict[w]:
#             del w_dict[w]

#         ans[i] = (now_H + 1, now_W + 1)

#         now_W += w
#         W -= w

#     elif W in w_dict:
#         i, h = w_dict[W].pop()

#         if not w_dict[W]:
#             del w_dict[W]

#         h, w = i2hw[i]

#         h_dict[h].remove((i, w))
#         if not h_dict[h]:
#             del h_dict[h]

#         ans[i] = (now_H + 1, now_W + 1)

#         now_H += h
#         H -= h

#     else:
#         # 再構成できない入力への安全策
#         break

# for a in ans:
#     print(*a)

# D - Many Repunit Sum
#累積和？　いもす方とかで桁分やってその後reverseとかで？
# N = int(input())
# A =list(map(int, input().split()))

# prefix = [0]*(2*10**6)

# for i in range(N):
#     prefix[A[i]] += -1
#     prefix[0] += 1

# for i in range(len(prefix)-1):
#     prefix[i+1] += prefix[i]

# carry = 0
# prev= 0
# for i in range(len(prefix)):
#     carry = (prefix[i]+prev)//10
#     prefix[i] = (prefix[i]+prev)%10
#     prev = carry

# j = len(prefix)-1
# while prefix[j] == 0:
#     j -= 1

# print(''.join(map(str, reversed(prefix[:j+1]))))

# D - Pawn Line
# import heapq

# T = int(input())

# for _ in range(T):
#     N = int(input())
#     R = list(map(int, input().split()))

#     INF = float('inf')
#     ans = [INF]*N

#     que = []

#     for i in range(N):
#         heapq.heappush(que, (R[i], i))

#     while que:
#         value, i = heapq.heappop(que)
#         if ans[i] != INF:
#             continue
#         ans[i] = value

#         if i > 0 and ans[i-1] == INF:
#             heapq.heappush(que, (value+1, i-1))
#         if i+1 < N and ans[i+1] == INF:
#             heapq.heappush(que, (value+1, i+1))

#     answer = sum(R[i]-ans[i] for i in range(N))
#     print(answer)

# D - Swap and Range Sum
# from atcoder.fenwicktree import FenwickTree
# N, Q = map(int, input().split())
# A = list(map(int, input().split()))
# fw = FenwickTree(N+1)

# for i in range(len(A)):
#     fw.add(i, A[i])

# for i in range(Q):
#     q,  *a = map(int, input().split())

#     if q == 1:
#         a = int(a[0])
#         a -= 1
#         l = fw.sum(a, a+1)
#         r = fw.sum(a+1, a+2)
#         fw.add(a, -l+r)
#         fw.add(a+1, -r+l)
#     else:
#         l, r = a
#         l -= 1
#         print(fw.sum(l, r))

# from atcoder.segtree import SegTree
# N, Q = map(int, input().split())
# A = list(map(int, input().split()))

# sg = SegTree(lambda a,b: a+b, 0, A)

# for i in range(Q):
#     q,  *a = map(int, input().split())

#     if q == 1:
#         a = int(a[0])
#         a -= 1
#         l = sg.get(a)
#         r = sg.get(a+1)
#         sg.set(a, r)
#         sg.set(a+1, l)
#     else:
#         l, r = a
#         l -= 1
#         print(sg.prod(l, r))


# D - Paid Walk
# from collections import defaultdict, deque
# 4^10回が10回目までいったときの最大解数なのでT回graphを進めばいいのでは
# N, M, L, S, T = map(int, input().split())

# graph = defaultdict(list)
# for i in range(M):
#     u, v, c = map(int, input().split())

#     graph[u-1].append((v-1, c))

# que = deque() #index, cost
# que.append((0, 0))
# for i in range(L):
#     nxtque = deque()

#     while que:
#         index, cost = que.popleft()

#         for v, c in graph[index]:
#             if cost+c > T:
#                 continue
#             nxtque.append((v, cost+c))
#     que = nxtque.copy()

# ans = []
# for ii, cc in que:
#     if not S <= cc <= T:
#         continue
#     ans.append(ii)

# ans = [a+1 for a in sorted(set(ans))]
# print(*ans)
    

# D - Concat Power of 2
# N = int(input())

# good = [set() for _ in range(10)]

# for i in range(30):
#     x = 2**i
#     if x >= 10**9:
#         break
#     digit = len(str(x))
#     good[digit].add(x)

# for digit in range(1, 10):
#     for power_digit in range(1, digit+1):
#         left_digit = digit-power_digit

#         if left_digit == 0:
#             continue

#         for left in good[left_digit]:
#             for power in good[power_digit]:
#                 x = left*(10**power_digit)+power

#                 if x < 10**9:
#                     good[digit].add(x)
# ans = []

# for digit in range(1, 10):
#     ans.extend(good[digit])

# ans.sort()

# print(ans[N-1])


# D - Teleport Maze
# from collections import deque, defaultdict

# H, W = map(int, input().split())
# grid = [list(input()) for _ in range(H)]

# # 各文字のワープマス一覧
# c_grid = defaultdict(list)

# for i in range(H):
#     for j in range(W):
#         if grid[i][j].isalpha():
#             c_grid[grid[i][j]].append((i, j))

# q = deque([(0, 0, 0)])
# visited = {(0, 0)}

# # すでにワープ処理を行った文字
# used_warp = set()

# diff = (
#     (1, 0),
#     (-1, 0),
#     (0, 1),
#     (0, -1),
# )

# while q:
#     y, x, cnt = q.popleft()

#     if y == H - 1 and x == W - 1:
#         print(cnt)
#         break

#     # 上下左右へ歩く
#     for dy, dx in diff:
#         ny = y + dy
#         nx = x + dx

#         if not (0 <= ny < H and 0 <= nx < W):
#             continue

#         if grid[ny][nx] == "#":
#             continue

#         if (ny, nx) in visited:
#             continue

#         visited.add((ny, nx))
#         q.append((ny, nx, cnt + 1))

#     # 現在地がワープマスならワープする
#     char = grid[y][x]

#     if char.isalpha() and char not in used_warp:
#         used_warp.add(char)

#         for ny, nx in c_grid[char]:
#             if (ny, nx) in visited:
#                 continue

#             visited.add((ny, nx))
#             q.append((ny, nx, cnt + 1))

# else:
#     print(-1)


# D - Minimize Range
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

# for i in range(N):
#     A[i] = A[i]%K

# A = sorted(set(A))
# L = len(A)
# A = A+[x+K for x in A]

# ans = float('inf')
# r = L-1
# for l in range(L):
#     ans = min(ans, A[r]-A[l])
#     r += 1

# print(ans)

# D - Placing Rooks
# N, M = map(int, input().split())
# timestamps = []
# for i in range(M):
#     r, c = map(int, input().split())
#     timestamps.append((r, c))

# timestamps.reverse()

# r_set = set()
# c_set = set()
# ans = 0
# for r, c in timestamps:
#     if r in r_set or c in c_set:
#         r_set.add(r)
#         c_set.add(c)
#     else:
#         r_set.add(r)
#         c_set.add(c)

#         ans += 1
# print(ans)

# E - Range Flip
# N, K = map(int, input().split())
# A = []
# B = []
# for i in range(N):
#     a, b = map(int, input().split())
#     A.append(a)
#     B.append(b)

# dp_a = [0]*(K+1)
# dp_b = [0]*(K+1)

# for i in range(N):
#     a = A[i]
#     b = B[i]
#     nxt_a = [0]*(K+1)
#     nxt_b = [0]*(K+1)

#     for k in range(K+1):
#         if k < 1:
#             nxt_a[k] = a+dp_a[k]
#             nxt_b[k] = b+dp_b[k]
#         else:
#             nxt_a[k] = (dp_a[k] if dp_a[k] > dp_b[k] else dp_b[k]) + a
#             nxt_b[k] = (dp_b[k] if dp_b[k] > dp_a[k-1] else dp_a[k-1]) + b
#     dp_a, dp_b = nxt_a, nxt_b
    
# print(max(max(dp_a), max(dp_b)))
            
# D - Flat Subsequence
# from atcoder.segtree import SegTree
# N, K = map(int, input().split())
# A = [int(input()) for _ in range(N)]
# seg = SegTree(max, 0, [0]*(300000+1))
# for i in range(N):
#     l = 0 if A[i]-K < 0 else A[i]-K
#     r = 300000 if A[i]+K > 300000 else A[i]+K
#     a = seg.prod(l, r+1)+1
#     seg.set(A[i], a)

# print(seg.all_prod())

# E - A > B substring
# from atcoder.fenwicktree import FenwickTree
# N = int(input())
# S = list(input())
# fenwick = FenwickTree(2*N+1)
# ans = 0
# now = 0
# fenwick.add(now+N, 1)


# for i in range(N):
#     if S[i] == 'A':
#         now += 1
#         fenwick.add(now+N, 1)
#     elif S[i] == 'B':
#         now -= 1
#         fenwick.add(now+N, 1)
#     else:
#         fenwick.add(now+N, 1)
#     ans += fenwick.sum(0, now+N)

# print(ans)

# E - Sequence Sum
# from collections import defaultdict
# N, X, M = map(int, input().split())

# wariprefix = [0]
# waridict = defaultdict(int)
# total = 0

# target_l = 1
# target_i = 1
# while N > 0:
#     if X not in waridict:
#         wariprefix.append(X)
#         waridict[X] = len(wariprefix)-1
#         total += X
#         X = (X*X)%M
#         N -= 1
#     else:
#         target_l = len(wariprefix)-waridict[X]
#         target_i = waridict[X]
#         break

# target_sum = 0
# for a in wariprefix[target_i:]:
#     target_sum += a

# warikiri = N//target_l
# amari = N%target_l
# N -= warikiri*target_l
# total += warikiri*target_sum


# for a in range(amari):
#     total += wariprefix[target_+a]

# print(total)

# N, X, M = map(int, input().split())

# LOG = N.bit_length()

# nxt = [[0]*M for _ in range(LOG)]

# total = [[0] * M for _ in range(LOG)]

# for x in range(M):
#     nxt[0][x] = x*x%M
#     total[0][x] = x

# for k in range(LOG-1):
#     for x in range(M):
#         mid = nxt[k][x]

#         nxt[k+1][x] = nxt[k][mid]
#         total[k+1][x] = total[k][x]+total[k][mid]

# answer = 0
# current = X

# for k in range(LOG):
#     if (N >> k) & 1:
#         answer += total[k][current]
#         current = nxt[k][current]
# print(answer)

# D - Make Target 2
# L, R, D, U = map(int, input().split())

# ans = 0

# # ① |x| > |y| の場合
# # このとき max(|x|, |y|) = |x|
# # よって x が偶数なら数える
# for x in range(L, R + 1):
#     if x % 2 == 0:
#         low = max(D, -abs(x) + 1)
#         high = min(U, abs(x) - 1)

#         cnt = high - low + 1
#         ans += max(cnt, 0)

# # ② |x| <= |y| の場合
# # このとき max(|x|, |y|) = |y|
# # よって y が偶数なら数える
# for y in range(D, U + 1):
#     if y % 2 == 0:
#         low = max(L, -abs(y))
#         high = min(R, abs(y))

#         cnt = high - low + 1
#         ans += max(cnt, 0)

# print(ans)

# D - Long Waiting
# import heapq

# N, K = map(int, input().split())
# heap = []
# time = 0
# for i in range(N):
#     a, b, c = map(int, input().split())

#     if K >= c:
#         time = max(time, a)
#         K -= c
#         print(time)
#         heapq.heappush(heap, (time+b, c))
#     else:
#         while K < c:
#             live_time, cus = heapq.heappop(heap)
#             time = max(time, live_time)
#             K += cus

#         time = max(time, a)
#         K -= c
#         print(time)
#         heapq.heappush(heap, (time+b, c))

# D - Minimum Width
# N, M = map(int, input().split())

# L = list(map(int, input().split()))

# l, r = 0, 10**18

# while r -l > 1:
#     mid = (l+r)//2
#     now = mid-L[0]
#     if now < 0:
#         l = mid
#         continue
#     cnt = 1
#     for a in L[1:]:
#         if a > mid:
#             cnt = M+1
#             break

#         if now - (a+1) < 0:
#             cnt += 1
#             now = mid-a
#         else:
#            now -= a+1

#     if cnt > M:
#         l = mid
#     else:
#         r = mid

# print(r)

# D - Relative Position
# 1は原点であることがわかっている。１とつながるものから順にBFSを進めていくと片方が確定していてそれに付随するもう一方も確定されていく。
#全ての辺へのアクセスを終わった時に、確定されていない点があればそれはundecidableになる。
# from collections import defaultdict, deque
# N, M = map(int, input().split())
# candidates = defaultdict(list)
# visited = set()
# for i in range(M):
#     a, b, x, y = map(int, input().split())

#     candidates[a].append((b, x, y))
#     candidates[b].append((a, -x, -y))

# q = deque()
# position = defaultdict(list)
# position[1] = [0, 0]
# for b, x, y in candidates[1]:
#     visited.add(1)
#     q.append((1, b, x, y))

# while q:
#     a, b, x, y = q.popleft()
#     # print(a, b, x, y)
#     if b in visited:
#         continue
#     position[b] = [x+position[a][0], y+position[a][1]]
#     visited.add(b)

#     for c, nx, ny in candidates[b]:
#         if c in visited:
#             continue

#         q.append((b, c, nx, ny))

# for i in range(1, N+1):
#     if len(position[i]) == 2:
#         print(*position[i])
#     else:
#         print("undecidable")

# D - Set Menu
# import bisect
# N, M, P = map(int, input().split())

# A = sorted(list(map(int, input().split())), reverse=True)
# B = sorted(list(map(int, input().split())))

# b_prefix = [0]*(M+1)
# for i in range(M):
#     b_prefix[i+1] += b_prefix[i]+B[i]


# ans = 0
# b_i = 0
# b_total = 0
# for a in A:
#     if a >= P:
#         ans += M*P
#         continue

#     diff = P-a
#     while b_i < M and P-a > B[b_i]:
#         b_i += 1

#     ans += b_prefix[b_i]+b_i*a+(M-b_i)*P
# # print(b_i, b_prefix)

# print(ans)
    

# D - Teleport Maze
# from collections import deque, defaultdict
# H, W = map(int, input().split())

# grid = [list(input()) for _ in range(H)]
# c_dict = defaultdict(list)

# for i in range(H):
#     for j in range(W):
#         if grid[i][j] != '.' and grid[i][j] != '#':
#             c_dict[grid[i][j]].append((i, j))
# # print(c_dict)

# q = deque()
# q.append((0, 0, 0))
# visited = set()
# visited.add((0, 0))
# diff = ((1, 0), (-1, 0), (0, 1), (0, -1))
# ansgrid = [[0]*W for _ in range(H)]
# already = set()
# already.add('.')

# while q:
#     i, j, cnt = q.popleft()
#     ansgrid[i][j] = cnt
#     if i == H-1 and j == W-1:
#         print(cnt)
#         exit()
#     cnt += 1
#     # print(i, j)
#     # print(c_dict[grid[i][j]])
#     if grid[i][j] not in already:
#         for ii, jj in c_dict[grid[i][j]]:
#             if (ii, jj) in visited:
#                 continue
#             q.append((ii, jj, cnt))
#             visited.add((ii, jj))
#     already.add(grid[i][j])

#     for dy, dx in diff:
#         y = dy+i
#         x = dx+j

#         if 0 <= y < H and 0 <= x < W and (y, x) not in visited and grid[y][x] != '#':
#             q.append((y, x, cnt))
#             visited.add((y, x))

# # print(ansgrid)
# print(-1)

# D - Polyomino
# 3つある4*4のグリッドを90度回転を4回ずつやる。
# １つの向きに対してその向きでのグリットの左位置を右下から進めていく。
# つまり、4*4のグリッドを右下から進めて'#'である部分が全てその指定グリッドに含まれているのであれば、
# そのブロックを指定した範囲を左端とした4*4の位置として持ち次のポリオミオに進めるこれを３つ分やるので
# 計算量は3*4*4*4かな？

# P = []

# for _ in range(3):
#     shape = []

#     for y in range(4):
#         row = input()

#         for x in range(4):
#             if row[x] == '#':
#                 shape.append((y, x))

#     P.append(shape)


# def rotate(shape):
#     return [(x, 3-y) for y, x in shape]


# def make_candidates(shape):
#     res = []

#     for _ in range(4):

#         for dy in range(-3, 4):
#             for dx in range(-3, 4):

#                 placed = set()
#                 ok = True

#                 for y, x in shape:
#                     ny = y + dy
#                     nx = x + dx

#                     if not (0 <= ny < 4) or not (0 <= nx < 4):
#                         ok = False
#                         break

#                     placed.add((ny, nx))

#                 if ok:
#                     res.append(placed)

#         shape = rotate(shape)

#     return res


# c1 = make_candidates(P[0])
# c2 = make_candidates(P[1])
# c3 = make_candidates(P[2])

# for a in c1:
#     for b in c2:

#         if a & b:
#             continue

#         for c in c3:

#             if a & c or b & c:
#                 continue

#             if len(a | b | c) == 16:
#                 print('Yes')
#                 exit()

# print('No')

# D - Flat Subsequence
# from atcoder.segtree import SegTree
# N, K = map(int, input().split())
# A = []
# for a in range(N):
#     A.append(int(input()))

# sg = SegTree(max, 0, [0]*300001)
# for a in A:
#     left = max(0, a-K)
#     right = min(300001, a+K+1)

#     now_max = sg.prod(left, right)

#     sg.set(a, now_max+1)

# print(sg.prod(0, 300001))

# D - Go Straight
#上、下、右、左からそのセルに入ったというgridを作成してそのセルに入った時の方向ごとにvisitedを管理する。
# これをDFSやBFSでできるところまで続けて最初にGした時に終了する。それぞれのセルにはそれがどこからきたものかを管理しておけば解けそう
# from collections import deque

# H, W = map(int, input().split())
# grid = [list(input()) for _ in range(H)]

# prev = [[[None] * 4 for _ in range(W)] for _ in range(H)]

# for i in range(H):
#     for j in range(W):
#         if grid[i][j] == 'S':
#             sy, sx = i, j
#         elif grid[i][j] == 'G':
#             gy, gx = i, j

# directions = [
#     (1, 0),   # D
#     (-1, 0),  # U
#     (0, -1),  # L
#     (0, 1)    # R
# ]

# q = deque()

# # Sには「直前方向」がないので、最初の移動を直接キューへ
# for nd, (dy, dx) in enumerate(directions):
#     y = sy + dy
#     x = sx + dx

#     if not (0 <= y < H and 0 <= x < W):
#         continue
#     if grid[y][x] == '#':
#         continue

#     prev[y][x][nd] = (sy, sx, -1)
#     q.append((y, x, nd))

# goal_state = None

# while q:
#     i, j, d = q.popleft()

#     if grid[i][j] == 'G':
#         goal_state = (i, j, d)
#         break

#     for nd, (dy, dx) in enumerate(directions):

#         # 現在のマスが o → 同じ方向のみ
#         if grid[i][j] == 'o' and nd != d:
#             continue

#         # 現在のマスが x → 同じ方向は禁止
#         if grid[i][j] == 'x' and nd == d:
#             continue

#         y = i + dy
#         x = j + dx

#         if not (0 <= y < H and 0 <= x < W):
#             continue

#         if grid[y][x] == '#':
#             continue

#         if prev[y][x][nd] is not None:
#             continue

#         prev[y][x][nd] = (i, j, d)
#         q.append((y, x, nd))


# if goal_state is None:
#     print("No")
#     exit()

# print("Yes")

# ans = []

# i, j, d = goal_state

# while True:
#     ans.append(d)

#     pi, pj, pd = prev[i][j][d]

#     if pd == -1:
#         break

#     i, j, d = pi, pj, pd

# ans.reverse()

# char = {
#     0: 'D',
#     1: 'U',
#     2: 'L',
#     3: 'R'
# }

# print(''.join(char[d] for d in ans))

# D - No-Subsequence Substring
# import math
# S = list(input())
# T = list(input())

# dp = [-1]*len(T)
# ans = (len(S)*(len(S)+1))//2
# for i in range(len(S)):
#     for j in range(len(T)-1, -1, -1):
#         # print(dp)
#         if S[i] == T[j] and (j == 0 or dp[j-1] > dp[j]):
#             dp[j] = i if j == 0 else dp[j-1]
#     if dp[-1] != -1:
#         ans -= dp[-1] + 1
#         # print(dp[-1] + 1)
            
# print(ans)

# D - Make Target 2
# L, R, D, U = map(int, input().split())

# ans = 0

# for i in range(L, R+1):
#     if i % 2 == 0:
#         low = max(D, -abs(i)+1)
#         high = min(U, abs(i)-1)

#         cnt = high-low+1
#         ans += max(cnt, 0)
#         # print(cnt)

# for i in range(D, U+1):
#     if i % 2 == 0:
#         low = max(L, -abs(i))
#         high = min(R, abs(i))

#         cnt = high-low+1
#         ans += max(cnt, 0)
#         # print(cnt)

# print(ans)

# D - Pawn Line

# T = int(input())

# for _ in range(T):
#     N = int(input())
#     R = list(map(int, input().split()))
#     final = R[:]
#     total = sum(final)
#     for i in range(1, N):
#         # print(final, i, final[i], R[i-1]+1)
#         final[i] = min(final[i], final[i-1]+1)
#     # print(final)
#     for i in range(N-1, 0, -1):
#         final[i-1] = min(final[i-1], final[i]+1)
#     # print(final)
#     print(total-sum(final))


# D - Count Subgrid Sum = K
# import bisect
# H, W, K = map(int, input().split())

# grid = [list(map(int, input())) for _ in range(H)]
# # print(grid)


# prefix = [[0]*W]

# for i in range(H):
#     tmp = [0]*W
#     for j in range(W):
#         tmp[j] = prefix[-1][j]+grid[i][j]
#     prefix.append(tmp)

# # print(prefix)

# ans = 0
# for low in range(H+1):
#     for high in range(low+1, H+1):
#         cnt_dict = {}
#         cnt_dict[0] = cnt_dict.get(0, 0)+1
#         now = [0]*(W+1)
#         for i in range(W):
#             now[i+1] = prefix[high][i]-prefix[low][i]+now[i]

#             if now[i+1]-K in cnt_dict:
#                 ans += cnt_dict[now[i+1]-K]

#             cnt_dict[now[i+1]] = cnt_dict.get(now[i+1], 0)+1

# print(ans)

# E - E-liter
# from atcoder.fenwicktree import FenwickTree
# N, Q = map(int, input().split())
# row = [-1]*N
# col = [0]*N
# fw_row = FenwickTree(Q+1)
# fw_col = FenwickTree(Q+1)
# total = 0
# for i in range(1, Q+1):
#     q, num = map(int, input().split())
#     # print(row)
#     # print(col)

#     if q == 1:
#         now = row[num-1]
#         row[num-1] = i
#         cnt = fw_col.sum(now+1, i+1)
#         total += cnt if now != -1 else N
#         print(total)
#         fw_row.add(i, 1)
#     else:
#         now = col[num-1]
#         row[num-1] = i
#         cnt = fw_row.sum(now+1, i+1)
#         total -= cnt
#         print(total)
#         fw_col.add(i, 1)

# C - Cookies and Greedy Takahashi
# N = int(input())
# A = list(map(int, input().split()))



# minus = []
# plus = []

# for a in A:
#     if a > 0:
#         plus.append(a)
#     else:
#         minus.append(a)

# now = 0

# plus.sort(reverse=True)
# minus.sort()
# ans = 0
# while plus or minus:
#     # print(plus, minus, ans, now)
#     if not minus:
#         a = plus.pop()
#         ans += abs(now-a)
#         now = a
#         continue
#     if not plus:
#         a = minus.pop()
#         ans += abs(now-a)
#         now = a
#         continue

#     if abs(now-plus[-1]) >= abs(now-minus[-1]):
#         a = minus.pop()
#         ans += abs(now-a)
#         now = a
#     else:
#         a = plus.pop()
#         ans += abs(now-a)
#         now = a

# print(ans)

# D - Merge Slimes
# 2**nのうち割り切れる最大でわる。あまりをどうにかする。
#それぞれが10**9なので30回ぐらいで済むので、数が小さいものから順にこれをやっていき、数を最小化する。
# x = 1
# from sortedcontainers import SortedDict
# N = int(input())
# sd = SortedDict()
# for i in range(N):
#     s, c = map(int, input().split())
#     sd[s] = c

# ans = 0
# while sd:
#     key, val = sd.popitem(0)
#     carry = val//2
#     ans += val%2

#     if carry > 0:
#         sd[key*2] = sd.get(key*2, 0)+carry


# print(ans)

# D - Square Permutation
# from collections import Counter
# N = int(input())
# S = list(int(a) for a in input())
# s_cnt = Counter(S)

# ans_target = [a**2 for a in range(5*10**6)]
# ans = 0
# for a in ans_target:
#     if len(str(a)) > len(S):
#         break
#     # print(a)
#     s_copy = s_cnt.copy()

#     a_cnt = Counter([int(b) for b in str(a)])

#     if a_cnt == s_copy:
#         ans += 1
#         continue
#     else:
#         while s_copy[0] > 0:
#             s_copy[0] -= 1
#             if a_cnt == s_copy:
#                 ans += 1
#                 break
# print(ans)


# D - Good Tuple Problem
# from collections import defaultdict, deque
# N, M = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# graph = defaultdict(list)

# for a, b in zip(A, B):
#     graph[a].append(b)
#     graph[b].append(a)

# color = [-1]*(N+1)

# q = deque()
# for i in range(1, N+1):
#     if color[i] != -1:
#         continue

#     color[i] = 0
#     q.append((i, 1)) #now_i, nxt_c

#     while q:
#         ii, nc = q.popleft()

#         for ni in graph[ii]:
#             if color[ni] == -1:
#                 color[ni] = nc
#                 nnc = 1 if nc == 0 else 0
#                 q.append((ni, nnc))
#             elif color[ni] != nc:
#                 print('No')
#                 exit()
# print("Yes")

# D - Take ABC
# from collections import deque
# S = list(input())

# prev = []
# nxt = deque(S)

# while True:
#     if len(nxt) > 2 and nxt[0] == 'A' and nxt[1] == 'B' and nxt[2] == 'C':
#         nxt.popleft()
#         nxt.popleft()
#         nxt.popleft()

#     if len(prev) > 2 and prev[-1] == 'C' and prev[-2] == 'B' and prev[-3] == 'A':
#         prev.pop()
#         prev.pop()
#         prev.pop()

#     if not nxt:
#         break
#     # print(nxt)
#     now = nxt.popleft()
#     prev.append(now)

# print("".join(prev))

# D - Election Quick Report
# import heapq
# N, M = map(int, input().split())
# heap = []
# cnt_n = [0]*(N+1)

# for a in list(map(int, input().split())):
#     cnt_n[a] += 1
#     heapq.heappush(heap, (-cnt_n[a], a))
#     print(heap[0][1])

# import heapq
# N, M = map(int, input().split())
# heap = []
# cnt_n = [0]*(N+1)
# ans = 0
# for a in list(map(int, input().split())):
#     cnt_n[a] += 1
#     if cnt_n[ans] < cnt_n[a]: ans = a
#     elif cnt_n[ans] == cnt_n[a]: ans = min(ans, a)
#     print(ans)

# D - Counting Ls
# N = int(input())
# S = [list(input()) for _ in range(N)]

# col_o = [0]*N
# row_o = [0]*N
# for i in range(N):
#     for j in range(N):
#         col_o[j] += 1 if S[i][j] == 'o' else 0
#         row_o[i] += 1 if S[i][j] == 'o' else 0

# ans = 0
# for i in range(N):
#     for j in range(N):
#         if S[i][j] == 'o':
#             # print(i, j, (col_o[j]-1)*(row_o[i]-1))
#             ans += (col_o[j]-1)*(row_o[i]-1)

# print(ans)

# D - Placing Rooks
# N, M = map(int, input().split())

# play = []
# for i in range(M):
#     r, c = map(int, input().split())

#     play.append((r, c))

# play.reverse()
# col_visited = set()
# row_visited = set()

# ans = 0
# for i in range(M):
#     row, col = play[i]

#     if row not in row_visited and col not in col_visited:
#         ans += 1

#     row_visited.add(row)
#     col_visited.add(col)

# print(ans)

# D - Pre-Palindrome
# S = input()
# L = len(S)

# ans = 0

# diff = 0
# for i in range(L):
#     l = i
#     r = l+1
#     diff = 0
#     while r < L and 0 <= l:
#         if S[l] != S[r]:
#             diff += 1
#         if diff > 1:
#             break
#         ans += 1
#         l -= 1
#         r += 1

# for i in range(L):
#     l = i
#     r = l
#     diff = 0
#     while r < L and 0 <= l:
#         if S[l] != S[r]:
#             diff += 1
#         if diff > 1:
#             break
#         ans += 1
#         l -= 1
#         r += 1


# print(ans)

# D - Good Tuple Problem
# import sys
# from collections import defaultdict
# sys.setrecursionlimit(10**6)
# N, M = map(int, input().split())

# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# graph = defaultdict(list)

# for a, b in zip(A, B):
#     graph[a-1].append(b-1)
#     graph[b-1].append(a-1)

# color = [-1]*N

# def drowcolor(i, iro):
#     color[i] = iro

#     for nxt in graph[i]:
#         if color[nxt] == iro:
#             return False
#         if color[nxt] != -1:
#             continue

#         if not drowcolor(nxt, 1-iro):
#             return False
#     return True

# ok = True
# for i in range(N):
#     if color[i] != -1:
#         continue

#     if not drowcolor(i, 0):
#         ok = False
#         break


# print('Yes' if ok else 'No')


# C - Striped Horse
#w ごとに分けて、そのlistにcostをsumしていく。
#w*2してそれをwindowでwごとにとっていく。それのminが答え。

# T = int(input())

# for _ in range(T):
#     N, W = map(int, input().split())

#     C = list(map(int, input().split()))
#     w_list = [0]*(W*2)
#     for i, c in enumerate(C):
#         w_list[i%(W*2)] += c

#     w_list = w_list+w_list

#     prefix = [0]

#     for w in w_list:
#         prefix.append(prefix[-1]+w)

#     ans = float('inf')
#     for i in range(W*2):
#         ans = min(ans, prefix[i+W]-prefix[i])

#     print(ans)


# C - AtCoder Riko
# from collections import deque
# N = int(input())
# A = list(map(int, input().split()))

# candidates = [max(A), max(A)+min(A)]
# A_c = deque(sorted(A))
# ans = []
# for c in candidates:
#     ok = True
#     A = A_c.copy()
#     while A:
#         # print(A)
#         if A[-1] == c:
#             A.pop()
#         elif len(A) > 1 and A[-1]+A[0] == c:
#             A.pop()
#             A.popleft()
#         else:
#             ok = False
#             # print(A)
#             # print(c)
#             break

#     if ok:
#         # print(c)
#         ans.append(c)

# print(*ans)


# D - Minimize Range
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

# a_list = []
# for a in A:
#     target = a%K
#     a_list.append(target)
#     a_list.append(target+K)

# a_list = sorted(a_list)
# # print(a_list)

# ans = float('inf')
# for i in range(N):
#     ans = min(ans, a_list[i+N-1]-a_list[i])

# print(ans)


# C - Bipartize
from collections import defaultdict
N, M = map(int, input().split())
graph = defaultdict(list)

for m in range(M):
    u, v = map(int, input().split())

    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

ans = float('inf')
for mask in range(1 << N):
    cnt = 0

    for i in range(N):
        for j in graph[i]:
            if ((mask >> i) & 1) == ((mask >> j) & 1):
                cnt += 1

    ans = min(ans, cnt//2)

print(ans)