# import itertools

# # 入力の読み込み
# N = int(input())
# P = tuple(map(int, input().split()))
# Q = tuple(map(int, input().split()))

# # 全ての順列を生成
# perm_list = list(itertools.permutations(range(1, N+1)))

# # 辞書順にソート
# perm_list.sort()

# # P と Q の位置を特定（0始まり）
# a = perm_list.index(P)
# b = perm_list.index(Q)

# # 差の絶対値を計算して出力
# print(abs(a - b))


# S = [list(input()) for _ in range(8)]

# square =list([True]*8 for _ in range(8))
# for i in range(8):
#     for j in range(8):
#         if S[i][j] == "#":
#             for k in range(8):
#                 square[i][k] = False
#                 square[k][j] = False

# count = 0
# for i in range(8):
#     for j in range(8):
#         if square[i][j] == True:
#             count += 1
# print(count)

# N, M = map(int, input().split())
# a = [None]*M
# b = [None]*M

# for i in range(M):
#     a[i], b[i] = map(int, input().split())

# S = list([True]*N for _ in range(N))

# for i in range(M):
#     if 0 <= a[i]+2 < N and 0 <= b[i]+1 < N:
#         S[a[i]+2][b[i]+1] = False
#     if 0 <= a[i]+1 < N and 0 <= b[i]+2 < N:
#         S[a[i]+1][b[i]+2] = False
#     if 0 <= a[i]-1 < N and 0 <= b[i]+2 < N:
#         S[a[i]-1][b[i]+2] = False
#     if 0 <= a[i]-2 < N and 0 <= b[i]+1 < N:
#         S[a[i]-2][b[i]+1] = False
#     if 0 <= a[i]-2 < N and 0 <= b[i]-1 < N:
#         S[a[i]-2][b[i]-1] = False
#     if 0 <= a[i]-1 < N and 0 <= b[i]-2 < N:
#         S[a[i]-1][b[i]-2] = False
#     if 0 <= a[i]+1 < N and 0 <= b[i]-2 < N:
#         S[a[i]+1][b[i]-2] = False
#     if 0 <= a[i]+2 < N and 0 <= b[i]-1 < N:
#         S[a[i]+2][b[i]-1] = False
    
# count = 0
# for i in range(N):
#     for j in range(N):
#         if S[i][j] == True:
#             count += 1

# print(count)

# 問D
# N, M = map(int, input().split())
# L = [None]*N
# R = [None]*N
# for i in range(N):
#     L[i], R[i] = map(int, input().split())

# for i in range(N):
#     if 

# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# occupied = set()
# moves = [
#     (2, 1), (1, 2), (-1, 2), (-2, 1),
#     (-2, -1), (-1, -2), (1, -2), (2, -1)
# ]

# for _ in range(M):
#     a, b = map(int, input().split())
#     occupied.add((a, b))
#     for dx, dy in moves:
#         ni, nj = a + dx, b + dy
#         if 1 <= ni <= N and 1 <= nj <= N:
#             occupied.add((ni, nj))

# total_cells = N * N
# cannot_place = len(occupied)
# result = total_cells - cannot_place

# print(result)

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)

buy_x = 0
for i in range(N):
    if i == N-1:
        buy_x += A[i]
        break
    elif A[i] <= B[i]:
        continue
    elif A[i] > B[i] and buy_x == 0:
        buy_x += A[i]
        B.append(buy_x)
        B.sort(reverse=True)
    elif A[i] > B[i] and buy_x != 0:
        buy_x = -1
        break

print(buy_x)
