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

# D - The Big Two
# N, M = map(int, input().split())
# a_b = []
# for i in range(M):
#     a, b = map(int, input().split())
#     a_b.append((a, b))

# ans = 0
# for candidate in (a_b[0][0], a_b[0][1]):
#     t = -1
#     for i, now in enumerate(a_b[1:]):
#         a, b = now
#         if a != candidate and b != candidate:
#             t = i+1
#             break
#     if t == -1:
#         ans += N-1 
#         continue

#     tmp = 0
#     ca, cb = a_b[t]
#     for c in (ca, cb):
#         ok = True
#         for i in range(M):
#             a, b = a_b[i]
#             if (c == a or candidate == a) or (c == b or candidate == b):
#                 continue
#             else:
#                 ok = False
#                 break
#         if ok:
#             ans += 1
# c, d = a_b[0]                               # 二重計上を1つ引く
# ok = True
# for a, b in a_b:
#     if a != c and a != d and b != c and b != d:
#         ok = False
#         break
# if ok:
#     ans -= 1

# print(ans)
