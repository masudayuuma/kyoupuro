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
# from collections import defaultdict
# from collections import deque
# N = int(input())

# have_skill = deque()
# dict = defaultdict(list)
# skill_flag = [False]*N
# ans = 0
# for i in range(N):
#     a, b = map(int, input().split())
#     if a == 0 and b == 0:
#         skill_flag[i] = True
#         have_skill.append(i+1)
#         ans += 1
#     else:
#         dict[a].append(i+1)
#         dict[b].append(i+1)

# while have_skill:
#     skill = have_skill.popleft()

#     for s in dict[skill]:
#         if skill_flag[s-1] == False:
#             skill_flag[s-1] = True
#             have_skill.append(s)
#             ans += 1

# print(ans)


# C - Lock All Doors
# N, S = map(int, input().split())
# A = list(map(int, input().split()))

# idx0 = [i for i, a in enumerate(A) if a == 0]
# if len(idx0) == 0:
#     print(0)
#     exit()

# L = min(S, idx0[0])
# R = max(S, idx0[-1]+1)

# print(sum(A[L:R])+(R-L))
        

# C - Mixture　ビットDP問題
# T = int(input())

# for t in range(T):
#     n = int(input())
#     s = (input())
    
#     def is_safe(state):
#         if state == 0:
#             return True
#         return s[state-1] == '0'

#     dp = [False]*(1 << n)
#     dp[0] = True 

#     for state in range(1 << n):
#         if not dp[state]:
#             continue

#         for i in range(n):
#             if state & (1 << i):
#                 continue
#             next_state = state | (1 << i)

#             if is_safe(next_state):
#                 dp[next_state] = True

#     target = (1 << n)-1
#     print('Yes' if dp[target] else 'No')

# C - Palindromic in Both Bases
# def is_pal_base(x, base):
#     if x == 0:
#         return True
#     digits = []
#     while x > 0:
#         digits.append(x % base)
#         x //= base
#     i, j = 0, len(digits)-1
#     while i < j:
#         if digits[i] != digits[j]:
#             return False
#         i += 1
#         j -= 1
#     return True

# a = int(input())
# n = int(input())

# ans = 0

# def check(s):
#     global ans
#     y = int(s)
#     if y <= n and is_pal_base(y, a):
#         ans += y

# for x in range(1, 10**6):
#     sx = str(x)
#     even_pal = sx + sx[::-1]
#     check(even_pal)
#     odd_pal = sx + sx[:-1][::-1]
#     check(odd_pal)

# print(ans)

# C - Upgrade Required
# n, q = map(int, input().split())
# pc = [0] + [1] * n  # pc[0]=0, pc[1]~pc[n]=1
# o = 1

# for _ in range(q):
#     x, y = map(int, input().split())
#     res = 0
#     while o <= x:
#         res += pc[o]
#         pc[y] += pc[o]
#         o += 1
#     print(res)

# from collections import defaultdict
# n, q = map(int, input().split())

# dict = defaultdict(int)
# for i in range(n):
#     dict[i+1] = 1

# min_n = 1
# for i in range(q):
#     x, y = map(int, input().split())
#     cnt = 0
#     if min_n <= x:
#         for j in range(min_n, x+1):
#             cnt += dict[j]
#         dict[y] += cnt
#         min_n = x+1
#         print(cnt)
#         continue
    
#     print(cnt)


# C - Perfect Standings
# a, b, c, d, e = map(int, input().split())
# chars = ['A', 'B', 'C', 'D', 'E']
# point_dict = {'A':a, 'B':b, 'C':c, 'D':d, 'E':e}

# result_dict = {}
# for mask in range(1 << 5):
#     combo_chars = []
#     total_value = 0

#     for i in range(5):
#         if mask & (1 << i):
#             combo_chars.append(chars[i])
#             total_value += point_dict[chars[i]]
#     key = ''.join(combo_chars)
#     result_dict[key] = total_value

# sorted_values = sorted(result_dict.items(), key=lambda x: (-x[1], x[0]))

# result_array = [combo for combo, score in sorted_values]

# for combo in result_array:
#     print(combo)

# point = list(map(int, input().split()))

# point = [-p for p in point]

# standings = []
# for bit in range(1 << 5):
#     soleved_point = 0
#     name = ''
#     for digit in range(5):
#         if bit & 1 << digit:
#             soleved_point += point[digit]
#             name += "ABCDE"[digit]
#     standings.append((soleved_point, name))

# for _, name in sorted(standings):
#     print(name)


# C - Illuminate Buildings
# N = int(input())
# H = list(map(int, input().split()))

# ans = 1

# for j in range(N):
#     for i in range(j+1, N):
#         if i < N and H[j] == H[i]:
#             cnt = 1
#             a = i-j
#             while i < N and H[i] == H[j]:
#                 cnt += 1
#                 i += a
                
#             ans = max(ans, cnt)

# print(ans)

#dpバージョン
# N = int(input())
# H = list(map(int, input().split()))

# dp = [[1] * N for _ in range(N)]
# ans = 1

# for i in range(N):
#     for j in range(1, N):
#         if i + j < N and H[i+j] == H[i]:
#             dp[i+j][j] = dp[i][j] + 1
#             ans = max(ans, dp[i+j][j])

# print(ans)


# # C - 11/22 Substring　Nで計算可能
# N = int(input())
# S = input()

# max_len = 1

# for i in range(len(S)):
#     if S[i] == '/':
#         target_diff = 1
#         while 0 <= i-target_diff and target_diff+i < N:
#             if S[i-target_diff] == '1' and S[target_diff+i] == '2':
                
#                 max_len = max(max_len, target_diff*2+1)
#                 target_diff += 1
#             else:
#                 break

# print(max_len)

# C - Kaiten Sushi 
# from collections import defaultdict
# from bisect import bisect_right
# N, M = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# min_a = float('inf')
# a_dict = defaultdict(int)
# new_a_list = []
# for i in range(len(A)):
#     if min_a > A[i]:
#         a_dict[A[i]] = i+1
#         new_a_list.append(A[i])
#         min_a = A[i]

# sort_distinct_a = sorted(new_a_list)
# length = len(sort_distinct_a)

# for i in range(len(B)):
#     ans_i = bisect_right(sort_distinct_a, B[i])-1
#     if ans_i < 0:
#         print(-1)
#         continue
#     ans = a_dict[sort_distinct_a[ans_i]]
#     print(ans)

# C - Move Segment
# N, K = map(int, input().split())

# S = (input())

# ranlenght = []
# base_i = [S[0], 0]
# for i in range(1, len(S)):
#     if base_i[0] == S[i]:
#         continue
#     else:
#         ranlenght.append((base_i[0], i-base_i[1]))
#         base_i = [S[i], i]
# ranlenght.append((base_i[0], len(S)-base_i[1]))

# cnt_1 = 0
# for i in range(len(ranlenght)):
#     if ranlenght[i][0] == '1':
#         cnt_1 += 1
    
#     if cnt_1 == K:
#         if i > 0 and ranlenght[i-1][0] == '0':
#             ranlenght[i], ranlenght[i-1] = ranlenght[i-1], ranlenght[i]
#         break

# ans_paths = []
# for n, lenght in ranlenght:
#     ans_paths.append(n*lenght)

# print(''.join(ans_paths))

# C - Repeating 
# from collections import defaultdict
# N = int(input())
# A = list(map(int, input().split()))

# dict_n_to_i = defaultdict(list)
# ans_arr = []
# for i in range(len(A)):
#     if A[i] in dict_n_to_i:
#         ans_arr.append(dict_n_to_i[A[i]][-1])
#     else:
#         ans_arr.append(-1)
    
#     dict_n_to_i[A[i]].append(i+1)

# print(*ans_arr)

# C - Sowing Stones
# ...existing code...

# C - Sowing Stones
# N, M = map(int, input().split())
# X = list(map(int, input().split()))
# A = list(map(int, input().split()))

# # 総数が N でなければ不可能
# if sum(A) != N:
#     print(-1)
#     exit()

# pairs = sorted(zip(X, A))  # 位置でソート（必須）

# cnt = 0
# moved_i = 0
# for x, a in reversed(pairs):  # 右から処理
#     if N - x + 1 < a + moved_i:
#         print(-1)
#         exit()
#     cnt += a * (N - x) - (a * moved_i + a * (a - 1) // 2)
#     moved_i += a

# print(cnt)

# C - Bipartize 
# N, M = map(int, input().split())

# edges = [tuple(map(int, input().split())) for _ in range(M)]

# ans = M
# # 2^N 通りの塗り方を全部探索する
# for bit in range(2 ** N):
#     delete_count = 0
#     for u, v in edges: # それぞれの辺を見て
#         if (1 & (bit >> u)) == (1 & (bit >> v)): # 結んでいる頂点が同じ色で塗られていたら
#                 delete_count += 1 # カウントを増やす
#     ans = min(ans, delete_count)

# print(ans)

# C - Bipartize
# n, m = map(int, input().split())
# edges = [tuple(int(x)-1 for x in input().split()) for _ in range(M)]
# ans = m
# for bit in range(1 << N):
#     delete_cnt = 0
#     for u, v in edges:
#         if (bit >> u) & 1 and (bit >> v) & 1:
#             delete_cnt += 1
#             if delete_cnt >= ans:
#                 break
        
#     if delete_cnt < ans:
#         ans = delete_cnt
# print(ans)

# C - ~ 
# N = int(input())
# P = list(map(int, input().split()))

# up_or_down = []
# for i in range(1, len(P)):
#     up_or_down.append(1 if P[i-1] < P[i] else -1)

# zikkou = []
# cur = up_or_down[0]
# lenght = 1
# for i in range(1, len(up_or_down)):
#     if up_or_down[i] == cur:
#         lenght += 1
#     else:
#         zikkou.append((cur, lenght))
#         cur = up_or_down[i]
#         lenght = 1
# zikkou.append((cur, lenght))

# ans = 0
# for i in range(len(zikkou)-2):
#     (sg1, a), (sg2, b), (sg3, c) = zikkou[i], zikkou[i+1], zikkou[i+2]
#     if sg1 == 1 and sg2 == -1 and sg3 == 1:
#         add = a* c
#         # if b == 1:  # 最短区間補正
#         #     add -= 1
#         ans += add

# print(ans)

# C - Prepare Another Box 
# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# sort_A = sorted(A, reverse=True)
# sort_B = sorted(B, reverse=True)

# skip_A_i = []
# B_i = 0
# for i in range(N):
#     if B_i == N-1:
#         skip_A_i.append(i)
#         break
#     if sort_B[B_i] >= sort_A[i]:
#         B_i += 1
#     else:
#         skip_A_i.append(i)

#     if len(skip_A_i) >= 2:
#         print(-1)
#         exit()

# print(sort_A[skip_A_i[0]])

# C - 2^a b^2
# import math

# N = int(input())

# ans = 0
# a = 1

# while True:
#     M = N >> a
#     if M == 0:
#         break
#     r = math.isqrt(M)
#     ans += (r+1)//2
#     a += 1

# print(ans)

# C - Humidifier 3
# from collections import deque
# H, W, D = map(int, input().split())
# S = [list(input()) for _ in range(H)]

# INF = 10**10
# dist = [[INF] * W for _ in range(H)]
# queue = deque()
# ans_cnt = 0
# diff = ((1,0), (-1, 0), (0, 1), (0, -1))
# for j in range(H):
#     for i in range(W):
#         if S[j][i] == 'H':
#             dist[j][i] = 0
#             queue.append((j, i))


# while queue:
#     j, i = queue.popleft()
#     d = dist[j][i]
#     for dy, dx in diff:
#         if not 0 <= dy+j < H or not 0 <= dx+i < W:
#             continue
#         if S[dy+j][dx+i] == '#':
#             continue
#         if dist[dy+j][dx+i] != INF:
#             continue

#         dist[dy+j][dx+i] = d+1
#         queue.append((dy+j, dx+i))

# for i in range(H):
#     for j in range(W):
#         if dist[i][j] <= D:
#             ans_cnt += 1

# print(ans_cnt)

# C - Brackets Stack Query
# from collections import deque
# Q = int(input())
# queue = deque()
# open = 0
# close = 0
# add_n = 0
# for i in range(Q):
#     n, *c = input().split(' ')
#     if n == '1':
#         queue.append(c[0])
#         if c[0] == '(':
#             open += 1
#         else:
#             close += 1
#         if close > open and add_n == 0:
#             add_n += 1
#         elif add_n > 0:
#             add_n += 1
#     else:
#         target =  queue.pop()
#         if target == '(':
#             open -= 1
#         else:
#             close -= 1
#         if add_n > 0:
#             add_n -= 1

#     if open != close or add_n > 0:
#         print('No')
#     else:
#         print('Yes')

# C - Avoid K Palindrome 2
# 解法合ってると思うけどTLEおそらくpythonのため
# from itertools import permutations
# N, K = map(int, input().split())

# S = input()
# chars_list = set(permutations(S, N))
# ans = len(chars_list)
# for chars in chars_list:
#     for i in range(N-K+1):
#         left = 0+i
#         right = K-1+i
#         kaibun_flag = True
#         while left <= right:
#             if chars[left] != chars[right]:
#                 kaibun_flag = False
#                 break
#             else:
#                 left += 1
#                 right -= 1

#         if kaibun_flag == True:
#             ans -= 1
#             break

# print(ans)

# これやったら行けた
# filepath: [atcoder_cmondaisennomonn.py](http://_vscodecontentref_/0)
# C - Avoid K Palindrome 2
# from more_itertools import distinct_permutations
# N, K = map(int, input().split())
# S = input()
# ans = 0

# for perm in distinct_permutations(S):
#     has_palindrome = False
#     for i in range(N-K+1):
#         is_palindrome = True
#         for j in range(K):
#             if perm[i+j] != perm[i+K-j-1]:
#                 is_palindrome = False
#                 break
#         if is_palindrome:
#             has_palindrome = True
#             break
    
#     if not has_palindrome:
#         ans += 1

# print(ans)

# C - Odd One Subsequence
# from collections import Counter
# from math import comb
# N = int(input())
# A = list(map(int, input().split()))

# A_cnt = Counter(A)
# total = 0
# for num, i in A_cnt.items():
#     comb_n = 0
#     if i >= 2:
#         comb_n = comb(i, 2)

#     else_n = N-i
#     ans = else_n*comb_n
#     total += ans

# print(total)

# C - Truck Driver
# from bisect import bisect_right, bisect_left
# N, A, B = map(int, input().split())
# S = input()
# a_prefix = [0]
# b_prefix = [0]
# a_cnt = 0
# b_cnt = 0
# for s in S:
#     if s == 'a':
#         a_cnt += 1
#         a_prefix.append(a_cnt)
#         b_prefix.append(b_cnt)
#     else:
#         b_cnt += 1
#         b_prefix.append(b_cnt)
#         a_prefix.append(a_cnt)
# ans = 0
# for l in range(N):
#     a_r = bisect_left(a_prefix, A+a_prefix[l], l+1)
#     if a_r > N:
#         continue
#     b_r = bisect_left(b_prefix, B+b_prefix[l], l+1)
#     if a_r <= b_r:
#         ans += b_r-a_r

# print(ans)

# C - Robot Factory
# from sortedcontainers import SortedList
# N, M, K = map(int, input().split())

# H = SortedList(list(map(int, input().split())))
# B = SortedList(list(map(int, input().split())))

# for i in range(K):
#     target_i = B.bisect_left(H[i])
#     if target_i >= len(B):
#         print('No')
#         exit()
#     B.pop(target_i)

# print('Yes')

# C - Max Ai+Bj
# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# max_A = max(A)
# max_B = max(B)

# print(max_A+max_B)

# C - Separated Lunch
# N = int(input())
# K = list(map(int, input().split()))
# ans = 10**9
# for mask in range(1 << N):
#     a_group = 0
#     b_group = 0
#     for i in range(N):
#         if mask >> i & 1:
#             a_group += K[i]
#         else:
#             b_group += K[i]
#     # print(a_group, b_group)
#     target = max(a_group, b_group)
#     # print(target)
#     ans = min(ans, target)

# print(ans)

# C - Spiral Rotation
# N = int(input())

# A = [list(input()) for _ in range(N)]

# step = N//2

# step_cnt_grid = [[0 for _ in range(N)] for _ in range(N)]

# for i in range(N):
#     for j in range(N):
#         step_cnt_grid[i][j] = min(i, j, N-1-i, N-1-j) + 1


# ans_grid = [[0 for _ in range(N)] for _ in range(N)]
# for i in range(N):
#     for j in range(N):
#         cnt = step_cnt_grid[i][j] % 4
#         target_cell = A[i][j]
#         t_i, t_j = i, j
#         for c in range(cnt):
#             t_i, t_j = t_j, N-1-t_i
#         ans_grid[t_i][t_j] = target_cell

# for i in range(N):
#     print(''.join(ans_grid[i]))

# C - Candy Tribulation
# N, X, Y = map(int, input().split())

# A = list(map(int, input().split()))

# min_weight = min(A)*Y
# diff = Y-X
# ans = 0
# for i in range(N):
#     if (A[i]*Y-min_weight)%diff != 0:
#         print(-1)
#         exit()
#     cnt = (A[i]*Y-min_weight)//diff
#     if cnt <= A[i]:
#         ans += A[i]-cnt
#     else:
#         print(-1)
#         exit()

# print(ans)

# C - Count ABC Again
# setでA,B,Cのindexを持つ
# 初期の個数もつ
# N, Q = map(int, input().split())
# S = list(input())

# cnt = 0
# for i in range(N-2):
#     if S[i] == 'A' and S[i+1] == 'B' and S[i+2] == 'C':
#         cnt += 1
 
# for i in range(Q):
#     x, c = map(str, input().split())
#     x = int(x)
#     diff = 0
#     for i in range(3):
#         if i+x-2-1 >= 0 and i+x-1 < N:
#             if S[i+x-2-1] == 'A' and S[i+x-2] == 'B' and S[i+x-1] == 'C':
#                 diff -= 1

#     S[x-1] = c

#     for i in range(3):
#         if i+x-2-1 >= 0 and i+x-1 < N:
#             if S[i+x-2-1] == 'A' and S[i+x-2] == 'B' and S[i+x-1] == 'C':
#                 diff += 1    
#     cnt += diff
#     print(cnt)

# C - Balls and Bag Query
# from collections import defaultdict
# Q = int(input())
# boll_box = defaultdict(int)
# type_cnt = 0
# for q in range(Q):
#     query = list(map(int, input().split()))
#     if query[0] == 1:
#         if boll_box[query[1]] == 0:
#             type_cnt += 1
#         boll_box[query[1]] += 1
#     elif query[0] == 2:
#         boll_box[query[1]] -= 1
#         if boll_box[query[1]] == 0:
#             type_cnt -= 1
#     elif query[0] == 3:
#         print(type_cnt)

# C - Make Isomorphic 
# from collections import defaultdict
# from itertools import permutations

# N = int(input())
# Mg = int(input())
# u_dict = defaultdict(set)
# for _ in range(Mg):
#     u, v = map(int, input().split())
#     u_dict[u].add(v)
#     u_dict[v].add(u)

# Mh = int(input())
# a_dict = defaultdict(set)
# for _ in range(Mh):
#     a, b = map(int, input().split())
#     a_dict[a].add(b)
#     a_dict[b].add(a)

# cost = [[0]*(N+1) for _ in range(N+1)]
# for i in range(1, N):
#     row = list(map(int, input().split()))
#     for j in range(i+1, N+1):
#         c = row[j-(i+1)]
#         cost[i][j] = c
#         cost[j][i] = c

# ans = 10**18

# G = list(range(1, N+1))

# for perm in permutations(range(1, N+1)):
#     H = list(perm)

#     cur = 0
#     for i in range(N):
#         gi = G[i]
#         hi = H[i]
#         for j in range(i+1, N):
#             gj = G[j]
#             hj = H[j]

#             edge_in_G = (gi in u_dict[gi])
#             edge_in_H = (hi in a_dict[hi])

#             if edge_in_G != edge_in_H:
#                 cur += cost[hi][hj]
#                 if cur >= ans:
#                     break
#         else:
#             continue
#         break
#     ans = min(ans, cur)

# print(ans)

# from collections import defaultdict
# from itertools import permutations

# N = int(input())

# # --- G の読み込み ---
# Mg = int(input())
# u_dict = defaultdict(set)
# for _ in range(Mg):
#     u, v = map(int, input().split())
#     u_dict[u].add(v)
#     u_dict[v].add(u)

# # --- H の読み込み ---
# Mh = int(input())
# a_dict = defaultdict(set)
# for _ in range(Mh):
#     a, b = map(int, input().split())
#     a_dict[a].add(b)
#     a_dict[b].add(a)

# # --- コスト行列を 1-index の対称行列として構築 ---
# cost = [[0] * (N + 1) for _ in range(N + 1)]
# for i in range(1, N):
#     row = list(map(int, input().split()))
#     for j in range(i + 1, N + 1):
#         c = row[j - (i + 1)]  # 行 i の (i+1)番目から順に入っている
#         cost[i][j] = c
#         cost[j][i] = c

# ans = 10**18

# # G の頂点番号（1..N）
# G = list(range(1, N + 1))

# for perm in permutations(range(1, N + 1)):
#     H = list(perm)  # G[i] に対応する H の頂点が H[i]

#     cur = 0
#     # 無向グラフなので i < j の組だけ見る
#     for i in range(N):
#         gi = G[i]
#         hi = H[i]
#         for j in range(i + 1, N):
#             gj = G[j]
#             hj = H[j]

#             # G と H（対応後）で辺があるかどうか
#             edge_in_G = (gj in u_dict[gi])
#             edge_in_H = (hj in a_dict[hi])

#             if edge_in_G != edge_in_H:
#                 # H 側の (hi, hj) の辺をトグルする必要があるので、
#                 # そのペアのコストを足す
#                 cur += cost[hi][hj]
#                 # 既に ans 以上なら打ち切り
#                 if cur >= ans:
#                     break
#         else:
#             continue
#         break

#     ans = min(ans, cur)

# print(ans)

# C - Sum = 0
# N = int(input())

# diff_list = []
# total = 0
# min_total = 0
# ans_list = []
# for i in range(N):
#     l, r = map(int, input().split())
#     diff = r-l
#     diff_list.append((diff, l, r))
#     ans_list.append(r)
#     total += r
#     min_total += l

# if not min_total <= 0 <= total:
#     print('No')
#     exit()

# for i in range(N):
#     if total == 0:
#         break

#     diff, l, r = diff_list[i]
#     if total-diff > 0:
#         total -= diff
#         ans_list[i] = l
#     else:
#         cost = total
#         total = 0
#         ans_list[i] -= cost
#         break

# if total == 0:
#     print('Yes')
#     print(*ans_list)
# else:
#     print('No')

# C - Word Ladder
# C - Word Ladder
# S = list(input())
# T = list(input())
# cnt = 0
# Z = []
# for i in range(len(S)):
#     s = S[i]
#     t = T[i]
#     if s == t:
#         continue

#     if s > t:
#         S[i] = t
#         cnt += 1
#         z = ''.join(S)
#         Z.append(z)
#     else:
#         continue

# for i in range(len(S)-1, -1, -1):
#     s = S[i]
#     t = T[i]
#     if s == t:
#         continue
#     else:
#         S[i] = t
#         cnt += 1
#         z = ''.join(S)
#         Z.append(z)

# print(cnt)
# for string in Z:
#     print(string)

# C - Count Arithmetic Subarrays
# N = int(input())
# A = list(map(int, input().split()))
# ans = N

# if N >= 2:
#     l = 0
#     while l < N-1:
#         r = l+1
#         d = A[r] - A[l]

#         while r+1 < N and A[r+1]-A[r] == d:
#             r +=1

#         length = r-l+1
#         ans += length*(length-1)//2
#         l = r

# print(ans)

# C - Triple Attack
# N = int(input())
# H = list(map(int, input().split()))

# T = 0
# for i in range(N):
#     hp = H[i]

#     while T % 3 != 0 and hp > 0:
#         T += 1
#         if T % 3 == 0:
#             hp -= 3
#         else:
#             hp -= 1
#     if hp <= 0:
#         continue

#     sets = hp // 5
#     T += sets * 3
#     hp -= sets * 5

#     while hp > 0:
#         T += 1
#         if T % 3 == 0:
#             hp -= 3
#         else:
#             hp -= 1


# print(T)

# C - Enumerate Sequences
# from itertools import product
# N, K = map(int, input().split())
# R = list(map(int, input().split()))
# ans_list = []
# ranges = [range(1, r+1) for r in R]
# for perm in product(*ranges):
#     if sum(perm) % K == 0:
#         ans_list.append(perm)

    

# ans = sorted(ans_list)

# for a in ans:
#     print(*a)

# C - Transportation Expenses
# from bisect import bisect_left

# N, M = map(int, input().split())
# A = sorted(list(map(int, input().split())))

# prefix = [0]*(N+1)
# for i in range(N):
#     prefix[i+1] = prefix[i]+A[i]

# if prefix[N] <= M:
#     print('infinite')
#     exit()

# ok, ng = 0, 10**9
# while ok+1 < ng:
#     mid = (ok+ng)//2
#     i = bisect_left(A, mid)
#     total = prefix[i]+mid*(N-i)
#     if total <= M:
#         ok = mid
#     else:
#         ng = mid

# print(ok)

# C - Tile Distance 2
# sx, sy = map(int, input().split())
# tx, ty = map(int, input().split())

# if ((sx+sy)% 2 == 1):
#     sx -= 1
# if ((tx+ty)% 2 == 1):
#     tx -= 1
# x = abs(sx-tx)
# y = abs(sy-ty)
# if (y > x):
#     print(y)
# else:
#     print((x+y)//2)

# C - Move It
# from collections import defaultdict
# N = int(input())
# A = list(map(int, input().split()))
# W = list(map(int, input().split()))

# ans = 0
# best_dict = defaultdict(int)
# for i in range(N):
#     if best_dict[A[i]] == 0:
#         best_dict[A[i]] = W[i]
#         continue

#     if best_dict[A[i]] < W[i]:
#         ans += best_dict[A[i]]
#         best_dict[A[i]] = W[i]
#     else:
#         ans += W[i]

# print(ans)

# C - Minimum Glutton
# N, X, Y = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# sorted_A = sorted(A, reverse= True)
# sorted_B = sorted(B, reverse=True)

# v_a = 0
# v_b = 0
# c_a = 0
# c_b = 0

# for a in (sorted_A):
#     v_a += a
#     c_a += 1
#     if v_a > X:
#         break

# for b in (sorted_B):
#     v_b += b
#     c_b += 1
#     if v_b > Y:
#         break

# print(min(c_a, c_b))

# C - Make Them Narrow
# N, K = map(int, input().split())

# A = sorted(list(map(int, input().split())))

# ans = A[N-K-1] - A[0]
# for i in range(1, N-(N-K)+1):
#     ans = min(ans, A[i+N-K-1]-A[i])

# print(ans)

