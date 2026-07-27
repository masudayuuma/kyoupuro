# A - Maximal Value / 
# N = int(input())
# A = list(map(int, input().split()))
# ans = 0
# for i in range(N-2):
#     if A[i] < A[i+1] and A[i+1] > A[i+2]:
#         # print(A[i], A[i+1], A[i+2])
#         ans += 1

# print(ans)

# B - Corridor Watch
# M, D = map(int, input().split())
# S = list(input())
# ans = 0
# ans_list = ['.']*M

# for i in range(M):
#     if S[i] == 'G':
#         for j in range(D+1):
#             if i+j >= M:
#                 break
#             ans_list[i+j] = 'G'
# for i in range(M-1, -1, -1):
#     if S[i] == 'G':
#         for j in range(D+1):
#             if i-j < 0:
#                 break
#             ans_list[i-j] = 'G'

# for i in range(M):
#     if ans_list[i] == '.':
#         ans += 1

# print(ans)

# m, d = map(int, input().split())
# s = input()
# ans = 0

# for x in range(m):
#     ok = False
#     for i in range(m):
#         ok |= s[i] == "G" and abs(x-i) <= d
#     ans += not ok
# print(ok)

# C - Between P and Q
# import itertools

# N = int(input())
# P = tuple(list(map(int, input().split())))
# Q = tuple(list(map(int, input().split())))
# numbers = list(range(1, N + 1))
# all_permutations = sorted(list(itertools.permutations(numbers)))

# # print(all_permutations)

# P_i = all_permutations.index(P)
# Q_i = all_permutations.index(Q)

# if P_i >= Q_i:
#     print(0)
# else:
#     print(Q_i-P_i-1)

# import itertools

# n = int(input())
# p = list(map(int, input().split()))
# q = list(map(int, input().split()))
# ans = 0
# for a in itertools.permutations([i+1 for i in range(n)]):
#     ans += p < list(a) < q
# print(ans)

# D - Pre-Palindrome
# S = input()
# N = len(S)
# ans = 0

# for center in range(N):
#     left = center
#     right = center
#     miss = 0

#     while left >= 0 and right < N:
#         if S[left] != S[right]:
#             miss += 1
#         if miss > 1:
#             break
#         ans += 1

#         left -= 1
#         right += 1

# for center in range(N - 1):
#     left = center
#     right = center + 1
#     miss = 0

#     while left >= 0 and right < N:
#         if S[left] != S[right]:
#             miss += 1
#         if miss > 1:
#             break

#         ans += 1
#         left -= 1
#         right += 1

# print(ans)

# s = input()
# n = len(s)
# ans = 0

# for k in range(2):
#     for st in range(n):
#         l, r = st-k, st
#         cnt = 0
#         while 0 <= l and r < n:
#             if s[l] != s[r]:
#                 cnt += 1
#                 if cnt == 2:
#                     break
#             l -= 1
#             r += 1
#             ans += 1
# print(ans)

# E - Sum of Average
# MOD = 998244353

# N = int(input())
# A = list(map(int, input().split()))

# b = [0]*N
# for i in range(N):
#     b[i] = pow(i+1, MOD-2, MOD)

# sa = [0]*(N+1)
# sb = [0]*(N+1)

# for i in range(N):
#     sa[i+1] = (sa[i]+A[i]) % MOD
#     sb[i+1] = (sb[i] + b[i]) % MOD

# ans = 0
# l = 0
# r = N

# while l < r:
#     sum_a = (sa[r]-sa[l]) % MOD
#     sum_inv = (sb[r] -sb[l]) % MOD

#     ans += sum_a * sum_inv
#     ans %= MOD

#     l += 1
#     r -= 1

# print(ans)

