# S = input()
# world, stage = S.split('-')
# world = int(world)
# stage = int(stage)

# if stage == 8:
#     world += 1
#     print(f'{world}-1')
# elif stage < 8:
#     stage += 1
#     print(f'{world}-{stage}')

# B - Looped Rope
# H, W = map(int, input().split())

# S = [input() for _ in range(H)]

# for i in range(H):
#     for j in range(W):
#         cnt = 0
#         if S[i][j] == '#':
#             if i-1 >= 0 and S[i-1][j] == '#':
#                 cnt += 1
#             if i+1 < H and S[i+1][j] == '#':
#                 cnt += 1
#             if j-1 >= 0 and S[i][j-1] == '#':
#                 cnt += 1
#             if j+1 < W and S[i][j+1] == '#':
#                 cnt += 1
#             if cnt == 2 or cnt == 4:
#                 continue
#             else:
#                 print('No')
#                 exit()

# print('Yes')

# C - AtCoder AAC Contest
# T = int(input())

# for _ in range(T):
#     na, nb, nc = map(int, input().split())
#     min_A_C = min(na, nc)
#     S = na + nb + nc
#     print(min(min_A_C, S // 3))
   
# D - Least Unbalanced
# n, k = map(int, input().split())

# a = [k]
# for _ in range(n):
#     na = []
#     for x in a:
#         left = x // 2
#         right = x -left
#         na.append(left)
#         na.append(right)
#     a = na

# U = 0 if (k % (1 << n) == 0) else 1

# print(U)
# print(*a)