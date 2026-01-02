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
N, M = map(int, input().split())

S = [list(input()) for _ in range(N)]
ans = float('inf')
for mask in range(1 << N):
    ans_set = set()
    tmp_cnt = 0
    for j in range(N):
        if mask >> j & 1:
            tmp_cnt += 1
            for i in range(M):
                if S[j][i] == 'o':
                    ans_set.add(i)

    if len(ans_set) == M:
        ans = min(ans, tmp_cnt)

print(ans)
