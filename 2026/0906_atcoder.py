# X = int(input())

# if X == 1:
#     print(2)
# elif X == 2:
#     print(3)
# else:
#     print(1)

# B - Exit Order / 
# import math
# N = int(input())

# P = list(map(int, input().split()))

# i = 0
# for c in range(math.ceil(N/10)):
#     ok = True
#     while c*10 > i and N > i:
#         if P[i] <= c*10:
#             i += 1
#             continue
#         else:
#             ok = False
#             break
        

#     if not ok:
#         print('No')
#         exit()

# print('Yes')


# C - Remove and Append
# from collections import defaultdict
# N, Q = map(int, input().split())

# P = list(map(int, input().split()))

# cnt_dict = defaultdict(int)
# for i, p in enumerate(P):
#     cnt_dict[p] = i

# now_end = N-1
# for i in range(Q):
#     a = int(input())
#     if now_end == cnt_dict[a]:
#         continue
#     else:
#         now_end += 1
#         cnt_dict[a] = now_end

# ans = sorted(range(1, N+1), key=lambda x: cnt_dict[x])

# print(*ans)

# D - Outweigh
# N = int(input())

# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# ans_w = [0]*N
# ok = False
# for i in range(N):
#     a = A[i]
#     b = B[i]
#     diff = a-b
#     if a-b > 0:
#         ok = True
#         ans_w[i] = 10**18
#     else:
#         ans_w[i] = 1

# if ok == False:
#     print('No')
# else:
#     print('Yes')
#     print(*ans_w)


# E - One Time Coupon
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     sum_a = 0
#     min_a = 10**18
#     diff = []

#     for _ in range(N):
#         a, b = map(int, input().split())

#         sum_a += a
#         min_a = min(min_a, a)
#         diff.append(a - b)

#     diff.sort(reverse=True)
#     ans = sum_a
#     saving = 0

#     for k in range(1, N + 1):
#         saving += diff[k - 1]

#         lack = max(0, k - (N - k))

#         cost = sum_a - saving + lack * min_a

#         ans = min(ans, cost)

#     print(ans)