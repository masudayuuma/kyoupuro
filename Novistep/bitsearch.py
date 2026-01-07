# Enumeration of Subsets I
# n = int(input())

# for d in range(1 << n):
#     elements = []
#     for i in range(n):
#         if (d >> i) & 1:
#             elements.append(i)
#     if elements:
#         print(f"{d}: {' '.join(map(str, elements))}")
#     else:
#         print(f"{d}:")

# C - Monotonically Increasing
# N, M = map(int, input().split())
# ans_list = []

# for mask in range(1 << M):
#     tmp_ans = []
#     for i in range(M):
#         if mask >> i & 1:
#             tmp_ans.append(i+1)
    
#     if len(tmp_ans) == N:
#         ans_list.append(tmp_ans)

# ans_list.sort()
# for ans in ans_list:
#     print(' '.join(map(str, ans)))

# C - Separated Lunch
# N = int(input())

# K = list(map(int, input().split()))
# ans = float('inf')

# for mask in range(1 << N):
#     group_B = 0
#     group_A = 0
#     for i in range(N):
#         if mask >> i & 1:
#             group_A += K[i]
#         else:
#             group_B += K[i]
#     ans = min(ans, max(group_A, group_B))

# print(ans)

# C - Popcorn
# N, M = map(int, input().split())

# S = [list(input()) for _ in range(N)]
# ans = float('inf')
# for mask in range(1 << N):
#     ans_set = set()
#     tmp_cnt = 0
#     for j in range(N):
#         if mask >> j & 1:
#             tmp_cnt += 1
#             for i in range(M):
#                 if S[j][i] == 'o':
#                     ans_set.add(i)

#     if len(ans_set) == M:
#         ans = min(ans, tmp_cnt)

# print(ans)

# C - Coverage
# N, M = map(int, input().split())
# group_list = []
# ans = 0
# for m in range(M):
#     c = int(input())
#     a = set(list(map(int, input().split())))
#     group_list.append(a)

# for mask in range(1 << M):
#     tmp = set()
#     for i in range(M):
#         if mask >> i & 1:
#             tmp |= group_list[i]
    
#     if len(tmp) == N:
#         ans += 1

# print(ans)

# C - Submask
# N = int(input())
# hot_i = []
# for i in range(60):
#     if 1 << i & N:
#         hot_i.append(i)

# for mask in range(1 << len(hot_i)):
#     tmp = 0
#     for i in range(len(hot_i)):
#         if mask >> i & 1:
#             tmp += 2**hot_i[i]

#     print(tmp)

# C - Switches
N, M = map(int, input().split())
swiches_list = []
for m in range(M):
    k, *s = list(map(int, input().split()))
    swiches_list.append(s)

P = list(map(int, input().split()))
ans = 0
for mask in range(1 << N):
    cnt = 0
    for m in range(M):
        right_tmp = 0
        for target_swich in swiches_list[m]:
            if mask >> (target_swich-1) & 1:
                right_tmp += 1
        if right_tmp % 2 == P[m]:
            cnt += 1
    if cnt == M:
        ans += 1

print(ans)