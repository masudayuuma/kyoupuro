#C - K-bonacci 
# N, K = map(int, input().split())
# list = [0 for _ in range(N+1)]
# pref = [0 for _ in range(N+1)]

# if N < K:
#     print(1)
#     exit()

# for i in range(K):
#     list[i] = 1
#     pref[i] = (pref[i-1] + list[i])

# for i in range(K, N+1):
#     list[i] = (pref[i-1] - pref[i-K-1]) % (10**9)
#     pref[i] = (pref[i-1] + list[i]) % (10**9)

# print(list[N])

#C - Sum of Product
# N = int(input())
# A = list(map(int, input().split()))

# total = 0
# presum = 0
# for i in A:
#     total += i*presum
#     presum += i

# print(total)

#C - ~
# N = int(input())
# P = list(map(int, input().split()))

# count_tani = 0
# count_yama = 0
# tani_yama_list = []

# for n in range(N-1):
#     if P[n] < P[n+1]:
#         tani_yama_list.append(1)
#     else:
#         tani_yama_list.append(-1)

# zikkou = []
# cur = tani_yama_list[0]
# length = 1
# for l in range(1, len(tani_yama_list)):
#     if tani_yama_list[l] == cur:
#         length += 1
#     else:
#         zikkou.append((cur, length))
#         cur = tani_yama_list[l]
#         length = 1
# zikkou.append((cur, length))

# ans = 0
# for i in range(len(zikkou)-2):
#     (sg1, a), (sg2, b), (sg3, c) =zikkou[i],zikkou[i+1],zikkou[i+2]
#     if sg1 == 1 and sg2 == -1 and sg3 == 1:     # + - +
#         add = a * c
#         if b == 1:                              # 最短区間 (長さ3) を除く
#             add -= 1
#         ans += add

# print(ans)


#C - Security 2
# S = input()

# A_count = len(S)
# n = len(S)
# B_count = int(S[-1])


# for i in range(1, n+1):
#     str_B = str(B_count)
#     if S[n - i] >= str_B[-1]:
#         B_count += int(S[n - i]) - int(str_B[-1])
#     else:
#         B_count += (int(S[n-i])+10) - int(str_B[-1])
    

# print(B_count+A_count)

#C - Equilateral Triangle
# from collections import defaultdict
# import sys
# input = sys.stdin.readline

# N, L = map(int, input().split())
# D = list(map(int, input().split()))

# if not L % 3 == 0:
#     print(0)
#     exit()
# cnt = defaultdict(int)
# cnt[0] = 1
# total_seihoukei = 0
# wari = L//3

# sum_d = 0
# for d in D:
#     sum_d += d
#     cnt[sum_d%L] += 1

# for i in range(wari):
#     if cnt[i] and cnt[i+wari] and cnt[i+wari*2]:
#         total_seihoukei += cnt[i] * cnt[i+wari] * cnt[i+wari*2]

# print(total_seihoukei)

#C - Not All Covered
# N, M = map(int, input().split())
# kabe = [0]*(N+1)
# for i in range(M):
#     l,m = map(int, input().split())
#     l = l-1
#     m = m-1
#     kabe[l] += 1
#     kabe[m+1] -= 1

# for i in range(1, N+1):
#     kabe[i] += kabe[i-1]

# print(min(kabe[:N]))


#C - Rotatable Array  / 
# N, Q = map(int, input().split())
# A = [i for i in range(1, N+1)]
# offset = 0

# for i in range(Q):
#     q = list(map(int, input().split()))

#     if q[0] == 1:
#         real_idx = (q[1]-1 - offset )%N
#         A[real_idx] = q[2]
#     if q[0] == 2:
#         real_idx = (q[1]-1 - offset)%N
#         print(A[real_idx])
#     if q[0] == 3:
#         offset = (offset - q[1]) % N

#C - Mixture
# import sys
# from collections import deque

# input = sys.stdin.buffer.readline
# q = int(input())

# que = deque()
# out = []

# for _ in range(q):
#     nums = list(map(int, input().split()))
#     t = nums[0]

#     if t == 1:
#         _, c, x = nums
#         que.append([c, x])

#     else:
#         _, k = nums
#         ans = 0

#         while que and k >= que[0][0]:
#             c, x = que.popleft()
#             ans += c*x
#             k -= c
#         if k:
#             que[0][0] -= k
#             ans += k*que[0][1]

#         out.append(ans)

# for a in out:
#     print(a)
