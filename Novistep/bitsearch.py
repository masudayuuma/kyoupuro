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
# N, M = map(int, input().split())

# S = [list(input()) for _ in range(N)]
# ans = float('inf')
# for mask in range(1 << N):
#     ans_set = set()
#     tmp_cnt = 0
#     for j in range(N):
#         if mask >> j & 1:
#             tmp_cnt += 1
#             for i in range(M):
#                 if S[j][i] == 'o':
#                     ans_set.add(i)

#     if len(ans_set) == M:
#         ans = min(ans, tmp_cnt)

# print(ans)

# C - Coverage
# N, M = map(int, input().split())
# group_list = []
# ans = 0
# for m in range(M):
#     c = int(input())
#     a = set(list(map(int, input().split())))
#     group_list.append(a)

# for mask in range(1 << M):
#     tmp = set()
#     for i in range(M):
#         if mask >> i & 1:
#             tmp |= group_list[i]
    
#     if len(tmp) == N:
#         ans += 1

# print(ans)

# C - Submask
# N = int(input())
# hot_i = []
# for i in range(60):
#     if 1 << i & N:
#         hot_i.append(i)

# for mask in range(1 << len(hot_i)):
#     tmp = 0
#     for i in range(len(hot_i)):
#         if mask >> i & 1:
#             tmp += 2**hot_i[i]

#     print(tmp)

# C - Switches
# N, M = map(int, input().split())
# swiches_list = []
# for m in range(M):
#     k, *s = list(map(int, input().split()))
#     swiches_list.append(s)

# P = list(map(int, input().split()))
# ans = 0
# for mask in range(1 << N):
#     cnt = 0
#     for m in range(M):
#         right_tmp = 0
#         for target_swich in swiches_list[m]:
#             if mask >> (target_swich-1) & 1:
#                 right_tmp += 1
#         if right_tmp % 2 == P[m]:
#             cnt += 1
#     if cnt == M:
#         ans += 1

# print(ans)

# C - Skill Up
# N, M, X = map(int, input().split())
# book2skills = []
# cost = []
# for n in range(N):
#     c, *a = map(int, input().split())
#     book2skills.append(a)
#     cost.append(c)
# ans_cost = float('inf')

# for mask in range(1 << N):
#     get_skills = [0]*M
#     tmp_total= 0
#     for n in range(N):
#         if mask >> n & 1:
#             tmp_total += cost[n]
#             for i in range(M):
#                 get_skills[i] += book2skills[n][i]
#     flag = True
#     for x in get_skills:
#         if x < X:
#             flag = False
#             break

#     if flag == True and tmp_total < ans_cost:
#         ans_cost = tmp_total

# print(ans_cost if ans_cost != float('inf') else -1)

# C - Bowls and Dishes
# N, M = map(int, input().split())

# ans = 0
# conditions = []
# for i in range(M):
#     a, b = map(int, input().split())
#     conditions.append((a, b))

# K = int(input())

# people2choices = []
# for i in range(K):
#     c, d = map(int, input().split())
#     people2choices.append((c, d))

# for mask in range(1 << K):
#     tmp = 0
#     choices_set = set()
#     choices = [0]*K
#     for k in range(K):
#         if mask >> k & 1:
#             choices[k] = 1
        
#     for i in range(K):
#         if choices[i] == 1:
#             choices_set.add(people2choices[i][1])
#         else:
#             choices_set.add(people2choices[i][0])

#     for c in conditions:
#         a, b = c
#         if a in choices_set and b in choices_set:
#             tmp += 1

#     ans = max(ans, tmp)

# print(ans)

# C - Perfect Standings
# a, b, c, d, e = map(int, input().split())

# str_dict = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E'}
# point_dict = {0:a, 1:b, 2:c, 3:d, 4:e}
# ans = []
# for mask in range(1 << 5):
#     tmp = ''
#     point = 0
#     for i in range(5):
#         if mask >> i & 1:
#             tmp += str_dict[i]
#             point += point_dict[i]
#     ans.append((point, tmp))

# ans.sort(key=lambda x: (-x[0], x[1]))
# answers = [s for p, s in ans]

# print('\n'.join(map(str, answers)))

# F - 一触即発
# 断念
# N, M = map(int, input().split())
# a_b_c_list = list()
# ans_cnt = 0
# for m in range(M):
#     a, b, c = map(int, input().split())
#     a_b_c_list.append(set((a, b, c)))

# for mask in range(1 << N):
#     way_cnt = [0]*M
#     continue_flag = True
#     for i in range(N):
#         if mask >> i & 1:
#             for index, a_b_c in enumerate(a_b_c_list):
#                 if i+1 in a_b_c:
#                     way_cnt[index] += 1
#                     if way_cnt[index] > 2:
#                         continue_flag = False
#                         break
#     if continue_flag == False:
#         continue
#     tmp = 0
#     if continue_flag == True:
#         for way in way_cnt:
#             if way == 2:
#                 tmp += 1

#     ans_cnt = max(tmp, ans_cnt)

# print(ans_cnt)

# F - 一触即発
# N, M = map(int, input().split())
# a_b_c_list = []
# for m in range(M):
#     a, b, c = map(int, input().split())
#     a_b_c_list.append({a, b, c})

# ans_cnt = 0

# for mask in range(1 << N):
#     selected = {i+1 for i in range(N) if mask >> i & 1}
#     explode = False
#     for abc in a_b_c_list:
#         if len(selected & abc) >= 3:
#             explode = True
#             break
#     if explode:
#         continue

#     danger_drugs = set()
#     for abc in a_b_c_list:
#         overlap = selected & abc
#         if len(overlap) == 2:
#             remaining = abc - selected
#             danger_drugs |= remaining
#     ans_cnt = max(ans_cnt, len(danger_drugs))

# print(ans_cnt)

# D - 派閥
# N, M = map(int, input().split())
# ans = 0
# p2m = []
# for m in range(M):
#     x, y = map(int, input().split())
#     p2m.append((x, y))

# for mask in range(1 << N):
#     cnt = 0
#     for i in range(N):
#         if mask >> i & 1:
#             for x, y in p2m:
#                 if (i == (x-1) or (y-1) == i) and mask >> x & 1 and mask >> y & 1:
#                     cnt += 1
#     ans = max(ans, cnt)

# print(ans)

# N, M = map(int, input().split())

# adj = [[False]*N for _ in range(N)]
# for _ in range(M):
#     x, y = map(int, input().split())
#     x -= 1
#     y -= 1
#     adj[x][y] = True
#     adj[y][x] = True

# ans = 0

# for mask in range(1 << N):
#     members = []
#     for i in range(N):
#         if mask & (1 << i):
#             members.append(i)

#     is_clique = True
#     for i in range(len(members)):
#         for j in range(i+1, len(members)):
#             if not adj[members[i]][members[j]]:
#                 is_clique = False
#                 break
#         if not is_clique:
#             break
#     if is_clique:
#         ans = max(ans, len(members))
# print(ans)

# C - To 3
# N = input()
# ans = float('inf')
# for mask in range(1, 1 << len(N)):
#     total = 0
#     cnt = 0
#     for n in range(len(N)):
#         if mask >> n & 1:
#             total += int(N[n])
#         else:
#             cnt += 1

#     if total % 3 == 0:
#         ans = min(ans, cnt)
# print(-1 if ans == float('inf') else ans)

# 002 - Encyclopedia of Parentheses（★3）
# N = int(input())
# nums = []
# for mask in range(1 << N):
#     cnt = 0
#     flag = True
#     for i in range(N):
#         if mask >> i & 1:
#             cnt += 1
#         else:
#             cnt -= 1

#         if cnt < 0:
#             flag = False
#             break
#     if flag == True and cnt == 0:
#         nums.append(mask)

# for mask in nums:
#     chars = ''
#     for m in format(mask, f'0{N}b'):
#         if m == '1':
#             chars += ')'
#         else:
#             chars += '('

#     print(chars)

# C - Just K
# from collections import Counter
# N, K = map(int, input().split())

# ans = 0
# chars = []
# for _ in range(N):
#     s = input()
#     chars.append(s)

# for mask in range(1 << N):
#     total = ''
#     tmp_ans = 0
#     for i in range(N):
#         if mask >> i & 1:
#             total += chars[i]
#     total_cnt = Counter(total)

#     for c in total_cnt:
#         if total_cnt[c] == K:
#             tmp_ans += 1

#     ans = max(tmp_ans, ans)

# print(ans)

# C - Keys
# N, M, K = map(int, input().split())

# test_result = []
# test_num = []
# cnt = 0
# for m in range(M):
#     c, *query = input().split()
#     test_result.append(query.pop())
#     query = list(map(int, query))
#     test_num.append(set(query))

# for mask in range(1 << N):
#     flag = True
#     for q, n in zip(test_num, test_result):
#         tmp_correct = set()
#         for i in q:
#             if mask >> (i-1) & 1:
#                 tmp_correct.add(i)

#         if (n == 'o' and len(tmp_correct) < K) or (n == 'x' and len(tmp_correct) >= K):
#             flag = False
#             break

#     if flag == True:
#         cnt += 1

# print(cnt)

# C - HonestOrUnkind2
# from collections import defaultdict
# N = int(input())
# answer = 0
# p2inv = defaultdict(list)
# for i in range(N):
#     a = int(input())
#     for _ in range(a):
#         x, y = map(int, input().split())
#         p2inv[x-1].append((i, y))

# for mask in range(1 << N):
#     cnt = 0
#     flag = True
#     for i in range(N):
#         if mask >> i & 1:
#             cnt += 1
#         for x, y in p2inv[i]:
#             if (mask >> x) & 1 == 0:
#                 continue

#             if y == 1 and (mask >> i & 1) == 0:
#                 flag = False
#                 break
#             if y == 0 and (mask >> i & 1) == 1:
#                 flag = False
#                 break

#         if flag == False:
#             break

#     if flag == True:
#         answer = max(cnt, answer)

# print(answer)

# # C - ORXOR
# N = int(input())

# A = list(map(int, input().split()))
# final = float('inf')
# for mask in range(1 << N):
#     ans = 0
#     tmp = 0
#     for i in range(N):
#         if mask >> i & 1:
#             if tmp == 0:
#                 tmp = A[i]
#             else:
#                 tmp |= A[i]
#             ans ^= tmp
#             tmp = 0
#         else:
#             if tmp == 0:
#                 tmp = A[i]
#             else:
#                 tmp |= A[i]
#     if tmp != 0:
#         ans ^= tmp

#     final = min(final, ans)

# print(final)