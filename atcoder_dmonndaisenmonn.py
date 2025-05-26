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
def solve():
    # 入力読み込み
    H, W = map(int, input().split())
    grid = []
    for i in range(H):
        row = list(map(int, input().split()))
        grid.append(row)
    
    # 全マスの値を1次元リストに変換
    values = []
    for i in range(H):
        for j in range(W):
            values.append(grid[i][j])
    
    total_cells = H * W
    max_score = 0
    
    # 全ての可能なドミノ配置を試す
    # ビットマスクで各マスが使用されているかを管理
    def backtrack(pos, used_mask, current_xor):
        nonlocal max_score
        
        if pos == total_cells:
            max_score = max(max_score, current_xor)
            return
        
        # 現在のマスが既に使用されている場合、次へ
        if used_mask & (1 << pos):
            backtrack(pos + 1, used_mask, current_xor)
            return
        
        # 1次元位置を2次元座標に変換
        i, j = pos // W, pos % W
        
        # オプション1: このマスに何も置かない（マスの値をXORに含める）
        backtrack(pos + 1, used_mask, current_xor ^ values[pos])
        
        # オプション2: 右隣とドミノを置く（水平）
        if j + 1 < W:
            right_pos = pos + 1
            if not (used_mask & (1 << right_pos)):
                new_mask = used_mask | (1 << pos) | (1 << right_pos)
                backtrack(pos + 1, new_mask, current_xor)
        
        # オプション3: 下隣とドミノを置く（垂直）
        if i + 1 < H:
            down_pos = pos + W
            if not (used_mask & (1 << down_pos)):
                new_mask = used_mask | (1 << pos) | (1 << down_pos)
                backtrack(pos + 1, new_mask, current_xor)
    
    backtrack(0, 0, 0)
    print(max_score)

solve()