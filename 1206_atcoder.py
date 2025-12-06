# A - Triangular Number
# N = int(input())
# ans = 0
# for i in range(1, N+1):
#     ans += i

# print(ans)

# B - No-Divisible Range
# N = int(input())
# A = list(map(int, input().split()))
# ans = 0
# for i in range(N-1):
#     tmp_sum = A[i]
#     tmp_list = [A[i]]
#     for j in range(i+1, N):
#         tmp_sum += A[j]
#         tmp_list.append(A[j])
#         flag = True
#         for k in tmp_list:
#             if tmp_sum % k == 0:
#                 flag = False
#                 break
#         if flag == True:
#             ans += 1
# print(ans)

# C - Domino
# N = int(input())
# A = list(map(int, input().split()))
# ans = 1
# can_do = A[0]-1
# for i in range(1, N):
#     if can_do > 0:
#         ans += 1
#         can_do = max(can_do-1, A[i]-1)
#         continue
#     else:
#         break

# print(ans)

# D - Reachability Query 2
# N, M = map(int, input().split())
# move_ret = [set() for _ in range(N + 1)]
# for _ in range(M):
#     x, y = map(int, input().split())
#     move_ret[y].append(x)

# Q = int(input())
# can_path = [False] * (N + 1)

# ans = []

# for _ in range(Q):
#     n, v = map(int, input().split())
#     if n == 1:
#         if not can_path[v]:
#             stack = [v]
#             while stack:
#                 u = stack.pop()
#                 if can_path[u]:
#                     continue
#                 can_path[u] = True
#                 for prev in move_ret[u]:
#                     if not can_path[prev]:
#                         stack.append(prev)
#     else:
#         ans.append("Yes" if can_path[v] else "No")

# for i in ans:
#     print(i)

# E - Cover query
from sortedcontainers import SortedList

N, Q = map(int, input().split())

ans_list = SortedList()
total_b = 0

for _ in range(Q):
    L, R = map(int, input().split())
    
    t_l, t_r = L, R
    
    idx = ans_list.bisect_left((L, 0))
    
    if idx > 0 and ans_list[idx-1][1] >= L-1:
        idx -= 1
    
    while idx < len(ans_list) and ans_list[idx][0] < t_r + 2:
        l, r = ans_list[idx]
        total_b -= (r-l+1)
        t_l = min(t_l, l)
        t_r = max(t_r, r)
        ans_list.pop(idx)
    
    ans_list.add((t_l, t_r))
    total_b += (t_r-t_l+1)
    
    print(N-total_b)