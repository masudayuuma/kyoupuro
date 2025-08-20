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


# C - Cycle Graph?
# from collections import defaultdict
# from collections import deque

# N, M = map(int, input().split())
# if N != M:
#     print('No')
#     exit()

# graph = defaultdict(list)
# for i in range(M):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# for v in range(1, N+1):
#     if len(graph[v]) != 2:
#         print('No')
#         exit()

# q =deque([1])
# seen = [False]*(N+1)
# seen[1] = True
# cnt = 0
# while q:
#     node = q.popleft()
#     cnt += 1
#     for n in graph[node]:
#         if seen[n] == False:
#             seen[n] = True
#             q.append(n)
            
    
# if cnt != N:
#     print('No')
#     exit()

# print('Yes')

# C - 403 Forbidden
# N, M, Q = map(int, input().split())
# kannri_list = [set() for _ in range(N)]
# viwe_all = [False]*N
# for _ in range(Q):
#     t, *q = map(int, input().split())
#     x = q[0] -1
#     if t == 1:
#         y = q[1] -1
#         kannri_list[x].add(y)
#     elif t == 2:
#         viwe_all[x] = True
#     else:
#         y = q[1] -1
#         print('Yes' if viwe_all[x] or y in kannri_list[x] else 'No')


# C - Dislike Foods
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())

# # ing_to_menus[x] = 食材 x(0-index) を含む料理IDのリスト
# ing_to_menus = [[] for _ in range(n)]
# need = [0] * m  # 各料理に残っている「苦手食材」の数

# for i in range(m):
#     data = list(map(int, input().split()))
#     k, a = data[0], data[1:]
#     need[i] = k
#     for x in a:
#         ing_to_menus[x - 1].append(i)  # 0-index 化

# B = list(map(int, input().split()))    # N 個が1行で来る

# eat = 0
# out = []
# for b in B:
#     b -= 1
#     for menu_id in ing_to_menus[b]:
#         if need[menu_id] > 0:
#             need[menu_id] -= 1
#             if need[menu_id] == 0:
#                 eat += 1
#     out.append(eat)

# print("\n".join(map(str, out)))


# C - Uniqueness
# from collections import defaultdict
# N = int(input())
# A = list(map(int, input().split()))

# n = len(A)
# if n == 1:
#     print(1)
#     exit()
# dict = defaultdict(list)
# max_i = -1
# max_n = 0
# for i in range(n):
#     dict[A[i]].append(i+1)

# for val, i in dict.items():
#     if len(i) == 1:
#         if val > max_n:
#             max_n = val
#             max_i = i[0]

# print(max_i)
    

# from collections import defaultdict

# N = int(input())
# A = list(map(int, input().split()))

# d = defaultdict(list)
# for i, a in enumerate(A):
#     d[a].append(i)

# for key in sorted(d, reverse=True):
#     if len(d[key])==1:
#         print(d[key][0]+1)
#         exit()

# print(-1)


# C - Make it Forest
# from atcoder.dsu import DSU
# n, m = map(int, input().split())
# uf = DSU(n)
# ans = 0

# for _ in range(m):
#     a, b = map(int, input().split())
#     a -= 1; b-= 1
#     if uf.same(a, b):
#         ans += 1
#     else:
#         uf.merge(a, b)

# print(ans)

# C - Shortest Duplicate Subarray
# from collections import defaultdict
# N = input()
# A = list(map(int, input().split()))
# INF = 10**8
# dict = defaultdict(int)
# ans = INF
# for a in range(len(A)):
#     if A[a] in dict:
#         ans = min(a-dict[A[a]]+1, ans)
#     else:
#         dict[A[a]] = a

# print(ans if INF != ans else -1)

# C - Debug 
# S = input()
# S = list(S)
# i = 0

# for i in range(len(S)-1, 0, -1):
#     if S[i] == 'A' and S[i-1] == 'W':
#         S[i] = 'C'
#         S[i-1] = 'A'

# print(''.join(S))
        
# C - Buy Balls
N, M = map(int, input().split())
B = list(map(int, input().split()))
W = list(map(int, input().split()))

B.sort(reverse=True)
W.sort(reverse=True)
ans = 0
for i in range(N):
    if i < M and W[i] > 0:
        if B[i] < 0 and abs(B[i]) > W[i]:
            break     
        ans += B[i]+W[i]
    elif B[i] > 0:
        ans += B[i]
    else:
        break

    
print(ans)