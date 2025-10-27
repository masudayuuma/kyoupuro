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
