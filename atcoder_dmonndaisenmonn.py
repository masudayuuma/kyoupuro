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
N, M =map(int, input().split())

C =list(map(int, input().split()))

a = []
for _ in range(M):
    tmp = list(map(int, input().split()))
    k, arr = tmp[0], tmp[1:]
    arr = [z-1 for z in arr]
    a.append(arr)

p3 = [1]*(N+1)
for i in range(N):
    p3[i+1] = p3[i]*3

INF = float('inf')
ans = INF

for s in range(p3[N]):
    t_i = [0]*N
    cost = 0

    for i in range(N):
        t = (s // p3[i]) %3
        t_i[i] = t
        cost += C[i]*t
    if cost >= ans:
        continue

    ok = True
    for j in range(M):
        cnt = 0
        for z in a[j]:
            cnt += t_i[z]
        if cnt < 2:
            ok = False
            break

    if ok:
        ans = cost
print(ans)