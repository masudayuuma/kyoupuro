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
# N, M = map(int, input().split())
# B = list(map(int, input().split()))
# W = list(map(int, input().split()))

# B.sort(reverse=True)
# W.sort(reverse=True)
# ans = 0
# for i in range(N):
#     if i < M and W[i] > 0:
#         if B[i] < 0 and abs(B[i]) > W[i]:
#             break     
#         ans += B[i]+W[i]
#     elif B[i] > 0:
#         ans += B[i]
#     else:
#         break

# print(ans)

# C - Variety Split Easy 
# from collections import Counter
# N = int(input())
# A = list(map(int, input().split()))

# right_counter = Counter(A[1:])
# left_counter = Counter(A[:1])

# ans = len(right_counter)+len(left_counter)
# for i in range(1, N-1):
#     right_counter[A[i]] -= 1
#     if right_counter[A[i]] == 0:
#         del right_counter[A[i]]
#     left_counter[A[i]] += 1

#     ans = max(len(right_counter)+len(left_counter), ans)

# print(ans)

# C - Bib
# N = int(input())
# P = list(map(int, input().split()))
# Q = list(map(int, input().split()))

# ans = [0 for _ in range(N)] 

# for i in range(N):
#     ans[Q[i]-1] = Q[P[i]-1]

# # print(*ans)
# print(' '.join(map(str, ans)))

# C - Make it Simple
# from collections import defaultdict
# N, M = map(int, input().split())
# ans = 0
# has_sides = set()
# for i in range(M):
#     u, v = map(int, input().split())
#     if u == v:
#         ans += 1
#         continue
#     else:
#         if (u, v) in has_sides or (v, u) in has_sides:
#             ans += 1
#             continue
#         else:
#             has_sides.add((u, v))

# print(ans)

# C - Pigeonhole Query
# from collections import defaultdict
# N, Q = map(int, input().split())

# now_dict = {}
# num_dict = defaultdict(lambda: 1)
# ans = 0
# for i in range(Q):
#     query = list(map(int, input().split()))
#     if query[0] == 1:
#         now_hole = now_dict.get(query[1], query[1])
#         num_dict[now_hole] -= 1
#         num_dict[query[2]] += 1
#         if num_dict[now_hole] == 1:
#             ans  -= 1
#         if num_dict[query[2]] == 2:
#             ans += 1
#         now_dict[query[1]] = query[2]
#     else:
#         print(ans)


# C - たくさんの数式
# S = input()
# n = len(S)
# # hugou = 0*(n-1)
# total = 0
# for mask in range(1 << n-1):
#     formula = S[0]
#     for i in range(n-1):
#         if mask & (1 << i):
#             formula += '+' + S[i+1]
#         else:
#             formula += S[i+1]
#     # print(formula)  
#     total += eval(formula)

# print(total)

# C - Skill Up
# INF = 10**8
# N, M, X = map(int, input().split())
# A = []
# ans_level = [0]*M
# ans = INF
# # cost = 0
# C = []
# for i in range(N):
#     c, *a = map(int, input().split())
#     C.append(c)
#     A.append(a)

# for mask in range(1 << N):
#     cost = 0
#     ans_level = [0]*M
#     for i in range(N):
#         if mask & (1 << i):
#             cost += C[i]
#             for j in range(M):
#                 ans_level[j] += A[i][j]
                
#     flag = True
#     for level in ans_level:
#         if not level >= X:
#             flag = False
#     if flag == True:
#         ans = min(cost, ans)

# print(-1 if ans == INF else ans)

# C - Paint to make a rectangle
# H, W = map(int, input().split())
# S = [input() for _ in range(H)]
# b_h_min = float('inf')
# b_w_min = float('inf')
# b_h_max = float('-inf')
# b_w_max = float('-inf')

# for i in range(H):
#     for j in range(W):
#         if S[i][j] == '#':
#             b_h_min = min(b_h_min, i)
#             b_w_min = min(b_w_min, j)
#             b_h_max = max(b_h_max, i)
#             b_w_max = max(b_w_max, j)

# for i in range(b_h_min, b_h_max+1):
#     for j in range(b_w_min, b_w_max+1):
#         if S[i][j] == '.':
#             print('No')
#             exit()

        
# print('Yes')


# C - Black Intervals
# N, Q = map(int, input().split())
# A = list(map(int, input().split()))

# flag = [False]*N
# ans = 0
# for i, a in enumerate(A):
#     pos = a-1
#     if flag[pos]:
#         flag[pos] = False
#         left_black = pos > 0 and flag[pos-1]
#         right_black = pos < N-1 and flag[pos+1]
#         if left_black and right_black:
#             ans += 1
#         elif left_black or right_black:
#             ans += 0
#         else:
#             ans -= 1
#     else:
#         flag[pos] = True
#         left_black = pos > 0 and flag[pos-1]
#         right_black = pos < N-1 and flag[pos+1]

#         if left_black and right_black:
#             ans -= 1
#         elif left_black or right_black:
#             ans += 0
#         else:
#             ans +=1
        
#     print(ans)

# n, q = map(int, input().split())
# c = [0]*(n+2)
# ans = 0

# def add(i, x):
#     if c[i] == 1 and c[i+1] == 1:
#         ans += x

# for _ in range(q):
#     a = int(input())

#     add(a-1, -1)
#     add(a, -1)

#     c[a] ^= 1
#     add(a-1, 1)
#     add(a, 1)

#     print(ans)

# C - Snake Queue
# Q = int(input())

# save_i = []
# total = 0
# next_head = 0
# hiku_l = 0
# head = 0
# for i in range(Q):
#     query = list(map(int, input().split()))
#     if query[0] == 1:
#         save_i.append((total, query[1]))
#         next_head += query[1]
#         total += query[1]
#     if query[0] == 2:
#         hiku_l -= save_i[head][1]
#         # print(save_i[head])
#         head += 1
#     if query[0] == 3:
#         target = head+query[1]-1
#         # print(target, hiku_l)
#         print(save_i[target][0]+hiku_l)

# C - Giant Domino 解ききれなかった、解放はあってる
# import bisect 
# T = int(input())

# for i in range(T):
#     n = int(input())
#     S = list(map(int, input().split()))
#     s_s, s_e, new_s = S[0], S[-1], sorted(S[1:n-1])
#     total_min = 2
#     while new_s:
#         if s_s*2 <= s_e:
#             print(total_min)
#             break
#         ans_i = bisect.bisect_right(new_s, s_s*2)
#         if s_e/2 <= new_s[ans_i] <= s_s*2:
#             s_s = new_s[ans_i]
#             new_s = new_s[s_s:]
#             continue
#         elif new_s[ans_i] >= new_s[0]:
#             s_s = new_s[ans_i]
#             new_s = new_s[s_s:]
#         else:
#             print(-1)
#             break

# import bisect 
# import sys

# input = sys.stdin.readline

# T = int(input())

# for _ in range(T):
#     n = int(input())
#     S = list(map(int, input().split()))
#     s_s, s_e = S[0], S[-1]
#     new_s = sorted(S[1:n-1])  # 中間のコマを昇順
#     total_min = 2              # [1, N] の2個から開始（途中を挟めば都度+1）

#     # まずは S1 だけで SN に届くか
#     if s_e <= 2 * s_s:
#         print(total_min)
#         continue

#     # 進捗を“インデックス”で管理（削除はしない）
#     last_idx = -1

#     while True:
#         # 先に SN に届くかを毎回チェック（届いた瞬間が最短）
#         if s_e <= 2 * s_s:
#             print(total_min)
#             break

#         # <= 2*s_s の範囲で取れる最大値の位置（右端）
#         idx = bisect.bisect_right(new_s, 2 * s_s) - 1

#         # 1つも届かない
#         if idx < 0:
#             print(-1)
#             break

#         # 前回より右に進めない = 新しいコマを選べない → 詰み
#         if idx <= last_idx:
#             print(-1)
#             break

#         # 取れる中で最大のコマにジャンプ
#         s_s = new_s[idx]
#         last_idx = idx
#         total_min += 1

# C - Various Kagamimochi
# from bisect import bisect_left
# N = int(input())
# A = list(map(int, input().split()))
# total = 0
# for i in range(N-1):
#     target = A[i]*2
#     cnt = bisect_left(A, target)
#     ans = N-cnt
#     total += ans

# print(total)

# C - Operate 1 
# K = int(input())
# S = input()
# T = input()

# def can_transform(s, t):
#     if abs(len(s) - len(t)) > 1:
#         return False
    
#     if len(s) == len(t):
#         # 長さが同じ → 1文字置換で済むか
#         diff = sum(1 for i in range(len(s)) if s[i] != t[i])
#         return diff <= 1
    
#     elif len(s) == len(t) + 1:
#         # sの方が1文字長い → sから1文字削除でtになるか
#         j = 0
#         for i in range(len(s)):
#             if j < len(t) and s[i] == t[j]:
#                 j += 1
#             elif j == i:  # 最初の不一致 → この文字を削除
#                 j += 0  # jはそのまま
#             else:  # 2回目の不一致 → 不可能
#                 return False
#         return j == len(t)
    
#     else:  # len(s) == len(t) - 1
#         # tの方が1文字長い → sに1文字挿入でtになるか
#         i = 0
#         for j in range(len(t)):
#             if i < len(s) and s[i] == t[j]:
#                 i += 1
#             elif i == j:  # 最初の不一致 → この位置に文字を挿入
#                 i += 0  # iはそのまま
#             else:  # 2回目の不一致 → 不可能
#                 return False
#         return i == len(s)

# print('Yes' if can_transform(S, T) else 'No')

# C - Rotate and Sum Query
# N, Q = map(int, input().split())
# A_list = list(map(int, input().split()))
# calc_list = A_list+A_list
# index = 0

# ruisekiwa = [0]
# ruiseki_total = 0
# for i in range(N*2):
#     ruiseki_total += calc_list[i]
#     ruisekiwa.append(ruiseki_total)


# for i in range(Q):
#     q = list(map(int, input().split()))
#     if q[0] == 1:
#         index += q[1]
#     elif q[0] == 2:
#         left_i = q[1]-1+index
#         right_i = q[2]-1+index
#         if left_i >= N:
#             left_i %= N
#         if right_i >= N:
#             right_i %= N
#         if left_i > right_i:
#             right_i += N
#         ans = ruisekiwa[right_i+1]-ruisekiwa[left_i]
#         print(ans)

# import sys
# input = sys.stdin.readline

# n, q = map(int, input().split())
# a = list(map(int, input().split()))

# b = a+a
# for i in range(2*n-1, 0, -1):
#     b[i-1]+= b[i]
# rui_c = 0
# for _ in range(q):
#     query = list(map(int, input().split()))
#     if query[0] == 1:
#         c = query[1]
#         rui_c += c
#         rui_c %= n
#     else:
#         l, r = query[1]-1, query[2]
#         print(b[l+rui_c]-b[r+rui_c])


# C - New Skill Acquired
from collections import defaultdict
from collections import deque
N = int(input())

have_skill = deque()
dict = defaultdict(list)
skill_flag = [False]*N
ans = 0
for i in range(N):
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        skill_flag[i] = True
        have_skill.append(i+1)
        ans += 1
    else:
        dict[a].append(i+1)
        dict[b].append(i+1)

while have_skill:
    skill = have_skill.popleft()

    for s in dict[skill]:
        if skill_flag[s-1] == False:
            skill_flag[s-1] = True
            have_skill.append(s)
            ans += 1


print(ans)



