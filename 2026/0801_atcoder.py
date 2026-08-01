# # A - Train Car
# N, K = map(int, input().split())
# # 𝑁−𝐾+1
# print(N-K+1)

# B - Isolated Seats
# N = int(input())
# S = list(input())
# ans  = 0
# for i, s in enumerate(S):
#     if i <= 0 or S[i-1] == 'x':
#         if i >= N-1 or S[i+1] == 'x':
#             if S[i] == 'x':
#                 ans += 1

# print(ans)

# C - Cantrip
# import bisect
# N = int(input())
# S = list(input())

# prefix_o = [0]*(N+1)
# prefix_x = [0]*(N+1)

# for i in range(N):
#     if S[i] == 'o':
#         prefix_o[i+1] = prefix_o[i]+1
#         prefix_x[i+1] = prefix_x[i]
#     else:
#         prefix_o[i+1] = prefix_o[i]
#         prefix_x[i+1] = prefix_x[i]+1
# ans = []
# for i in range(N):
#     now = prefix_x[i+1]+prefix_o[i+1]
#     t_i = bisect.bisect_left(prefix_x, now)

#     ans.append(t_i if t_i < N else N)

# for a in ans:
#     print(a)

# D - The Big Two
# N, M = map(int, input().split())
# A = []
# B = []
# for i in range(M):
#     a, b = map(int, input().split())
#     A.append(a)
#     B.append(b)

# ans = 0
# for c in (A[0], B[0]):
#     t = -1
#     for i in range(M):
#         if A[i] != c and B[i] != c:
#             t = i
#             break
#     if t == -1:
#         ans += N - 1
#         continue
#     for y in (A[t], B[t]):
#         if all(A[i] in (c, y) or B[i] in (c, y) for i in range(M)):
#             ans += 1

# a, b = A[0], B[0]
# if all(A[i] in (a, b) or B[i] in (a, b) for i in range(M)):
#     ans -= 1
# print(ans)

# 